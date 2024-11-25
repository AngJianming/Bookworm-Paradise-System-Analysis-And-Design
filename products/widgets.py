""" File storing widget settings """
from django.forms.widgets import ClearableFileInput
from django.utils.translation import gettext_lazy as _


class CustomClearableFileInput(ClearableFileInput):
    """ CustomClearableFileInput widget settings """
    clear_checkbox_label = _('Remove')
    initial_text = _('Current Image')
    input_text = _('')
    t = 'products/custom_widget_templates/custom_clearable_file_input.html'
    template_name = t
