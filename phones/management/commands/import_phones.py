import csv

from django.core.management.base import BaseCommand
from phones.models import Phone
from datetime import datetime
import requests


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('/home/dell-ubuntu/Документы/Python/django/Phones/phones.csv', 'r') as csvfile:

            phone_reader = csv.reader(csvfile, delimiter=';')
            # пропускаем заголовок
            next(phone_reader)
            for line in phone_reader:
                # TODO: Добавьте сохранение модели
                phone = Phone()
                phone.name=line[1]
                phone.price=line[3]
                phone.image=line[2]
                with open(f'media/{phone.name}.jpeg', 'bw') as img:
                    data = requests.get(phone.image)
                    img.write(data.content)
                phone.release_date=datetime.strptime(line[4], '%Y-%m-%d')
                phone.lte_exists=line[5]
                phone.slug=phone.name.split()[0]
                phone.save()


# test = Command()
# test.handle()test = Command()
# test.handle()