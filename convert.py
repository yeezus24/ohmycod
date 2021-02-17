import yaml
import tldextract
from numpy import array

def numberify(url_to_check):
	examples = open('examples.txt', 'r').read()
	array_list = open('array_list.txt', 'r').read()
	converted_examples = []
	outputs = []
	converted_url = []

	# Convert the URLs in examples to sparse arrays
	for domains in examples.split("\n"):
		if domains != "":
			domain_array = []
			domain, value = domains.partition("=")[::2]
			for keyword in array_list.split():
				if keyword in domain:
					domain_array.append(1)
				else:
					domain_array.append(0)
			converted_examples.append(domain_array)
			outputs.append(int(value))

	if url_to_check != None:
		for keyword in array_list.split():
			if keyword in url_to_check:
				converted_url.append(1)
			else:
				converted_url.append(0)

	return converted_examples, outputs, converted_url
