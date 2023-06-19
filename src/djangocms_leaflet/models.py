from cms.models import CMSPlugin
from django.db import models
from django.utils.translation import gettext as _


class Map(CMSPlugin):
    """Map with name and location, optionally with a marker set in the centre"""
    name = models.CharField(verbose_name=_('name'), blank=True, max_length=100)
    latitude = models.FloatField(
        verbose_name=_('latitude'), help_text=_('in °')
    )
    longitude = models.FloatField(
        verbose_name=_('longitude'), help_text=_('in °')
    )
    zoom_level = models.PositiveSmallIntegerField(
        verbose_name=_('zoom level'), help_text=_('0…18'), default=10
    )
    height = models.PositiveSmallIntegerField(
        verbose_name=_('height of map'), help_text=_('in px'), default=400
    )
    set_marker = models.BooleanField(
        verbose_name=_('set marker'),
        help_text=_('Set marker with name at the centre'),
        default=400
    )

    def __str__(self):
        return (
            self.name if self.name else
            f'{self.latitude}° {self.longitude}°, zoom {self.zoom_level}'
        )


class Marker(CMSPlugin):
    """Marker that can be added to a map"""
    name = models.CharField(verbose_name=_('name'), max_length=100)
    latitude = models.FloatField(verbose_name=_('latitude'))
    longitude = models.FloatField(verbose_name=_('longitude'))

    def __str__(self):
        return (
            self.name if self.name else
            f'{self.latitude}° {self.longitude}°, zoom {self.zoom_level}'
        )
