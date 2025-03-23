from django import forms
from django.core.validators import RegexValidator
def f1(value): #проверка с помощью функции
    if not value.isdigit():
        raise forms.ValidationError("Код из цифр") #текст с ошибкой
    if len(value) != 4:
        raise forms.ValidationError('4 символа')

class formComent(forms.Form):
    name = forms.CharField(label='Имя', max_length=100, min_length=5,
                           #сообщения с ошибками которые появятся на экране
                           error_messages={'min_length':'мало символов',
                                           'max_length':'слишком много символов',
                                           'required':'заполните имя'},
                           #доп проверка , имя должно начинаться с большой буквы
                           validators=[RegexValidator(regex='^[A-ZА-Я]',message='С большой буквы')])
    text = forms.CharField(widget=forms.Textarea(attrs={'name':'text','rows':5,'cols':50}),
                           label='Напишите комментарий', min_length=5,
                           error_messages={'min_length': 'минимальная длина сообщения 5',
                                           'required': 'заполните комментарий'})
    email = forms.EmailField(
                            #не обязательное поле
                            required=False, label='Укажите почту',
                             #доп провека, почта mail.ru
                             validators=[RegexValidator(regex='^[a-z0-9]+(@mail.ru)$', message='неверный формат')],
                             #подсказка на экране
                             widget=forms.TextInput(attrs={'placeholder':'*@mail.ru'}))
    nerobot = forms.BooleanField(label='Не робот',
                                 error_messages={'required':'вы робот'})
    pincode = forms.CharField(label='Секретный код',
                              #проверка с помощью функции
                              validators=[f1], widget=forms.TextInput(attrs={'placeholder':'0000'}))#^[0-9]{4}$