from django import forms
from .models import Todolist

import datetime

class TodoForm(forms.ModelForm):

    class Meta:
        model=Todolist
        fields =('title', 'content','category', 'due_date')


    def clean_due_date(self):
        due_date = self.cleaned_data['due_date']
        today_date = datetime.date.today()
        if due_date<today_date:
            raise forms.ValidationError("Due  date cannot be a past date")
        return due_date

