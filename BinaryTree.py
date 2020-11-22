class Node:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None


class BinarySearchTree:
	def __init__(self):
		self.root = None


	def setRoot(self, value):
		self.root = Node(value)

	def insertNodeUtil(self, root, value):
		if value <= root.value:
			if root.left:
				self.insertNodeUtil(root.left, value)
			else:
				root.left = Node(value)

		else:
			if root.right:
				self.insertNodeUtil(root.right, value)
			else:
				root.right = Node(value)


	def insertNode(self, value):
		if not self.root:
			self.setRoot(value)

		else:
			self.insertNodeUtil(self.root, value)


	def searchUtil(self, root, value):
		if root.value == value:
			return root

		elif value < root.value:
			if root.left:
				self.searchUtil(root.left, value)
			else:
				return False

		else:
			if root.right:
				self.searchUtil(root.right, value)

			else:
				return False


	def search(self, value):
		return self.searchUtil(self.root, value)


	def getNodeInfo(self, value):
		node = self.search(value)
		if not node:
			print("Given Node not Present in Tree!")

		else:
			if not node.left:
				if not node.right:
					return (node.value, None, None)

				else:
					return (node.value, None, node.right.value)

			else:

				if not node.right:
					return (node.value, node.left.value, None)

				else:
					return (node.value, node.left.value, node.right.value)

	def getRoot(self):
		return self.root


	def minNextNode(self, root):
		while(root.left):
			root = root.left

		return root


	def deleteNodeUtil(self, root, value):
		if not root:
			return None

		elif value < root.value:
			root.left = self.deleteNodeUtil(root.left, value)

		elif value > root.value:
			root.right = self.deleteNodeUtil(root.right, value)

		else:

			if not root.left:
				node = root.right
				root = None
				return node

			elif not root.right:
				node = root.left
				root = None
				return node

			inOrderSuccessor = self.minNextNode(root.right)
			root.value = inOrderSuccessor.value

			root.right = self.deleteNodeUtil(root.right, inOrderSuccessor.value)

		return root


	def deleteNode(self, value):
		return self.deleteNodeUtil(self.root, value)


	def inOrderTraversalUtil(self, root, inOrderTraversal):
		if root.left:
			self.inOrderTraversalUtil(root.left, inOrderTraversal)
		inOrderTraversal.append(root.value)
		if root.right:
			self.inOrderTraversalUtil(root.right, inOrderTraversal)


	def inOrderTraversal(self):
		inOrderTraversal = []
		self.inOrderTraversalUtil(self.root, inOrderTraversal)

		return inOrderTraversal

	def preOrderTraversalUtil(self, root, preOrderTraversal):
		preOrderTraversal.append(root.value)
		if root.left:
			self.preOrderTraversalUtil(root.left, preOrderTraversal)
		if root.right:
			self.preOrderTraversalUtil(root.right, preOrderTraversal)


	def preOrderTraversal(self):
		preOrderTraversal = []
		self.preOrderTraversalUtil(self.root, preOrderTraversal)

		return preOrderTraversal

	def postOrderTraversalUtil(self, root, postOrderTraversal):
		
		if root.left:
			self.postOrderTraversalUtil(root.left, postOrderTraversal)
		if root.right:
			self.postOrderTraversalUtil(root.right, postOrderTraversal)
		postOrderTraversal.append(root.value)


	def postOrderTraversal(self):
		postOrderTraversal = []
		self.postOrderTraversalUtil(self.root, postOrderTraversal)

		return postOrderTraversal


	def getHeightUtil(self, root):
		if not root:
			return 0

		else:
			return 1 + max(self.getHeightUtil(root.left), self.getHeightUtil(root.right))


	def getHeight(self):
		self.getHeightUtil(self.root, height)


class AVLTreeNode(value):
	def __init__(self):
		self.value = value
		self.left = None
		self.right = None
		self.height = 0


