class Node:
	def __init__(self, key=None):
		self.key = key
		self.prev = self
		self.next = self
	def __str__(self):
		return str(self.key)

class DoublyLinkedList:
	def __init__(self):
		self.head = Node() # create an empty list with only dummy node

	def __iter__(self):
		v = self.head.next
		while v != self.head:
			yield v
			v = v.next
	def __str__(self):
		return " -> ".join(str(v.key) for v in self)

	def printList(self):
		v = self.head.next
		print("h -> ", end="")
		while v != self.head:
			print(str(v.key)+" -> ", end="")
			v = v.next
		print("h")
	# 나머지 코드
	def splice(self, a, b, x):
		if a == None or b == None or x == None:
			return
		ap = a.prev
		bn = b.next
		xn = x.next
		
		#cut
		ap.next = bn
		bn.prev = ap
		
		#paste
		xn.prev = b
		b.next = xn
		a.prev = x
		x.next = a
	
	def moveAfter(self, a, x):
		self.splice(a, a, x)
		
	def moveBefore(self, a, x):
		self.splice(a, a, x.prev)
	
	def insertBefore(self, x, key):
		self.moveBefore(Node(key), x)
	
	def insertAfter(self, x, key):
		self.moveAfter(Node(key), x)
	
	def pushFront(self, key):
		self.insertAfter(self.head, key)
		
	def pushBack(self, key):
		self.insertBefore(self.head, key)
		
	def deleteNode(self, x):
		if x == None or x == self.head:
			return
		x.prev.next, x.next.prev = x.next, x.prev
		
	def popFront(self):
		if self.isEmpty():
			return None
		key = self.head.next.key
		self.deleteNode(self.head.next)
		return key
	
	def popBack(self):
		if self.isEmpty():
			return None
		key = self.head.prev.key
		self.deleteNode(self.head.prev)
		return key
	
	def search(self, key):
		v = self.head.next
		while v != self.head:
			if v.key == key:
				return v
			v = v.next
		return None
	
	def first(self):
		if self.isEmpty():
			return None
		return self.head.next
	
	def last(self):
		if self.isEmpty():
			return None
		return self.head.prev
	
	def isEmpty(self):
		if self.head.next == self.head and self.head.prev == self.head:
			return True
		else:
			return False
		
	def findMax(self):
		if self.isEmpty():
			return None
		v = self.head.next
		maxKey = -99999999999999
		while v != self.head:
			if v.key > maxKey:
				maxKey = v.key
			v = v.next
		return maxKey

	def deleteMax(self):
		if self.isEmpty():
			return None
		maxKey = self.findMax()
		self.deleteNode(self.search(maxKey))
		return maxKey
	
	def sort(self):
		sortedLst = DoublyLinkedList()
		while not self.isEmpty():
			sortedLst.pushFront(self.deleteMax())
		return sortedLst

	def join(self, another_lst):
		sBack = self.head.prev
		aBack = another_lst.head.prev
		aFront = another_lst.head.next

		another_lst.head.next, another_lst.head.prev = another_lst.head, another_lst.head # another_lst initialize
    
    # attatch another_lst front to self back
		aFront.prev = sBack
		sBack.next = aFront

    # attatch another_lst back to self.head
		aBack.next = self.head
		self.head.prev = aBack

    ### total 6 link updated

	def split(self, v): # make self front ~ v.prev / return v.next ~ self back
		back_lst = DoublyLinkedList()
		vn = v.next # goes to back_lst.head
		vb = v.prev # goes to self.head
		sBack = self.head.prev # goes to back_lst.head

    # attatch vn to back_lst.head
		vn.prev = back_lst.head
		back_lst.head.next = vn

    # attatch sBack to back_lst.head
		sBack.next = back_lst.head
		back_lst.head.prev = sBack

	# attatch vb to self.head
		vb.next = self.head
		self.head.prev = vb

    ### total 6 link updated
		return back_lst


L = DoublyLinkedList()
for i in range(10):
	L.pushFront(i)
print(L)
M = DoublyLinkedList()
for i in range(10,20):
	M.pushFront(i)

print(M)

L.join(M)
print(L)

print(L.split(L.search(0)))
print(L)