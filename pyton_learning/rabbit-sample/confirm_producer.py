#-*-coding:UTF-8-*-
'''
Created on 2016年4月20日
@author: Administrator
'''

import pika, sys
from pika import spec
import time

credentials = pika.PlainCredentials("sample", "sample")
conn_params = pika.ConnectionParameters("192.168.1.235", credentials = credentials)

#建立到代理服务器的连接
conn_broker = pika.BlockingConnection(conn_params)  
#获得信道
channel = conn_broker.channel();

msg_ids = []

def confirm_handler(frame) : 
    print "confirm handler..."
    if type(frame.method) == spec.Confirm.SelectOk :
        print "Channel in 'confirm' mode."
    elif type(frame.method) == spec.Basic.Nack : 
        if frame.method.delivery_tag in msg_ids : 
            print "Message lost!"
    elif type(frame.method) == spec.Basic.Ack :     
        if frame.method.delivery_tag in msg_ids : 
            print "Confirm received!"
            msg_ids.remove(frame.method.delivery_tag)
            
channel.confirm_delivery()
channel.add_on_return_callback(confirm_handler)

msg = "Hello World!"
msg_props = pika.BasicProperties()
msg_props.content_type = "text/plain"
msg_props.delivery_mode = 2


channel.basic_publish(exchange = "hello-exchange", 
                      routing_key = "hola", 
                      body = msg, 
                      properties = msg_props)
msg_ids.append(len(msg_ids) + 1)
time.sleep(10)
channel.close()
print "...producer exit!"