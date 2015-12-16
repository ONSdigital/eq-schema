from eq.model.question import Question
from eq.model.questions.simple_value_question import SimpleValueQuestion
from eq.model.questions.compound_value_question import CompoundValueQuestion

class QuestionFactory(object):

    @staticmethod
    def create_question(question_type):
        types = [
            'SimpleValueQuestion',
            'CompoundValueQuestion'
        ]
        if questionType in types:
            return questionType()
        else:
            raise QuestionnaireException("Unknown question type: {question_type}".format(question_type=question_type))
