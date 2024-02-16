from .models import User, Retreat, Feedback, Favorite, Booking, Payment
from .exceptions import LoginError, PasswordError, RegisterError, UserAttributesError, RetreatAttributesError, \
    AttributesEnteringError
import logging

logger = logging.getLogger(__name__)


def login(user_email, password_hash) -> User:
    user = User.objects.filter(email=user_email).first()
    if user:
        if user.password_hash == password_hash:
            return user
        else:
            raise PasswordError()
    else:
        raise LoginError()


def register(user_email, user_password_hash, replay_password_hash) -> User:
    user = User.objects.filter(email=user_email).first()
    if user:
        raise RegisterError()
    else:
        if user_password_hash == replay_password_hash:
            raise PasswordError()
        user = User(email=user_email, password_hash=user_password_hash)
        user.save()
        logger.info(f'Создан новый пользователь: {user.pk=}')
        return user


def edit_user_detail(date: dict) -> User:
    params = date.keys()
    user = User.objects.filter(email=date['email']).first()
    for param in params:
        if date[param]:
            try:
                user.param = date[param]
            except AttributeError:
                raise UserAttributesError()
    user.save()
    logger.info(f'Внесены изменения в данные пользователя: {user.pk=}')
    return user


def create_retreat(date: dict) -> Retreat:
    params = date.keys()
    try:
        retreat = Retreat(**date)
    except AttributeError:
        raise RetreatAttributesError
    retreat.save()
    logger.info(f'Создан новый ретрит: {retreat.pk=}')
    return retreat


def edit_retreat_detail(date: dict) -> Retreat:
    params = date.keys()
    retreat = Retreat.objects.filter(pk=date['id']).first()
    for param in params:
        if date[param]:
            try:
                retreat.param = date[param]
            except AttributeError:
                raise RetreatAttributesError
    retreat.save()
    logger.info(f'Внесены изменения в ретрит: {retreat.pk=}')
    return retreat


def create_favorite(date: dict) -> Favorite:
    try:
        favorite = Favorite(**date)
    except AttributeError:
        raise AttributesEnteringError
    favorite.save()
    logger.info(f'Добавлен ретрит в избранное: {favorite.pk=}')
    return favorite


def create_feedback(date: dict) -> Feedback:
    try:
        feedback = Feedback(**date)
    except AttributeError:
        raise AttributesEnteringError
    feedback.save()
    logger.info(f'Создан новый отзыв: {feedback.pk=}')
    return feedback


def create_booking(date: dict) -> Booking:
    try:
        booking = Booking(**date)
    except AttributeError:
        raise AttributesEnteringError
    booking.save()
    logger.info(f'Создано новое бронирование: {booking.pk=}')
    return booking


def create_payment(date: dict) -> Payment:
    try:
        payment = Payment(**date)
    except AttributeError:
        raise AttributesEnteringError
    payment.save()
    logger.info(f'Создан новый платеж: {payment.pk=}')
    return payment


def get_cookies(request) -> dict:
    try:
        name = request.COOKIES['user_name']
    except:
        name = ''
    cookies = {'name': name}
    return cookies
