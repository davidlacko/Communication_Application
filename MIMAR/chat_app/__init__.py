from otree.api import *

doc = """
Interaction app
"""

# MODELS
class C(BaseConstants):
    NAME_IN_URL = 'chat_app'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    INT1 = models.StringField(label="Do jakých sociálních skupin patříte?", blank=True)
    INT2 = models.StringField(label="Jak se jmenujete?", blank=True)
    INT3 = models.StringField(label="Jaké jsou Vaše zájmy?", blank=True)
    INT4 = models.StringField(label="Jak by měl ideálně vypadat Váš život?", blank=True)
    INT5 = models.StringField(label="Co jste vždycky chtěl/a dělat, ale pravděpodobně to nikdy nebude možné?", blank=True)
    INT6 = models.StringField(label="Pokud byste mohl/a kamkoliv cestovat, kam by to bylo a proč?", blank=True)
    INT7 = models.StringField(label="Co Vás stresuje?", blank=True)
    INT8 = models.StringField(label="Kdybyste u sebe mohl/a změnit jednu věc, co by to bylo?", blank=True)
    INT9 = models.StringField(label="Co Vás na druhých rozčiluje?", blank=True)
    INT10 = models.StringField(label="Je pro Vás obtížné nebo snadné potkávat nové lidi a proč?", blank=True)
    INT11 = models.StringField(label="Máte nějaký zážitek související s nějakým dobrým přítelem/dobrou přítelkyní, který Vás emočně zasáhl?", blank=True)
    INT12 = models.StringField(label="Kdybyste mohl/a mít jedno přání, co by to bylo?", blank=True)
    INT13 = models.StringField(label="Z čeho máte největší strach?", blank=True)
    INT14 = models.StringField(label="Jaká je Vaše nejhorší raná vzpomínka?", blank=True)
    INT15 = models.StringField(label="Máte nějaký úspěch z nedávné doby, na který jste hrdý/á?", blank=True)
    INT16 = models.StringField(label="Jaká je Vaše nejšťastnější vzpomínka z raného dětství?", blank=True)
    INT17 = models.StringField(label="Řekněte svému partnerovi/své partnerce o sobě jednu věc, kterou většina lidí, kteří Vás již znají, neví.", blank=True)
    INT18 = models.StringField(label="Řekněte partnerovi/partnerce, jak jste vnímali interakci.", blank=True)

# PAGES
class ChatOne(Page):
    form_model = 'player'

class Int1_man(Page):
    form_model = 'player'
    form_fields = ["INT1"]
    @staticmethod
    def is_displayed(player: Player):
       return player.participant.gender == "Muž"

class Int1_woman(Page):
    form_model = 'player'
    form_fields = ["INT1"]
    @staticmethod
    def is_displayed(player: Player):
       return player.participant.gender != "Muž"

class Int2_man(Page):
    form_model = 'player'
    form_fields = ["INT2"]
    @staticmethod
    def is_displayed(player: Player):
       return player.participant.gender == "Muž"

class Int2_woman(Page):
    form_model = 'player'
    form_fields = ["INT2"]
    @staticmethod
    def is_displayed(player: Player):
       return player.participant.gender != "Muž"

class Int3_pos_man(Page):
    form_model = 'player'
    form_fields = ["INT3"]
    @staticmethod
    def is_displayed(player: Player):
       return (player.participant.treatment == "pos_threat" or player.participant.treatment == "pos_no_threat") and player.participant.gender == "Muž"

class Int3_pos_woman(Page):
    form_model = 'player'
    form_fields = ["INT3"]
    @staticmethod
    def is_displayed(player: Player):
       return (player.participant.treatment == "pos_threat" or player.participant.treatment == "pos_no_threat") and player.participant.gender != "Muž"

class Int3_neg_man_woman(Page):
    form_model = 'player'
    form_fields = ["INT3"]
    @staticmethod
    def is_displayed(player: Player):
       return player.participant.treatment == "neg_threat" or player.participant.treatment == "neg_no_threat"

class Int4_pos(Page):
    form_model = 'player'
    form_fields = ["INT4"]
    @staticmethod
    def is_displayed(player: Player):
       return player.participant.treatment == "pos_threat" or player.participant.treatment == "pos_no_threat"

class Int4_neg(Page):
    form_model = 'player'
    form_fields = ["INT4"]
    @staticmethod
    def is_displayed(player: Player):
       return player.participant.treatment == "neg_threat" or player.participant.treatment == "neg_no_threat"

