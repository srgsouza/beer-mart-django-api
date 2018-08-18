from django import forms
from .models import Beer, Comment

class BeerForm(forms.ModelForm):
  class Meta:
    model = Beer
    fields = ('brewery_name','beer_name', 'description', 'abv', 'ibu','price', 'package', 'user')

class CommentForm(forms.ModelForm):
  class Meta:
    model = Comment
    fields = ('comment', 'beer')
