class Value:
	def __init__(self, data, _children=(), _op=''):
		self.data = data
		self.grad = 0
		self._backward = lambda: None
		self._prev = set(_children)
		self._op = _op

	def __repr__(self):
		def fmt(x):
			return int(x) if float(x).is_integer() else round(x, 4)
		
		return f"Value(data={fmt(self.data)}, grad={fmt(self.grad)})"

	def __add__(self, other):
		# Implement addition here
		if not isinstance(other, Value):
			other = Value(other)

		parent = Value(self.data + other.data, (self, other), 'add')

		def local_backward():
			self.grad += parent.grad
			other.grad += parent.grad

		parent._backward = local_backward 

		return parent

	def __mul__(self, other):
		# Implement multiplication here
		if not isinstance(other, Value):
			other = Value(other)

		parent = Value(self.data * other.data, (self, other), 'mul')

		def local_backward():
			self.grad += other.data * parent.grad
			other.grad += self.data * parent.grad

		parent._backward = local_backward 

		return parent

	def relu(self):
		# Implement ReLU here
		parent = Value(self.data if self.data > 0 else 0, (self,), 'relu')

		def local_backward():
			self.grad += parent.grad if self.data > 0 else 0

		parent._backward = local_backward

		return parent

	def backward(self):
		# Implement backward pass here
		topo = []
		visited = set()

		def build(v):
			if v not in visited:
				visited.add(v)

				for c in v._prev:
					build(c)

				topo.append(v)

		build(self)

		# Reset all gradients so backward() is idempotent
		for n in topo:
			n.grad = 0

		self.grad = 1

		for n in reversed(topo):
			n._backward()