from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import Comment
from crispy_forms.helper import FormHelper

class ArticleForm(forms.Form):
    article = forms.CharField(widget=CKEditorWidget(),required=True,min_length=50)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name','email','body')

        widgets = {
            'body':forms.Textarea(attrs = {'class':'form-control','rows':3, 'cols':10})
        }

        labels={
            'body': ('Comment')
        }
        error_messages = {
            'name': {
            'min_length': ("This writer's name is too long."),
    },
}