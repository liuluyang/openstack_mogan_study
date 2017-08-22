#coding:utf8

import pika
'''
connection = pika.BlockingConnection(pika.ConnectionParameters(host='127.0.0.1'))
print '1'
channel = connection.channel()

channel.queue_declare(queue='hello')
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='this is my send message'
                      )
print 'sending my message to queue of hello'
connection.close()
'''
import pika

connection = pika.BlockingConnection()
#pika.SelectConnection()
'''
channel = connection.channel()

channel.queue_declare(queue='hello')

channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')
print " [x] Sent 'Hello World!'"
import time
time.sleep(3)
connection.close()
'''