from eq.parser.schema_parser import SchemaParser as AbstractSchemaParser
from eq.model.questionnaire import Questionnaire

class SchemaParser(AbstractSchemaParser):
    def __init__(self, schema):
        self._version = "alpha"
        self._schema = schema

    def get_parser_version(self):
        return self._version

    def parse(self):
        questionnaire = Questionnaire()

        questionnaire.id = int(self._parse_property(self._schema, 'questionnaire_id'))
        questionnaire.title = self._parse_property(self._schema, 'questionnaire_title')
        questionnaire.description = self._parse_property(self._schema, 'overview')

        return questionnaire

    # Return a property from the schema, throws an exception if missing
    def _parse_property(self, obj, prop_name):
        if prop_name in obj.keys():
            return obj[prop_name]
        else:
            raise SchemaParserException("Cannot find property '{prop_name}'".format(prop_name=prop_name))
