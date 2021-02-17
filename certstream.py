import certstream
import sys
import datetime
import logging
import yaml

def print_callback(message, context):
	if message['message_type'] == "certificate_update":
		all_domains = message['data']['leaf_cert']['all_domains']
		if len(all_domains) == 0:
			domain = "NULL"
		else:
			domain = all_domains[0]

		sys.stdout.write(u"[{}] {} (SAN: {})\n".format(datetime.datetime.now().strftime('%m/%d/%y %H:%M:%S'), domain, ", ".join(message['data']['leaf_cert']['all_domains'][1:])))
		sys.stdout.flush()
		
		score = 0

		for t in suspicious['tlds']:
			if domain.endswith(t):
				score += 20



logging.basicConfig(format='[%(levelname)s:%(name)s] %(asctime)s - %(messgae)s', level=logging.INFO)

certstream.listen_for_events(print_callback, url='wss://certstream.calidog.io/')

