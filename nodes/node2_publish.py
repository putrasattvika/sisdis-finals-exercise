#!/usr/bin/env python
import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

e = 'GREEN_EX'
r = 'NODE2'

channel.basic_publish(exchange=e,
                      routing_key=r,
                      body='Hello from NODE2!')

print("[x] Sent 'Hello from NODE2 to ex={}, r={}'".format(e, r))

connection.close()
