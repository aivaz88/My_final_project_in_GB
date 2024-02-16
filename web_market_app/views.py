from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
import logging
from . import models
from . import processes
from .forms import LoginForm, RegisterForm,  RecoveryPasswordForm, EditProfileForm, FeedbackForm, BookingForm, \
    CreateRetreatForm
from .exceptions import PasswordError, LoginError, RegisterError, UserAttributesError, RetreatAttributesError, \
    AttributesEnteringError

logger = logging.getLogger(__name__)


def main(request):
    content = {}
    retreats = models.Retreat.objects.all().order_by('-id')[:50]
    content['retreats'] = retreats
    content['cookies'] = processes.get_cookies(request)
    logger.info('Main page accessed')
    return render(request, 'web_market_app/main.html', content)


def get_by_categories(request, category):
    content = {}
    retreats = models.Retreat.objects.filter(category=category).order_by('-id')[:50]
    content['retreats'] = retreats
    content['cookies'] = processes.get_cookies(request)
    logger.info('Retreats by categories accessed')
    return render(request, 'web_market_app/main.html', content)


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            try:
                user = processes.login(form.email, form.password_hash)
            except (PasswordError or LoginError) as er:
                logger.info(er)
                form = LoginForm()
                return render(request, 'web_market_app/login.html/', {'form': form,
                                                                      'message': 'Не правильно ввели почту или пароль!'})
            logger.info(f'Выполнен вход пользователя {user.pk=}')
            response = redirect('/')
            response.set_cookie('email', user.email)
            return response
    else:
        form = LoginForm()
    return render(request, 'web_market_app/login.html/', {'form': form})


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            try:
                user = processes.register(form.email, form.password_hash, form.replay_password_hash)
            except RegisterError as er:
                logger.info(er)
                form = RegisterForm()
                return render(request, 'web_market_app/register.html/',
                              {'form': form, 'message': 'Пользователь с такой почтой уже зарегистрирован!'})
            except PasswordError as er:
                logger.info(er)
                form = RegisterForm()
                return render(request, 'web_market_app/register.html/',
                              {'form': form, 'message': 'Ошибка ввода пароля!'})
            except AttributeError as er:
                logger.info(er)
                form = LoginForm()
                return render(request, 'web_market_app/register.html/', {'form': form})
            logger.info(f'Зарегистрирован новый пользователь: {user.pk=}')
            response = redirect('/')
            response.set_cookie('email', user.email)
            return response
    else:
        form = RegisterForm()
    return render(request, 'web_market_app/register.html/', {'form': form})


def edit_user_card(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST)
        if form.is_valid():
            data = vars(form) | processes.get_cookies(request)
            try:
                user = processes.edit_user_detail(data)
            except UserAttributesError:
                form = LoginForm()
                return render(request, 'web_market_app/edit_profile.html/', {'form': form})
            logger.info(f'Редактирование данных пользователя: {user.pk=}')
            response = redirect(f'account/{user.pk}/')
            return response
    else:
        form = EditProfileForm()
    return render(request, 'web_market_app/edit_profile.html/', {'form': form})


def recovery_password(request):
    if request.method == 'POST':
        form = RecoveryPasswordForm(request.POST)
        if form.is_valid():
            data = vars(form) | processes.get_cookies(request)
            try:
                user = processes.edit_user_detail(data)
            except UserAttributesError:
                form = RecoveryPasswordForm()
                return render(request, 'web_market_app/recovery_password.html/', {'form': form})
            logger.info(f'Изменение пароля пользователя: {user.pk=}')
            response = redirect(f'account/{user.pk}/')
            return response
    else:
        form = RecoveryPasswordForm()
    return render(request, 'web_market_app/recovery_password.html/', {'form': form})


def get_user_card(request):
    content = {}
    cookies = processes.get_cookies(request)
    user = models.User.objects.filter(pk=cookies['user_id']).first()
    content['user'] = user
    content['cookies'] = cookies
    logger.info('User card showing')
    return render(request, 'web_market_app/account.html', content)


