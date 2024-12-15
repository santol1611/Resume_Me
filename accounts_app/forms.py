from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

from accounts_app.models import UserProfile

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name', 'email']  # ระบุฟิลด์ที่ต้องการใช้งาน
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer',
                'placeholder': ' ',
                'id': 'floating_username'
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer',
                'placeholder': ' ',
                'id': 'floating_first_name'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer',
                'placeholder': ' ',
                'id': 'floating_first_name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer',
                'placeholder': ' ',
                'id': 'floating_email'
            }),
        }

    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        
        # เพิ่ม class สำหรับ password1 และ password2
        self.fields['password1'].widget.attrs.update({
            'class': 'block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer',
            'placeholder': ' ',
            'id': 'floating_password'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer',
            'placeholder': ' ',
            'id': 'floating_repeat_password'
        })

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email")

class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ("birthday", "phone", "image")

        