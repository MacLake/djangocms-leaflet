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
## Usage

Add a map plugin to a placeholder and fill in the form. Add markers as sub plugins if needed.
In the template `src/djangocms_leaflet/templates/djangocms_leaflet/map.html` the tile server
of the OpenStreetMap website is defined. Make sure you comply with their usage policy or
use another tile server by replacing the tile server’s URL.

## License

`djangocms-leaflet` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.

## Integrated library

| Name                                                   | Description                | License                                                                       |
|--------------------------------------------------------|-----------------------------|-------------------------------------------------------------------------------|
| [Leaflet](https://leafletjs.com/)                      | JavaScript library for maps | [BSD-2-Clause license](https://github.com/Leaflet/Leaflet/blob/main/LICENSE)  |

