from django import forms
from .models import CustomUser, UserProfile


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'id': 'password',
        'placeholder': 'Enter Password',
    }))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'id': 'confirm_password',
        'placeholder': 'Confirm Password'
    }))

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'password']

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError(
                "Password does not match!"
            )

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs = {
            'id': 'first_name',
            'placeholder': 'Enter First Name'
        }
        self.fields['last_name'].widget.attrs = {
            'id': 'last_name',
            'placeholder': 'Enter last Name'
        }
        self.fields['email'].widget.attrs = {
            'id': 'email',
            'placeholder': 'Enter Email Address'
        }
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'


class UserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name',)

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'


class UserProfileForm(forms.ModelForm):

    dates_of_birth = forms.DateField(widget=forms.DateInput(attrs={
        'id': 'dob',
        'type': 'date',
    }))

    profile_picture = forms.ImageField(
        required=False,
        error_messages={'invalid': ("Image files only")},
        widget=forms.FileInput
    )

    class Meta:
        model = UserProfile
        fields = (
            'dates_of_birth',
            'phone_number',
            'address_line_1',
            'address_line_2',
            'postal_code',
            'city',
            'state',
            'country',
            'profile_picture'
        )

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
