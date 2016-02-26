class Field(object):
    def __init__(self, id, q_code):
        self.id = id
        self.q_code = q_code


class NumericField(Field):
    def __init__(self, id, q_code):
        super().__init__(id, q_code)

