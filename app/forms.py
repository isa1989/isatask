from django import forms
from .models import Task, Comment


class TaskForm(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        super(TaskForm, self).__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs={'class':'form-control'}
            self.fields['end_time'].widget.attrs['placeholder'] = '2019-01-01 00:00:00'

    class Meta:
        model = Task
        fields = ['other_user', 'comment_user', 'name', 'description', 'end_time']





class CommentForm(forms.ModelForm):

    def __init__(self, *args,**kwargs):
        super(CommentForm, self).__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs={'class':'form-control'}

    class Meta:
        model = Comment
        fields = ['description']

