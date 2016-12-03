import os

DESCRIPTION = ('Pulsar - asynchronous framework for python 3')
AUTHENTICATION_BACKENDS = ['lux.core:SimpleBackend']
CONTENT_REPO = os.path.dirname(os.path.dirname(__file__))
API_URL = '/api'
APP_NAME = 'PulsarWeb'
HTML_TITLE = 'Pulsar'
DEFAULT_CONTENT_TYPE = 'text/html'
EXTENSIONS = [
    'lux.extensions.sitemap',
    'lux.extensions.rest',
    'lux.extensions.content',
    'lux.extensions.oauth'
]

CONTENT_GROUPS = {
    "site": {
        "path": "*",
        "meta": {
            "priority": 1,
            "body_template": "home.html",
            "image": "/giotto-banner.png"
        }
    },
    "context": {}
}


HTML_SCRIPTS = [
    '/require.js',
    '/pulsar.js'
]

HTML_LINKS = [
    "/pulsar.css",
    {"rel": "apple-touch-icon", "sizes": "57x57", "href": "/icons/apple-icon-57x57.png"},
    {"rel": "apple-touch-icon", "sizes": "57x57", "href": "/icons/apple-icon-57x57.png"},
    {"rel": "apple-touch-icon", "sizes": "60x60", "href": "/icons/apple-icon-60x60.png"},
    {"rel": "apple-touch-icon", "sizes": "72x72", "href": "/icons/apple-icon-72x72.png"},
    {"rel": "apple-touch-icon", "sizes": "76x76", "href": "/icons/apple-icon-76x76.png"},
    {"rel": "apple-touch-icon", "sizes": "114x114", "href": "/icons/apple-icon-114x114.png"},
    {"rel": "apple-touch-icon", "sizes": "120x120", "href": "/icons/apple-icon-120x120.png"},
    {"rel": "apple-touch-icon", "sizes": "144x144", "href": "/icons/apple-icon-144x144.png"},
    {"rel": "apple-touch-icon", "sizes": "152x152", "href": "/icons/apple-icon-152x152.png"},
    {"rel": "apple-touch-icon", "sizes": "180x180", "href": "/icons/apple-icon-180x180.png"},
    {"rel": "apple-touch-icon", "sizes": "152x152", "href": "/icons/apple-icon-152x152.png"},
    {"rel": "apple-touch-icon", "sizes": "152x152", "href": "/icons/apple-icon-152x152.png"},
    {"rel": "icon", "type": "image/png", "sizes": "16x16", "href": "/icons/favicon-16x16.png"},
    {"rel": "icon", "type": "image/png", "sizes": "32x32", "href": "/icons/favicon-32x32.png"},
    {"rel": "icon", "type": "image/png", "sizes": "96x96", "href": "/icons/favicon-96x96.png"},
    {"rel": "icon", "type": "image/png", "sizes": "192x192", "href": "/icons/android-icon-192x192.png"},
    {"rel": "manifest", "href": "/icons/manifest.json"}
]
HTML_META = [
    {'http-equiv': 'X-UA-Compatible', 'content': 'IE=edge'},
    {'name': 'viewport', 'content': 'width=device-width, initial-scale=1'},
    {'name': 'msapplication-TileColor', 'content': '#ffffff'},
    {'name': 'msapplication-TileImage', 'content': '/icons/ms-icon-144x144.png'},
    {'name': 'theme-color', 'content': '#ffffff'},
    {'name': 'description', 'content': DESCRIPTION}
]

OAUTH_PROVIDERS = {
    'google': {'analytics_id': 'UA-54439804-4'},
    'twitter': {'site': '@quantmind'}
}

CONTENT_LINKS = {
    'd3': 'https://d3js.org/',
    'd3js': 'https://d3js.org/'
}

workers = 0
