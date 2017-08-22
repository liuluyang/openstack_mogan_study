import pika
import time
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

def callback(ch, method, properties, body):
    time.sleep( body.count('.') )
    print body,'this is body'

channel.basic_consume(callback,
                      queue='hello',
                      no_ack=True
                      )

print 'Waiting for message . to exit press ctrl+c'
channel.start_consuming()