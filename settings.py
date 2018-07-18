from os import environ

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

mturk_hit_settings = {
    'keywords': ['bonus', 'study'],
    'title': 'orhun1',
    'description': 'Add a description here',
    'frame_height': 500,
    'preview_template': 'global/MTurkPreview.html',
    'minutes_allotted_per_assignment': 60,
    'expiration_hours': 7*24, # 7 days
    #'grant_qualification_id': 'YOUR_QUALIFICATION_ID_HERE',# to prevent retakes
    'qualification_requirements': []
}

SESSION_CONFIG_DEFAULTS = {
    'real_world_currency_per_point': 1.00,
    'participation_fee': 0.00,
    'doc': "",
    'mturk_hit_settings': mturk_hit_settings,
}

SESSION_CONFIGS = [
    {
       'name': 'orhun1',
       'display_name': 'orhun1',
       'num_demo_participants': 6,
       'app_sequence': ['baseline', 'waitpage', 'game1', 'game2'],
       'lower_bound': 0,
       'upper_bound': 25,
       'min_players': 6,
       'time_limit': 5,
       #'use_browser_bots': True,
    },
    {
       'name': 'baseline',
       'display_name': 'baseline',
       'num_demo_participants': 1,
       'app_sequence': ['baseline'],
       'lower_bound': 0,
       'upper_bound': 10
    },
    {
       'name': 'game1',
       'display_name': 'game 1',
       'num_demo_participants': 3,
       'app_sequence': ['game1'],
       'lower_bound': 0,
       'upper_bound': 10
    },

    {
       'name': 'game2',
       'display_name': 'game 2',
       'num_demo_participants': 3,
       'app_sequence': ['game2'],
       'lower_bound': 0,
       'upper_bound': 10
    },

    {
       'name': 'pilot',
       'display_name': 'pilot',
       'num_demo_participants': 3,
       'app_sequence': ['baseline', 'game1'],
       'lower_bound': 0,
       'upper_bound': 25,
       'min_players': 3,
       'time_limit': 5
    },
]

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = False
POINTS_DECIMAL_PLACES = 2

ROOMS = []


# AUTH_LEVEL:
# this setting controls which parts of your site are freely accessible,
# and which are password protected:
# - If it's not set (the default), then the whole site is freely accessible.
# - If you are launching a study and want visitors to only be able to
#   play your app if you provided them with a start link, set it to STUDY.
# - If you would like to put your site online in public demo mode where
#   anybody can play a demo version of your game, but not access the rest
#   of the admin interface, set it to DEMO.

# for flexibility, you can set it in the environment variable OTREE_AUTH_LEVEL
AUTH_LEVEL = environ.get('OTREE_AUTH_LEVEL')

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')


# Consider '', None, and '0' to be empty/false
DEBUG = (environ.get('OTREE_PRODUCTION') in {None, '', '0'})

DEMO_PAGE_INTRO_HTML = """ """

# don't share this with anybody.
SECRET_KEY = 'f8ho&pte=i&(vr-z0@2dw(z=4z&sg^o=30tjt)$v=lhd3j0dl*'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']
