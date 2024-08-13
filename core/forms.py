from django import forms
from .models import PatientRequest

class PatientRequestForm(forms.ModelForm):
    class Meta:
        model = PatientRequest
        fields = ['name', 'age', 'phone', 'gender', 'symptoms']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'الاسم الكامل'}),
            'age': forms.NumberInput(attrs={'placeholder': 'العمر'}),
            'phone': forms.TextInput(attrs={'placeholder': 'رقم الهاتف المحمول'}),
            'gender': forms.Select(),
            'symptoms': forms.Textarea(attrs={'rows': 4, 'placeholder': 'الأعراض'}),
        }
