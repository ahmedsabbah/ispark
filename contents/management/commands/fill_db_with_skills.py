from django.core.management.base import BaseCommand
from contents.models import Skill
import os
from ispark.settings import BASE_DIR
class Command(BaseCommand):

    def handle(self, *args, **options):
        with open(os.path.join(BASE_DIR, 'skills.txt'), "r") as file:
            print "Filling database with skills.."
            for line in file:
                skill = Skill(name=line)
                skill.save()
            print "Done.."
