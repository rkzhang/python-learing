'''
Created on 2016年6月14日

@author: Administrator
'''
from email import Message
import smtplib

def send_mail(recipients, subject, message) :
    """ E-mail generator for received alerts. """
    headers = ("From: %s\r\nTo: \r\nDate: \r\n Subject: %s\r\n\r\n") % ("alerts@ourcompany.com", subject)
    
    smtp_server = smtplib.SMTP()
    smtp_server.connect("mail.ourcompany.com", 25)
    smtp_server.senmail("alerts@ourcompany.com", recipients, headers + str(message))
    smtp_server.close()
    
def critical_notify(channel, method, header, body) : 
    """ Sends CRITICAL alerts to administrators via e-mail."""
    EMAIL_RECIPS = ["opts.team@ourcompany.com"]
    
    message = json.loads(body)
    
    send_mail(EMAIL_RECIPS, "CRITICAL ALERT", message)
    print ("Sent alert via e-mail! Alert Text : %s Recipients: %s") % (str(message), str(EMAIL_RECIPS))
    
    channel.basic_ack(delivery_tag=method.delivery_tag)
    
def rate_limit_notify(channel, method, header, body) :
    """ Sends the message to the administrators via e-mail. """
    
if __name__ == '__main__':
    pass