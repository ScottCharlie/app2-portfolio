import smtplib, ssl


def send_email(message):
    # Standard host and port variables
    host = "smtp.gmail.com"
    port = 465
    # Username and password
    username = "scottcaruso22@gmail.com"
    password = "zykgvbufgbggljgr"
    # Create secure content
    receiver = "scottcaruso22@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
