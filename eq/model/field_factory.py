from eq.model.fields.text_field import TextField

class FieldFactory(object):
    @staticmethod
    def create_field(field_type):
        if field_type == 'TextField':
            return TextField(None)
        else:
            raise QuestionnaireException("Unsupoorted field type: {field_type}".format(field_type=field_type))
