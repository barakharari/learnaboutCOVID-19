from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'ACb7d8a96e52e32f6fbf96c442579a93cc'
auth_token = 'f3dff9b3d93c8faaef2d7a824c038d35'
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
         body="Join Earth's mightiest heroes. Like Kevin Bacon.",
         messaging_service_sid='MG81aab724c570dd4478659e6484bc7749',
         to='+19177210271'
     )

print(message.sid)
