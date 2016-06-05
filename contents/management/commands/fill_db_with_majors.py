from django.core.management.base import BaseCommand
from contents.models import Category, Major
import os
from ispark.settings import BASE_DIR
class Command(BaseCommand):

    def handle(self, *args, **options):
        with open(os.path.join(BASE_DIR, 'majors.txt'), "r") as file:
            print "Filling database with categories and related majors.."
            while True:
                category_line = file.readline()
                if not category_line.strip():
                    break
                category = Category(name=category_line)
                category.save()

                while True:
                    major_line = file.readline()
                    if not major_line.strip():
                        break
                    major = Major(name=major_line, category=category)
                    major.save()
            print "Done.."
