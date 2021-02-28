import smtplib

from django.http import HttpResponse


# Create your views here.
def send_mail(request):
    # Sender email
    sender_email = "linked.clubs@gmail.com"
    # Receiver email
    receiver_email = request.GET['rec']
    # Message to send
    message = request.GET['message']

    msg = f'subject: LinkedClubs\n\n{message}'

    # Initialize the server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    # Start the server
    server.starttls()

    # Login
    server.login(sender_email, "linkedclubs2020")
    print("Login success !")

    # Send the message
    server.sendmail(sender_email, receiver_email, msg)

    print("Email has been sent successfully !")

    return HttpResponse('<h1>Sent</h1>')

