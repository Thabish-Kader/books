# Generated by Django 3.1.14 on 2022-07-01 10:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_book_cover'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'permissions': [('special_status', 'Can read alll books')]},
        ),
    ]
