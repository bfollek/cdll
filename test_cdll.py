# This runs from the circular_doubly_linked_list folder

import time

from data_structures.circular_doubly_linked_list.cdll import CircularDoublyLinkedList, Node

def test_empty():
    cdll = CircularDoublyLinkedList()
    assert cdll.to_list() == []

def test_one_node():
    cdll = CircularDoublyLinkedList()
    node = Node(time.time())
    cdll.insert_at_beg(node)
    assert cdll.to_list() == [node.data]

def test_all_inserts():
    cdll = CircularDoublyLinkedList()
    node_1 = Node(time.time() + id(cdll))
    node_2 = Node(time.time() + id(node_1))
    node_3 = Node(time.time() + id(node_2))
    node_4 = Node(time.time() + id(node_3))
    cdll.insert_at_beg(node_1)
    cdll.insert_after(node_1, node_2)
    cdll.insert_at_end(node_4)
    cdll.insert_before(node_4, node_3)
    assert cdll.to_list() == [node_1.data, node_2.data, node_3.data, node_4.data]

def test_remove_from_beginning():
    cdll = CircularDoublyLinkedList()
    node_1 = Node(time.time() + id(cdll))
    node_2 = Node(time.time() + id(node_1))
    node_3 = Node(time.time() + id(node_2))
    cdll.insert_at_beg(node_1)
    cdll.insert_after(node_1, node_2)
    cdll.insert_at_end(node_3)
    assert cdll.to_list() == [node_1.data, node_2.data, node_3.data]
    cdll.remove(node_1)
    assert cdll.to_list() == [node_2.data, node_3.data]

def test_remove_from_middle():
    cdll = CircularDoublyLinkedList()
    node_1 = Node(time.time() + id(cdll))
    node_2 = Node(time.time() + id(node_1))
    node_3 = Node(time.time() + id(node_2))
    cdll.insert_at_beg(node_1)
    cdll.insert_at_end(node_3)
    cdll.insert_before(node_3, node_2)
    assert cdll.to_list() == [node_1.data, node_2.data, node_3.data]
    cdll.remove(node_2)
    assert cdll.to_list() == [node_1.data, node_3.data]

def test_remove_from_end():
    cdll = CircularDoublyLinkedList()
    node_1 = Node(time.time() + id(cdll))
    node_2 = Node(time.time() + id(node_1))
    node_3 = Node(time.time() + id(node_2))
    cdll.insert_at_beg(node_3)
    cdll.insert_at_beg(node_2)
    cdll.insert_at_beg(node_1)
    assert cdll.to_list() == [node_1.data, node_2.data, node_3.data]
    cdll.remove(node_3)
    assert cdll.to_list() == [node_1.data, node_2.data]
