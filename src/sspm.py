# -*- coding: utf-8 -*-
import os
import urllib
import locale
import sys

GREEN = '\033[92m'
RED = '\033[91m'
END_COLOR = '\033[0m'

locale.setlocale( locale.LC_ALL, '' )

def printHeader():
	print('');
	print('┌────────┬────────┬──────────────┬──────────────┬──────────────┬───────────┐');
	print('│ {0:<6} │ {1:<6} │ {2:<12} │ {3:<12} │ {4:<12} │ {5:<9} │'.format('SYMBOL','SHARES','PRICE PAID','MARKET VALUE','CHANGE $','CHANGE %'));
	return;

def printFooter():
	print('├────────┼────────┼──────────────┼──────────────┼──────────────┼───────────┤');
	return;

def printHeaderTotals():
	print('└────────┴────────┼──────────────┼──────────────┼──────────────┼───────────┤');
	return;

def printFooterTotals():
	print('                  └──────────────┴──────────────┴──────────────┴───────────┘');
	print('');
	return;

def printRow(symbol, shares, price_paid, market_value, change_money, change_percent):
	# if the stock has gone up or down, color it
	change_color = GREEN
	if(change_money < 0):
		change_color = RED
	print('│ {0:<6} │ {1:>6} │ {2:>12} │ {3:>12} │ {4}{5:>12}{6} │ {7}{8:>8.2f}%{9} │'. format(symbol, shares, locale.currency(int(price_paid), grouping=True)[:-3], locale.currency(int(market_value), grouping=True)[:-3], change_color, locale.currency(int(change_money), grouping=True)[:-3], END_COLOR, change_color, change_percent * 100, END_COLOR ));
	return;

def printTotalRow(total_price_paid, total_market_value, total_change_money, total_change_percent):
	# if the stock has gone up or down, color it
	status_color = GREEN
	if(total_change_money < 0):
		status_color = RED
	print('                  │ {0:>12} │ {1:>12} │ {2}{3:>12}{4} │ {5}{6:>8.2f}%{7} │'.format(locale.currency(int(total_price_paid), grouping=True)[:-3],locale.currency(int(total_market_value),grouping=True)[:-3],status_color,locale.currency(int(total_change_money),grouping=True)[:-3],END_COLOR,status_color,total_change_percent * 100,END_COLOR));
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
price_paid = [];
market_value = [];
change_money = [];
change_percent = [];

total_price_paid = 0;
total_market_value = 0;
total_change_money = 0;
total_change_percent = 0;

for l in lines:
	# SYMBOL SHARES PURCHASE_PRICE
	values = l.split();
	symbol.append(values[0]);
	shares.append(int(values[1]));
	price_paid.append(float(values[2]) * shares[-1]);
	market_value.append(float(getStockPrice(values[0])) * shares[-1]);
	change_money.append(market_value[-1] - price_paid[-1]);
	change_percent.append(change_money[-1] / price_paid[-1]);

	# Add totals
	total_price_paid += price_paid[-1];
	total_market_value += market_value[-1];
	total_change_money += change_money[-1];

total_change_percent = total_change_money / total_price_paid;

printHeader();
printFooter();

for i in range(len(symbol)):
	printRow(symbol[i], shares[i], price_paid[i], market_value[i], change_money[i], change_percent[i]);
	if(i != len(symbol) - 1):
		printFooter();

printHeaderTotals();
printTotalRow(total_price_paid, total_market_value, total_change_money, total_change_percent);
printFooterTotals();
