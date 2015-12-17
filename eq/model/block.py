from questionnaire_exception import QuestionnaireException

class Block(object):
    def __init__(self):
        self._section = None
        self._questions = []
        self._current_question_index = 0

    def set_section(self, section):
        from section import Section # avoid circular imports, Section is only needed here
        if isinstance(section, Section):
            self._section = section
        else:
            raise QuestionnaireException("Must be an instance of Section")

    def add_question(self, question):
        from question import Question # avoid circular imports
        if isinstance(question, Question):
            self._questions.append(question)
        else:
            raise QuestionnaireException('Only Question objects can be added to a Block')

    def remove_question(self, question):
        if question in self._questions:
            self._questions.remove(question)
        else:
            raise QuestionnaireException("Question is not in Block")

    def get_current_question(self):
        if len(self._questions) > self._current_question_index:
            return self._questions[self._current_question_index]
        else:
            raise QuestionnaireException("No current question")

    def has_more_questions(self):
        return len(self._questions) > self._current_question_index + 1

    def next_question(self):
        pass
