from otree.api import *

doc = """
Informed consent and basic demographic questions
"""
# MODELS
class C(BaseConstants):
    NAME_IN_URL = 'pre_qre'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    is_age = models.BooleanField(label="Výzkumu se mohou účastnit pouze osoby starší 18 let.",
                                 choices=[
                                         [True, "Je mi 18 let nebo více."],
                                         [False, "Je mi méně než 18 let."]])
    is_living = models.BooleanField(label="Výzkumu se mohou účastnit pouze osoby aktuálně žijící v České republice",
                                    choices=[
                                         [True, "V současné době žiji v České republice."],
                                         [False, "V současné době nežiji v České republice."]])
    is_consent = models.BooleanField(label="Pokud jste si přečetli výše uvedené informace a souhlasíte s účastí zaškrtněte prosím příslušné políčko níže a můžete začít.",
                                 choices=[
                                     [True, "Ano, souhlasím s účastí."],
                                     [False, "Ne, nesouhlasím s účastí."]])
    age = models.IntegerField(label="Kolik je Vám let?",
                              min=18, max=99,
                              blank=True)
    gender = models.StringField(label="Jste:",
                                choices=["Muž","Žena","Jiné","Nechci odpovídat"],
                                blank=True)
    education = models.StringField(label="Jaké je Vaše nejvyšší dosažené vzdělání?",
                                   choices=["Základní","Středoškolské bez maturity","Středoškolské s maturitou","Vysokoškolské"],
                                   blank=True)
    etnicity = models.StringField(label="Do jaké etnické skupiny patříte?",
                                  choices=["česká","slovenská","romská","vietnamská", "jiná"])
    politics = models.IntegerField(label="Jaká je Vaše politická orientace?",
                                   widget=widgets.RadioSelectHorizontal,
                                   choices=[[1, 'Levice'],[2, ''],[3, ''],[4, ''],[5, ''],[6, ''],[7, 'Pravice']],
                                   blank=True)
    religion = models.StringField(label="Jaké je Vaše náboženské vyznání?",
                                  choices=["křesťanství","islám","buddhismus","žádné/ateismus","jiné"],
                                  blank=True)

# PAGES
class SurveyOne(Page):
    form_model = "player"
    form_fields = ["is_age","is_living","is_consent"]

class SurveyEnd(Page):
    ### Display only to participants who pass all three mandatory conditions
    @staticmethod
    def is_displayed(player):
        return player.is_age == False or player.is_living == False or player.is_consent == False

class SurveyTwo(Page):
    form_model = "player"
    form_fields = ["age","gender", "education", "etnicity","politics","religion"]
    ### Store the variable gender for next use
    @staticmethod
    def before_next_page(player, timeout_happened):
        player.participant.gender = player.gender

class SurveyEndTwo(Page):
    ### Display only to participants who are Czechs
    @staticmethod
    def is_displayed(player):
        return player.etnicity != "česká"


page_sequence = [SurveyOne, SurveyEnd, SurveyTwo, SurveyEndTwo]