import unittest

from scriptable.mustache_engine import MustacheEngine


class MustacheEngineTest(unittest.TestCase):

    def test_property(self):
        self.assertEqual(MustacheEngine.parse("{{name}}").execute({"name": "abc"}), "abc")
        self.assertEqual(MustacheEngine.parse("test {{name}}").execute({"name": "abc"}), "test abc")
        self.assertEqual(MustacheEngine.parse("ab {{name}} cd").execute({"name": "abc"}), "ab abc cd")

    def test_if(self):
        engine = MustacheEngine.parse("{{#expr}}body{{/expr}}")
        self.assertEqual(engine.execute({"expr": True}), "body")
        self.assertEqual(engine.execute({"expr": False}), "")

    def test_if_with_property(self):
        engine = MustacheEngine.parse("{{#expr}}{{name}}{{name}}{{/expr}}")
        self.assertEqual(engine.execute({"expr": True, "name": "abc"}), "abcabc")

    def test_loop(self):
        engine = MustacheEngine.parse("{{#expr}}{{.}}{{/expr}}")
        self.assertEqual(engine.execute({"expr": ["a", "b", "c", "d"]}), "abcd")
