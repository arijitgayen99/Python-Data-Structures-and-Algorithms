class UndirectedGraph:
	def __init__(self, nodes, edges, nodeWeights = None, edgeWeights = None):
		
		self.nodeWeights = nodeWeights
		self.edgeWeights = edgeWeights

		self.nodes = nodes

		if not edgeWeights:
			self.edges = edges
		else:
			self.edges = []
			for index in range(len(edges)):
				edge = list(edges[index])
				edge.append(edgeWeights[index])
				edge = tuple(edge)
				self.edges.append(edge)


		self.Graph = {}


	def createGraph(self):
		for index in range(len(self.nodes)):
			node = self.nodes[index]
			self.Graph[node] = []

		for edge in self.edges:
			first_node = edge[0]
			second_node = edge[1]

			if self.edgeWeights:
				weight = edge[2]
				self.Graph[first_node].append((second_node, weight))
				self.Graph[second_node].append((first_node, weight))

			else:
				self.Graph[first_node].append(second_node)
				self.Graph[second_node].append(first_node)

	def getNodes(self):
		if not self.nodeWeights:
			return list(self.nodes)
		else:
			weightedNodes = {}
			for index in range(len(self.nodes)):
				weightedNodes[self.nodes[index]] = self.nodeWeights[index]

			return weightedNodes

	def getEdges(self):
		return list(self.edges)

	def getWeightOfNode(self, node):
		if not self.nodeWeights:
			print("Nodes are not Weighted!")
		else:
			return self.getNodes()[node]


	def getDegree(self, node):
		return len(self.Graph[node])
									

	def getAdjacencyList(self):
		return self.Graph

	def getAdjacencyMatrix(self, weighted = True):
		adjacencyMatrix = [[0 for i in range(len(self.nodes))] for i in range(len(self.nodes))]

		if (not self.edgeWeights) or (not weighted):
			for edge in self.edges:
				first_node_index = self.nodes.index[edge[0]]
				second_node_index = self.nodes.index[edge[1]]

				adjacencyMatrix[first_node_index][second_node_index] = 1
				adjacencyMatrix[second_node_index][first_node_index] = 1

		else:
			for edge in self.edges:
				first_node_index = self.nodes.index[edge[0]]
				second_node_index = self.nodes.index[edge[1]]
				weight = edge[2]

				adjacencyMatrix[first_node_index][second_node_index] = weight
				adjacencyMatrix[second_node_index][first_node_index] = weight

		return adjacencyMatrix


	def getAdjacentNodes(self, node):
		return list(self.Graph[node])

	def addNode(self, node, weight = 0):
		if node not in self.nodes:
			if not self.nodeWeights:
				self.nodes.append(node)
				self.Graph[node] = []

			else:
				self.nodes.append(node)
				self.Graph[node] = []
				self.nodeWeights.append(weight)


		else:
			print("Node Already Present!")

	def addEdge(self, edge, weight = 0):
		if edge not in self.edges:

			if edge[0] not in self.nodes or edge[1] not in self.nodes:
				print("Edge contains Node not present in Graph!")
			
			elif not self.edgeWeights:
				self.edges.append(edge)
				self.Graph[edge[0]].append(edge[1])
				self.Graph[edge[1]].append(edge[0])

			else:
				edge = list(edge)
				edge.append(weight)
				edge = tuple(edge)
				self.edges.append(edge)
				self.Graph[edge[0]].append((edge[1], weight))
				self.Graph[edge[1]].append((edge[0], weight))

		else:
			print("Edge Already Present!")

	def breadthFirstSearch(self, source = None):
		if not source:
			source = self.nodes[0]

		from LinearDataStructures import Queue

		Q = Queue()
		visited = {}
		for node in self.nodes:
			visited[node] = False

		BFStraversal = []

		Q.insert(source)
		visited[source] = True
		BFStraversal.append(source)

		while not Q.isEmpty():
			node = Q.pop()

			for neighbor in self.getAdjacentNodes(node):
				if self.edgeWeights:
					neighbor = neighbor[0]
				if not visited[neighbor]:
					Q.insert(neighbor)
					visited[neighbor] = True
					BFStraversal.append(neighbor)

		return BFStraversal

	def depthFirstSearch(self, source = None):
		if not source:
			source = self.nodes[0]

		from LinearDataStructures import Stack

		S = Stack()
		visited = {}
		for node in self.nodes:
			visited[node] = False

		DFStraversal = []

		S.insert(source)
		visited[source] = True
		DFStraversal.append(source)

		while not S.isEmpty():
			node = S.pop()

			for neighbor in self.getAdjacentNodes(node):
				if self.edgeWeights:
					neighbor = neighbor[0]
				if not visited[neighbor]:
					S.insert(neighbor)
					visited[neighbor] = True
					DFStraversal.append(neighbor)

		return DFStraversal



	def primsMst(self):

		if not self.edgeWeights:
			print("Edges should be Weighted to apply Prim's Algorithm!")

		else:
			import math

			adjacencyMatrix = self.getAdjacencyMatrix()
			noOfNodes = len(self.nodes)
			visited = [0] * noOfNodes

			noOfEdges = 0
			edgesMst = []
			costMst = 0
			visited[0] = True

			while (noOfEdges < noOfNodes-1):
				minimum = math.inf
				first_node = 0
				second_node = 0
				for u in range(noOfNodes):
					if visited[u]:
						for v in range(noOfNodes):
							if ((not visited[v]) and adjacencyMatrix[u][v]):  
								if minimum > adjacencyMatrix[u][v]:
									minimum = adjacencyMatrix[u][v]
									first_node = u
									second_node = v
				edge = (self.nodes[first_node], self.nodes[second_node], adjacencyMatrix[first_node][second_node])
				costMst += adjacencyMatrix[first_node][second_node]
				edgesMst.append(edge)
				visited[second_node] = True
				noOfEdges += 1
			return edgesMst, costMst
			

	def kruskalMstUtilOne(self, parent, index):
		if parent[index] == index:
			return index

		return self.kruskalMstUtilOne(parent, parent[index])

	def kruskalMstUtilTwo(self, parent, rank, u, v):
		u_parent = self.kruskalMstUtilOne(parent, u)
		v_parent = self.kruskalMstUtilOne(parent, v)

		if rank[u_parent] < rank[v_parent]:
			parent[u_parent] = v_parent
		elif rank[u_parent] > rank[v_parent]:
			parent[v_parent] = u_parent
		else:
			parent[v_parent] = u_parent
			rank[u_parent] += 1
		

	def kruskalMst(self):
		if not self.edgeWeights:
			print("Edges should be Weighted to apply Kruskal's Algorithm!")

		else:

			edgesMst = []
			costMst = 0
			weightedEdges = []

			for index in range(len(self.edges)):
				first_node, second_node, weight = self.edges[index]
				first_node_index = self.nodes.index(first_node)
				second_node_index = self.nodes.index(second_node)

				edge = [first_node_index, second_node_index, weight]
				weightedEdges.append(edge)

			weightedEdges = sorted(weightedEdges, key = lambda x:x[2])

			noOfNodes = len(self.nodes)
			parent = []
			rank = []

			i = 0
			j = 0

			for index in range(noOfNodes):
				parent.append(index)
				rank.append(0)

			while j < noOfNodes-1:
				first_node, second_node, weight = weightedEdges[i]

				u = self.kruskalMstUtilOne(parent, first_node)
				v = self.kruskalMstUtilOne(parent, second_node)

				if u != v:
					j += 1
					edgesMst.append((self.nodes[weightedEdges[i][0]], self.nodes[weightedEdges[i][1]], weightedEdges[i][2]))
					costMst += weightedEdges[i][2]
					self.kruskalMstUtilTwo(parent, rank, u, v)

				i += 1

			return edgesMst, costMst



	def dijkstraShortestPath(self, node):
		if not self.edgeWeights:
			print("Edges should be Weighted to apply Dijkstra's Algorithm!")

		else: 

			import math

			noOfNodes = len(self.nodes)
			adjacencyMatrix = self.getAdjacencyMatrix()
			source = self.nodes.index(node)

			distance = [math.inf] * noOfNodes
			sptSet = [False] * noOfNodes

			distance[source] = 0

			for index in range(noOfNodes):
				minimum = math.inf

				for v in range(noOfNodes):
					if distance[v] < minimum and (not sptSet[v]):
						minimum = distance[v]
						minimum_index = v


				sptSet[minimum_index] = True

				for v in range(noOfNodes):
					if adjacencyMatrix[minimum_index][v] and (not sptSet[v]) and distance[v] > (distance[minimum_index] + adjacencyMatrix[minimum_index][v]):
						distance[v] = distance[minimum_index] + adjacencyMatrix[minimum_index][v]

			shortestPaths = {}
			for index in range(len(distance)):
				shortestPaths[self.nodes[index]] = distance[index]

			return shortestPaths


	def shortestPath(self, source, destination):
		shortestPaths = self.dijkstraShortestPath(source)

		destinationIndex = self.nodes.index(destination)
		return shortestPaths[destinationIndex]


	def isCycle(self):
		if len(self.edges) >= len(self.nodes):
			return True

		else:
			return False

	def findPathUtil(self, source, destination, visited, path, allPaths):

		visited[self.nodes.index(source)] = True
		path.append(source)
		
		if source == destination:
			allPaths.append(path[:])
		
		for adj in self.getAdjacentNodes(source):
			if self.edgeWeights:
				adj = adj[0]

			if not visited[self.nodes.index(adj)]:
				self.findPathUtil(adj, destination, visited, path, allPaths)
		
		visited[self.nodes.index(source)] = False
		path.pop()

	def findPath(self, source, destination):
		if (source not in self.nodes) or (destination not in self.nodes):
			print("Source or Destination Node not present in Graph")
	 
		else:
			noOfNodes = len(self.nodes)
			visited = [False] * noOfNodes
			path = []
			allPaths = []

			self.findPathUtil(source, destination, visited, path, allPaths)
		
			return allPaths



	def getConnectedComponentsUtil(self, index, visited, component):
		visited[index] = True
		component.append(self.nodes[index])

		for adj in self.Graph[self.nodes[index]]:
			if self.edgeWeights:
				adj = adj[0]

			adjIndex = self.nodes.index(adj)
			if not visited[adjIndex]:
				component = self.getConnectedComponentsUtil(adjIndex, visited, component)

		return component



	def getConnectedComponents(self):
		noOfNodes = len(self.nodes)

		visited = [False] * noOfNodes
		components = []

		for index in range(noOfNodes):
			if not visited[index]:
				component = []
				component = self.getConnectedComponentsUtil(index, visited, component)
				components.append(component)

		return components


