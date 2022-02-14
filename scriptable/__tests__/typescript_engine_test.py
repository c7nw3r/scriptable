import unittest

from scriptable.typescript_engine import TypescriptEngine


class TypescriptEngineTest(unittest.TestCase):

    def test_max_precision(self):
        with self.assertRaises(AssertionError) as error:
            TypescriptEngine.parse("10000000000 + 2")
        self.assertEqual("max value precision exceeded", error.exception.args[0])

    def test_max_scale(self):
        with self.assertRaises(AssertionError) as error:
            TypescriptEngine.parse("1.00000 + 2")
        self.assertEqual("max value scale exceeded", error.exception.args[0])

    def test_expression(self):
        self.assertAlmostEqual(TypescriptEngine.parse("1 + 2").execute(), 3)
        self.assertAlmostEqual(TypescriptEngine.parse("1.1 + 2.2").execute(), 3.3)

        self.assertAlmostEqual(TypescriptEngine.parse("1 - 2").execute(), -1)
        self.assertAlmostEqual(TypescriptEngine.parse("1 * 2").execute(), 2)
        self.assertAlmostEqual(TypescriptEngine.parse("1 / 2").execute(), 0.5)

    def test_arithmetic_order(self):
        self.assertAlmostEqual(TypescriptEngine.parse("1 + 2 * 3").execute(), 7)
        self.assertAlmostEqual(TypescriptEngine.parse("1 + 2 * 3 - 1 / 2").execute(), 6.5)
        self.assertAlmostEqual(TypescriptEngine.parse("(1 + 2) * 3").execute(), 9)
        self.assertAlmostEqual(TypescriptEngine.parse("(1 + 2) * (3 - 1) / 2").execute(), 3)

    def test_logic_expression(self):
        # boolean expression
        self.assertEqual(TypescriptEngine.parse("true && true").execute(), True)
        self.assertEqual(TypescriptEngine.parse("true && false").execute(), False)
        self.assertEqual(TypescriptEngine.parse("false && true").execute(), False)
        self.assertEqual(TypescriptEngine.parse("false && false").execute(), False)
        self.assertEqual(TypescriptEngine.parse("true || true").execute(), True)
        self.assertEqual(TypescriptEngine.parse("true || false").execute(), True)
        self.assertEqual(TypescriptEngine.parse("false || true").execute(), True)
        self.assertEqual(TypescriptEngine.parse("false || false").execute(), False)
        self.assertEqual(TypescriptEngine.parse("true && true || false").execute(), True)
        self.assertEqual(TypescriptEngine.parse("true && false || false").execute(), False)
        self.assertEqual(TypescriptEngine.parse("true == true").execute(), True)
        self.assertEqual(TypescriptEngine.parse("true === true").execute(), True)
        self.assertEqual(TypescriptEngine.parse("true == false").execute(), False)
        self.assertEqual(TypescriptEngine.parse("true === false").execute(), False)

        # number expression
        self.assertEqual(TypescriptEngine.parse("1 == 1").execute(), True)
        self.assertEqual(TypescriptEngine.parse("1 != 1").execute(), False)
        self.assertEqual(TypescriptEngine.parse("1 > 1").execute(), False)
        self.assertEqual(TypescriptEngine.parse("1 >= 1").execute(), True)
        self.assertEqual(TypescriptEngine.parse("1 < 1").execute(), False)
        self.assertEqual(TypescriptEngine.parse("1 <= 1").execute(), True)

        # string expression
        self.assertEqual(TypescriptEngine.parse("'test' == 'test'").execute(), True)
        self.assertEqual(TypescriptEngine.parse("'test' != 'test'").execute(), False)
        self.assertEqual(TypescriptEngine.parse("'a' + 'b' + 'c'").execute(), "abc")

    def test_parenthesizes(self):
        self.assertAlmostEqual(TypescriptEngine.parse("(((1 + 2)))").execute(), 3)
        self.assertAlmostEqual(TypescriptEngine.parse("(((true && true)))").execute(), True)
        self.assertAlmostEqual(TypescriptEngine.parse("false && (false || true)").execute(), False)

    def test_property_access(self):
        self.assertAlmostEqual(TypescriptEngine.parse("'test'.length").execute(), 4)
        self.assertEqual(TypescriptEngine.parse("'abcd'[1]").execute(), "b")

    def test_function_access(self):
        self.assertEqual(TypescriptEngine.parse("'abc'.slice(-1)").execute(), "c")
        self.assertEqual(TypescriptEngine.parse("'abc'.substring(1)").execute(), "bc")
        self.assertEqual(TypescriptEngine.parse("'abc'.substring(1, 2)").execute(), "b")
        self.assertEqual(TypescriptEngine.parse("'abcdefg'.substr(2, 3)").execute(), "cde")
        self.assertEqual(TypescriptEngine.parse("'abcdefg'.replace('cde', '')").execute(), "abfg")
        self.assertEqual(TypescriptEngine.parse("'abc'.concat('defg')").execute(), "abcdefg")
        self.assertEqual(TypescriptEngine.parse("'  abc  '.trim()").execute(), "abc")
        self.assertEqual(TypescriptEngine.parse("'abc'.padStart(5, 0)").execute(), "00abc")
        self.assertEqual(TypescriptEngine.parse("'abc'.padEnd(5, 0)").execute(), "abc00")
        self.assertEqual(TypescriptEngine.parse("'abc'.charAt(1)").execute(), "b")
        self.assertEqual(TypescriptEngine.parse("'abcd'.charCodeAt(3)").execute(), 100)
        self.assertEqual(TypescriptEngine.parse("'a,b,c'.split(',')").execute(), ["a", "b", "c"])

    def test_if_control(self):
        self.assertEqual(TypescriptEngine.parse("if (true) { return 1 } return 0").execute(), 1)
        self.assertEqual(TypescriptEngine.parse("if (false) { return 1 } return 0").execute(), 0)

    def test_console(self):
        TypescriptEngine.parse("console.assert('a')").execute()

    def test_value(self):
        # array
        self.assertEqual(TypescriptEngine.parse("['a', 'b', 'c']").execute(), ["a", "b", "c"])
        self.assertEqual(TypescriptEngine.parse("[1, 2, 3]").execute(), [1, 2, 3])
        self.assertEqual(TypescriptEngine.parse("[[1, 2, 3]]").execute(), [[1, 2, 3]])
        # map
        self.assertEqual(TypescriptEngine.parse("{'a':0, 'b':1, 'c':2}").execute(), {"a": 0, "b": 1, "c": 2})
        # string
        self.assertEqual(TypescriptEngine.parse("'abc'").execute(), "abc")

    def test_function_without_args(self):
        engine = TypescriptEngine.parse("""
function test() {
   return "test"
}
test()
        """)
        self.assertEqual(engine.execute(), "test")

    def test_function_with_args(self):
        engine = TypescriptEngine.parse("""
function test(a:string, b:string) {
   return a + b
}
test('te', 'st')
        """)
        self.assertEqual(engine.execute(), "test")

    def test_overloading(self):
        self.assertEqual(TypescriptEngine.parse("'a' + 'b' + 'c'").execute(), "abc")
        self.assertEqual(TypescriptEngine.parse("function test(a) { return a } test('a' + 'b' + 'c')").execute(), "abc")
