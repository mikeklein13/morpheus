import os
import sys

def append_paths():
	for root, dirs, files in os.walk('static'):
		for filename in files:
			filepath = os.path.join(root, filename)

		if root not in static:
		    static[root] = []

		static[root].append(filepath)

append_paths()