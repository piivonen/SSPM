# Simple Stock Portfolio Manager (SSPM)

SSPM is a simple python script that allows you to quickly and easily track the performance of your stock portfolio.

## Requirements

SSPM requires python to have been installed.

## Installation 

Place the **sspm.py** file and the **portfolio.txt** file anywhere on your system. (ie. ~/.ssmp)

Now you can run SSMP with (if using ~/.ssmp as install directory):

	python ~/.ssmp/ssmp.py ~/.ssmp/portfolio.txt

You can alias this by adding the following to your **~.bashrc**:

	alias sspm="python ~/.ssmp/ssmp.py ~/.ssmp/portfolio.txt"

Now you can run SSMP any time in the terminal just by running:

	sspm

## Portfolio Format

Edit the **portfolio.txt** file to include your stock portfolio data.

It is stored in the following format:

	SYMBOL	NUMBER_OF_SHARES	PRICE_PAID

Just add another line for each stock you want to track.
