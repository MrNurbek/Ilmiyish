# Generated by Django 4.1.1 on 2022-10-04 06:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='location2',
            new_name='location',
        ),
    ]
