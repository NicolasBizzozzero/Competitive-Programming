class Edge:
	def __init__(self, value, from_, to):
		self.value = value
		self.from_ = from_
		self.to    = to

class Node:
	def __init__(self, color, edges = []):
		self.color = color
		self.edges = edges

GREEN = 0
ORANGE = 1
RED = 2

class Problem:
	def __init__(self, stream = input, n, m, q, s):
		self.n, self.m, self.q, self.s = n, m, q, s

		nodes = [None for i in range(n)]
		for e in range(m):
			u, v, w = map(int, stream().split(' '))
			nodes[u] = Node(RED) if nodes[u] == None else nodes[u]
			nodes[v] = Node(RED) if nodes[v] == None else nodes[v]
			# Creer le edges
			edg = Edge(w, nodes[u], nodes[v])
			nodes[u].edges.append(edg)
		self.nodes = nodes

		query = []
		for iq in range(q):
			pass

		self.query




def parse_pbs(stream = input):
	header = stream()
	problems = []
	while (header != '0 0 0 0'):
		n, m, q, s = stream().split(' ')
		problems.append(Problem(stream, n, m, q, s))

	return problems

if __name__ == '__main__':
	p = Problem()
