from otree.api import *

doc = """
Post treatment measurement
"""

# MODELS
class C(BaseConstants):
    NAME_IN_URL = 'post_qre'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    open_interaction = models.LongStringField(label="Chcete výzkumníkům a výzkumnicím ohledně interakce něco sdělit?",
                                          blank=True)
    attention_check1 = models.StringField(label="Z jaké etnické skupiny pocházel/a Váš komunikační partner/Vaše komunikační partnerka?",
                                          blank=True)
    attention_check2 = models.StringField(label="Jakého byl/a pohlaví?",
                                          blank=True)
    interaction1 = models.IntegerField(label="Jak příjemný byl pro Vás způsob, jakým s Vámi Váš komunikační partner/Vaše komunikační partnerka komunikoval/a?",
                                   widget=widgets.RadioSelectHorizontal,
                                   choices=[[1, 'Vůbec ne'],[2, ''],[3, ''],[4, ''],[5, ''],[6, ''],[7, 'Velmi']],
                                   blank=True)
    interaction2 = models.IntegerField(label="Jak nepříjemný byl pro Vás způsob, jakým s Vámi Váš komunikační partner/Vaše komunikační partnerka komunikoval/a?",
                                   widget=widgets.RadioSelectHorizontal,
                                   choices=[[1, 'Vůbec ne'],[2, ''],[3, ''],[4, ''],[5, ''],[6, ''],[7, 'Velmi']],
                                   blank=True)
    Vietnam2 = models.IntegerField(blank=True)
    behav_tend1 = models.IntegerField(label="jít s nimi do konfliktu?",
                                   widget=widgets.RadioSelectHorizontal,
                                   choices=[[1, 'Vůbec ne'],[2, ''],[3, ''],[4, ''],[5, ''],[6, ''],[7, 'Velmi']],
                                   blank=True)
    behav_tend2 = models.IntegerField(label="jim odporovat (např. při diskuzi)?",
                                   widget=widgets.RadioSelectHorizontal,
                                   choices=[[1, 'Vůbec ne'],[2, ''],[3, ''],[4, ''],[5, ''],[6, ''],[7, 'Velmi']],
                                   blank=True)
    behav_tend3 = models.IntegerField(label="se s nimi hádat?",
                                   widget=widgets.RadioSelectHorizontal,
                                   choices=[[1, 'Vůbec ne'],[2, ''],[3, ''],[4, ''],[5, ''],[6, ''],[7, 'Velmi']],
                                   blank=True)
    behav_tend4 = models.IntegerField(label="se jim vyhýbat?",
                                   widget=widgets.RadioSelectHorizontal,
                                   choices=[[1, 'Vůbec ne'],[2, ''],[3, ''],[4, ''],[5, ''],[6, ''],[7, 'Velmi']],
                                   blank=True)
    behav_tend5 = models.IntegerField(label="s nimi nemít nic společného?",
                                   widget=widgets.RadioSelectHorizontal,
                                   choices=[[1, 'Vůbec ne'],[2, ''],[3, ''],[4, ''],[5, ''],[6, ''],[7, 'Velmi']],
                                   blank=True)
    behav_tend6 = models.IntegerField(label="si od nich držet odstup?",
                                   widget=widgets.RadioSelectHorizontal,
                                   choices=[[1, 'Vůbec ne'],[2, ''],[3, ''],[4, ''],[5, ''],[6, ''],[7, 'Velmi']],
                                   blank=True)
    behav_tend7 = models.IntegerField(label="s nimi mluvit?",
                                   widget=widgets.RadioSelectHorizontal,
                                   choices=[[1, 'Vůbec ne'],[2, ''],[3, ''],[4, ''],[5, ''],[6, ''],[7, 'Velmi']],
                                   blank=True)
    behav_tend8 = models.IntegerField(label="si o nich zjistit více informací?",
                                   widget=widgets.RadioSelectHorizontal,
                                   choices=[[1, 'Vůbec ne'],[2, ''],[3, ''],[4, ''],[5, ''],[6, ''],[7, 'Velmi']],
                                   blank=True)
    behav_tend9 = models.IntegerField(label="s nimi trávit čas?",
                                   widget=widgets.RadioSelectHorizontal,
                                   choices=[[1, 'Vůbec ne'],[2, ''],[3, ''],[4, ''],[5, ''],[6, ''],[7, 'Velmi']],
                                   blank=True)
    accult_stra_a1 = models.IntegerField(label="Vietnamci a Vietnamky žijící v ČR by si měli uchovat svou vlastní kulturu.",
                                   widget=widgets.RadioSelectHorizontal,
                                   choices=[[1, 'Rozhodně nesouhlasím'],[2, ''],[3, ''],[4, ''],[5, ''],[6, ''],[7, 'Rozhodně souhlasím']],
                                   blank=True)
    accult_stra_a2 = models.IntegerField(label="Vietnamci a Vietnamky žijící v ČR by si měli uchovat své vlastní náboženství.",
                                   widget=widgets.RadioSelectHorizontal,
                                   choices=[[1, 'Rozhodně nesouhlasím'],[2, ''],[3, ''],[4, ''],[5, ''],[6, ''],[7, 'Rozhodně souhlasím']],
                                   blank=True)
    accult_stra_a3 = models.IntegerField(label="Vietnamci a Vietnamky žijící v ČR by si měli uchovat svůj vlastní jazyk.",
                                   widget=widgets.RadioSelectHorizontal,
                                   choices=[[1, 'Rozhodně nesouhlasím'],[2, ''],[3, ''],[4, ''],[5, ''],[6, ''],[7, 'Rozhodně souhlasím']],
                                   blank=True)
    accult_stra_a4 = models.IntegerField(label="Vietnamci a Vietnamky žijící v ČR by si měli uchovat svůj vlastní způsob života.",
                                   widget=widgets.RadioSelectHorizontal,
                                   choices=[[1, 'Rozhodně nesouhlasím'],[2, ''],[3, ''],[4, ''],[5, ''],[6, ''],[7, 'Rozhodně souhlasím']],
                                   blank=True)
    accult_stra_a5 = models.IntegerField(label="Vietnamci a Vietnamky žijící v ČR by si měli uchovat své vlastní zvyky a tradice.",
                                   widget=widgets.RadioSelectHorizontal,
                                   choices=[[1, 'Rozhodně nesouhlasím'],[2, ''],[3, ''],[4, ''],[5, ''],[6, ''],[7, 'Rozhodně souhlasím']],
                                   blank=True)
    accult_stra_a6 = models.IntegerField(label="Vietnamci a Vietnamky žijící v ČR by měli vychovávat své děti tak, jak je to ve Vietnamu obvyklé.",
                                   widget=widgets.RadioSelectHorizontal,
                                   choices=[[1, 'Rozhodně nesouhlasím'],[2, ''],[3, ''],[4, ''],[5, ''],[6, ''],[7, 'Rozhodně souhlasím']],
                                   blank=True)
    accult_stra_a7 = models.IntegerField(label="Vietnamci a Vietnamky žijící v ČR by měli zůstat opravdovými Vietnamci.",
                                   widget=widgets.RadioSelectHorizontal,
                                   choices=[[1, 'Rozhodně nesouhlasím'],[2, ''],[3, ''],[4, ''],[5, ''],[6, ''],[7, 'Rozhodně souhlasím']],
                                   blank=True)
    accult_stra_b1 = models.IntegerField(label="Vietnamci a Vietnamky žijící v ČR by měli převzít českou kulturu.",
                                         widget=widgets.RadioSelectHorizontal,
                                         choices=[[1, 'Rozhodně nesouhlasím'], [2, ''], [3, ''], [4, ''], [5, ''],[6, ''], [7, 'Rozhodně souhlasím']],
                                         blank=True)
    accult_stra_b2 = models.IntegerField(label="Vietnamci a Vietnamky žijící v ČR by měli přijmout náboženství vyznávaná Čechy.",
                                         widget=widgets.RadioSelectHorizontal,
                                         choices=[[1, 'Rozhodně nesouhlasím'], [2, ''], [3, ''], [4, ''], [5, ''],[6, ''], [7, 'Rozhodně souhlasím']],
                                         blank=True)
    accult_stra_b3 = models.IntegerField(label="Vietnamci a Vietnamky žijící v ČR by měli mluvit česky.",
                                         widget=widgets.RadioSelectHorizontal,
                                         choices=[[1, 'Rozhodně nesouhlasím'], [2, ''], [3, ''], [4, ''], [5, ''],[6, ''], [7, 'Rozhodně souhlasím']],
                                         blank=True)
    accult_stra_b4 = models.IntegerField(label="Vietnamci a Vietnamky žijící v ČR by měli převzít způsob života obvyklý u Čechů.",
                                         widget=widgets.RadioSelectHorizontal,
                                         choices=[[1, 'Rozhodně nesouhlasím'], [2, ''], [3, ''], [4, ''], [5, ''],[6, ''], [7, 'Rozhodně souhlasím']],
                                         blank=True)
    accult_stra_b5 = models.IntegerField(label="Vietnamci a Vietnamky žijící v ČR by měli převzít zvyky a tradice Čechů.",
                                         widget=widgets.RadioSelectHorizontal,
                                         choices=[[1, 'Rozhodně nesouhlasím'], [2, ''], [3, ''], [4, ''], [5, ''],[6, ''], [7, 'Rozhodně souhlasím']],
                                         blank=True)
    accult_stra_b6 = models.IntegerField(label="Vietnamci a Vietnamky žijící v ČR by měli vychovávat své děti způsobem obvyklým v ČR.",
                                         widget=widgets.RadioSelectHorizontal,
                                         choices=[[1, 'Rozhodně nesouhlasím'], [2, ''], [3, ''], [4, ''], [5, ''], [6, ''],[7, 'Rozhodně souhlasím']],
                                         blank=True)
    accult_stra_b7 = models.IntegerField(label="Vietnamci a Vietnamky žijící v ČR by se měli stát skutečnými Čechy.",
                                         widget=widgets.RadioSelectHorizontal,
                                         choices=[[1, 'Rozhodně nesouhlasím'], [2, ''], [3, ''], [4, ''], [5, ''],[6, ''], [7, 'Rozhodně souhlasím']],
                                         blank=True)
    contact_freq = models.IntegerField(label="Jak často se setkáváte s Vietnamci a Vietnamkami, přičemž mezi Vámi dochází k bližšímu kontaktu např. rozhovor, podání ruky?",
                                         widget=widgets.RadioSelectHorizontal,
                                         choices=[[1, 'Nikdy'], [2, 'Zřídka'], [3, 'Občas'], [4, 'Často'], [5, 'Velmi často']],
                                         blank=True)
    contact_pos = models.IntegerField(label="Jak často jsou Vaše zkušenosti s Vietnamci a Vietnamkami žijícími v České republice pozitivní?",
                                         widget=widgets.RadioSelectHorizontal,
                                         choices=[[1, 'Nikdy'], [2, 'Zřídka'], [3, 'Občas'], [4, 'Často'], [5, 'Velmi často']],
                                         blank=True)
    contact_neg = models.IntegerField(label="Jak často jsou Vaše zkušenosti s Vietnamci a Vietnamkami žijícími v České republice negativní?",
                                         widget=widgets.RadioSelectHorizontal,
                                         choices=[[1, 'Nikdy'], [2, 'Zřídka'], [3, 'Občas'], [4, 'Často'], [5, 'Velmi často']],
                                         blank=True)
    contact_freq2 = models.IntegerField(label="Kolik máte vietnamských kamarádek/kamarádů? Odpovězte, prosím, číslem:",
                                        min=0, max=50,
                                        blank=True)
    contact_mass_pos = models.IntegerField(label="Jak často slýcháte z masmédií pozitivní informace o Vietnamcích a Vietnamkách žijících v České republice?",
                                         widget=widgets.RadioSelectHorizontal,
                                         choices=[[1, 'Nikdy'], [2, 'Zřídka'], [3, 'Občas'], [4, 'Často'], [5, 'Velmi často']],
                                         blank=True)
    contact_mass_neg = models.IntegerField(label="Jak často slýcháte z masmédií negativní informace o Vietnamcích a Vietnamkách žijících v České republice?",
                                         widget=widgets.RadioSelectHorizontal,
                                         choices=[[1, 'Nikdy'], [2, 'Zřídka'], [3, 'Občas'], [4, 'Často'], [5, 'Velmi často']],
                                         blank=True)
    threat1 = models.IntegerField(label="Vietnamci a Vietnamky žijící v ČR se snaží vylepšit svoji ekonomickou situaci na úkor Čechů. ",
                                         widget=widgets.RadioSelectHorizontal,
                                         choices=[[1, 'Rozhodně nesouhlasím'], [2, ''], [3, ''], [4, ''], [5, ''],[6, ''], [7, 'Rozhodně souhlasím']],
                                         blank=True)
    threat2 = models.IntegerField(label="Vietnamci a Vietnamky žijící v ČR berou Čechům kvalitní pracovní místa.",
                                         widget=widgets.RadioSelectHorizontal,
                                         choices=[[1, 'Rozhodně nesouhlasím'], [2, ''], [3, ''], [4, ''], [5, ''],[6, ''], [7, 'Rozhodně souhlasím']],
                                         blank=True)
    threat3 = models.IntegerField(label="Čím jsou Vietnamci a Vietnamky žijící v ČR bohatší, tím méně toho zbývá pro Čechy.",
                                         widget=widgets.RadioSelectHorizontal,
                                         choices=[[1, 'Rozhodně nesouhlasím'], [2, ''], [3, ''], [4, ''], [5, ''],[6, ''], [7, 'Rozhodně souhlasím']],
                                         blank=True)
    interaction3 = models.IntegerField(label="Do jaké míry Vám odpovědi komunikačního partnera/komunikační partnerky připadaly smysluplné?",
                                         widget=widgets.RadioSelectHorizontal,
                                         choices=[[1, 'Vůbec ne'], [2, ''], [3, ''], [4, ''], [5, ''],[6, ''], [7, 'Zcela']],
                                         blank=True)
    interaction4 = models.IntegerField(label="Do jaké míry Vám odpovědi komunikačního partnera/komunikační partnerky připadaly upřímné?",
                                         widget=widgets.RadioSelectHorizontal,
                                         choices=[[1, 'Vůbec ne'], [2, ''], [3, ''], [4, ''], [5, ''],[6, ''], [7, 'Zcela']],
                                         blank=True)
    interaction5 = models.IntegerField(label="Bez ohledu na to, co jste si myslel/a o svém komunikačním partnerovi/své komunikační partnerce, jak se Vám komunikovalo v rámci interakční aplikace?",
                                         widget=widgets.RadioSelectHorizontal,
                                         choices=[[1, 'Velmi špatně'], [2, ''], [3, ''], [4, ''], [5, ''],[6, ''], [7, 'Velmi dobře']],
                                         blank=True)
    open_interaction2 = models.LongStringField(label="Budeme vděčni za jakékoli další připomínky, které byste s námi chtěl/a sdílet.",
                                          blank=True)
    additional1 = models.StringField(label="Jak jste se dozvěděli o výzkumu?",
                                choices=["Oficiálním emailem od univerzity","Emailem od vyučující/ho předmětu, který navštěvuji","Sociální média univerzity (např. Facebook)","Od známých, kamarádů","Jinak"],
                                blank=True)
    additional2 = models.StringField(label="Studujete na univerzitě?",
                                     choices=["ano", "ne"],
                                     blank=True)
    is_keep = models.BooleanField(label="Chcete své odpovědi v datovém souboru ponechat?",
                                         choices=[
                                                 [True, "Ano, ponechte mé odpovědi v souboru."],
                                                 [False, "Ne, vymažte mé odpovědi."]],
                                          blank=True)
    open_general = models.LongStringField(label="Zde můžete napsat Váš komentář pro výzkumnice a výzkumníky:",
                                          blank=True)
    open_email = models.StringField(label="Pokud se chcete zúčastnit loterie o finanční ceny, zanechte nám zde Váš e-mail:",
                                          blank=True)