def create_retreat(request):
    if request.method == 'POST':
        form = CreateRetreatForm(request.POST)
        if form.is_valid():
            data = vars(form) | {'user_id': processes.get_cookies(request)['id']}
            try:
                retreat = processes.create_retreat(data)
            except RetreatAttributesError as er:
                logger.info(er)
                form = CreateRetreatForm()
                return render(request, 'web_market_app/create_retreat.html/', {'form': form})
            logger.info(f'Создан новый ретрит: {retreat.pk=}')
            response = redirect(f'retreat/{retreat.pk}/')
            return response
    else:
        form = CreateRetreatForm()
    return render(request, 'web_market_app/create_retreat.html/', {'form': form})


def get_retreat_card(request, retreat_id):
    content = {}
    retreat = models.Retreat.objects.filter(pk=retreat_id).first()
    content['retreat'] = retreat
    content['cookies'] = processes.get_cookies(request)
    logger.info('Retreat card showing')
    return render(request, 'web_market_app/retreat_card.html', content)


def get_organizer_card(request, user_id):
    content = {}
    user = models.User.objects.filter(pk=user_id).first()
    content['user'] = user
    content['cookies'] = processes.get_cookies(request)
    logger.info('Organizer card showing')
    return render(request, 'web_market_app/organizer.html', content)


def create_booking(request, retreat_id):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            retreat = models.Retreat.objects.filter(pk=retreat_id).first()
            data = vars(form) | {'user_id': processes.get_cookies(request)['id'], 'retreat_id': retreat_id,
                                 'booking_coast': form.tickets_amount * retreat.price}
            try:
                new_booking = processes.create_booking(data)
                processes.create_payment(data)
            except AttributesEnteringError as er:
                logger.info(er)
                form = BookingForm()
                return render(request, 'web_market_app/booking.html/', {'form': form})
            logger.info(f'Создано новое бронирование: {new_booking.pk=}')
            response = redirect(f'retreat/{new_booking.retreat_id}/')
            return response
    else:
        form = BookingForm()
    return render(request, 'web_market_app/booking.html/', {'form': form})


def get_my_bookings(request):
    content = {}
    cookies = processes.get_cookies(request)
    user = models.User.objects.filter(email=cookies['email']).first()
    bookings = models.Booking.objects.filter(user_id=user.pk)
    content['bookings'] = bookings
    content['cookies'] = cookies
    logger.info(f'Bookings for {user.pk=} showing')
    return render(request, 'web_market_app/my_bookings.html', content)


def get_payments(request):
    content = {}
    cookies = processes.get_cookies(request)
    user = models.User.objects.filter(email=cookies['email']).first()
    payments = models.Payment.objects.filter(user_id=user.pk)
    content['payments'] = payments
    content['cookies'] = cookies
    logger.info(f'Payments for {user.pk=} showing')
    return render(request, 'web_market_app/my_payments.html', content)


def get_favorites(request):
    content = {}
    cookies = processes.get_cookies(request)
    user = models.User.objects.filter(email=cookies['email']).first()
    favorites = models.Favorite.objects.filter(user_id=user.pk)
    content['favorites'] = favorites
    content['cookies'] = cookies
    logger.info(f'Favorites for {user.pk=} showing')
    return render(request, 'web_market_app/favorites.html', content)


def create_feedback(request, retreat_id):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            data = vars(form) | {'user_id': processes.get_cookies(request)['id'], 'retreat_id': retreat_id}
            try:
                new_feedback = processes.create_feedback(data)
            except AttributesEnteringError as er:
                logger.info(er)
                form = BookingForm()
                return render(request, 'web_market_app/feedback.html/', {'form': form})
            response = redirect(f'retreat/{new_feedback.retreat_id}/')
            return response
    else:
        form = BookingForm()
    return render(request, 'web_market_app/feedback.html/', {'form': form})
