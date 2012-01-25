# Simple Stock Portfolio Manager (SSPM)

SSPM is a simple python script that allows you to quickly and easily track the performance of your stock portfolio.

## Requirements

SSPM requires python to have been installed.

## Installation 

Place the **sspm.py** file and the **portfolio.txt** file anywhere on your system. (ie. ~/.sspm)

Now you can run SSPM with (if using ~/.sspm as install directory):

	python ~/.sspm/sspm.py ~/.sspm/portfolio.txt

You can alias this by adding the following to your **~/.bashrc**:

	alias sspm="python ~/.sspm/sspm.py ~/.sspm/portfolio.txt"

Now you can run SSPM any time in the terminal just by running:

	sspm

## Portfolio Format

Edit the **portfolio.txt** file to include your stock portfolio data.

It is stored in the following format:

	SYMBOL	NUMBER_OF_SHARES	PRICE_PAID

Just add another line for each stock you want to track.

## Sample Output

This is an example of what the output looks like on a terminal.

>sspm

	┌────────┬────────┬──────────────┬──────────────┬──────────────┬───────────┐
	│ SYMBOL │ SHARES │ PRICE PAID   │ MARKET VALUE │ CHANGE $     │ CHANGE %  │
	├────────┼────────┼──────────────┼──────────────┼──────────────┼───────────┤
	│ GOOG   │     27 │      $11,141 │      $15,685 │       $4,544 │    40.79% │
	├────────┼────────┼──────────────┼──────────────┼──────────────┼───────────┤
	│ MSFT   │     95 │       $2,229 │       $2,787 │         $557 │    25.01% │
	├────────┼────────┼──────────────┼──────────────┼──────────────┼───────────┤
	│ AAPL   │     40 │       $3,226 │      $16,816 │      $13,589 │   421.15% │
	├────────┼────────┼──────────────┼──────────────┼──────────────┼───────────┤
	│ AMZN   │     14 │       $2,180 │       $2,618 │         $437 │    20.04% │
	└────────┴────────┼──────────────┼──────────────┼──────────────┼───────────┤
	                  │      $18,778 │      $37,906 │      $19,128 │   101.86% │
	                  └──────────────┴──────────────┴──────────────┴───────────┘

