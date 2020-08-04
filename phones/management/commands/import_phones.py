import csv

from main import settings
from django.core.management.base import BaseCommand
from django.utils.text import slugify
from phones.models import Phone
from datetime import datetime



class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open(settings.BASE_DIR+'/phones.csv', 'r') as csvfile:

            phone_reader = csv.reader(csvfile, delimiter=';')
            # пропускаем заголовок
            next(phone_reader)
            for line in phone_reader:
                # TODO: Добавьте сохранение модели
                phone = Phone()
                phone.name=line[1]
                phone.price=line[3]
                phone.image=line[2]
                phone.release_date=datetime.strptime(line[4], '%Y-%m-%d')
                phone.lte_exists=line[5]
                phone.slug=phone.name.split()[0]
                phone.slug = slugify(phone.name)
                phone.save()
