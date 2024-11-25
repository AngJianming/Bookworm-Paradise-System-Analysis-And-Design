""" File storing form information for products app """
from django import forms
from .widgets import CustomClearableFileInput
from .models import Review, Book, Genre


class BookForm(forms.ModelForm):
    """ Data for the book add/edit form and widgets to be displayed. """

    class Meta:
        """ Meta class specifying fields and widgets to be displayed. """
        model = Book
        fields = '__all__'

    image = forms.ImageField(
        label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        genres = Genre.objects.all()
        friendly_names = [(g.id, g.get_friendly_name()) for g in genres]

        self.fields['genre'].choices = friendly_names
        self.fields['genre'].widget.attrs['class'] = 'add-form-input'
        self.fields['price'].widget.attrs['class'] = 'add-form-input'
        self.fields['rating'].widget.attrs['class'] = 'add-form-input'
        self.fields['image_url'].widget.attrs['class'] = 'add-form-input'


class ReviewForm(forms.ModelForm):
    """ Data for review form and widgets to be displayed. """
    class Meta:
        """ Meta class specifying fields and widgets to be displayed. """
        model = Review
        fields = ('title', 'body',)
        widgets = {
            'title': forms.TextInput(
                attrs={'placeholder': 'Give your review a title'}),
            'body': forms.Textarea(
                attrs={'placeholder': 'Leave your review here'}),
        }
