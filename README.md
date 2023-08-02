# djangocms-leaflet

This app provides plug-ins for the JavaScript map library [Leaflet](https://leafletjs.com/).

[![PyPI - Version](https://img.shields.io/pypi/v/djangocms-leaflet.svg)](https://pypi.org/project/djangocms-leaflet)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/djangocms-leaflet.svg)](https://pypi.org/project/djangocms-leaflet)

-----

**Table of Contents**

- [Installation](#installation)
- [License](#license)

## Installation

```console
pip install djangocms-leaflet
```

or add `djangocms-leaflet` to the dependencies of your project, e. g. in `pyproject.toml`:
```toml
dependencies = [
    # …
    'djangocms-leaflet',
    # …
]
```


Add it to `INSTALLED_APPS` in the settings::

```python
INSTALLED_APPS: list[str] = [
    # …
    'djangocms_leaflet',
    # …
]
```
## Usage

Add a map plugin to a placeholder and fill in the form. Add markers as sub plugins if needed.
In the template `src/djangocms_leaflet/templates/djangocms_leaflet/map.html` the tile server
of the OpenStreetMap website is defined. Make sure you comply with their usage policy or
use another tile server by replacing the tile server’s URL.

You can either specify latitude and longitude of the map or marker or enter a search term.
If no coordinates are entered, they will be searched with Nominatim and the first hit in the result list location will
be used as coordinates.

## License

`djangocms-leaflet` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.

## Integrated library

| Name                                                   | Description                | License                                                                       |
|--------------------------------------------------------|-----------------------------|-------------------------------------------------------------------------------|
| [Leaflet](https://leafletjs.com/)                      | JavaScript library for maps | [BSD-2-Clause license](https://github.com/Leaflet/Leaflet/blob/main/LICENSE)  |

