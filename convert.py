import yaml
import tldextract
from numpy import array

def numberify(array_list):
	idea = ["facebook", "paypal", "facebook-fake", "op", "com", "gg", "org", "zip"]

	master_domain_list = []
	with open('examples.yaml', 'r') as examples:
		outputs = []
		for domains in examples:
			domain, value = domains.partition("=")[::2]
			domain_list = []
			tld = tldextract.extract(domain).suffix
			non_tld = tldextract.extract(domain).domain
			for i in idea:
				if i in non_tld or i in tld:
					domain_list.append(1)
				else:
					domain_list.append(0)
			outputs.append(int(value))
			#print(domain + ": " + str(array(domain_list)) + " - " + str(value))
			master_domain_list.append(array(domain_list))
	return master_domain_list, outputs

