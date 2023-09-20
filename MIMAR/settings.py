from os import environ

# The order of apps
SESSION_CONFIGS = [
    dict(
        name='pre_qre',
        display_name='Dotaznik 1',
        app_sequence=['pre_qre', "sliders", "timing", "threat_info", "chat_app", "post_qre"],
        num_demo_participants=20,
    ),
    dict(
        name='sliders',
        display_name='Slider',
        app_sequence=['pre_qre', "sliders", "timing", "threat_info", "chat_app", "post_qre"],
        num_demo_participants=20,
    ),
    dict(
        name='threat_info',
        display_name='Hrozba',
        app_sequence=['pre_qre', "sliders", "timing", "threat_info", "chat_app", "post_qre"],
        num_demo_participants=20,
        treatment=["pos_threat", "neg_threat", "pos_no_threat", "neg_no_threat"],
    ),
    dict(
        name='timing',
        display_name='Casovac',
        app_sequence=['pre_qre', "sliders", "timing", "threat_info", "chat_app", "post_qre"],
        num_demo_participants=20,
        treatment=["pos_threat", "neg_threat", "pos_no_threat", "neg_no_threat"],
    ),
    dict(
        name='chat_app',
        display_name='chat',
        app_sequence=['pre_qre', "sliders", "timing", "threat_info", "chat_app", "post_qre"],
        num_demo_participants=20,
        treatment=["pos_threat", "neg_threat", "pos_no_threat", "neg_no_threat"],
    ),
    dict(
        name='post_qre',
        display_name='Dotaznik 2',
        app_sequence=['pre_qre', "sliders", "timing", "threat_info", "chat_app", "post_qre"],
        num_demo_participants=20,
        treatment=["pos_threat", "neg_threat", "pos_no_threat", "neg_no_threat"],
    ),
]

SESSION_CONFIG_DEFAULTS = dict(real_world_currency_per_point=1.00, participation_fee=0.00, doc="")

# Variables that are stable across apps (treatmens)
PARTICIPANT_FIELDS = ["treatment", "gender"]
SESSION_FIELDS = []
ROOMS = [
    dict(
        name='mimar_exp',
        display_name='Výzkum internetové komunikace'
    )
]

LANGUAGE_CODE = 'cs'
REAL_WORLD_CURRENCY_CODE = 'CZK'
USE_POINTS = True

ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '2359384111782'