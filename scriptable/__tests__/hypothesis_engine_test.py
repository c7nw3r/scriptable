import unittest

from scriptable.hypothesis_engine import HypothesisEngine


class HypothesisEngineTest(unittest.TestCase):

    def test_max_precision(self):
        with self.assertRaises(AssertionError) as error:
            HypothesisEngine.parse("10000000000 + 2")
        self.assertEqual("max value precision exceeded", error.exception.args[0])

    def test_max_scale(self):
        with self.assertRaises(AssertionError) as error:
            HypothesisEngine.parse("1.00000 + 2")
        self.assertEqual("max value scale exceeded", error.exception.args[0])

    def test_expression(self):
        self.assertAlmostEqual(HypothesisEngine.parse("1 + 2").execute(), 3)
        self.assertAlmostEqual(HypothesisEngine.parse("1.1 + 2.2").execute(), 3.3)

        self.assertAlmostEqual(HypothesisEngine.parse("1 - 2").execute(), -1)
        self.assertAlmostEqual(HypothesisEngine.parse("1 * 2").execute(), 2)
        self.assertAlmostEqual(HypothesisEngine.parse("1 / 2").execute(), 0.5)

    def test_arithmetic_order(self):
        self.assertAlmostEqual(HypothesisEngine.parse("1 + 2 * 3").execute(), 7)
        self.assertAlmostEqual(HypothesisEngine.parse("1 + 2 * 3 - 1 / 2").execute(), 6.5)
        self.assertAlmostEqual(HypothesisEngine.parse("(1 + 2) * 3").execute(), 9)
        self.assertAlmostEqual(HypothesisEngine.parse("(1 + 2) * (3 - 1) / 2").execute(), 3)

    def test_logic_expression(self):
        # boolean expression
        self.assertEqual(HypothesisEngine.parse("true && true").execute(), True)
        self.assertEqual(HypothesisEngine.parse("true && false").execute(), False)
        self.assertEqual(HypothesisEngine.parse("false && true").execute(), False)
        self.assertEqual(HypothesisEngine.parse("false && false").execute(), False)
        self.assertEqual(HypothesisEngine.parse("true || true").execute(), True)
        self.assertEqual(HypothesisEngine.parse("true || false").execute(), True)
        self.assertEqual(HypothesisEngine.parse("false || true").execute(), True)
        self.assertEqual(HypothesisEngine.parse("false || false").execute(), False)
        self.assertEqual(HypothesisEngine.parse("true && true || false").execute(), True)
        self.assertEqual(HypothesisEngine.parse("true && false || false").execute(), False)
        self.assertEqual(HypothesisEngine.parse("true == true").execute(), True)
        self.assertEqual(HypothesisEngine.parse("true === true").execute(), True)
        self.assertEqual(HypothesisEngine.parse("true == false").execute(), False)
        self.assertEqual(HypothesisEngine.parse("true === false").execute(), False)
        self.assertEqual(HypothesisEngine.parse("x === true").execute({"x": True}), True)

        self.assertEqual(HypothesisEngine.parse("1 == 1").execute(), True)
        self.assertEqual(HypothesisEngine.parse("1 != 1").execute(), False)
        self.assertEqual(HypothesisEngine.parse("1 > 1").execute(), False)
        self.assertEqual(HypothesisEngine.parse("1 >= 1").execute(), True)
        self.assertEqual(HypothesisEngine.parse("1 < 1").execute(), False)
        self.assertEqual(HypothesisEngine.parse("1 <= 1").execute(), True)

        self.assertEqual(HypothesisEngine.parse("'test' == 'test'").execute(), True)
        self.assertEqual(HypothesisEngine.parse("'test' != 'test'").execute(), False)
        self.assertEqual(HypothesisEngine.parse("'a' + 'b' + 'c'").execute(), "abc")

    def test_parenthesizes(self):
        self.assertAlmostEqual(HypothesisEngine.parse("(((true && true)))").execute(), True)
        self.assertAlmostEqual(HypothesisEngine.parse("false && (false || true)").execute(), False)
