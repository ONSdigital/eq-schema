from questionnaire_exception import QuestionnaireException
from section import Section

class Questionnaire(object):
    def __init__(self):
        self._sections = []
        self._current_section_index = 0
        self.title = ''
        self.id = 0
        self.description = ''

    def add_section(self, section):
        if isinstance(section, Section):
            section.set_questionnaire(self)
            self._sections.append(section)
        else:
            raise QuestionnaireException("Can only add sections to a questionnaire")

    def remove_section(self, section):
        if section in self._sections:
            self._sections.remove(section)
        else:
            raise QuestionnaireException("Section is not in questionnaire")

    def get_current_section(self):
        if len(self._sections) > self._current_section_index:
            return self._sections[self._current_section_index]
        else:
            raise QuestionnaireException("No current section")

    def has_more_sections(self):
        return len(self._sections) > self._current_section_index + 1

    def next_section(self):
        pass
