from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class DjangocmsLeafletConfig(AppConfig):
    name = 'djangocms_leaflet'
    verbose_name = _('DjangoCMS Leaflet Map')
