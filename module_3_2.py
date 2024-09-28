# Способы вызова функции
def check(recipient, sender,*arg):
    if ((recipient[-4:] in arg) or (recipient[-3:]  in arg)) and ((sender[-4:]  in arg) or (sender[-3:]  in arg)):
        return(True)
    else:
        return(False)

def send_email(message,recipient,*,sender = "university.@helpgmail.ru"):
    if recipient == sender:
        print("Нельзя отправить письмо самому себе!")
    elif (('@' in recipient) and ('@' in sender)) and (check(recipient,sender,'.net','.com','.ru')):
        if sender != "university.@helpgmail.ru":
            print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")
        else:
            print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    else:
        print(f"Невозможно отправить письмо с адреса {sender}> на адрес {recipient}")

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')

