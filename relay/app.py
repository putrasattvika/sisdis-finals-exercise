import pika
import time
import logging

from usagi.consumer import Node1RelayConsumer, Node2RelayConsumer
from usagi.connection import ConnectionManager

HOST = 'localhost'
USERNAME = 'guest'
PASSWORD = 'guest'

NODE1 = {
	'SRC_EX': 'ORANGE_EX',
	'SRC_KEY': 'NODE1',
	'DST_EX': 'BLUE_EX',
	'DST_KEY': 'NODE2'
}

NODE2 = {
	'SRC_EX': 'GREEN_EX',
	'SRC_KEY': 'NODE2',
	'DST_EX': 'BLUE_EX',
	'DST_KEY': 'NODE1'
}

logging.getLogger("pika").setLevel(logging.WARNING)
logger = logging.getLogger('relay.app')
format = '[%(asctime)s] %(levelname)s:%(name)s %(message)s'
logging.basicConfig(format=format, level=logging.INFO)

def main():
	node1_conn_mgrs = {
		'src_conn_mgr': ConnectionManager(
			HOST, USERNAME, PASSWORD,
			NODE1['SRC_EX'],
			routing_key=NODE1['SRC_KEY']
		),
		'dst_conn_mgr': ConnectionManager(
			HOST, USERNAME, PASSWORD,
			NODE1['DST_EX'],
			routing_key=NODE1['DST_KEY']
		),
	}

	node2_conn_mgrs = {
		'src_conn_mgr': ConnectionManager(
			HOST, USERNAME, PASSWORD,
			NODE2['SRC_EX'],
			routing_key=NODE2['SRC_KEY']
		),
		'dst_conn_mgr': ConnectionManager(
			HOST, USERNAME, PASSWORD,
			NODE2['DST_EX'],
			routing_key=NODE2['DST_KEY']
		),
	}

	node1_relay_consumer = Node1RelayConsumer(
		node1_conn_mgrs['src_conn_mgr'],
		node1_conn_mgrs['dst_conn_mgr'],
	)

	node2_relay_consumer = Node2RelayConsumer(
		node2_conn_mgrs['src_conn_mgr'],
		node2_conn_mgrs['dst_conn_mgr'],
	)

	bg_jobs = [node1_relay_consumer, node2_relay_consumer]

	logger.info('starting background jobs..')
	for job in bg_jobs:
		job.start()

	while True:
		try:
			time.sleep(10)
		except KeyboardInterrupt:
			logger.info('exiting, caugh KeyboardInterrupt')
			break
		except Exception as e:
			logger.info('exiting, caugh exception: {}'.format(e.message))
			break

	logger.info('stopping background jobs')
	for job in bg_jobs:
		job.stop()

if __name__ == '__main__':
	main()
