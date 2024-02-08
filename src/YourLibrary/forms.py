from django import forms
from store.models import Book

JOBS = (
    ('primary_sector', 'farmer'),
    ('secondary_sector', 'food processing'),
    ('tertiary_sector', 'site developer')
)

class SignupForm(forms.Form):
    
    pseudo = forms.CharField(max_length=8)
    email = forms.EmailField()
    password = forms.CharField(min_length=6, widget=forms.PasswordInput())
    job = forms.ChoiceField(choices=JOBS, widget=forms.RadioSelect())
    detail = forms.CharField(widget=forms.Textarea(), required=False)
    cgu_accept = forms.BooleanField(initial=True)

    def clean_pseudo(self):
        pseudo = self.cleaned_data.get('pseudo')
        if '$' in pseudo:
            raise forms.ValidationError('The pseudo can\'t contains $ sign.')
        return pseudo


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'title',
            'kind',
            'slug',
        ]
        labels = {'title' : 'titre',
                'kind' : 'genre'}
        #widgets = {'date': 'forms.SelectDateWidget(years=range(1990, 2024))'}