class Int5_pos_man(Page):
    form_model = 'player'
    form_fields = ["INT5"]
    @staticmethod
    def is_displayed(player: Player):
       return (player.participant.treatment == "pos_threat" or player.participant.treatment == "pos_no_threat") and player.participant.gender == "Muž"

class Int5_pos_woman(Page):
    form_model = 'player'
    form_fields = ["INT5"]
    @staticmethod
    def is_displayed(player: Player):
       return (player.participant.treatment == "pos_threat" or player.participant.treatment == "pos_no_threat") and player.participant.gender != "Muž"

class Int5_neg_man_woman(Page):
    form_model = 'player'
    form_fields = ["INT5"]
    @staticmethod
    def is_displayed(player: Player):
       return player.participant.treatment == "neg_threat" or player.participant.treatment == "neg_no_threat"

class Int6_neg_man(Page):
    form_model = 'player'
    form_fields = ["INT6"]
    @staticmethod
    def is_displayed(player: Player):
       return (player.participant.treatment == "neg_threat" or player.participant.treatment == "neg_no_threat") and player.participant.gender == "Muž"

class Int6_neg_woman(Page):
    form_model = 'player'
    form_fields = ["INT6"]
    @staticmethod
    def is_displayed(player: Player):
       return (player.participant.treatment == "neg_threat" or player.participant.treatment == "neg_no_threat") and player.participant.gender != "Muž"

class Int6_pos_man_woman(Page):
    form_model = 'player'
    form_fields = ["INT6"]
    @staticmethod
    def is_displayed(player: Player):
       return player.participant.treatment == "pos_threat" or player.participant.treatment == "pos_no_threat"

class Int7_pos(Page):
    form_model = 'player'
    form_fields = ["INT7"]
    @staticmethod
    def is_displayed(player: Player):
       return player.participant.treatment == "pos_threat" or player.participant.treatment == "pos_no_threat"

class Int7_neg(Page):
    form_model = 'player'
    form_fields = ["INT7"]
    @staticmethod
    def is_displayed(player: Player):
       return player.participant.treatment == "neg_threat" or player.participant.treatment == "neg_no_threat"

class Int8_neg(Page):
    form_model = 'player'
    form_fields = ["INT8"]
    @staticmethod
    def is_displayed(player: Player):
       return player.participant.treatment == "neg_threat" or player.participant.treatment == "neg_no_threat"

class Int8_pos(Page):
    form_model = 'player'
    form_fields = ["INT8"]
    @staticmethod
    def is_displayed(player: Player):
       return player.participant.treatment == "pos_threat" or player.participant.treatment == "pos_no_threat"

class Int9_pos(Page):
    form_model = 'player'
    form_fields = ["INT9"]
    @staticmethod
    def is_displayed(player: Player):
       return player.participant.treatment == "pos_threat" or player.participant.treatment == "pos_no_threat"

class Int9_neg(Page):
    form_model = 'player'
    form_fields = ["INT9"]
    @staticmethod
    def is_displayed(player: Player):
       return player.participant.treatment == "neg_threat" or player.participant.treatment == "neg_no_threat"

class Int10_pos(Page):
    form_model = 'player'
    form_fields = ["INT10"]
    @staticmethod
    def is_displayed(player: Player):
       return player.participant.treatment == "pos_threat" or player.participant.treatment == "pos_no_threat"

class Int10_neg(Page):
    form_model = 'player'
    form_fields = ["INT10"]
    @staticmethod
    def is_displayed(player: Player):
       return player.participant.treatment == "neg_threat" or player.participant.treatment == "neg_no_threat"

class Int11_pos(Page):
    form_model = 'player'
    form_fields = ["INT11"]
    @staticmethod
    def is_displayed(player: Player):
       return player.participant.treatment == "pos_threat" or player.participant.treatment == "pos_no_threat"

class Int11_neg(Page):
    form_model = 'player'
    form_fields = ["INT11"]
    @staticmethod
    def is_displayed(player: Player):
       return player.participant.treatment == "neg_threat" or player.participant.treatment == "neg_no_threat"

class Int12_neg(Page):
    form_model = 'player'
    form_fields = ["INT12"]
    @staticmethod
    def is_displayed(player: Player):
       return player.participant.treatment == "neg_threat" or player.participant.treatment == "neg_no_threat"

class Int12_pos(Page):
    form_model = 'player'
    form_fields = ["INT12"]
    @staticmethod
    def is_displayed(player: Player):
       return player.participant.treatment == "pos_threat" or player.participant.treatment == "pos_no_threat"

class Int13_pos(Page):
    form_model = 'player'
    form_fields = ["INT13"]
    @staticmethod
    def is_displayed(player: Player):
       return player.participant.treatment == "pos_threat" or player.participant.treatment == "pos_no_threat"

