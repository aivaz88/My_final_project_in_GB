from django import forms


class LoginForm(forms.Form):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control',
                                                                           'placeholder': 'example@example.ru'}))
    password_hash = forms.CharField(max_length=128, required=True,
                                    widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Пароль'}))


class RegisterForm(forms.Form):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control',
                                                                           'placeholder': 'example@example.ru'}))
    password_hash = forms.CharField(max_length=128, required=True,
                                    widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Пароль'}))
    replay_password_hash = forms.CharField(max_length=128, required=True,
                                           widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                             'placeholder': 'Пароль'}))


class RecoveryPasswordForm(forms.Form):
    password_hash = forms.CharField(max_length=128, required=True,
                                    widget=forms.PasswordInput(
                                        attrs={'class': 'form-control', 'placeholder': 'Пароль'}))
    replay_password_hash = forms.CharField(max_length=128, required=True,
                                           widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                             'placeholder': 'Пароль'}))


class EditProfileForm(forms.Form):
    name = forms.CharField(max_length=50, required=False, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                                       'placeholder': 'Имя'}))
    surname = forms.CharField(max_length=50, required=False, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                                          'placeholder': 'Фамилия'}))
    telephone = forms.CharField(max_length=11, required=False, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                                            'placeholder': '7-9XX-XXX-XX-XX'}))
    address = forms.CharField(max_length=300, required=False, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                                           'placeholder': 'Адресс'}))
    links_media = forms.CharField(max_length=300, required=False, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                                            'placeholder': 'Ссылка на соцсеть'}))
    avatar = forms.ImageField(required=False)


class CreateRetreatForm(forms.Form):
    name = forms.CharField(max_length=128, required=True, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                                        'placeholder': 'Название'}))
    description = forms.CharField(required=True, widget=forms.Textarea(attrs={'class': 'form-control',
                                                                                        'placeholder': 'Описание'}))
    country = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                                       'placeholder': 'Страна'}))
    city = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                                       'placeholder': 'Город'}))
    address = forms.CharField(max_length=128, required=True, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                                       'placeholder': 'Адресс'}))
    space = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                                       'placeholder': 'Название'}))
    category = forms.ChoiceField(required=True, choices=[(1, 'category1'), (2, 'category2')])
    photo = forms.ImageField(required=True)
    tag = forms.CharField(max_length=300, required=False, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                                            'placeholder': 'Хэш-теги'}))
    link_preview = forms.CharField(max_length=128, required=True, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                                       'placeholder': 'Ссылка на соцсети'}))
    date_start = forms.DateTimeField(required=True, widget=forms.DateTimeInput(attrs={'class': 'form-control',
                                                                                      'placeholder': 'Дата начала'}))
    date_stop = forms.DateTimeField(required=True, widget=forms.DateTimeInput(attrs={'class': 'form-control',
                                                                                      'placeholder': 'Дата начала'}))
    price = forms.FloatField(required=True)
    retreat_form = forms.ChoiceField(required=True, widget=forms.Select(attrs={'class': 'form-control',
                                                                               'placeholder': 'Форма проведения'}))


class BookingForm(forms.Form):
    tickets_amount = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={'class': 'form-control',
                                                                                       'placeholder': 'Кол-во'}))


class FeedbackForm(forms.Form):
    description = forms.CharField(required=True, widget=forms.Textarea(attrs={'class': 'form-control',
                                                                              'placeholder': 'Ваш отзыв'}))
    rating = forms.ChoiceField(required=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])
