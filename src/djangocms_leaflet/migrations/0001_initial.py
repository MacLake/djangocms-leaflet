# Generated by Django 2.2.10 on 2020-02-07 19:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cms', '0022_auto_20180620_1551'),
    ]

    operations = [
        migrations.CreateModel(
            name='Map',
            fields=[
                (
                    'cmsplugin_ptr',
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        related_name='djangocms_leaflet_map',
                        serialize=False,
                        to='cms.CMSPlugin'
                    )
                ),
                (
                    'name',
                    models.CharField(
                        blank=True, max_length=100, verbose_name='name'
                    )
                ),
                ('latitude', models.FloatField(verbose_name='latitude')),
                ('longitude', models.FloatField(verbose_name='longitude')),
                (
                    'zoom_level',
                    models.PositiveSmallIntegerField(
                        default=10, help_text='0…21', verbose_name='zoom level'
                    )
                ),
                (
                    'height',
                    models.PositiveSmallIntegerField(
                        default=400,
                        help_text='in px',
                        verbose_name='height of map'
                    )
                ),
                (
                    'set_marker',
                    models.BooleanField(
                        default=400,
                        help_text='Set marker with name at the centre',
                        verbose_name='set marker'
                    )
                ),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin', ),
        ),
        migrations.CreateModel(
            name='Marker',
            fields=[
                (
                    'cmsplugin_ptr',
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        related_name='djangocms_leaflet_marker',
                        serialize=False,
                        to='cms.CMSPlugin'
                    )
                ),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('latitude', models.FloatField(verbose_name='latitude')),
                ('longitude', models.FloatField(verbose_name='longitude')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin', ),
        ),
    ]