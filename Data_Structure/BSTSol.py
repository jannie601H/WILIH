class Node:
    def __init__(self, key):
        self.key = key
        self.parent = self.left = self.right = None
        self.height = 0  # 높이 정보도 유지함에 유의!!

    def __str__(self):
        return str(self.key)

class BST:
	def __init__(self):
		self.root = None
		self.size = 0
	def __len__(self):
		return self.size

	def preorder(self, v):
		if v != None:
			print(v.key, end=' ')	
			self.preorder(v.left)
			self.preorder(v.right)
			
	def inorder(self, v):
		if v != None:
			self.inorder(v.left)
			print(v.key, end=' ')
			self.inorder(v.right)

	def postorder(self, v):
		if v != None:
			self.postorder(v.left)
			self.postorder(v.right)
			print(v.key, end=' ')
		
	def recal_height(self, v): # generated function (recal_height)
		if v != None:
			l = self.recal_height(v.left) 
			r = self.recal_height(v.right)
			v.height = max(l, r)
			return v.height + 1
		else:
			return 0
			
	def find_loc(self, key):
		if self.size == 0:
			return None
		tmp = self.root
		while tmp:
			if tmp.key == key:
				break			
			elif tmp.key < key:
				if tmp.right == None:
					break
				tmp = tmp.right
			elif tmp.key > key:
				if tmp.left == None:
					break
				tmp = tmp.left
		return tmp
				
	
	def search(self, key):
		tmp = self.find_loc(key)
		if tmp:
			if tmp.key == key:
				return tmp
		return None	
		
	def insert(self, key):
		# 노드들의 height 정보 update 필요
		n = Node(key)
		if self.root is None:
			self.root = n
		else:
			tmp = self.find_loc(key)
			if tmp.key > key:
				tmp.left = n
			else:
				tmp.right = n
			n.parent = tmp
		self.size += 1
		self.recal_height(self.root)
		return n
	
	def right_node(self, x): # generated function (right_node)
		while x.right:
			x = x.right
		return x
	
	def left_node(self, x):
		while x.left:
			x = x.left
		return x
	
	def deleteByMerging(self, x):
		# 노드들의 height 정보 update 필요
		if x != None:
			l, r, pt = x.left, x.right, x.parent
			if l != None:
				lr = self.right_node(l)
				lr.right = r
				if r != None:
					r.parent = lr
				m = l
			elif l == None and r != None:
				m = r
			else:
				m = None
					
			if x == self.root:
				self.root = m
			elif pt.left == x:
				pt.left = m
				if m:
					m.parent = pt
			else:
				pt.right = m
				if m:
					m.parent = pt
			# height update
			del x
			self.recal_height(self.root)
			self.size -= 1

				
	def deleteByCopying(self, x):
		# 노드들의 height 정보 update 필요
		if x != None:
			l, r, pt = x.left, x.right, x.parent			
			if x == self.root and self.size == 1:
				self.root = None
				del x				
			elif l == None and r == None:
				if pt.key > x.key:
					pt.left = None
				else:
					pt.right = None
				del x
				x = pt
			else:
				if l == None:
					t = self.left_node(r)
					if t.right != None:
						x.right = t.right
						t.right.parent = x
					else:
						if t.parent.key > t.key:
							t.parent.left = None
						else:
							t.parent.right = None
				else:
					t = self.right_node(l)
					if t.left != None:
						x.left = t.left
						t.left.parent = x
					else:
						if t.parent.key > t.key:
							t.parent.left = None
						else:
							t.parent.right = None
				x.key = t.key
				del t
			self.recal_height(self.root)
			self.size -= 1
			return x

	def height(self, x): # 노드 x의 height 값을 리턴
		if x == None: return -1
		else: return x.height

	def succ(self, x): # key값의 오름차순 순서에서 x.key 값의 다음 노드(successor) 리턴
		# x의 successor가 없다면 (즉, x.key가 최대값이면) None 리턴
		if x:
			if x.right != None:
				l = self.left_node(x.right)
				return l
			if x.parent.key > x.key:
				return x.parent
		return None

	def pred(self, x): # key값의 오름차순 순서에서 x.key 값의 이전 노드(predecssor) 리턴
		# x의 predecessor가 없다면 (즉, x.key가 최소값이면) None 리턴
		if x == None:
			return None
		if x.left != None:
			r = self.right_node(x.left)
			return r
		if x.parent.key < x.key:
			return x.parent
		return None

	def rotateLeft(self, x): # 균형이진탐색트리의 1차시 동영상 시청 필요 (height 정보 수정 필요)
		r, pt = x.right, x.parent
		if r != None:
			r.parent = pt
			x.parent = r
			x.right = r.left
			if r.left:
				r.left.parent = x
			r.left = x

			if pt != None:
				if pt.key < x.key:
					pt.right = r
				else:
					pt.left = r
			else:
				self.root = r
		
	def rotateRight(self, x): # 균형이진탐색트리의 1차시 동영상 시청 필요 (height 정보 수정 필요)
		l, pt = x.left, x.parent
		if l != None:
			l.parent = pt
			x.parent = l
			x.left = l.right
			if l.right:
				l.right.parent = x
			l.right = x

			if pt != None:
				if pt.key < x.key:
					pt.right = l
				else:
					pt.left = l
			else:
				self.root = l	

class AVL(BST):
	def __init__(self):
		self.root = None
		self.size = 0
        
	def is_avl(self, v):
		return abs(self.right_height(v) - self.left_height(v)) <= 1
    
    
	def left_height(self, v):
		return v.left.height if v.left else -1
    
	def right_height(self, v):
		return v.right.height if v.right else -1

	def rebalance(self, x, y, z):
		# assure that x, y, z != None
		# return the new 'top' node after rotations
		# z - y - x의 경우(linear vs. triangle)에 따라 회전해서 균형잡음
		if z.left == y:
			if y.left == x:
				# left-left
				self.rotateRight(z)
				return y
			else:
				# left-right
				self.rotateLeft(y)
				self.rotateRight(z)
				return x
		else:
			if y.left == x:
				self.rotateRight(y)
				self.rotateLeft(z)
				return x
			else:
				self.rotateLeft(z)
				return y

	def insert(self, key):
		# BST에서도 같은 이름의 insert가 있으므로, BST의 insert 함수를 호출하려면 
		# super(class_name, instance_name).method()으로 호출
		# 새로 삽입된 노드가 리턴됨에 유의!
		v = super(AVL, self).insert(key)
		# x, y, z를 찾아 rebalance(x, y, z)를 호출
		
		x, y, z = v, v.parent, None
		while y:
			z = y.parent
			if z and self.is_avl(z):
				x, y = y, z
			else:
				if z:
					self.rebalance(x, y, z)
				break
		self.recal_height(self.root)
		return v
        
	def delete(self, u): # delete the node u
		v = self.deleteByCopying(u) # 또는 self.deleteByMerging을 호출가능하다. 그러나 이 과제에서는 deleteByCopying으로 호출한다
		# height가 변경될 수 있는 가장 깊이 있는 노드를 리턴받아 v에 저장
        
		while v:
			# v가 AVL 높이조건을 만족하는지 보면서 루트 방향으로 이동
			# z - y - x를 정한 후, rebalance(x, y, z)을 호출
			if not self.is_avl(v):
				z = v
				y = z.left if self.left_height(z) >= self.right_height(z) else z.right
				x = y.left if self.left_height(y) >= self.right_height(y) else y.right
				v = self.rebalance(x, y, z)
				self.recal_height(self.root)
			v = v.parent