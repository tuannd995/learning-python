from django import forms

class CommentForm(forms.Form):
    your_name = forms.CharField(widget=forms.Textarea)