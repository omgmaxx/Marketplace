from django import forms

from app_catalog.models import Commentary


class CommentForm(forms.ModelForm):
    review = forms.CharField()
    name = forms.CharField(required=False)
    email = forms.EmailField(required=False)

    class Meta:
        model = Commentary
        fields = ('review', 'name', 'email')