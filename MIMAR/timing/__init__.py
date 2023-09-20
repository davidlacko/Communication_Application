from otree.api import *

doc = """
Waiting page
"""

# MODELS
class C(BaseConstants):
    NAME_IN_URL = 'timing'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    pass

# PAGES
class SearchOne(Page):
    form_model = 'player'

page_sequence = [SearchOne]