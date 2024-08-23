from typing import List


class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.height = height
        self.width = width
        self.food = food
        self.i = 0  # ptr on food
        self.snake = []  # linked list of ints
        self.snakeHead = (0, 0)
        # self.visited = [[False for _ in range(width)] for _ in range(height)]
        self.visited = set()
        # snake tail is head of linkedList
        # snake head is tail of linkedList
        self.snake.append(self.snakeHead)

    def move(self, direction: str) -> int:  # O(1)
        if direction == "R":
            # self.snakeHead[1] += 1
            self.snakeHead = (self.snakeHead[0], self.snakeHead[1]+1)
        elif direction == "U":
            # self.snakeHead[0] -= 1
            self.snakeHead = (self.snakeHead[0]-1, self.snakeHead[1])
        elif direction == "L":
            # self.snakeHead[1] -= 1
            self.snakeHead = (self.snakeHead[0], self.snakeHead[1]-1)
        elif direction == "D":
            # self.snakeHead[0] += 1
            self.snakeHead = (self.snakeHead[0]+1, self.snakeHead[1])

        # bounds check
        if (self.snakeHead[0] < 0 or self.snakeHead[0] == self.height
                or self.snakeHead[1] < 0 or self.snakeHead[1] == self.width):
            return -1
        # if snake hits itself
        # never mark the tail inside  - skip checking the tail
        # tail = snake[0]
        if (self.snakeHead[0], self.snakeHead[1]) in self.visited:
            return -1
        # food move
        if self.i < len(self.food):
            foodLoc = self.food[self.i]
            if (self.snakeHead[0] == foodLoc[0]
                    and self.snakeHead[1] == foodLoc[1]):
                # eat food
                self.i += 1
                self.snake.append(self.snakeHead)
                # self.visited[self.snakeHead[0]][self.snakeHead[1]] = True
                self.visited.add((self.snakeHead[0], self.snakeHead[1]))
                return len(self.snake) - 1

        # normal move
        self.snake.append(self.snakeHead)
        # make new head
        # self.visited[self.snakeHead[0]][self.snakeHead[1]] = True
        self.visited.add((self.snakeHead[0], self.snakeHead[1]))
        self.snake.pop(0)
        tail = self.snake[0]
        # self.visited[tail[0]][tail[1]] = False
        self.visited.remove((tail[0], tail[1]))

        return len(self.snake) - 1

# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)
