# -*- coding: utf-8 -*-
import os
import urllib
import locale
import sys

locale.setlocale( locale.LC_ALL, '' )

def printHeader():
	print('');
	print('┌────────┬──────────┬───────────┬───────────────┬──────────────┬──────────────┐');
	print('│ {0} │ {1:<8} │ {2:<9} │ {3:<13} │ {4:<12} │ {5:<12} │'.format('SYMBOL','SHARES','PURCHASE','PRICE', 'CHANGE', 'VALUE'));
	print('├────────┼──────────┼───────────┼───────────────┼──────────────┼──────────────┤');
	return;

def printFooter():
	print('├────────┼──────────┼───────────┼───────────────┼──────────────┼──────────────┤');
	return;

def printHeaderTotals():
	print('└────────┴──────────┴───────────┴───────────────┼──────────────┼──────────────┤');
	return;

def printFooterTotals():
	print('                                                └──────────────┴──────────────┘');
	print('');
	return;

def printRow(symbol, shares, purchase_price, current_price, change, value):
	print('│ {0:>6} │ {1:>8} │ {2:>9} │ {3:>13} │ {4:>12} │ {5:>12} │'. format(symbol, shares, locale.currency(purchase_price), locale.currency(current_price), locale.currency(change), locale.currency(value) ));
	return;

def printTotalRow(total_change, total_value):
	print('                                                │ {0:>12} │ {1:>12} │'.format(locale.currency(total_change), locale.currency(total_value)));
	return;

def getStockPrice(symbol):
	url = 'http://finance.yahoo.com/d/quotes.csv?s={0}&f={1}'.format(symbol, 'l1');
	return urllib.urlopen(url).read().strip().strip('"')

def printErrorMsg():
	print('Error reading '+portfolioPath+' file.');
	print('Create '+portfolioPath+' and add your stock information.');
	print('In format: SYMBOL SHARES PURCHASE_PRICE');
	print('ie. BAC 250 5.67');
	return;

def printParamErrorMsg():
	print('Please pass the location of your stock portfolio file.');
	return;

###############################################################################################	

if(len(sys.argv) <= 1):
	printParamErrorMsg();
	exit();

portfolioPath = sys.argv[1];

try:
	file = open(portfolioPath,'r');
except IOError as e:
	printFileErrorMsg();
	exit();

lines = file.read().splitlines();
symbol = [];
shares = [];
purchase_price = [];
current_price = [];
change = [];
value = [];

total_change = 0;
total_value = 0;

for l in lines:
	values = l.split();
	symbol.append(values[0]);
	shares.append(int(values[1]));
	purchase_price.append(float(values[2]));
	current_price.append(float(getStockPrice(values[0])));
	change.append(current_price[-1] - float(values[2]));
	value.append(current_price[-1] * float(values[1]));

	total_change += change[-1] * shares[-1];
	total_value += current_price[-1] * shares[-1];

printHeader();

for i in range(len(symbol)):
	printRow(symbol[i], shares[i], purchase_price[i], current_price[i], change[i], value[i]);
	if(i != len(symbol) - 1):
		printFooter();

printHeaderTotals();
printTotalRow(total_change, total_value);
printFooterTotals();
