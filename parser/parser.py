import json
from model.questionnaire import Questionnaire
from model.section import Section
from model.block import Block
from model.question_group import QuestionGroup
from model.question import SimpleValueQuestion
from model.content import Content
from model.field import Field, NumericField


class Parser(object):
    def __init__(self, schema):
        self.schema = json.loads(schema)
        print(self.schema)
        self.questionnaire = self.__create_questionnaire()

    def __create_questionnaire(self):
        questionnaire = self.schema
        schema_version = self.__create(questionnaire, "schema_version")
        questionnaire_id = self.__create(questionnaire, "questionnaire_id")
        survey_id = self.__create(questionnaire, "survey_id")
        language_code = self.__create(questionnaire, "language_code")
        title = self.__create(questionnaire, "title")
        description = self.__create(questionnaire, "description")
        sections = self.__create_sections(self.__create(questionnaire, "sections"))

        return Questionnaire(schema_version=schema_version, questionnaire_id=questionnaire_id, survey_id=survey_id,
                             language_code=language_code, title=title, description=description, sections=sections)

    def __create_sections(self, sections_schema):
        sections = []
        for section_schema in sections_schema:
            section = self.__create_section(section_schema)
            sections.append(section)
        return sections

    def __create_section(self, section_schema):
        id = self.__create(section_schema, "id")
        title = self.__create(section_schema, "title")
        blocks = self.__create_blocks(self.__create(section_schema, "blocks"))
        return Section(id=id, title=title, blocks=blocks)

    def __create_blocks(self, blocks_schema):
        blocks = []
        for block_schema in blocks_schema:
            block = self.__create_block(block_schema)
            blocks.append(block)
        return blocks

    def __create_block(self,  block_schema):
        id = self.__create(block_schema, "id")
        title = self.__create(block_schema, "title")
        question_groups = self.__create_question_groups(self.__create(block_schema, "question_groups"))
        return Block(id=id, title=title, question_groups=question_groups)

    def __create_question_groups(self, question_groups_schema):
        question_groups = []
        for question_group_schema in question_groups_schema:
            question_group = self.__create_question_group(question_group_schema)
            question_groups.append(question_group)
        return question_groups

    def __create_question_group(self,  question_group_schema):
        id = self.__create(question_group_schema, "id")
        title = self.__create(question_group_schema, "title")
        questions = self.__create_questions(self.__create(question_group_schema, "questions"))
        return QuestionGroup(id=id, title=title, questions=questions)

    def __create_questions(self, questions_schema):
        questions = []
        for question_schema in questions_schema:
            question = self.__create_question(question_schema)
            questions.append(question)
        return questions

    def __create_question(self, question_schema):
        id = self.__create(question_schema, "id")
        type = self.__create(question_schema, "type")
        content = self.__create_content(self.__create(question_schema, "content"))
        fields = self.__create_fields(self.__create(question_schema, "fields"))
        if type == "SimpleValueQuestion":
            return SimpleValueQuestion(id=id, content=content, fields=fields)

    def __create_content(self, content_schema):
        label = self.__create(content_schema, "label")
        guidance = self.__create(content_schema, "guidance")
        return Content(label=label, guidance=guidance)

    def __create_fields(self, fields_schema):
        fields = []
        for field_schema in fields_schema:
            field = self.__create_field(field_schema)
            fields.append(field)
        return fields

    def __create_field(self, field_schema):
        id = self.__create(field_schema, "id")
        q_code = self.__create(field_schema, "q_code")
        type = self.__create(field_schema, "type")
        if type == "NumericField":
            return NumericField(id=id, q_code=q_code)
        else:
            return Field(id=id, q_code=q_code)

    def __create(self, schema, field):
        print("Parsing field " + field)
        value = schema[field]
        if isinstance(value, str):
            print("Value " + value)
        return value
