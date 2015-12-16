import unittest
from eq.parser.alpha.schema_parser import SchemaParser

class TestSchemaParser(unittest.TestCase):
    def test___init__(self):
        # schema_parser = SchemaParser(schema)
        assert True # TODO: implement your test here

    def test_get_parser_version(self):
        # schema_parser = SchemaParser(schema)
        # self.assertEqual(expected, schema_parser.get_parser_version())
        assert True # TODO: implement your test here

    def test__parse_property(self):
        schema = {
            "questionnaire_id" : "1234",
            "questionnaire_title":"Test Schema",
            "overview" : "This should be the description"
        }

        parser = SchemaParser(schema)

        assert parser._parse_property(schema, "questionnaire_id") == "1234"
        assert parser._parse_property(schema, "questionnaire_title") == "Test Schema"
        assert parser._parse_property(schema, "overview") == "This should be the description"


    def test_parse_simple_schema(self):
        schema_parser = SchemaParser({
            "questionnaire_id" : "1234",
            "questionnaire_title":"Test Schema",
            "overview" : "This should be the description"
        })

        questionnaire = schema_parser.parse()

        assert questionnaire.title == "Test Schema"
        assert questionnaire.description == "This should be the description"
        assert questionnaire.id == 1234 # should be numeric


if __name__ == '__main__':
    unittest.main()
