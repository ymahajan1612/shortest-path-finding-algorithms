from collections import deque
import pygame as pg

class Grid:
	def __init__(self):
		self.maze_arr = self.setUpMaze()
		self.width = len(self.maze_arr[0])
		self.height = len(self.maze_arr)


	def setUpMaze(self):
		maze = []
		width = int(input("Enter the width"))
		height = int(input("Enter a height"))
		for i in range(height):
			row = []
			for j in range(width):
				row.append("#")
			maze.append(row)
		return maze

	def printMaze(self, path=""):
		print(self.maze_arr)


	def getNeighbours(self,cell_index):
		neighbours = []
		if cell_index[0] > 0:
			neighbours.append((cell_index[0] - 1, cell_index[1]))
		if cell_index[0] < len(self.maze_arr):
			neighbours.append((cell_index[0] + 1, cell_index[1]))
		if cell_index[1] > 0:
			neighbours.append((cell_index[0],cell_index[1]-1))
		if cell_index[1] < len(self.maze_arr[0]):
			neighbours.append((cell_index[0],cell_index[1]+1))
		return [pos for pos in neighbours if self.maze_arr[pos[0]][pos[1]]!="#"]


	def getStart(self):
		for i,row in enumerate(self.maze_arr):
			for j,value in enumerate(row):
				if value == "S":
					return (i,j)
	def getEnd(self):
		for i,row in enumerate(self.maze_arr):
			for j,value in enumerate(row):
				if value == "E":
					return (i,j)

	def getArray(self):
		return self.maze_arr


class BFS:
	def __init__(self,maze_obj):
		self.maze_obj = maze_obj
		self.solved_maze = maze_obj.getArray()
		self.q = deque()
		self.start = maze_obj.getStart()
		self.visited = []

	def run(self):
		self.visited.append(self.start)
		self.q.append(self.start)
		while len(self.q)>0:
			curr_node = self.q.popleft()
			if curr_node == self.maze_obj.getEnd():
				return curr_node
			else:
				for neighbour in self.maze_obj.getNeighbours(curr_node):
					if neighbour not in self.visited:
						self.visited.append(neighbour)
						self.q.append(neighbour)



new_grid = Grid()
new_grid.printMaze()