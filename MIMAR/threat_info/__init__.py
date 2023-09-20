from otree.api import *

doc = """
Threat manipulation
"""

# FUNCTIONS
### Balanced randomization of participants into four experimental conditions
def creating_session(subsession):
    import itertools
    treatments = itertools.cycle(["pos_threat", "pos_no_threat", "neg_threat", "neg_no_threat"])
    for player in subsession.get_players():
        participant = player.participant
        participant.treatment = next(treatments)

# MODELS
class C(BaseConstants):
    NAME_IN_URL = 'threat_info'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    treatment = models.IntegerField()

# PAGES
class ThreatYes(Page):
    form_model = 'player'
    ### Display only to threat codnitions
    @staticmethod
    def is_displayed(player: Player):
        return player.participant.treatment == "pos_threat" or player.participant.treatment == "neg_threat"

class ThreatNo(Page):
    form_model = 'player'
    ### Display only to no threat codnitions
    @staticmethod
    def is_displayed(player: Player):
        return player.participant.treatment == "pos_no_threat" or player.participant.treatment == "neg_no_threat"

page_sequence = [ThreatYes, ThreatNo]