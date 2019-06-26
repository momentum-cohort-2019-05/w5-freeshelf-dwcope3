from django.db import migrations
from django.conf import settings
import csv
import os

def data_pull(apps, schema_editor):
    Book = apps.get_model('core', 'Book')
    Author = apps.get_model('core', 'Author')

    filename = os.path.join(settings.BASE_DIR, 'sample_books.csv')

    with open(filename) as file:
        reader = csv.DictReader(file)
        for row in reader:
            author = Author(name=row['author'],)
            author.save()
            book =  Book(title=row['title'], url=row['url'], description=row['description'], author=author)
            book.save()


def do_nothing(apps, schema_editor):
    pass



class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(data_pull, do_nothing)
    ]

