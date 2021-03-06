#!/usr/bin/python3

import sys

args = len(sys.argv) - 1
if args < 1:
	print('wrong number of arguments')
	exit()

filename = sys.argv[1]
numRows = -1
delimiter = '\t'
headerRowNum = 0

if args >= 2:
	numRows = int(sys.argv[2])
#if args >= 3:
#	delimiter = sys.argv[3]
if args >= 3:
	headerRowNum = int(sys.argv[3])

try:
	handle = open(filename)
except:
	'filename used not in path'
	exit()

while headerRowNum != 0:
	handle.readline()
	headerRowNum -= 1

headers = handle.readline().strip().split(delimiter)

currentRow = 0
rows = list()

while currentRow != numRows:
	line = handle.readline()
	if not line:
		break
	columns = line.strip().split(delimiter)
	if len(headers) == len(columns):
		rows.append(columns)
		currentRow += 1
	line = handle.readline().strip()


for row in rows:
	for index in range(len(headers)):
		print(headers[index], '::\t', row[index])
	print('\n')
