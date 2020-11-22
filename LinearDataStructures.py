class Queue:
	def __init__(self, maxSize = None):
		self.maxSize = maxSize
		self.size = 0

		if maxSize:
			self.queue = [None] * maxSize

		else:
			self.queue = []


	def getSize(self):
		
		return self.size


	def insert(self, value):
		if not self.maxSize:
			self.queue.append(value)
			self.size += 1

		else:
			if self.isFull():
				print("Queue is Full!")

			else:
				self.queue[self.size] = value
				self.size += 1


	def pop(self):
		if self.isEmpty():
			print("Queue is Empty!")

		else:
			temp = self.queue[0]
			self.queue = self.queue[1:]
			self.size -= 1
			return temp


	def peek(self):
		if not self.maxSize:
			return self.queue

		else:
			return self.queue[:self.size]



	def isEmpty(self):
		if self.size == 0:
			return True
		else:
			return False


	def isFull(self):
		if not self.maxSize:
			print("Queue Size not Fixed!")

		else:
			if self.size == self.maxSize:
				return True

			else:
				return False



class Stack:
	def __init__(self, maxSize = None):
		self.maxSize = maxSize
		self.size = 0

		if maxSize:
			self.stack = [None] * maxSize

		else:
			self.stack = []


	def getSize(self):
		
		return self.size


	def insert(self, value):
		if not self.maxSize:
			self.stack.append(value)
			self.size += 1

		else:
			if self.isFull():
				print("Stack is Full!")

			else:
				self.stack[self.size] = value
				self.size += 1


	def pop(self):
		if self.isEmpty():
			print("Stack is Empty!")

		else:
			temp = self.stack[self.size-1]
			self.stack = self.stack[:self.size]
			self.size -= 1
			return temp


	def peek(self):
		if not self.maxSize:
			return self.stack

		else:
			return self.stack[:self.size]



	def isEmpty(self):
		if self.size == 0:
			return True
		else:
			return False


	def isFull(self):
		if not self.maxSize:
			print("Stack Size not Fixed!")

		else:
			if self.size == self.maxSize:
				return True

			else:
				return False


class LLNode:
	def __init__(self, value):
		self.value = value
		self.next = None


class DLLNode:
	def __init__(self, value):
		self.value = value
		self.next = None
		self.previous = None


class LinkedList:
	def __init__(self, maxSize = None):
		self.maxSize = maxSize
		self.size = 0
		self.head = None


	def setHead(self, value):
		self.head = LLNode(value)


	def isFull(self):
		if not self.maxSize:
			print("Linked List Size is not Fixed!")
			return False

		else:
			if self.size == self.maxSize:
				return True
			else:
				return False


	def isEmpty(self):
		if self.size == 0:
			return True

		return False

	def getSize(self):
		return self.size


	def insertAtEnd(self, value):
		if not self.head:
			self.setHead(value)
			self.size += 1

		else:
			if (not self.maxSize) or (not self.isFull()):

				pointer = self.head
				while pointer.next:
					pointer = pointer.next

				pointer.next = LLNode(value)
				self.size += 1

			elif self.isFull():
				print("Linked List is Full!")


		return self.head


	def insertAtBeginning(self, value):
		if not self.head:
			self.setHead(value)
			self.size += 1

		else:
			if (not self.maxSize) or (not self.isFull()):

				pointer = self.head
				self.setHead(value)

				self.head.next = pointer
				self.size += 1

			elif self.isFull():
				print("Linked List is Full!")

		return self.head


	def insertAfter(self, nodeVal, value):
		node = self.search(nodeVal)
		if not node:
			print("Given Node not present in Linked List!")

		elif (not self.maxSize) or (not self.isFull()):

			if not node.next:
				node.next = LLNode(value)
				self.size += 1

			else:
				pointer = node.next
				node.next = LLNode(value)
				node.next.next = pointer
				self.size += 1

		elif self.isFull():
			print("Linked List is Full!")

		return self.head


	def search(self, value):
		pointer = self.head

		if not pointer:
			print("Linked List not set!")

		else:
			while pointer.next and pointer.value != value:
				pointer = pointer.next

			if pointer.value == value:
				return pointer

			else:
				return False


	def update(self, nodeVal, value):
		node = self.search(nodeVal)

		if not node:
			print("Node not present in Linked List!")

		else:
			node.value = value

		return self.head



	def delete(self, value):
		if not self.search(value):
			print("Node not present in Linked List!")

		else:

			pointer = self.head

			if pointer.value == value:
				self.head = pointer.next
				self.size -= 1

			else:
				nextPointer = pointer.next

				while nextPointer.value != value and nextPointer.next:
					pointer = nextPointer
					nextPointer = nextPointer.next

				if not nextPointer.next:
					pointer.next = None

				else:
					pointer.next = nextPointer.next

				self.size -= 1

		return self.head



	def checkCycle(self):
		slowPointer = self.head
		fastPointer = self.head

		while(slowPointer and fastPointer and fastPointer.next):
			slowPointer = slowPointer.next
			fastPointer = fastPointer.next.next

			if slowPointer == fastPointer:
				return True


		return False




