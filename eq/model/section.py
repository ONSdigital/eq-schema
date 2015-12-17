from questionnaire_exception import QuestionnaireException

class Section(object):
    def __init__(self):
        self._questionnaire = None
        self.id = 0
        self._blocks = []
        self._current_block_index = 0

    def add_block(self, block):
        from block import Block     # avoid circular import, Block only needed here
        if isinstance(block, Block):
            self._blocks.append(block)
        else:
            raise QuestionnaireException('Only Block objects can be added to a Section')

    def remove_block(self, block):
        if block in self._blocks:
            self._blocks.remove(block)
        else:
            raise QuestionnaireException("Block is not in Section")

    def get_current_block(self):
        if len(self._blocks) > self._current_block_index:
            return self._blocks[self._current_block_index]
        else:
            raise QuestionnaireException("No current Block")

    def has_more_blocks(self):
        return len(self._blocks) > self._current_block_index + 1

    def next_block(self):
        pass

    def set_questionnaire(self, questionnaire):
        from questionnaire import Questionnaire # avoid circular imports
        if isinstance(questionnaire, Questionnaire):
            self._questionnaire = questionnaire
        else:
            raise QuestionnaireException("Must be an instance of Questionnaire")
