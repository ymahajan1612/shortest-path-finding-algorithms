import queue


def createMaze():
	maze = []
	maze.append(["#", "#", "#", "#", "#", "O", "#"])
	maze.append(["#", " ", " ", " ", "#", " ", "#"])
	maze.append(["#", " ", "#", " ", "#", " ", "#"])
	maze.append(["#", " ", "#", " ", " ", " ", "#"])
	maze.append(["#", " ", "#", "#", "#", " ", "#"])
	maze.append(["#", " ", " ", " ", "#", " ", "#"])
	maze.append(["#", "#", "#", "#", "#", "X", "#"])

	return maze


def createMaze2():
	maze = []
	maze.append(["#", "#", "#", "#", "#", "O", "#", "#", "#"])
	maze.append(["#", " ", " ", " ", " ", " ", " ", " ", "#"])
	maze.append(["#", " ", "#", "#", " ", "#", "#", " ", "#"])
	maze.append(["#", " ", "#", " ", " ", " ", "#", " ", "#"])
	maze.append(["#", " ", "#", " ", "#", " ", "#", " ", "#"])
	maze.append(["#", " ", "#", " ", "#", " ", "#", " ", "#"])
	maze.append(["#", " ", "#", " ", "#", " ", "#", "#", "#"])
	maze.append(["#", " ", " ", " ", " ", " ", " ", " ", "#"])
	maze.append(["#", "#", "#", "#", "#", "#", "#", "X", "#"])

	return maze


def printMaze(maze, path=""):
	for x, pos in enumerate(maze[0]):
		if pos == "O":
			start = x

	i = start
	j = 0
	pos = set()

	for j, row in enumerate(maze):
		for i, col in enumerate(row):
			if (j, i) in pos:
				print("+ ", end="")
			else:
				print(col + " ", end="")
		print()

class Maze:
	def __init__(self,maze_arr):
		self.maze_arr = maze_arr

	def printMaze(self, path=""):
		for x, pos in enumerate(self.maze_arr[0]):
			if pos == "O":
				start = x

		i = start
		j = 0
		pos = set()

		for j, row in enumerate(self.maze_arr):
			for i, col in enumerate(row):
				if (j, i) in pos:
					print("+ ", end="")
				else:
					print(col + " ", end="")
			print()

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



test_maze = Maze(createMaze())
test_maze.printMaze()

