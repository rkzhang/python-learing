#-*-coding:UTF-8-*-
'''
Created on 2016年6月14日
@author: rkzhang
'''
import json, pika
from optparse import OptionParser
from pika import credentials

opt_parser = OptionParser()

opt_parser.add_options("-r", "--routing-key", dest="routing_key", help = "Routing key for message " + " (e.g. myalert.im)")

opt_parser.add_options("-m", "--message", dest="message", help="Message text for alert.")

args = opt_parser.parse_args()[0]

creds_broker = pika.PlainCredentials("sample", "sample")

conn_params = pika.ConnectionParameters("", virtual_host="/", credentials = creds_broker)

conn_broker = pika.BlockingConnection(conn_params)

channel = conn_broker.channel()

msg = json.dumps(args.message)
msg_props = pika.BasicProperties()
msg_props.content_type = "application/json"
msg_props.durable = False

channel.basic_publish(exchange, routing_key, body, properties, mandatory, immediate)