from django.forms import RadioSelect


class TableRadio(RadioSelect):
    template_name = 'widgets/multiple_input.html'
    option_template_name = 'widgets/input_option.html'

    def __init__(self, top_row=None, bottom_row=None, attrs=None, choices=(), ):
        self.top_row = top_row
        self.bottom_row = bottom_row
        return super().__init__(attrs, choices)

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        context['top_row'] = self.top_row
        context['bottom_row'] = self.bottom_row
        context['col_width'] = 100 / len(self.choices)
        return context
