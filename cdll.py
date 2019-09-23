# From https://www.sanfoundry.com/python-program-implement-circular-doubly-linked-list/

from typing import Any, List, Optional

class Node:
    def __init__(self, data: Any):
       self.data = data
       self.next: Optional[Node] = None
       self.prev: Optional[Node] = None

class CircularDoublyLinkedList:
    def __init__(self):
        self.first: Optional[Node] = None

    def get_node(self, index: int) -> Optional[Node]:
        current = self.first
        # index < 1 will fall through and return self.first
        for i in range(index):
            if current is not None:
                current = current.next
                # If we circle back to first, return None
                if current == self.first:
                    return None
        return current

    def insert_after(self, ref_node: Node, new_node: Node) -> None:
        if ref_node.prev is not None and ref_node.next is not None:
            new_node.prev = ref_node
            new_node.next = ref_node.next
            new_node.next.prev = new_node
            ref_node.next = new_node
        else:
            raise Exception("ref_node is missing prev or next")

    def insert_before(self, ref_node: Node, new_node: Node) -> None:
        if ref_node.prev is not None:
            self.insert_after(ref_node.prev, new_node)

    def insert_at_end(self, new_node: Node) -> None:
        if self.first is None:
            self.first = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            if self.first.prev is not None:
                self.insert_after(self.first.prev, new_node)
            else:
                raise Exception("first.prev should not be None")

    def insert_at_beg(self, new_node: Node) -> None:
        self.insert_at_end(new_node)
        self.first = new_node

    def remove(self, node: Node) -> None:
        assert self.first and node.next and node.prev
        if self.first.next == self.first:
            self.first = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            if self.first == node:
                self.first = node.next

    def display(self) -> None:
        if self.first is None:
            return
        current = self.first
        while True:
            print(current.data, end=' ')
            assert current.next
            current = current.next
            if current == self.first:
                break

    def to_list(self) -> List[Any]:
        lst: List[Any] = []
        if self.first is None:
            return lst
        current = self.first
        while True:
            lst.append(current.data)
            current = current.next if current.next else self.first
            if current == self.first:
                break
        return lst

    def __repr__(self) -> str:
        m = map(str, self.to_list())
        return f"CircularDoublyLinkedList({', '.join(m)})"
