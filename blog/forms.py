from django import forms
from tinymce.widgets import TinyMCE
from .models import Comment

class CommentForm(forms.ModelForm):
    # comment = forms.CharField(widget=forms.Textarea)
    content = forms.CharField(widget=TinyMCE(attrs={'rows': 10}))
    class Meta:
        model  = Comment
        fields = ['content']
        exclude= ['post', 'author']