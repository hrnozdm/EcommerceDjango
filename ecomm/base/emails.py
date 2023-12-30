# accounts/emails.py

from django.conf import settings
from django.core.mail import send_mail

def send_account_activation_email(email, email_token):
    subject = 'Your account needs to be verified'
    email_from = settings.EMAIL_HOST_USER
    message = f'Hi, click on the link to activate your account http://127.0.0.1:8000/accounts/activate/{email_token}'
    result = send_mail(subject, message, email_from, [email])

    # E-posta gönderme sonucunu kontrol et
    if result == 1:
        print("E-posta başarıyla gönderildi.")
    else:
        print("E-posta gönderilirken bir hata oluştu.")

    # Eğer hata varsa, result değişkenini ve hatayı inceleyin
    return result
