from django import forms
from hotels.models import Review

RATING_CHOICES = (
        (1, '1 Star'),
        (2, '2 Stars'),
        (3, '3 Stars'),
        (4, '4 Stars'),
        (5, '5 Stars'),
    )
class RatingForm(forms.Form):
    
    rating = forms.ChoiceField(choices=RATING_CHOICES,widget=forms.RadioSelect())
    comment = forms.CharField(widget=forms.Textarea(attrs={'rows': 8,}),required=False)
