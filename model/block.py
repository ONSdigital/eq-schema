class Block(object):
    def __init__(self, id, title, question_groups=[]):
        self.id = id
        self.title = title
        self.question_groups = question_groups
        