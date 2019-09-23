# This runs from the circular_doubly_linked_list folder

from data_structures.circular_doubly_linked_list.cdll import CircularDoublyLinkedList, Node
from utilities.random_string.random_string import RandomString

def test_to_list():
    cdll = CircularDoublyLinkedList()
    node_1 = Node(RandomString.make())
    cdll.insert_at_beg(node_1)
    node_2 = Node(RandomString.make())
    cdll.insert_after(node_1, node_2)
    node_3 = Node(RandomString.make())
    cdll.insert_after(node_2, node_3)
    assert cdll.to_list() == [node_1.data, node_2.data, node_3.data]

def test_to_list_empty():
    cdll = CircularDoublyLinkedList()
    assert cdll.to_list() == []

def test_one_node():
    cdll = CircularDoublyLinkedList()
    node = Node(RandomString.make())
    cdll.insert_at_beg(node)
    assert cdll.to_list() == [node.data]

def test_all_inserts():
    cdll = CircularDoublyLinkedList()
    node_1 = Node(RandomString.make())
    node_2 = Node(RandomString.make())
    node_3 = Node(RandomString.make())
    node_4 = Node(RandomString.make())
    cdll.insert_at_beg(node_1)
    cdll.insert_after(node_1, node_2)
    cdll.insert_at_end(node_4)
    cdll.insert_before(node_4, node_3)
    assert cdll.to_list() == [node_1.data, node_2.data, node_3.data, node_4.data]

def test_remove_from_beginning():
    cdll = CircularDoublyLinkedList()
    node_1 = Node(RandomString.make())
    node_2 = Node(RandomString.make())
    node_3 = Node(RandomString.make())
    cdll.insert_at_beg(node_1)
    cdll.insert_after(node_1, node_2)
    cdll.insert_at_end(node_3)
    assert cdll.to_list() == [node_1.data, node_2.data, node_3.data]
    cdll.remove(node_1)
    assert cdll.to_list() == [node_2.data, node_3.data]

def test_remove_from_middle():
    cdll = CircularDoublyLinkedList()
    node_1 = Node(RandomString.make())
    node_2 = Node(RandomString.make())
    node_3 = Node(RandomString.make())
    cdll.insert_at_beg(node_1)
    cdll.insert_at_end(node_3)
    cdll.insert_before(node_3, node_2)
    assert cdll.to_list() == [node_1.data, node_2.data, node_3.data]
    cdll.remove(node_2)
    assert cdll.to_list() == [node_1.data, node_3.data]

def test_remove_from_end():
    cdll = CircularDoublyLinkedList()
    node_1 = Node(RandomString.make())
    node_2 = Node(RandomString.make())
    node_3 = Node(RandomString.make())
    cdll.insert_at_beg(node_3)
    cdll.insert_at_beg(node_2)
    cdll.insert_at_beg(node_1)
    assert cdll.to_list() == [node_1.data, node_2.data, node_3.data]
    cdll.remove(node_3)
    assert cdll.to_list() == [node_1.data, node_2.data]

def test_get_node():
    cdll = CircularDoublyLinkedList()
    node_1 = Node(RandomString.make())
    node_2 = Node(RandomString.make())
    node_3 = Node(RandomString.make())
    cdll.insert_at_beg(node_1)
    assert node_1 == cdll.get_node(0)
    assert cdll.get_node(1) is None
    cdll.insert_after(node_1, node_2)
    cdll.insert_after(node_2, node_3)
    assert node_2 == cdll.get_node(1)
    assert node_3 == cdll.get_node(2)
    assert cdll.get_node(3) is None
    assert cdll.get_node(999) is None

def test_get_node_empty():
    cdll = CircularDoublyLinkedList()
    assert cdll.get_node(0) is None
    assert cdll.get_node(1) is None
    assert cdll.get_node(100) is None