class Int13_neg(Page):
    form_model = 'player'
    form_fields = ["INT13"]
    @staticmethod
    def is_displayed(player: Player):
       return player.participant.treatment == "neg_threat" or player.participant.treatment == "neg_no_threat"

class Int14_neg_man_woman(Page):
    form_model = 'player'
    form_fields = ["INT14"]
    @staticmethod
    def is_displayed(player: Player):
       return player.participant.treatment == "neg_threat" or player.participant.treatment == "neg_no_threat"

class Int14_pos_man(Page):
    form_model = 'player'
    form_fields = ["INT14"]
    @staticmethod
    def is_displayed(player: Player):
       return (player.participant.treatment == "pos_threat" or player.participant.treatment == "pos_no_threat") and player.participant.gender == "Muž"

class Int14_pos_woman(Page):
    form_model = 'player'
    form_fields = ["INT14"]
    @staticmethod
    def is_displayed(player: Player):
       return (player.participant.treatment == "pos_threat" or player.participant.treatment == "pos_no_threat") and player.participant.gender != "Muž"

class Int15_pos_man(Page):
    form_model = 'player'
    form_fields = ["INT15"]
    @staticmethod
    def is_displayed(player: Player):
       return (player.participant.treatment == "pos_threat" or player.participant.treatment == "pos_no_threat") and player.participant.gender == "Muž"

class Int15_pos_woman(Page):
    form_model = 'player'
    form_fields = ["INT15"]
    @staticmethod
    def is_displayed(player: Player):
       return (player.participant.treatment == "pos_threat" or player.participant.treatment == "pos_no_threat") and player.participant.gender != "Muž"

class Int15_neg_woman(Page):
    form_model = 'player'
    form_fields = ["INT15"]
    @staticmethod
    def is_displayed(player: Player):
       return (player.participant.treatment == "neg_threat" or player.participant.treatment == "neg_no_threat") and player.participant.gender != "Muž"

class Int15_neg_man(Page):
    form_model = 'player'
    form_fields = ["INT15"]
    @staticmethod
    def is_displayed(player: Player):
       return (player.participant.treatment == "neg_threat" or player.participant.treatment == "neg_no_threat") and player.participant.gender == "Muž"

class Int16_pos(Page):
    form_model = 'player'
    form_fields = ["INT16"]
    @staticmethod
    def is_displayed(player: Player):
       return player.participant.treatment == "pos_threat" or player.participant.treatment == "pos_no_threat"

class Int16_neg(Page):
    form_model = 'player'
    form_fields = ["INT16"]
    @staticmethod
    def is_displayed(player: Player):
       return player.participant.treatment == "neg_threat" or player.participant.treatment == "neg_no_threat"

class Int17_pos(Page):
    form_model = 'player'
    form_fields = ["INT17"]
    @staticmethod
    def is_displayed(player: Player):
       return player.participant.treatment == "pos_threat" or player.participant.treatment == "pos_no_threat"

class Int17_neg(Page):
    form_model = 'player'
    form_fields = ["INT17"]
    @staticmethod
    def is_displayed(player: Player):
       return player.participant.treatment == "neg_threat" or player.participant.treatment == "neg_no_threat"

class Int18_neg(Page):
    form_model = 'player'
    form_fields = ["INT18"]
    @staticmethod
    def is_displayed(player: Player):
       return player.participant.treatment == "neg_threat" or player.participant.treatment == "neg_no_threat"

class Int18_pos(Page):
    form_model = 'player'
    form_fields = ["INT18"]
    @staticmethod
    def is_displayed(player: Player):
       return player.participant.treatment == "pos_threat" or player.participant.treatment == "pos_no_threat"

page_sequence = [ChatOne, Int1_man, Int1_woman, Int2_man, Int2_woman, Int3_pos_woman, Int3_pos_man, Int3_neg_man_woman, Int4_pos, Int4_neg, Int5_pos_man, Int5_pos_woman, Int5_neg_man_woman, Int6_pos_man_woman, Int6_neg_man, Int6_neg_woman, Int7_pos, Int7_neg, Int8_pos, Int8_neg, Int9_pos, Int9_neg, Int10_pos, Int10_neg, Int11_pos, Int11_neg, Int12_pos, Int12_neg, Int13_pos, Int13_neg, Int14_pos_man, Int14_pos_woman, Int14_neg_man_woman, Int15_pos_man, Int15_pos_woman, Int15_neg_man, Int15_neg_woman, Int16_pos, Int16_neg, Int17_pos, Int17_neg, Int18_pos, Int18_neg]