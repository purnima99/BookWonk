from django import forms
from django.forms import fields
from .models import Member

class MemberRegistration( forms.ModelForm ):

    name = forms.CharField(
        label="name",
        widget=forms.TextInput(attrs={ 'placeholder' : 'Name', 'class' : 'form-control' })
    )

    email = forms.EmailField(
        label="email",
        widget=forms.TextInput(attrs={ 'placeholder' : 'Email', 'class' : 'form-control' })
    )

    mobile = forms.CharField(
        label="mobile",
        widget=forms.TextInput(attrs={ 'placeholder' : 'Mobile Number', 'class' : 'form-control' })
    )

    rollNo = forms.CharField(
        label="rollno",
        widget=forms.TextInput(attrs={ 'placeholder' : 'Roll Number', 'class' : 'form-control' })
    )

    degree = forms.CharField(
        label="degree",
        widget=forms.TextInput(attrs={ 'placeholder' : 'Your current Degree', 'class' : 'form-control' })
    )

    branch = forms.CharField(
        label="branch",
        widget=forms.TextInput(attrs={ 'placeholder' : 'Your branch', 'class' : 'form-control' })
    )

    year = forms.CharField(
        label="year",
        widget=forms.TextInput(attrs={ 'placeholder' : 'Present year', 'class' : 'form-control' })
    )

    class Meta :
        model = Member
        fields = {
            'name',
            'email',
            'mobile',
            'rollNo',
            'degree',
            'branch',
            'year'
        }