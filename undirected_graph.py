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
									

	def getAdjacencyList(self):
		return self.Graph

	def getAdjacencyMatrix(self):
		adjacencyMatrix = [[0 for i in range(len(self.nodes))] for i in range(len(self.nodes))]

		if not self.edgeWeights:
			for edge in self.edges:
				first_node = edge[0]
				second_node = edge[1]

				adjacencyMatrix[first_node-1][second_node-1] = 1
				adjacencyMatrix[second_node-1][first_node-1] = 1

		else:
			for edge in self.edges:
				first_node = edge[0]
				second_node = edge[1]
				weight = edge[2]

				adjacencyMatrix[first_node-1][second_node-1] = weight
				adjacencyMatrix[second_node-1][first_node-1] = weight

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

	def BreadthFirstSearch(self, source):
		from queue import Queue

		Q = Queue()
		visited = {}
		for node in self.nodes:
			visited[node] = False

		BFStraversal = []

		Q.put(source)
		visited[source] = True
		BFStraversal.append(source)

		while not Q.empty():
			node = Q.get()

			for neighbor in self.getAdjacentNodes(node):
				if not visited[neighbor]:
					Q.put(neighbor)
					visited[neighbor] = True
					BFStraversal.append(neighbor)

		return BFStraversal

	def DepthFirstSearch(self, source):
		from queue import LifoQueue

		S = LifoQueue()
		visited = {}
		for node in self.nodes:
			visited[node] = False

		DFStraversal = []

		S.put(source)
		visited[source] = True
		DFStraversal.append(source)

		while not S.empty():
			node = S.get()

			for neighbor in self.getAdjacentNodes(node):
				if not visited[neighbor]:
					S.put(neighbor)
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


	def isCycle(self):
		if len(self.edges) >= len(self.nodes):
			return True

		else:
			return False

