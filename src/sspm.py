# -*- coding: utf-8 -*-
import os
import ystockquote

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
	symbol.append(values[0]);
	shares.append(int(values[1]));
	purchase_price.append(float(values[2]));

	stockPrice = float(ystockquote.get_price(values[0]));
	current_price.append(stockPrice);

	change.append(stockPrice - float(values[2]));
	total_value.append(stockPrice * int(values[1]));

print(total_value);

printHeader();

print('│        │          │                │               │          │              │');

printHeaderTotals();

print('                                                     │          │              │');

printFooterTotals();
