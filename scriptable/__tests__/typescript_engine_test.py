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
        self.assertEqual(TypescriptEngine.parse("true && true").execute(), True)
        self.assertEqual(TypescriptEngine.parse("true && false").execute(), False)
        self.assertEqual(TypescriptEngine.parse("false && true").execute(), False)
        self.assertEqual(TypescriptEngine.parse("false && false").execute(), False)
        self.assertEqual(TypescriptEngine.parse("true || true").execute(), True)
        self.assertEqual(TypescriptEngine.parse("true || false").execute(), True)
        self.assertEqual(TypescriptEngine.parse("false || true").execute(), True)
        self.assertEqual(TypescriptEngine.parse("false || false").execute(), False)
