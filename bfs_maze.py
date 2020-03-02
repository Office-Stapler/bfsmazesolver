import queue, random
class Maze:
    def __init__(self, size):
        self.size = size
        start = (random.randint(0, size - 1), random.randint(0, size - 1))
        end = (random.randint(0, size - 1), random.randint(0, size - 1))
        imaze = []
        for i in range(0, size):
            nmaze =[]
            for j in range(0, size):
                if (i,j) == start:
                    nmaze.append('O')
                elif (i,j) == end:
                    nmaze.append('X')
                else:
                    nmaze.append(' ' if random.randint(0,10) % 4 else '#')
            imaze.append(nmaze)
        self.maze = imaze
        self.start = self.findStart()
        self.path = ''
        self.replaced = []
    
    def replaceMaze(self, path):
        move_y = {'U': -1, 'D': 1}
        move_x = {'R': 1, 'L': -1}
        x,y = self.start
        replaced = self.maze
        for i in path:
            replaced[y][x] = '+'
            if i in move_x:
                x += move_x[i]
            else:
                y += move_y[i]
        self.replaced = replaced
        self.replaced[self.start[1]][self.start[0]] = 'O'

    def valid(self, position, move, visited):
        move_y = {'U': -1, 'D': 1}
        move_x = {'R': 1, 'L': -1}
        x,y = position[0], position[1]

        if move in move_x:
            x += move_x[move]
        else:
            y += move_y[move]
        
        if (x,y) in visited:
            return False

        return True if  0 <= x < len(self.maze[0]) and 0 <= y < len(self.maze) and self.maze[y][x] != '#' else False

    def findStart(self):
        for i in enumerate(self.maze):
            if 'O' in self.maze[i[0]]:
                return (self.maze[i[0]].index('O'), i[0])
        return (-1,-1)

    def solveMaze(self):
        start = self.start
        move_y = {'U': -1, 'D': 1}
        move_x = {'R': 1, 'L': -1}
        x, y = start[0], start[1]
        q = queue.Queue()
        q.put(('', (x,y)))
        visited = []
        while not q.empty():
            curr = q.get()
            visited.append(curr[1])
            x,y = curr[1][0], curr[1][1]
            if self.maze[y][x] == 'X':
                path = curr[0]
                break
            for i in ['L', 'R', 'U', 'D']:
                if self.valid(curr[1], i, visited):
                    path = curr[0] + i
                    if i in move_x:
                        q.put((path, (x + move_x[i], y)))
                    else:
                        q.put((path, (x,y + move_y[i])))
        if self.maze[y][x] != 'X':
            path = ''
        self.path = path

    def printList(self, nList):
        for i in nList:
            print(i)


