from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.conf import settings

def send_password_reset_email(user):
    # Генерация uid и токена для сброса пароля
    uid = urlsafe_base64_encode(str(user.pk).encode())
    token = default_token_generator.make_token(user)

    # Подготовка контекста для шаблона
    context = {
        'protocol': 'http',  # Используйте 'https' на боевом сервере
        'domain': settings.SITE_DOMAIN,  # Настройте SITE_DOMAIN в settings.py
        'uid': uid,
        'token': token,
    }

    # Рендеринг HTML-письма
    subject = "Сброс пароля"
    email_body = render_to_string('registration/password_reset_email.html', context)

    # Отправка письма
    email = EmailMessage(
        subject=subject,
        body=email_body,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[user.email],
    )
    email.content_subtype = "html"  # Указываем, что письмо в формате HTML
    email.send()
    