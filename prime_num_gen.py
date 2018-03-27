# A prime number generator
# by Kai Staats, MSc
# 2018 03/27

import os
import sys
import csv
import numpy as np

np.set_printoptions(linewidth = 320) # set the terminal to print 320 characters before line-wrapping in order to view Trees

cwd = os.getcwd()

if len(sys.argv) == 1: print '\n\t\033[31mERROR!\033[0;0m You have assigned too few arguments.\n\n\tAssign [qty]. Try again ...'; sys.exit()
elif len(sys.argv) == 2: search = int(sys.argv[1]); mode = 's'
elif len(sys.argv) == 3: search = int(sys.argv[1]); mode = 'd'
else: print '\n\t\033[31mERROR!\033[0;0m You have assigned too many arguments.\n\n\tAssign [qty]. Try again ...'; sys.exit()

primes = [2]

for n in range(2, search + 1):
	if mode == 'd': print '\nsearch:'
	
	m = 0; nap = 0
	while m < len(primes):
		test = str(float(n)/primes[m]).split('.')[1] # divide 'search' by a known prime and capture the floating points
		if mode == 'd': print '\t', str(n) + ' / ' + str(primes[m]) + ' = .' + str(test)
		if int(test) == 0: nap = 1; m = len(primes) # not a prime, so terminate the while loop
		else: m = m + 1
		
	if nap == 0: 
		primes.append(n)
		if mode == 'd': print '\tprime'
		
	else: 
		if mode == 'd': print '\tnot prime'

print '\nqty of primes generated:', len(primes)


### Save the List of Primes ###

with open('prime_num.txt', 'w') as prime_list:
	for line in primes:
		prime_list.write(str(line) + '\n')


