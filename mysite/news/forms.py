from django import forms
from .models import Post


class PostForm(forms.ModelForm):  # model form
    class Meta:
        model = Post
        fields = ('title', 'content', 'created_date',)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'title'})
        }


class SendEmail(forms.Form):
    title = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'title'}))
    email = forms.EmailField()
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'class_name', 'id': 'content'}))
    cc = forms.BooleanField(required=False)
