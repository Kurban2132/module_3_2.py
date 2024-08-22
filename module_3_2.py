def send_email(message, recipient, sender="university.help@gmail.com"):
    message = "Сообщение"
    recipient = "vasyok1337@gmail.com"
    sender = "university.help@gmail.com"
    if ("recipient", "sender") != "@, .com/, .ru/,.net":
        print("Невозможно отправить письмо с адреса <sender> на адрес <recipient")

    elif ("sender" == "recipient"):
        print("Нельзя отправлят письмо самому себе")

    elif "university.help@gmail.com":
        print("Письмо успешно отправлено с адреса <sender> на адрес <recipient>")

    else:
        print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ")


send_email("Сообщение", "recipient", "sender")