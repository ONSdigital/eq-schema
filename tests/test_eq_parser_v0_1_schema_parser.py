import unittest
import os
import json
from eq.model.questionnaire import Questionnaire
from eq.parser.v0_1.schema_parser import SchemaParser
from eq.parser.schema_parser_exception import SchemaParserException
from settings import SCHEMA_DIR

class TestSchemaParser(unittest.TestCase):
    def _load_schema(self, filename):
        with open(os.path.join(SCHEMA_DIR, 'v0_1', filename)) as f:
            q_data = f.read()
            f.close()
            return json.loads(q_data)

    def test___init__(self):
        schema = {}

        parser = SchemaParser(schema)

        assert parser._schema == schema
        assert parser._version == 0.1

    def test_get_parser_version(self):
        schema_parser = SchemaParser({})
        assert schema_parser.get_parser_version() == 0.1

    def test_parse(self):
        schema = self._load_schema('simple-questionnaire.json')

        schema_parser = SchemaParser(schema)
        questionnaire = schema_parser.parse()

        assert isinstance(questionnaire, Questionnaire)

    def test__check_version(self):
        parser = SchemaParser({})

        self.assertRaises(SchemaParserException, parser._check_version, {})

        self.assertRaises(SchemaParserException, parser._check_version, {"schema":1.0})

        parser._check_version({"schema":0.1})

if __name__ == '__main__':
    unittest.main()
