from eq.parser.schema_parser_exception import SchemaParserException

class Parser(object):

    # gets the value associated with key in the dict, or throws an exception if it's not present
    @staticmethod
    def _get_required(obj, key):
        if key in obj.keys():
            return obj[key]
        else:
            raise SchemaParserException("Required field '{field}' missing in object".format(field=key))

    # gets the required string, and throws an exception if not present or not a string
    @staticmethod
    def _get_required_string(obj, key):
        value = Parser._get_required(obj, key)
        if isinstance(value, basestring):    # basestring is base class of str and unicode
            return value
        else:
            raise SchemaParserException("Required string '{field}' is not a string".format(field=key))

    # gets the required integer and casts it to an integer.  Throws an exception if it is missing or not an int
    @staticmethod
    def _get_required_integer(obj, key):
        value = Parser._get_required(obj, key)
        if isinstance(value, int):
            return int(value)
        else:
            raise SchemaParserException("Required integer '{field}' is not an integer".format(field=key))
