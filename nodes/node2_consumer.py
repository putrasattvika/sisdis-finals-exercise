#!/usr/bin/env python2
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

e = 'BLUE_EX'
r = 'NODE2'

q = channel.queue_declare()
channel.queue_bind(q.method.queue, e, routing_key=r)

def callback(ch, method, properties, body):
    print("  [x] Received %r" % body)

channel.basic_consume(callback,
                      queue=q.method.queue,
                      no_ack=True)

print('[*] Waiting for messages on {}. To exit press CTRL+C'.format(q))
channel.start_consuming()
channel.queue_delete()
