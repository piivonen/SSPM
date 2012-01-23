# -*- coding: utf-8 -*-
import os
import ystockquote
import locale

locale.setlocale( locale.LC_ALL, '' )

def printHeader():
	print('');
	print('┌────────┬──────────┬────────────────┬───────────────┬──────────┬──────────────┐');
	print('│ SYMBOL'.ljust(11) + '│' + '  SHARES'.ljust(10) + '│' + ' PURCHASE PRICE'.ljust(16) + '│' + ' CURRENT PRICE'.ljust(15) + '│' + '  CHANGE'.ljust(10) + '│' +  ' TOTAL VALUE'.ljust(14) + '│');
	print('├────────┼──────────┼────────────────┼───────────────┼──────────┼──────────────┤');
	return;

def printFooter():
	print('├────────┼──────────┼────────────────┼───────────────┼──────────┼──────────────┤');
	return;

def printHeaderTotals():
	print('└────────┴──────────┴────────────────┴───────────────┼──────────┼──────────────┤');
	return;

def printFooterTotals():
	print('                                                     └──────────┴──────────────┘');
	print('');
	return;


portfolioPath = os.getenv('HOME')+'/.sspm';
try:
	file = open(portfolioPath,'r');
except IOError as e:
	print('Error reading '+portfolioPath+' file.');
	print('Create '+portfolioPath+' and add your stock information.');
	print('In format: SYMBOL SHARES PURCHASE_PRICE');
	print('ie. BAC 250 5.67');
	exit();

lines = file.read().splitlines();
symbol = [];
shares = [];
purchase_price = [];
current_price = [];
change = [];
total_value = [];

for l in lines:
	values = l.split();
	stockPrice = float(ystockquote.get_price(values[0]));

	symbol.append(values[0]);
	shares.append(int(values[1]));
	purchase_price.append(float(values[2]));
	current_price.append(stockPrice);
	change.append(stockPrice - float(values[2]));
	total_value.append(stockPrice * float(values[1]));

printHeader();

for i in range(len(symbol)):
	print('│ {0:>6} │ {1:>8} │ {2:>14} │ {3:>13} │ {4:>8} │ {5:>12} │'.format(symbol[i], shares[i], locale.currency(purchase_price[i]), locale.currency(current_price[i]), locale.currency(change[i]), locale.currency(total_value[i]) ));
	if(i != len(symbol) - 1):
		printFooter();


#print('│        │          │                │               │          │              │');

printHeaderTotals();

print('                                                     │          │              │');

printFooterTotals();
