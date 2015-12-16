import unittest
from eq.parser.v0_1.schema_parser import SchemaParser
from eq.parser.schema_parser_exception import SchemaParserException

class TestSchemaParser(unittest.TestCase):
    def test___init__(self):
        # schema_parser = SchemaParser(schema)
        assert True # TODO: implement your test here

    def test_get_parser_version(self):
        # schema_parser = SchemaParser(schema)
        # self.assertEqual(expected, schema_parser.get_parser_version())
        assert True # TODO: implement your test here

    def test__parse_property(self):
        assert True

    def test_parse(self):
        # schema_parser = SchemaParser(schema)
        # self.assertEqual(expected, schema_parser.parse())
        assert True # TODO: implement your test here

    def test__check_version(self):
        parser = SchemaParser({})

        self.assertRaises(SchemaParserException, parser._check_version, {})

        self.assertRaises(SchemaParserException, parser._check_version, {"schema":1.0})

        parser._check_version({"schema":0.1})

if __name__ == '__main__':
    unittest.main()
