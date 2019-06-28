from django import forms

class SearchMovie(forms.Form):

    types = (
        ('t' , 'Unique'),
        ('s' , 'All'),
    )

    search_for = forms.ChoiceField(choices=types)
    search = forms.CharField(label='Search', max_length=100)
    email = forms.EmailField()
