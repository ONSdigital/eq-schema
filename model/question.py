class Question(object):
    def __init__(self, id, content, fields=[]):
        self.id = id
        self.content = content
        self.fields = fields


class SimpleValueQuestion(Question):
    def __init__(self,  id, content, fields=[]):
        super().__init__(id, content, fields)
