import sys
from kafka import SimpleProducer, SimpleClient
import os
import logging
import simplejson
logging.basicConfig(level=logging.INFO)
log = logging.getLogger("LogManager")


if __name__ == '__main__':	
	# inputDir = sys.argv[1]
	# if not os.path.exists(sys.argv[1]):
		# log.info("Input file does not exists")
		# sys.exit(0)
	# #f = open('/home/soundaryat/Downloads/datafile.txt','r')
	client = SimpleClient('localhost:9092')
	producer = SimpleProducer(client, async=False)	
	with open(sys.argv[1], 'r') as f:	
		for line in f: 
			producer.send_messages('test', line)