class DoubleLinkedList:

	def __init__(self, maxSize = None):
		self.maxSize = maxSize

		self.size = 0
		self.head = None

		
	def setHead(self, value):
		self.head = DLLNode(value)


	def isFull(self):
		if not self.maxSize:
			print("Linked List Size is not Fixed!")
			return False

		else:
			if self.size == self.maxSize:
				return True
			else:
				return False


	def isEmpty(self):
		if self.size == 0:
			return True

		return False

	def getSize(self):
		return self.size


	def insertAtEnd(self, value):
		if not self.head:
			self.setHead(value)
			self.size += 1

		else:
			if (not self.maxSize) or (not self.isFull()):

				pointer = self.head
				while pointer.next:
					pointer = pointer.next

				pointer.next = DLLNode(value)
				nextPointer = pointer.next
				nextPointer.previous = pointer

				self.size += 1

			elif self.isFull():
				print("Linked List is Full!")


		return self.head


	def insertAtBeginning(self, value):
		if not self.head:
			self.setHead(value)
			self.size += 1

		else:
			if (not self.maxSize) or (not self.isFull()):

				pointer = self.head
				self.setHead(value)

				self.head.next = pointer
				pointer.previous = self.head
				self.size += 1

			elif self.isFull():
				print("Linked List is Full!")

		return self.head


	def insertAfter(self, nodeVal, value):
		node = self.search(nodeVal)
		if not node:
			print("Given Node not present in Linked List!")

		elif (not self.maxSize) or (not self.isFull()):

			if not node.next:
				node.next = DLLNode(value)
				node.next.previous = node
				self.size += 1

			else:
				pointer = node.next
				node.next = DLLNode(value)
				nextPointer = node.next
				nextPointer.next = pointer
				nextPointer.previous = node
				nextPointer.next.previous = nextPointer
				self.size += 1

		elif self.isFull():
			print("Linked List is Full!")

		return self.head


	def search(self, value):
		pointer = self.head

		if not pointer:
			print("Linked List not set!")

		else:
			while pointer.next and pointer.value != value:
				pointer = pointer.next

			if pointer.value == value:
				return pointer

			else:
				return False


	def update(self, nodeVal, value):
		node = self.search(nodeVal)

		if not node:
			print("Node not present in Linked List!")

		else:
			node.value = value

		return self.head



	def delete(self, value):
		if not self.search(value):
			print("Node not present in Linked List!")

		else:

			pointer = self.head

			if pointer.value == value:
				self.head = pointer.next
				self.size -= 1

			else:

				while pointer.value != value:
					pointer = pointer.next

				if not pointer.next:
					pointer.previous.next = None

				else:
					pointer.previous.next = pointer.next
					pointer.next.previous = pointer.previous

				self.size -= 1

		return self.head



	def checkCycle(self):
		slowPointer = self.head
		fastPointer = self.head

		while(slowPointer and fastPointer and fastPointer.next):
			slowPointer = slowPointer.next
			fastPointer = fastPointer.next.next

			if slowPointer == fastPointer:
				return True


		return False

