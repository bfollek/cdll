# cdll
A circular doubly linked list class. From https://www.sanfoundry.com/python-program-implement-circular-doubly-linked-list/

To run the tests, you'll need [random_string](https://github.com/bfollek/random_string) on your PYTHONPATH.

I ran into an interesting challenge when I added typing. As soon as I typed Node.next and .prev as **Optional[Node]**, mypy insisted that I make sure .next and .prev weren't None before I used them as Nodes. This is good, and I caught a bug while I cleaned up the code. But it also raises questions about what to do when a value that shouldn't ever be None somehow is. I tried a few different approaches:

```
# truthy if, else raise exception
if self.first.prev
...
# chatty if, else raise exception
if self.first.prev is not None:
...
# assert and forget
assert self.first and node.next and node.prev
...
# ternary with reasonable else value.
current = current.next if current.next else self.first
```
