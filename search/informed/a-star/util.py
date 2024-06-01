from typing import List, Optional


class State:
    def __init__(self, row: int, column: int):
        self._items = (row, column)

    def __getitem__(self, index: int) -> int:
        return self._items[index]

    def __len__(self) -> int:
        return len(self._items)

    def __repr__(self) -> str:
        return repr(self._items)

    def __iter__(self) -> iter:
        return iter(self._items)

    def __eq__(self, other) -> bool:
        if isinstance(other, State):
            return self._items == other._items
        return False

    def __hash__(self) -> int:
        return hash(self._items)


class Action:
    def __init__(self, name: str, state: State) -> None:
        self.name = name
        self.state = state

    def __iter__(self) -> iter:
        return iter((self.name, self.state))


class Node:
    def __init__(
        self,
        state: State,
        parent: Optional['Node'],
        action: str
    ) -> None:
        self.state = state
        self.parent = parent
        self.action = action


class Frontier:
    def __init__(self, goal: State):
        self.goal = goal
        self.frontier: List[Node] = []

    def add(self, node: Node) -> None:
        self.frontier.append(node)

    def contains_state(self, state) -> None:
        return any(node.state == state for node in self.frontier)

    def empty(self) -> bool:
        return len(self.frontier) == 0

    def remove(self) -> Node:
        if self.empty():
            raise Exception("Empty frontier.")
        else:
            return self.frontier.pop(self._index_with_min_cost())

    def _index_with_min_cost(self) -> int:
        return min(range(self._length()), key=self._calculate_total_cost)

    def _length(self) -> int:
        return len(self.frontier)

    def _calculate_total_cost(self, index: int) -> int:
        node = self.frontier[index]
        g_cost = self._number_of_steps_to_current_node(node)
        h_cost = self._manhattan_distance(node)
        return g_cost + h_cost

    def _number_of_steps_to_current_node(self, node: Node) -> int:
        steps = 0
        current_node = node
        while current_node.parent is not None:
            steps += 1
            current_node = current_node.parent
        return steps

    def _manhattan_distance(self, node: Node) -> int:
        x2, y2 = self.goal
        x1, y1 = node.state
        return abs(x2 - x1) + abs(y2 - y1)
