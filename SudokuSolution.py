# KCT 2015
# Sudoku Solution program
#!/usr/bin/python

import sys

Boxes = range(9)
Rows = range(1,10)

def readSudoku(f):
	return [[int(k) for k in list(line.rstrip())] for line in f.readlines()]

def row(i, grid):
	return grid[i]

def column(j, grid):
	return [grid[i][j] for i in Boxes]

def block(i,j,grid):
	return [grid[(i/3)*3+k][(j/3)*3+t] for k in range(3) for t in range(3)]

def missing(first):
	return [x for x in Rows if x not in first]

def possible(i,j):
	if sudoku[i][j]: return[]
	else:
		return [x for x in Rows if x in missing(row(i,sudoku)) and x in missing
				(column(j, sudoku)) and x in missing(block(i,j,sudoku))]

def genPossibilities():
	return [[possible(i,j) for j in Boxes] for i in Boxes]

def drop(first, i):
	return [first[j] for j in range(len(first)) if i != j]

def flat(first):
	return [x for y in first for x in y]

def checkExcept(x, first, pos):
	return x not in flat(drop(first, pos))

puzzle = readSudoku(open(sys.argv[1])) 
change = True
while change:
	change = False
	possible = genPossibilities() for i in Boxes:
	for j in Boxes:
		if len(possible[i][j]) == 1:
			sudoku[i][j] = possible[i][j][0]
			change = True
			for x in possible[i][j]:
					if (checkExcept(x, block(i, j, possible), (i%3)*3 + j%3) or
					 checkExcept(x, column(j, possible), i) or 
					 checkExcept(x, row(i, possible), j)):
						change = True 
						sudoku[i][j] = x

						for I in Boxes: 
							print sudoku[i]