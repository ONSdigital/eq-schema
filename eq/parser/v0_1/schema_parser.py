from eq.parser.schema_parser import SchemaParser as AbstractSchemaParser
from eq.parser.schema_parser_exception import SchemaParserException
from eq.parser.v0_1.question_parser import QuestionParser
from eq.model.questionnaire import Questionnaire
from eq.model.section import Section
from eq.model.block import Block

class SchemaParser(AbstractSchemaParser):
    def __init__(self, schema):
        self._version = 0.1
        self._schema = schema

    def get_parser_version(self):
        return self._version

    def parse(self):
        questionnaire = Questionnaire()

        # check the schema version
        self._check_version(self._schema)

        questionnaire.id = self._get_required_integer(self._schema, "id")
        questionnaire.title = self._get_required_string(self._schema, "title")
        questionnaire.description = self._get_required_string(self._schema, "description")

        if "sections" in self._schema.keys():
            for sectionSchema in self._schema["sections"]:
                questionnaire.add_section(self._parse_section(sectionSchema))

        return questionnaire

    # parse and return a section
    def _parse_section(self, schema):
        section = Section()

        section.id = self._get_required_string(schema, 'id')
        section.repetition = self._parse_repetition(schema['repetition'])
        section.branching = self._parse_branching(schema['branching'])

        if 'blocks' in schema.keys():
            for block_schema in schema['blocks']:
                section.add_block(self._parse_block(block_schema))

        return section

    def _parse_repetition(self, schema):
        pass

    def _parse_branching(self, schema):
        pass

    def _parse_block(self, schema):
        block = Block()

        block.id = self._get_required_string(schema, 'id')
        block.repetition = self._parse_repetition(schema['repetition'])
        block.branching = self._parse_branching(schema['branching'])

        if 'questions' in schema.keys():
            for question in schema['questions']:
                block.add_question(self._parse_question(question))

        return block

    def _parse_question(self, schema):
        parser = QuestionParser(schema)
        return parser.parse()

    # checks the schema version, throws an exception if incorrect
    def _check_version(self, schema):
        if "schema" in schema.keys():
            if self._version != schema["schema"]:
                raise SchemaParserException("Incorrect version: Parser expecting {version}".format(version=self._version))
        else:
            raise SchemaParserException("No version found in schema")
