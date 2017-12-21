import pika
import logging
import threading

from base_consumer import BaseConsumer

class Node1RelayConsumer(BaseConsumer):
	def __init__(self, src_conn_mgr, dst_conn_mgr):
		super(Node1RelayConsumer, self).__init__(src_conn_mgr)
		
		Node1RelayConsumer.DST_CONN_MGR = dst_conn_mgr

	@staticmethod
	def callback_wrapper(ch, method, properties, body):
		return Node1RelayConsumer.callback(ch, method, properties, body)

	@staticmethod
	def callback(ch, method, properties, body):
		Node1RelayConsumer.DST_CONN_MGR.rmq_publish(
			Node1RelayConsumer.DST_CONN_MGR.exchange,
			Node1RelayConsumer.DST_CONN_MGR.routing_key,
			body
		)

class Node2RelayConsumer(BaseConsumer):
	def __init__(self, src_conn_mgr, dst_conn_mgr):
		super(Node2RelayConsumer, self).__init__(src_conn_mgr)
		
		Node2RelayConsumer.DST_CONN_MGR = dst_conn_mgr

	@staticmethod
	def callback_wrapper(ch, method, properties, body):
		return Node2RelayConsumer.callback(ch, method, properties, body)

	@staticmethod
	def callback(ch, method, properties, body):
		Node2RelayConsumer.DST_CONN_MGR.rmq_publish(
			Node2RelayConsumer.DST_CONN_MGR.exchange,
			Node2RelayConsumer.DST_CONN_MGR.routing_key,
			body
		)
