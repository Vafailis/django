from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from authapp.models import ShopUser
from django import forms

class ShopUserLoginForm(AuthenticationForm):
    class Meta:
        model = ShopUser
        fields = ('username', 'password')

    def __init__(self, *args, **kw):
        super(ShopUserLoginForm, self).__init__(*args, **kw)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ShopUserRegisterForm(UserCreationForm):
    class Meta:
        model = ShopUser
        fields = ('username', 'first_name', 'password1', 'password2', 'email', 'age', 'avatar')

    
    def __init__(self, *a, **kw):
        super().__init__(*a, **kw)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''

    def clean_age(self):
        data = self.changed_data['age']
        if data < 18:
            raise forms.ValidationError("Сайт не для тебя, малолетний!!!")

        return data
