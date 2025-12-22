from django import forms
from .models import BlogPost, Comment

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'text', 'image']
        labels = {'title': 'Title', 'text': 'Text', 'image': 'Image'}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        labels = {'text': 'Comment'}
        widgets = {'text': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Add a comment...'})}
