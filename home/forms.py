from django import forms
from .models import Volunteers

class VolunteerApplicationForm(forms.ModelForm):
    
    class Meta:
        model = Volunteers
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Jack Doe'}),
            'email': forms.TextInput(attrs={'placeholder': 'Jackdoe@gmail.com'}),
            'subject': forms.TextInput(attrs={'placeholder': 'Subject'}),
            'comment': forms.Textarea(attrs={"rows": "3", "placeholder": "Comment (Optional)"})
        }
        labels = {'cv': 'Upload your CV'}

    def __init__(self, *args, **kwargs):
        super(VolunteerApplicationForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
        self.fields['cv'].required = False
        self.fields['comment'].required = False


class ContactForm(forms.Form):
    name = forms.CharField(max_length=40, widget=forms.TextInput(attrs={'placeholder': 'Jack'}))
    surname = forms.CharField(max_length=40, widget=forms.TextInput(attrs={'placeholder': 'Doe'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'JackDoe@gmail.com'}))
    message = forms.CharField(widget=forms.Textarea(attrs={"rows": "5", 'placeholder': 'How can we help you?'}))
    
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'