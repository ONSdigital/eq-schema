import unittest
from eq.parser.schema_parser_factory import SchemaParserFactory
from eq.parser.schema_parser import SchemaParser

class TestSchemaParserFactory(unittest.TestCase):
    def test_create_parser_version_0_point_1(self):
        schema = {
            "schema":"0.1"
        }

        parser = SchemaParserFactory.create_parser(schema)

        assert isinstance(parser, SchemaParser) == True
        assert parser.get_parser_version() == 0.1

    def test_create_parser_version_alpha(self):
        schema = {
            # no version specified
        }

        parser = SchemaParserFactory.create_parser(schema)

        assert isinstance(parser, SchemaParser) == True
        assert parser.get_parser_version() == "alpha"


if __name__ == '__main__':
    unittest.main()
