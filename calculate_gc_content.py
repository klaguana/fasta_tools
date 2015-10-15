#!/usr/bin/env python

# Command line script to calculate base frequency from a .fasta file

from __future__ import division
import sys


a_count = 0
c_count = 0
g_count = 0
t_count = 0

with open(sys.argv[1], 'r') as fasta:
    for line in fasta:
        if line.startswith(">"):
            # Header line, skip it
            continue
        else:
            a_count += line.count("A")
	    c_count += line.count("C")
            g_count += line.count("G")
	    t_count += line.count("T")
	    p = a_count + c_count + g_count + t_count
   #    for base in line.strip():
   #         if base == "A":
   #             a_count += 1
   #         elif base == "C":
   #            c_count += 1
   #         elif base == "G":
   #             g_count += 1
   #         elif base == "T": 
   #             t_count += 1

print("Base counts for file %s:" % sys.argv[1])
print("A: %d" % a_count)
print '{:.0%}'.format(a_count/p)
print("C: %d" % c_count)
print '{:.0%}'.format(c_count/p)
print("G: %d" % g_count)
print '{:.0%}'.format(g_count/p)
print("T: %d" % t_count)
print '{:.0%}'.format(t_count/p)
