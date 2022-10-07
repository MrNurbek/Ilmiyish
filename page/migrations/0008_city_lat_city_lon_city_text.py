# Generated by Django 4.1.1 on 2022-10-05 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0007_rename_category_product_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='lat',
            field=models.FloatField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='city',
            name='lon',
            field=models.FloatField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='city',
            name='text',
            field=models.CharField(blank=True, max_length=1024, null=True),
        ),
    ]
