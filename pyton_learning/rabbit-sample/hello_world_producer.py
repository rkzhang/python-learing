#-*-coding:UTF-8-*-
'''
Created on 2016年4月19日

@author: Administrator
'''
import pika

credentials = pika.PlainCredentials("guest", "guest")
conn_params = pika.ConnectionParameters(SERVICE_IP, credentials = credentials)

#建立到代理服务器的连接
conn_broker = pika.BlockingConnection(conn_params)  
#获得信道
channel = conn_broker.channel();
#声明交换器
channel.exchange_declare(exchange = "hello-exchange",  #交换机名称
                         exchange_type = "direct",      #交换器类型 direct, fanout, topic
                         passive = False,               #如果你只是想检测队列是否存在，则可以设置passive选项为True
                         durable = True,                #决定了是否需要在崩溃或者重启之后重新创建队列，为True则不需要在服务器断电后重新创建队列和交换机 
                         auto_delete = False            #当最后一个消费者取消订阅的时候，队列就会自动移除
                        )

msg = "hello world"
msg_props = pika.BasicProperties()
msg_props.content_type = "text/plain"

channel.basic_publish(exchange = "hello-exchange", 
                      routing_key = "hola", 
                      body = msg, 
                      properties = msg_props)
print "send message : %s " % msg