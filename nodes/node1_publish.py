#!/usr/bin/env python
import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

e = 'ORANGE_EX'
r = 'NODE1'

channel.basic_publish(exchange=e,
                      routing_key=r,
                      body='Hello from NODE1!')

print("[x] Sent 'Hello from NODE1 to ex={}, r={}'".format(e, r))

connection.close()
