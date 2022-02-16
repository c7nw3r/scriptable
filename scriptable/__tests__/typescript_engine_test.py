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
        # self.assertAlmostEqual(TypescriptEngine.parse("'test'.length").execute(), 4)
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

    def test_fibonacci(self):
        engine = TypescriptEngine.parse("""
function fibonacci(n:number) {
   if (n == 0) return 0
   if (n == 1) return 1
   if (n == 2) return 1
   return fibonacci(n - 1) + fibonacci(n - 2)
}
fibonacci(8)
        """)
        self.assertEqual(engine.execute(), 21)

    def test_recursion_guard(self):
        with self.assertRaises(AssertionError) as error:
            TypescriptEngine.parse("""
    function test(n:number) {
       return test(n)
    }
    test(8)
            """).execute()
            self.assertEqual(error.exception.args[0], "recursion loop determined")

    def test_lambda(self):
        self.assertEqual(TypescriptEngine.parse("[4, 3, 2, 1].sort((a, b) => a - b)").execute(), [1, 2, 3, 4])

    def test_mutable_variable(self):
        engine = TypescriptEngine.parse("""
let test = 5
test
        """)
        self.assertEqual(engine.execute(), 5)

    def test_immutable_variable(self):
        engine = TypescriptEngine.parse("""
const test = 5
test
        """)
        self.assertEqual(engine.execute(), 5)

    def test_while(self):
        engine = TypescriptEngine.parse("""
let n = 5
while (n > 0) {
    n = n - 1
}
n
        """)
        self.assertEqual(engine.execute(), 0)

    def test_for(self):
        engine = TypescriptEngine.parse("""
let a = 5
for (let n = 5; n > 0; n--) {
    a = a - 1
}
a
        """)
        self.assertEqual(engine.execute(), 0)

    def test_for_of(self):
        engine = TypescriptEngine.parse("""
let a = ""
for (let char of "test") {
    a = a + char
}
a
        """)
        self.assertEqual(engine.execute(), "test")

    def test_for_in(self):
        engine = TypescriptEngine.parse("""
let a = []
for (let i in [1, 2, 3, 4]) {
    a.push(i)
}
a
        """)
        self.assertEqual(engine.execute(), [0, 1, 2, 3])

    def test_loop_guard(self):
        with self.assertRaises(AssertionError) as error:
            TypescriptEngine.parse("for (let i = 12; i > 0; i--) {}").execute()
        self.assertEqual(error.exception.args[0], "max loops exceeded")

    def test_break(self):
        engine = TypescriptEngine.parse("""
let a = 0
for (let n = 5; n > 0; n--) {
    if (n == 2) break
    a = a + 1
}
a
            """)
        self.assertEqual(engine.execute(), 3)

    def test_continue(self):
        engine = TypescriptEngine.parse("""
let a = 0
for (let n = 5; n > 0; n--) {
    if (n == 2) continue
    a = a + 1
}
a
            """)
        self.assertEqual(engine.execute(), 4)

    def test_process_env(self):
        self.assertEqual(TypescriptEngine.parse("process.env.test").execute({"test": "abc"}), "abc")
        self.assertEqual(TypescriptEngine.parse("process.env['test']").execute({"test": "abc"}), "abc")
