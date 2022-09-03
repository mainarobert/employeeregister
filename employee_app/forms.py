from cProfile import label
from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model= Employee
        fields= '__all__'
        labels= {
            'name':'Full Name',
            'idnum':'ID Number',
            'phoneNum':'Phone Number',
            'position':'Position'
        }

    def __init__(self, *args, **kwargs):
        super(EmployeeForm,self).__init__(*args, **kwargs)
        self.fields['position'].empty_label= "Select"