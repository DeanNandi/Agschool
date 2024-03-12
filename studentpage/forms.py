from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Candidate


class CreateUserForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email Address',
                             widget=forms.EmailInput(attrs={'placeholder': 'Email...', 'class': 'form-control'}))
    password1 = forms.CharField(label='Password',
                                widget=forms.PasswordInput(
                                    attrs={'placeholder': 'Enter password...', 'class': 'form-control'}))
    password2 = forms.CharField(label='Repeat Password',
                                widget=forms.PasswordInput(
                                    attrs={'placeholder': 'Re-enter password...', 'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Register Account'))

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("Email already exists")
        return email

    def save(self, commit=True):
        user = super(CreateUserForm, self).save(commit=False)
        user.username = self.cleaned_data['email']  # Use email as username
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


ALLOWED_FILE_TYPES = ['pdf', 'jpg', 'jpeg', 'png']
MAX_FILE_SIZE = 10 * 1024 * 1024  # 10MB limit


class DocumentUploadForm(forms.ModelForm):
    class Meta:
        model = Candidate
        fields = [
            'photo',
            'identification_card_file',
            'Birth_certificate',
            'High_School_file',
            'University_file',
            'resume_file',
            'Licence_file',
            'Nursing_Certificate',
            'Institution_file',
            'certificate_of_good_conduct',
            'passport'

        ]
        labels = {
            'photo': 'Passport Photo',
            'High_School_file': 'Secondary school results slip',
            'identification_card_file': 'National ID',
            'Licence_file': 'Nursing Council Practicing Licence',
            'Nursing_Certificate':'Nursing Council Certificate',
            'resume_file': 'Resume or CV',
            'University_file': 'University Transcript',
            'Institution_file': 'Work Experience',
            'passport': 'Passport'
        }

    def __init__(self, *args, **kwargs):
        super(DocumentUploadForm, self).__init__(*args, **kwargs)
        instance = kwargs.get('instance', None)

        if instance:
            for field_name in self.fields:
                if getattr(instance, field_name):
                    # Disable the field to prevent editing
                    self.fields[field_name].disabled = False
                    # Optionally, add help text to indicate the file exists
                    self.fields[field_name].help_text = "A file has been uploaded, click to view it."

    def clean(self):
        cleaned_data = super().clean()
        for field_name, field in self.fields.items():
            if field_name in self.Meta.fields and not field.disabled:
                file = cleaned_data.get(field_name)
                if file:
                    if not file.name.split('.')[-1].lower() in ALLOWED_FILE_TYPES:
                        self.add_error(field_name, "Only PDF, JPG, JPEG and PNG files are allowed.")
                    if file.size > MAX_FILE_SIZE:
                        self.add_error(field_name, "File too large ( > 10MB ).")
        return cleaned_data
