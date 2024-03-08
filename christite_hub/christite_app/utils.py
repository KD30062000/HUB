from twilio.rest import Client
from django.conf import settings


print("Running1")
def send_sms_notification(to, message):
    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
    try:
        client.messages.create(
            to=to,
            from_=settings.TWILIO_PHONE_NUMBER,
            body=message
        )
    except Exception as e:
        print("Error sending SMS:", str(e))