class DirectedGraph:
	def __init__(self, nodes, edges, nodeWeights = None, edgeWeights = None):
		
		self.nodeWeights = nodeWeights
		self.edgeWeights = edgeWeights

		self.nodes = nodes

		if not edgeWeights:
			self.edges = edges
		else:
			self.edges = []
			for index in range(len(edges)):
				edge = list(edges[index])
				edge.append(edgeWeights[index])
				edge = tuple(edge)
				self.edges.append(edge)


		self.Graph = {}


	def createGraph(self):
		for index in range(len(self.nodes)):
			node = self.nodes[index]
			self.Graph[node] = []

		for edge in self.edges:
			first_node = edge[0]
			second_node = edge[1]

			if self.edgeWeights:
				weight = edge[2]
				self.Graph[first_node].append((second_node, weight))

			else:
				self.Graph[first_node].append(second_node)

	def getNodes(self):
		if not self.nodeWeights:
			return list(self.nodes)
		else:
			weightedNodes = {}
			for index in range(len(self.nodes)):
				weightedNodes[self.nodes[index]] = self.nodeWeights[index]

			return weightedNodes

	def getEdges(self):
		return list(self.edges)

	def getWeightOfNode(self, node):
		if not self.nodeWeights:
			print("Nodes are not Weighted!")
		else:
			return self.getNodes()[node]


	def getOutDegree(self, node):
		return len(self.Graph[node])


	def getInDegree(self, node):
		inDegree = 0

		for edge in self.edges:
			if edge[1] == node:
				inDegree += 1

		return inDegree				

	def getAdjacencyList(self):
		return self.Graph

	def getAdjacencyMatrix(self, weighted = True):
		adjacencyMatrix = [[0 for i in range(len(self.nodes))] for i in range(len(self.nodes))]

		if (not self.edgeWeights) or (not weighted):
			for edge in self.edges:
				first_node_index = self.nodes.index[edge[0]]
				second_node_index = self.nodes.index[edge[1]]

				adjacencyMatrix[first_node_index][second_node_index] = 1

		else:
			for edge in self.edges:
				first_node_index = self.nodes.index(edge[0])
				second_node_index = self.nodes.index(edge[1])
				weight = edge[2]

				adjacencyMatrix[first_node_index][second_node_index] = weight

		return adjacencyMatrix


	def getAdjacentNodes(self, node):
		return list(self.Graph[node])

	def addNode(self, node, weight = 0):
		if node not in self.nodes:
			if not self.nodeWeights:
				self.nodes.append(node)
				self.Graph[node] = []

			else:
				self.nodes.append(node)
				self.Graph[node] = []
				self.nodeWeights.append(weight)


		else:
			print("Node Already Present!")

	def addEdge(self, edge, weight = 0):
		if edge not in self.edges:

			if edge[0] not in self.nodes or edge[1] not in self.nodes:
				print("Edge contains Node not present in Graph!")
			
			elif not self.edgeWeights:
				self.edges.append(edge)
				self.Graph[edge[0]].append(edge[1])

			else:
				edge = list(edge)
				edge.append(weight)
				edge = tuple(edge)
				self.edges.append(edge)
				self.Graph[edge[0]].append((edge[1], weight))

		else:
			print("Edge Already Present!")




	def breadthFirstSearch(self, source = None):
		if not source:
			source = self.nodes[0]

		from LinearDataStructures import Queue

		Q = Queue()
		visited = {}
		for node in self.nodes:
			visited[node] = False

		BFStraversal = []

		Q.insert(source)
		visited[source] = True
		BFStraversal.append(source)

		while not Q.isEmpty():
			node = Q.pop()

			for neighbor in self.getAdjacentNodes(node):
				if not self.edgeWeights:
					neighbor = neighbor[0]

				if not visited[neighbor]:
					Q.insert(neighbor)
					visited[neighbor] = True
					BFStraversal.append(neighbor)

		return BFStraversal

	def depthFirstSearch(self, source = None):
		if not source:
			source = self.nodes[0]

		from LinearDataStructures import Stack

		S = Stack()
		visited = {}
		for node in self.nodes:
			visited[node] = False

		DFStraversal = []

		S.insert(source)
		visited[source] = True
		DFStraversal.append(source)

		while not S.isEmpty():
			node = S.pop()

			for neighbor in self.getAdjacentNodes(node):
				if self.edgeWeights:
					neighbor = neighbor[0]

				if not visited[neighbor]:
					S.insert(neighbor)
					visited[neighbor] = True
					DFStraversal.append(neighbor)

		return DFStraversal



	def dijkstraShortestPath(self, node):
		if not self.edgeWeights:
			print("Edges should be Weighted to apply Dijkstra's Algorithm!")

		else: 

			import math

			noOfNodes = len(self.nodes)
			adjacencyMatrix = self.getAdjacencyMatrix()
			source = self.nodes.index(node)

			distance = [math.inf] * noOfNodes
			sptSet = [False] * noOfNodes

			distance[source] = 0

			for index in range(noOfNodes):
				minimum = math.inf

				for v in range(noOfNodes):
					if distance[v] < minimum and (not sptSet[v]):
						minimum = distance[v]
						minimum_index = v


				sptSet[minimum_index] = True

				for v in range(noOfNodes):
					if adjacencyMatrix[minimum_index][v] and (not sptSet[v]) and distance[v] > (distance[minimum_index] + adjacencyMatrix[minimum_index][v]):
						distance[v] = distance[minimum_index] + adjacencyMatrix[minimum_index][v]

			shortestPaths = {}
			for index in range(len(distance)):
				shortestPaths[self.nodes[index]] = distance[index]

			return shortestPaths


	def bellmanFord(self, source):
		if not self.edgeWeights:
			print("Edges should be weighted to apply Bellman Ford Algorithm!")

		else:

			import math

			noOfNodes = len(self.nodes)
			distance = [math.inf] * noOfNodes
			isNegativeCycle = False

			distance[self.nodes.index(source)] = 0

			for _ in range(noOfNodes):

				for edge in self.edges:
					first_node_index = self.nodes.index(edge[0])
					second_node_index = self.nodes.index(edge[1])
					weight = edge[2]

					if distance[first_node_index] + weight < distance[second_node_index]:
						distance[second_node_index] = distance[first_node_index] + weight


			for edge in self.edges:
				first_node_index = self.nodes.index(edge[0])
				second_node_index = self.nodes.index(edge[1])
				weight = edge[2]

				if distance[first_node_index] + weight < distance[second_node_index]:
					isNegativeCycle = True
					break

			shortestPaths = {}
			for index in range(len(distance)):
				shortestPaths[self.nodes[index]] = distance[index]

			return shortestPaths, isNegativeCycle


	def shortestPath(self, source, destination):
		shortestPaths = self.dijkstraShortestPath(source)

		destinationIndex = self.nodes.index(destination)
		return shortestPaths[destinationIndex]


	def floydWarshal(self):
		if not self.edgeWeights:
			print("Edges should be weighted for applying Floyd Warshal Algorithm!")


		else:
			import math

			noOfNodes = len(self.nodes)
			matrix = [[math.inf for i in range(noOfNodes)] for j in range(noOfNodes)]

			for index in range(noOfNodes):
				matrix[index][index] = 0

			for edge in self.edges:
				first_node_index = self.nodes.index(edge[0])
				second_node_index = self.nodes.index(edge[1])
				weight = edge[2]

				matrix[first_node_index][second_node_index] = weight

			for i in range(noOfNodes):
				for j in range(noOfNodes):
					for k in range(noOfNodes):

						matrix[j][k] = min(matrix[j][k], matrix[j][i] + matrix[i][k])


			return matrix

	def isCyclicUtil(self, nodeIndex, visited, Stack):
		visited[nodeIndex] = True
		Stack[nodeIndex] = True

		for adj in self.getAdjacentNodes(self.nodes[nodeIndex]):
			
			if self.edgeWeights:
				index = self.nodes.index(adj[0])
			else:
				index = self.nodes.index(adj)


			if not visited[index]:
				return self.isCyclicUtil(index, visited, Stack)

			elif Stack[index]:
				return True

		Stack[nodeIndex] = False
		return False


	def isCyclic(self):
		noOfNodes = len(self.nodes)
		visited = [False] * noOfNodes
		Stack = [False] * noOfNodes

		for index in range(noOfNodes):
			if not visited[index]:
				if self.isCyclicUtil(index, visited, Stack):
					return True

		return False


	def topologicalSortUtil(self, nodeIndex, visited, Stack):
		visited[nodeIndex] = True

		for adj in self.getAdjacentNodes(self.nodes[nodeIndex]):
			if self.edgeWeights:
				index = self.nodes.index(adj[0])

			else:
				index = self.nodes.index(adj)

			if not visited[index]:
				self.topologicalSortUtil(index, visited, Stack)

		Stack.append(nodeIndex)


	def topologicalSort(self):

		if self.isCyclic():
			print("Topological Sort not possible for Cyclic Graph")
	 
		else:
			noOfNodes = len(self.nodes)
			visited = [False] * noOfNodes
			Stack = []

			for index in range(noOfNodes):
				if not visited[index]:
					self.topologicalSortUtil(index, visited, Stack)

			Stack = Stack[::-1]
			sortedNodes = []
			for index in Stack:
				sortedNodes.append(self.nodes[index])
		
			return sortedNodes


	def findPathUtil(self, source, destination, visited, path, allPaths):

		visited[self.nodes.index(source)] = True
		path.append(source)
		
		if source == destination:
			allPaths.append(path[:])
		
		for adj in self.getAdjacentNodes(source):
			if self.edgeWeights:
				adj = adj[0]

			if not visited[self.nodes.index(adj)]:
				self.findPathUtil(adj, destination, visited, path, allPaths)
		
		visited[self.nodes.index(source)] = False
		path.pop()



	def findPath(self, source, destination):
		if (source not in self.nodes) or (destination not in self.nodes):
			print("Source or Destination Node not present in Graph")
	 
		else:
			noOfNodes = len(self.nodes)
			visited = [False] * noOfNodes
			path = []
			allPaths = []

			self.findPathUtil(source, destination, visited, path, allPaths)
		
			return allPaths



	def getStronglyConnectedComponents(self):

		
		