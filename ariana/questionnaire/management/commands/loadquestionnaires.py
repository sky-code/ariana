import json
from pathlib import Path

from django.core.management.base import BaseCommand, CommandError
from django.db import transaction

from ariana.questionnaire.models import Questionnaire, QuestionsAnswers


class Command(BaseCommand):
    help = 'Load questionnaires from JSON file'

    missing_args_message = (
        "No questionnaires JSON file specified. Please provide the path of at least "
        "one questionnaires JSON file in the command line."
    )

    def add_arguments(self, parser):
        parser.add_argument('args', metavar='questionnaires', nargs='+', help='questionnaires files.')

    def handle(self, *questionnaires_files, **options):
        with transaction.atomic():
            for questionnaires in questionnaires_files:
                self.load_questionnaires(questionnaires)
        self.stdout.write(self.style.SUCCESS('Successfully load questionnaires'))

    def load_questionnaires(self, questionnaires_file):
        path = Path(questionnaires_file)
        questionnaires_json_text = path.read_text()
        questionnaires_json = json.loads(questionnaires_json_text)
        questionnaire = Questionnaire()
        questionnaire.name = questionnaires_json['name']
        root_qa_node = self.create_questions_answers_tree(questionnaires_json['children'], None)
        questionnaire.first_qa = root_qa_node
        questionnaire.save()

    def create_questions_answers_tree(self, node, parent):
        node_title = node['title']
        if parent is None:
            qa = QuestionsAnswers.add_root(title=node_title)
        else:
            qa = parent.add_child(title=node_title)
        children = node.get('children', None)
        if children is None:
            return qa
        elif isinstance(children, list):
            for children_node in children:
                self.create_questions_answers_tree(children_node, qa)
        elif isinstance(children, dict):
            self.create_questions_answers_tree(children, qa)
        else:
            raise CommandError(f'unsupported type for children ({type(children)}) in node {node_title}')
        return qa
