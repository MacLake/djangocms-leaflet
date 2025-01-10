import requests
from cms.models import CMSPlugin
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext as _


class Geocode(CMSPlugin):
    _name = models.CharField(verbose_name=_('name'), blank=True, max_length=100)
    location_search_term = models.CharField(
        verbose_name=_('location search term'),
        blank=True,
        max_length=100,
        help_text=_(
            'Instead of coordinates you can enter the address or a search term, and Nominatim will try to look up the '
            'location. The first hit of the list will be used.'
        ),
    )
    latitude = models.FloatField(
        blank=True, verbose_name=_('latitude'), help_text=_('in °')
    )
    longitude = models.FloatField(
        blank=True,
        verbose_name=_('longitude in °'),
        help_text=_(
            'in °<br>If you enter both latitude and longitude, these data won’t be overridden by a geocode lookup.'
        ),
    )

    @property
    def name(self):
        return self._name if self._name else self.location_search_term

    class Meta:
        abstract = True

    def clean(self):
        if (
            self.latitude is None or self.longitude is None
        ) and self.location_search_term == '':
            raise ValidationError(
                _(
                    'If you don’t specify latitude and longitude, you need to enter a search term for the location.'
                )
            )
        if self.location_search_term and (
            self.latitude is None or self.longitude is None
        ):
            headers = {'user-agent': 'djangocms-leaflet'}
            payload: dict[str, str] = {
                'q': self.location_search_term,
                'format': 'jsonv2'
            }
            response: requests.Response = requests.get(
                'https://nominatim.openstreetmap.org/search',
                headers=headers,
                params=payload
            )
            geo_json: list[dict[str, any]] = response.json()
            try:
                self.latitude = geo_json[0]['lat']
                self.longitude = geo_json[0]['lon']
            except IndexError:
                raise ValidationError(_('Location not found.'))


class Map(Geocode):
    """Map with name and location, optionally with a marker set in the centre"""

    zoom_level = models.PositiveSmallIntegerField(
        verbose_name=_('zoom level'), help_text=_('0…18'), default=10
    )
    height = models.PositiveSmallIntegerField(
        verbose_name=_('height of map'), help_text=_('in px'), default=400
    )
    set_marker = models.BooleanField(
        verbose_name=_('set marker'),
        help_text=_('Set marker with name at the centre'),
        default=True
    )

    def __str__(self) -> str:
        return (
            self.name if self.name else
            self.location_search_term if self.location_search_term else
            f'{self.latitude}° {self.longitude}°, zoom {self.zoom_level}'
        )


class Marker(Geocode):
    """Marker that can be added to a map"""
    def __str__(self) -> str:
        return (
            self.name if self.name else self.location_search_term if
            self.location_search_term else f'{self.latitude}° {self.longitude}°'
        )
