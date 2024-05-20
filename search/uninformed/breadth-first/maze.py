import os
import sys
from PIL import Image, ImageDraw
from util import Node, QueueFrontier, State, Action
from typing import List, Set, Tuple


class Maze:
    def __init__(self, filename: str) -> None:
        self._load_maze(filename)

    def _load_maze(self, filename: str) -> None:
        self.maze: str = self._get_maze(filename)
        self.lines: List[str] = self.maze.splitlines()

        height, width = self._get_height_and_width()
        self.height: int = height
        self.width: int = width

        start, goal, walls = self._get_start_goal_and_walls()
        self.start: State = start
        self.goal: State = goal
        self.walls: List[List[bool]] = walls

        self.explored: Set[State] = None
        self.num_explored: int = 0
        self.solution: Tuple[List[State], List[Action]] = None

    def _get_maze(self, filename: str) -> str:
        maze = self._read(filename)
        self._validate(maze)
        return maze

    def _read(self, filename: str) -> str:
        try:
            with open(filename) as file:
                maze = file.read()
        except FileNotFoundError:
            print("File not found: %s" % filename)
            sys.exit(1)
        else:
            return maze

    def _validate(self, maze: str) -> None:
        if not maze:
            raise Exception("Invalid maze.")
        if self._does_not_have_exactly_one_start_point(maze):
            raise Exception("Maze must have exactly one start point.")
        if self._does_not_have_exactly_one_goal(maze):
            raise Exception("Maze must have exactly one goal.")

    def _does_not_have_exactly_one_start_point(self, maze: str) -> bool:
        return self._has_non_unique_occurrence(maze, "A")

    def _does_not_have_exactly_one_goal(self, maze: str) -> bool:
        return self._has_non_unique_occurrence(maze, "B")

    def _has_non_unique_occurrence(self, sentence: str, word: str) -> bool:
        return sentence.count(word) != 1

    def _get_height_and_width(self) -> Tuple[int, int]:
        height = len(self.lines)
        width = max(len(line) for line in self.lines)
        return height, width

    def _get_start_goal_and_walls(self) -> Tuple[State, State, List]:
        walls = []
        start = goal = None
        for i in range(self.height):
            row = []
            for j in range(self.width):
                try:
                    cell = self.lines[i][j]
                except IndexError:
                    row.append(False)
                else:
                    if cell == "A":
                        start = State(i, j)
                    if cell == "B":
                        goal = State(i, j)
                    row.append(cell == "#")
            walls.append(row)
        return start, goal, walls

    def solve(self) -> None:
        start = Node(state=self.start, parent=None, action=None)
        frontier = QueueFrontier()
        frontier.add(start)

        self.explored = set()
        self.num_explored = 0

        while True:
            if frontier.empty():
                print("No solution.")
                sys.exit(1)

            node = frontier.remove()
            self.num_explored += 1

            if node.state == self.goal:
                states: List[State] = []
                actions: List[Action] = []

                while node.parent is not None:
                    states.append(node.state)
                    actions.append(node.action)
                    node = node.parent

                states.reverse()
                actions.reverse()
                self.solution = (states, actions)
                return

            self.explored.add(node.state)

            for name, state in self._get_allowable_actions(node.state):
                not_in_frontier = not frontier.contains_state(state)
                not_in_explored = state not in self.explored

                if not_in_frontier and not_in_explored:
                    child = Node(state=state, parent=node, action=name)
                    frontier.add(child)

    def _get_allowable_actions(self, state: State) -> List[Action]:
        allowable_actions = []
        for action in self._get_actions(state):
            row, col = action.state

            height_range = 0 <= row < self.height
            width_range = 0 <= col < self.width

            if height_range and width_range and not self.walls[row][col]:
                allowable_actions.append(action)
        return allowable_actions

    def _get_actions(self, state: State) -> List[Action]:
        row, col = state

        actions = [
            Action("up", State(row - 1, col)),
            Action("down", State(row + 1, col)),
            Action("left", State(row, col - 1)),
            Action("right", State(row, col + 1))
        ]

        return actions

    def print(self) -> None:
        print()
        for i, row in enumerate(self.walls):
            for j, is_wall in enumerate(row):
                state = State(i, j)
                if is_wall:
                    print("█", end="")
                elif self._is_start(state):
                    print("A", end="")
                elif self._is_goal(state):
                    print("B", end="")
                elif self._in_solution(state):
                    print("*", end="")
                else:
                    print(" ", end="")
            print()
        print()

    def _is_start(self, state: State) -> bool:
        return state == self.start

    def _is_goal(self, state: State) -> bool:
        return state == self.goal

    def _in_solution(self, state: State) -> bool:
        states = self.solution[0] if self.solution is not None else None
        return states is not None and state in states

    def _was_explored(self, state: State) -> bool:
        return self.explored is not None and state in self.explored

    def output_image(
        self,
        filename: str,
        show_solution=True,
        show_explored=False
    ):
        cell_size = 50
        cell_border = 2

        width = self.width * cell_size
        height = self.height * cell_size
        size = (width, height)

        img = Image.new("RGBA", size, "black")
        draw = ImageDraw.Draw(img)

        for i, row in enumerate(self.walls):
            for j, is_wall in enumerate(row):
                state = State(i, j)
                if is_wall:
                    fill = (40, 40, 40)  # RGB: Ebony
                elif self._is_start(state):
                    fill = (255, 0, 0)  # RGB: Red
                elif self._is_goal(state):
                    fill = (0, 171, 28)  # RGB: Green
                elif self._in_solution(state) and show_solution:
                    fill = (220, 235, 113)  # RGB: Light Olive Green
                elif self._was_explored(state) and show_explored:
                    fill = (212, 97, 85)  # RGB: Coral Red
                else:
                    fill = (237, 240, 252)  # RGB: Pale Blue

                x1 = j * cell_size + cell_border
                y1 = i * cell_size + cell_border
                point1 = (x1, y1)

                x2 = (j + 1) * cell_size - cell_border
                y2 = (i + 1) * cell_size - cell_border
                point2 = (x2, y2)

                coordinates = [point1, point2]
                draw.rectangle(coordinates, fill=fill)

        img.save(filename)


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python maze.py maze.txt")

    filename = sys.argv[1]
    basename = os.path.basename(filename)
    name, extension = os.path.splitext(basename)

    if extension != ".txt":
        print("Extension not supported.")
        sys.exit(1)

    maze = Maze(filename)
    print("Maze:")
    maze.print()
    maze.output_image("images/" + name + ".png")

    print("Solving...")
    maze.solve()

    print("Solution:")
    maze.print()
    maze.output_image("images/" + name + "_solution.png")
    maze.output_image("images/" + name + "_explored.png", show_explored=True)
    print("States Explored:", maze.num_explored)


if __name__ == "__main__":
    main()
