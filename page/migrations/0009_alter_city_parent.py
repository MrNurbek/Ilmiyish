# Generated by Django 4.1.1 on 2022-10-05 15:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0008_city_lat_city_lon_city_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='page.city'),
        ),
    ]