class Questionnaire(object):
    def __init__(self, schema_version, questionnaire_id, survey_id, language_code, title, description, sections=[]):
        self.schema_version = schema_version
        self.questionnaire_id = questionnaire_id
        self.survey_id = survey_id
        self.language_code = language_code
        self.title = title
        self.description = description
        self.sections = sections
