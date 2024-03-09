#!/usr/bin/env python

from operator import itemgetter
from itertools import groupby


# Enter the data to be processed.
rows = [ 
	{ 'stock': 'IBM', 'date': '04/01/23', 'price': '23.32'},
	{ 'stock': 'APPL', 'date': '04/01/23', 'price': '26.23'},
	{ 'stock': 'MSFT', 'date': '04/01/23', 'price': '54.43'},
	{ 'stock': 'META', 'date': '04/01/23', 'price': '22.12'},
]

# Sort the rows by the stock symbol.
rows.sort(key=itemgetter('stock'))

# For symbol/item in group of rows -> get the stock symbol.
for sym, item in groupby (rows, key=itemgetter('stock')):
	# Print the symbol.
	print(sym)
	# Print the rest of the data associated with the symbol.
	for i in item:
		print('     ', i)

