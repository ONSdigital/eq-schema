from eq.parser.question_parser import QuestionParser as AbstractQuestionParser

from eq.parser.v0_1.display_conditions_parser import DisplayConditionsParser
from eq.parser.v0_1.display_properties_parser import DisplayPropertiesParser
from eq.parser.v0_1.field_parser import FieldParser

from eq.model.questions.simple_value_question import SimpleValueQuestion
from eq.model.questions.compound_value_question import CompoundValueQuestion

class QuestionParser(AbstractQuestionParser):
    def __init__(self, schema):
        super(QuestionParser, self).__init__(schema)
        self._schema = schema
        self._field_parser = FieldParser()
        self._display_properties_parser = DisplayPropertiesParser()
        self._display_conditions_parser = DisplayConditionsParser()

    def parse(self):
        if 'type' in self._schema.keys():

            question = None

            if self._schema['type'] == 'SimpleValueQuestion':
                question = SimpleValueQuestion()
            elif self._schema['type'] == 'CompoundValueQuestion':
                question = CompoundValueQuestion()
            else:
                raise SchemaParserException("Unknown question type: {q_type}".format(q_type=self._schema['type']))

            if question:
                question.id = self._get_required_string(self._schema, 'id')

                if 'content' in self._schema.keys():
                    content = self._schema['content']

                    question.introduction = self._get_required_string(content, 'introduction')
                    question.body = self._get_required_string(content, 'body')
                    question.hint = self._get_required_string(content, 'hint')

                if 'fields' in self._schema.keys():
                    for field in self._schema['fields']:
                        question.add_field(self._parse_field(field))

                if 'display' in self._schema.keys():
                    display = self._schema['display']
                    if 'conditions' in display.keys():
                        question.set_display_conditions(self._parse_display_conditions(display['conditions']))

                    if 'properties' in display.keys():
                        question.set_display_properties(self._parse_display_properties(display['properties']))

                return question
        else:
            raise SchemaParserException("Question must have a type")

    def _parse_field(self, schema):
        return self._field_parser.parse(schema)

    def _parse_display_properties(self, schema):
        return self._display_properties_parser.parse(schema)

    def _parse_display_conditions(self, schema):
        return self._display_conditions_parser.parse(schema)
