# Задача "Рассылка писем".
def send_email(message, recipient, sender="university.help@gmail.com"):
    def email(email):
        return "@" in email and (email.endswith(".com") or email.endswith(".ru") or email.endswith(".net"))

    if not email(recipient) or not email(sender):
        print('Невозможно отправить письмо с адреса:', sender, 'на адрес:', recipient)
        return

    # Проверка: совпадают ли адрес отправителя с адресом получателя
    if sender == recipient:
        print('Нельзя отправить письмо самому себе!')
        return

    # Проверка: используется ли адрес отправителя по умолчанию
    if sender == 'university.help@gmail.com':
        print('Письмо успешно отправлено с адреса:', sender, 'на адрес:', recipient)
    else:
        print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо успешно отправлено с адреса:', sender, 'на адрес:', recipient)
        return

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
