def send_email(message, recipient, sender="university.help@gmail.com"):
    doc = recipient + sender
    if doc != ("@", ".com", ".ru", ".net"):
        print("Невозможно отправить письмо с адреса sender на адрес recipient")
    if sender == recipient:
        print("Нельзя отправить письмо самому себе!")
    if "university.help@gmail.com":
        print("Письмо успешно отправлено с адреса sendor на адрес recipient")
    if recipient != sender:
        print("Нестандартный отправитель письмо отправлено с адреса sender на адрес recipient")






send_email("message", "recipient", "sender")



