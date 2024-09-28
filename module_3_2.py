# Способы вызова функции

def send_email(message,recipient,*,sender = "university.help@gmail.com"):
    not_check = (f"Невозможно отправить письмо с адреса {sender}> на адрес {recipient}")
    if '@' in (recipient or sender):
        if (recipient[-4:] or recipient[-3:]) == ('.com' or '.net' or '.ru') == (sender[-4:] or sender[-3:]):
            print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
        else:
            print(not_check)

    else:
        print(not_check)

send_email('my message','vasyok1337@gmail.com')

