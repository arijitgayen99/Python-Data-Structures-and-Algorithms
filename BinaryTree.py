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
				return self.searchUtil(root.left, value)
			else:
				return False

		else:
			if root.right:
				return self.searchUtil(root.right, value)

			else:
				return False


	def search(self, value):
		return self.searchUtil(self.root, value)


	def getNoofNodesInSubtreeUtil(self, root):
		if not root:
			return 0
		else:
			return 1 + self.getNoofNodesInSubtreeUtil(root.left) + self.getNoofNodesInSubtreeUtil(root.right)



	def getNoofNodesInSubtree(self, nodeVal):
		node = self.search(nodeVal)
		return self.getNoofNodesInSubtreeUtil(node)



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


class AVLTreeNode():
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None
		self.height = 1


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
		if not root:
			return 0
		return (self.getHeight(root.left) - self.getHeight(root.right))



	def getNoofNodesInSubtreeUtil(self, root):
		if not root:
			return 0
		else:
			return( 1 + self.getNoofNodesInSubtreeUtil(root.left) + self.getNoofNodesInSubtreeUtil(root.right))



	def getNoofNodesInSubtree(self, nodeVal):
		node = self.search(nodeVal)
		if not node:
			return 0
		else:
			return self.getNoofNodesInSubtreeUtil(node)


	def getNoofNodesInHeightUtil(self, root, height, count):
		if root.height < height:
			self.getNoofNodesInHeightUtil(root.left, height, count)
			self.getNoofNodesInHeightUtil(root.right, height, count)
			return

		elif root.height == height:
			count += 1
			return


	def getNoofNodesInHeight(self, height):
		if height == 0:
			return 1
		else:
			count = 0
			self.getNoofNodesInHeightUtil(self.root, height, count)
			return count


	def leftRotate(self, node):
		y = node.right
		T1 = y.left

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
		if value <= root.value:
			root.left = self.insertNodeUtil(root.left, value)
		else:
			root.right = self.insertNodeUtil(root.right, value)


		root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
		balance = self.getBalance(root)

		if balance > 1 and value < root.left.value:
			return self.rightRotate(root)

		if balance < -1 and value > root.right.value:
			return self.leftRotate(root)

		if balance > 1 and value > root.left.value:
			root.left = self.leftRotate(root.left)
			return self.rightRotate(root)

		if balance < -1 and value < root.right.value:
			root.right = self.rightRotate(root.right)
			return self.leftRotate(root)



		return root



	def insertNode(self, value):
		if not self.root:
			return self.setRoot(value)
		else:
			root = self.insertNodeUtil(self.root, value)
			self.root = root
			return root


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

		root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
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
		root = self.deleteNodeUtil(self.root, value)
		self.root = root
		return root


	def searchUtil(self, root, value):
		if root.value == value:
			return root

		elif value < root.value:
			if root.left:
				return self.searchUtil(root.left, value)
			else:
				return False

		else:
			if root.right:
				return self.searchUtil(root.right, value)

			else:
				return False


	def search(self, nodeVal):
		return self.searchUtil(self.root, nodeVal)



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




class SegmentTree:

	def __init__(self, arr):
		from math import ceil, log2

		height = (int) (ceil(log2(len(arr))))
		size = 2* (int)(2**height) - 1

		st = [0]*size
		self.constructTree(arr, 0, len(arr)-1, st, 0)

		self.segment_tree = st
		self.array = arr



	def constructTree(self, arr, low, high, st, size):

		if low == high:
			st[size] = arr[low]
			return arr[low]

		mid = low + (high-low)//2
		st[size] = self.constructTree(arr, low, mid, st, size*2+1) + self.constructTree(arr, mid+1, high, st, size*2+2)

		return st[size]
		



	def updateUtil(self, st, low, high, index, diff, size):
		if (index<low or index>high):

			return

		else:
			st[size] = st[size] + diff

			if low != high:
				mid = low+(high-low)//2
				self.updateUtil(st, low, mid, index, diff, size*2+1)
				self.updateUtil(st, mid+1, high, index, diff, size*2+2)




	def update(self, index, value):
		if index < 0 or index >= len(self.array):
			print("Invalid input, try again!")
			return

		else:
			diff = value-self.array[index]
			self.array[index] = value

			self.updateUtil(self.segment_tree, 0, len(self.array)-1, index, diff, 0)
		


	def rangeSumUtil(self, st, low, high, start_idx, end_idx, size):
		if (start_idx<=low and end_idx>=high):
			return st[size]

		if (start_idx > high or end_idx < low):
			return 0

		else:
			mid = low + (high-low)//2
			return self.rangeSumUtil(st, low, mid, start_idx, end_idx, size*2+1) + self.rangeSumUtil(st, mid+1, high, start_idx, end_idx, size*2+2)


	def rangeSum(self, start_idx, end_idx):
		if start_idx < 0 or end_idx >= len(self.array) or start_idx > end_idx:
			print("Invalid input, try again!")

		else:
			return self.rangeSumUtil(self.segment_tree, 0, len(self.array)-1, start_idx, end_idx, 0)




	def rangeMinimumUtil(self, st, low, high, start_idx, end_idx, size):
		import sys

		if (start_idx<=low and end_idx>=high):
			return st[size]

		if (start_idx > high or end_idx < low):
			return sys.maxsize


		mid = low+(high-low)//2
		return min(self.rangeMinimumUtil(st, low, mid, start_idx, end_idx, size*2+1), self.rangeMinimumUtil(st, mid+1, high, start_idx, end_idx, size*2+2))
		

	def getSegmentTree(self):
		return self.segment_tree


	def rangeMinimum(self, start_idx, end_idx):
		if start_idx < 0 or end_idx >= len(self.array) or start_idx > end_idx:
			print("Invalid input, try again!")

		else:
			return self.rangeMinimumUtil(self.segment_tree, 0, len(self.array)-1, start_idx, end_idx, 0)