class AVLTree:
	def __init__(self):
		self.root = None


	def setRoot(self, value):
		self.root = AVLTreeNode(value)
		return self.root


	def getHeight(self, node):
		if not node:
			return 0
		return node.height


	def getNodeInfo(self, nodeVal):
		node = self.search(nodeVal)
		if not node:
			print("Node not present in AVL Tree!")
			return False

		else:
			if not node.left:
				if not node.right:
					return (node.value, None, None)
				else:
					return (node.value, None, node.right.value)

			else:
				if not node.right:
					return (node.value, node.left.value, None)
				else:
					return (node.value, node.left.value, node.right.value)


	def getBalance(self, root):
		return (root.left.height - root.right.height)


	def leftRotate(self, node):
		T1 = node.left
		y = node.right

		y.left = node
		node.right = T1

		node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))
		y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

		return y


	def rightRotate(self, node):
		y = node.left
		T3 = y.right

		y.right = node
		node.left = T3

		node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))
		y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

		return y



	def insertNodeUtil(self, root, value):

		if not root:
			return AVLTreeNode(value)
		if value < root.value:
			root.left = self.insertNodeUtil(root.left, value)
		else:
			root.right = self.insertNodeUtil(root.right, value)


		root.height = 1 + max(root.left.height, root.right.height)
		balance = self.getBalance(root)


		if balance > 1 and value < root.left.value:
			return self.rightRotate(root)

		elif balance < -1 and value > root.right.value:
			return self.leftRotate(root)

		elif balance > 1 and value > root.left.value:
			root.left = self.leftRotate(root.left)
			return self.rightRotate(root)

		elif balance < -1 and value < root.right.value:
			root.right = self.rightRotate(root.right)
			return self.leftRotate(root)



		return root



	def insertNode(self, value):
		if not self.root:
			return self.setRoot(value)

		return self.insertNodeUtil(self.root, value)


	def minNextNode(self, root):
		while(root.left):
			root = root.left

		return root



	def deleteNodeUtil(self, root, value):
		if not root:
			return root

		elif root.value > value:
			root.left = self.deleteNodeUtil(root.left, value)

		elif root.value < value:
			root.right = self.deleteNodeUtil(root.right, value)

		else:

			if not root.left:
				node = root.right
				root = None
				return node

			elif not root.right:
				node = root.left
				root = None
				return node


			node = self.minNextNode(root.right)
			root.value = node.value
			root.right = self.deleteNodeUtil(root.right, node.value)

		if not root:
			return None

		root.height = 1 + max(root.left.height, root.right.height)
		balance = self.getBalance(root)


		if balance > 1 and self.getBalance(root.left) >= 0: 
			return self.rightRotate(root) 


		if balance < -1 and self.getBalance(root.right) <= 0: 
			return self.leftRotate(root) 
  

		if balance > 1 and self.getBalance(root.left) < 0: 
			root.left = self.leftRotate(root.left) 
			return self.rightRotate(root) 
  

		if balance < -1 and self.getBalance(root.right) > 0: 
			root.right = self.rightRotate(root.right) 
			return self.leftRotate(root) 

		return root


	def deleteNode(self, value):
		return self.deleteNodeUtil(self.root, value)


	def searchUtil(self, root, value):
		if root.value == value:
			return root

		elif value < root.value:
			if root.left:
				self.searchUtil(root.left, value)
			else:
				return False

		else:
			if root.right:
				self.searchUtil(root.right, value)

			else:
				return False


	def search(search, node):
		return self.searchUtil(self.root, value)



	def inOrderTraversalUtil(self, root, inOrderTraversal):
		if root.left:
			self.inOrderTraversalUtil(root.left, inOrderTraversal)
		inOrderTraversal.append(root.value)
		if root.right:
			self.inOrderTraversalUtil(root.right, inOrderTraversal)


	def inOrderTraversal(self):
		inOrderTraversal = []
		self.inOrderTraversalUtil(self.root, inOrderTraversal)

		return inOrderTraversal

	def preOrderTraversalUtil(self, root, preOrderTraversal):
		preOrderTraversal.append(root.value)
		if root.left:
			self.preOrderTraversalUtil(root.left, preOrderTraversal)
		if root.right:
			self.preOrderTraversalUtil(root.right, preOrderTraversal)


	def preOrderTraversal(self):
		preOrderTraversal = []
		self.preOrderTraversalUtil(self.root, preOrderTraversal)

		return preOrderTraversal

	def postOrderTraversalUtil(self, root, postOrderTraversal):
		
		if root.left:
			self.postOrderTraversalUtil(root.left, postOrderTraversal)
		if root.right:
			self.postOrderTraversalUtil(root.right, postOrderTraversal)
		postOrderTraversal.append(root.value)


	def postOrderTraversal(self):
		postOrderTraversal = []
		self.postOrderTraversalUtil(self.root, postOrderTraversal)

		return postOrderTraversal

