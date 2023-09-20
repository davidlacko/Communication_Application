from otree.api import *

doc = """
Slider slide
"""

# MODELS
class Constants(BaseConstants):
    name_in_url = 'slider'
    players_per_group = None
    num_rounds = 1

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    Roma = models.FloatField(blank=True)
    Vietnam = models.IntegerField(blank=True)
    Slovak = models.IntegerField(blank=True)
    Czech = models.IntegerField(blank=True)
    Left = models.IntegerField(blank=True)
    Right = models.IntegerField(blank=True)
    Christ = models.IntegerField(blank=True)
    Muslim = models.IntegerField(blank=True)
    Buddhism = models.IntegerField(blank=True)
    Atheist = models.IntegerField(blank=True)

# PAGES
class SliderPage(Page):
    form_model = 'player'
    form_fields = ['Roma', 'Vietnam',"Slovak","Czech","Left","Right","Christ","Muslim","Buddhism","Atheist"]

page_sequence = [SliderPage]