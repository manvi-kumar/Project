# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 17:36:30 2023

@author: MK
"""
import copy
from heapq import heappush, heappop
n = 3

# bottom, left, top, right
row = [ 1, 0, -1, 0 ]
col = [ 0, -1, 0, 1 ]


class priorityQueue:
	
	
	
	def __init__(self):
		self.heap = []

	
	def push(self, k):
		heappush(self.heap, k)

	# Method to remove minimum element from Priority Queue
	def pop(self):
		return heappop(self.heap)

	# Method to know if the Queue is empty
	def empty(self):
		if not self.heap:
			return True
		else:
			return False


class node:
	
	def __init__(self, parent, mat, empty_block_pos,
				cost, level):
					
		# Stores the parent node of the current node helps in tracing path when the answer is found
		self.parent = parent

		# Stores the matrix
		self.mat = mat

		# Stores the position at which the empty space block exists in the matrix
		self.empty_block_pos = empty_block_pos

		# Stores the number of misplaced block
		self.cost = cost

		# Stores the number of moves so far
		self.level = level

	# This method is defined so that the
	# priority queue is formed based on
	# the cost variable of the objects
	def __lt__(self, nxt):
		return self.cost < nxt.cost

#Function to count the number of non-blank blocks not in their final position
def calculateCost(mat, final) -> int:
	
	count = 0
	for i in range(n):
		for j in range(n):
			if ((mat[i][j]) and
				(mat[i][j] != final[i][j])):
				count += 1
				
	return count

def newNode(mat, empty_block_pos, new_empty_block_pos,
			level, parent, final) -> node:
				
	# Copy data from parent matrix to current matrix
	new_mat = copy.deepcopy(mat)

	# Move tile by 1 position
	x1 = empty_block_pos[0]
	y1 = empty_block_pos[1]
	x2 = new_empty_block_pos[0]
	y2 = new_empty_block_pos[1]
	new_mat[x1][y1], new_mat[x2][y2] = new_mat[x2][y2], new_mat[x1][y1]

	# Set number of misplaced blocks
	cost = calculateCost(new_mat, final)

	new_node = node(parent, new_mat, new_empty_block_pos,
					cost, level)
	return new_node

# Function to print the NxN matrix
def printMatrix(mat):
	
	for i in range(n):
		for j in range(n):
			print("%d " % (mat[i][j]), end = " ")
			
		print()

# Function to check if (x, y) is a valid matrix coordinate
def isSafe(x, y):
	
	return x >= 0 and x < n and y >= 0 and y < n

# Print path from root node to destination node
def printPath(root):
	
	if root == None:
		return
	
	printPath(root.parent)
	printMatrix(root.mat)
	print()

def solve(initial, empty_tile_pos, final):
	
	#a priority queue to store live nodes of search tree
	pq = priorityQueue()

	# Create the root node
	cost = calculateCost(initial, final)
	root = node(None, initial,
				empty_tile_pos, cost, 0)

	# Add root to list of live nodes
	pq.push(root)

	# Finds a live node with least cost, add its children to list of live nodes and finally deletes it from 
    #the list.
	while not pq.empty():

		# Find a live node with least estimated cost and delete it from the list of live nodes
		minimum = pq.pop()

		# If minimum is the answer node
		if minimum.cost == 0:
			
			# Print the path from root to destination;
			printPath(minimum)
			return

		# Generate all possible children
		for i in range(4):
			new_tile_pos = [
				minimum.empty_tile_pos[0] + row[i],
				minimum.empty_tile_pos[1] + col[i], ]
				
			if isSafe(new_tile_pos[0], new_tile_pos[1]):
				
				#Creating a child node
				child = newNode(minimum.mat,
								minimum.empty_tile_pos,
								new_tile_pos,
								minimum.level + 1,
								minimum, final,)

				# Add child to list of live nodes
				pq.push(child)



#Initial configuration
#0 is used for empty space
initial = [ [ 1, 8, 5 ],
			[ 3, 0, 4 ],
			[ 6, 7, 2 ] ]

#Solvable Final configuration
final = [ [ 1, 2, 3 ],
		[ 4, 5,  6 ],
		[ 7, 8, 0 ] ]

#Blank block coordinates in initial configuration
empty_tile_pos = [ 2, 2 ]

#Function call to solve the puzzle
solve(initial, empty_tile_pos, final)


