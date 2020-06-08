from django import forms
from .models import  Post






# class postform(forms.Form):
#     title =forms.CharField(label="title")
#     text=forms.CharField(label="text",widget=forms.Textarea)



#module Form 
class postform(forms.ModelForm):
    class Meta:
        model=Post
        fields =('title','text')