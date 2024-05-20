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


class QueueFrontier:
    def __init__(self):
        self.frontier: List[Node] = []

    def add(self, node: Node) -> None:
        self.frontier.append(node)

    def contains_state(self, state) -> None:
        return any(node.state == state for node in self.frontier)

    def empty(self) -> bool:
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise Exception("Empty frontier.")
        else:
            return self.frontier.pop(0)
