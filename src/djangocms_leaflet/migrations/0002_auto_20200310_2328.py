# Generated by Django 2.2.10 on 2020-03-10 22:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('djangocms_leaflet', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='map',
            name='latitude',
            field=models.FloatField(help_text='in °', verbose_name='latitude'),
        ),
        migrations.AlterField(
            model_name='map',
            name='longitude',
            field=models.FloatField(help_text='in °', verbose_name='longitude'),
        ),
        migrations.AlterField(
            model_name='map',
            name='zoom_level',
            field=models.PositiveSmallIntegerField(
                default=10, help_text='0…18', verbose_name='zoom level'
            ),
        ),
    ]
