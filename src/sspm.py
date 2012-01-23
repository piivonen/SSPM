# -*- coding: utf-8 -*-
import os
import ystockquote

stock = ystockquote.get_price('BAC');

portfolioPath = os.getenv('HOME')+'/.sspm';
try:
	file = open(portfolioPath,'r');
except IOError as e:
	print('Error reading '+portfolioPath+' file.');
	print('Create '+portfolioPath+' and add your stock information.');
	print('In format: SYMBOL SHARES PURCHASE_PRICE');
	print('ie. BAC 250 5.67');
	exit();

print('┌────────┬──────────┬────────────────┬───────────────┬──────────┬──────────────┐');
print('│ SYMBOL'.ljust(11) + '│' + '  SHARES'.ljust(10) + '│' + ' PURCHASE PRICE'.ljust(16) + '│' +
	' CURRENT PRICE'.ljust(15) + '│' + '  CHANGE'.ljust(10) + '│' +  ' TOTAL VALUE'.ljust(14) + '│');
print('└────────┴──────────┴────────────────┴───────────────┴──────────┴──────────────┘');
