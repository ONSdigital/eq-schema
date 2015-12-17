from eq.parser.parser import Parser
from eq.parser.schema_parser_exception import SchemaParserException
from eq.model.field_factory import FieldFactory

class FieldParser(Parser):

    def parse(self, schema):
        if 'type' in schema.keys():
            field = FieldFactory.create_field(schema['type'])

            if 'code' in schema.keys():
                field.set_code(self._get_required_integer(schema, 'code'))

            if 'label' in schema.keys():
                field.set_label(self._get_required_string(schema, 'label'))

            return field

        else:
            raise SchemaParserException('Field must have a type')