# PAGES
class SurveyThree(Page):
    form_model = "player"
    form_fields = ["open_interaction"]

class SurveyFour(Page):
    form_model = "player"

class SurveyFive(Page):
    form_model = "player"
    form_fields = ["attention_check1", "attention_check2"]

class SurveySix(Page):
    form_model = "player"
    form_fields = ["interaction1", "interaction2"]

class SurveySeven(Page):
    form_model = "player"
    form_fields = ["Vietnam2"]

class SurveyEight(Page):
    form_model = "player"
    def get_form_fields(player: Player):
        import random
        form_fields_r1 = ["behav_tend1", "behav_tend2", "behav_tend3", "behav_tend4", "behav_tend5", "behav_tend6","behav_tend7", "behav_tend8", "behav_tend9"]
        random.shuffle(form_fields_r1)
        return form_fields_r1

class SurveyNine(Page):
    form_model = "player"
    def get_form_fields(player: Player):
        import random
        form_fields_r2 = ["accult_stra_a1","accult_stra_a2","accult_stra_a3","accult_stra_a4","accult_stra_a5","accult_stra_a6","accult_stra_a7","accult_stra_b1","accult_stra_b2","accult_stra_b3","accult_stra_b4","accult_stra_b5","accult_stra_b6","accult_stra_b7"]
        random.shuffle(form_fields_r2)
        return form_fields_r2

class SurveyTen(Page):
    form_model = "player"
    form_fields = ["contact_freq","contact_pos","contact_neg","contact_freq2","contact_mass_pos","contact_mass_neg"]

class SurveyEleven(Page):
    form_model = "player"
    form_fields = ["threat1","threat2","threat3"]

class SurveyTwelve(Page):
    form_model = "player"
    form_fields = ["interaction3", "interaction4", "interaction5", "open_interaction2"]

class SurveyThirteen(Page):
    form_model = "player"
    form_fields = ["is_keep", "additional1", "additional2",  "open_general", "open_email"]

class SurveyFourteen(Page):
    form_model = "player"

page_sequence = [SurveyThree, SurveyFour, SurveyFive, SurveySix, SurveySeven, SurveyEight, SurveyNine, SurveyTen, SurveyEleven, SurveyTwelve, SurveyThirteen, SurveyFourteen]
