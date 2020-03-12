from flask import Flask
from flask_mail import Mail, Message
import os
app = Flask(__name__)

mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com', 
    "MAIL_USE_TLS": True, #Transport Layer Security
    "MAIL_USE_SSL": False,  #Secure Sockets Layer
    "MAIL_PORT": 587, 		 #For using SSL
    "MAIL_USERNAME": 'slackchatbot123@gmail.com',
    "MAIL_PASSWORD": 'upgrad123'
    }
app.config.update(mail_settings)
mail = Mail(app)

def mail_results(emailid, html_msg):
	with app.app_context():
		msg = Message(sender=app.config.get("MAIL_USERNAME"),recipients=[emailid])
		msg.subject = "Foodie search results"
		msg.html = html_msg
		mail.send(msg)
