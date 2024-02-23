"""
 Add 'selectitem' to the INSTALLED_APPS list
"""
INSTALLED_APPS = [
    ...
    'selectitem',
    ...
]
"""
 Make sure the TEMPLATES configuration includes the app directories loader
"""
TEMPLATES = [
    {
        ...
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        ...
    },
]
"""
 Add a URL pattern for the selectitem app in the main urls.py file if necessary
"""
