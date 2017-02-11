class Node():
	def __init__(self, value):
		self.next = None
		self.previous = None
		self.value = value

	def __str__(self):
		ans = 'NEXT IS ' + str(self.next.value)
		ans = ans + '\nPREVIOUS IS ' + str(self.previous.value) + '\n'
		return ans

class Buffer():

	def __init__(self):
		self.head = Node('HEAD')
		self.tail = Node('TAIL')
		self.head.next = self.tail
		self.tail.previous = self.head 
		self.storage = {}

	def contains(self, value):
		return value in self.storage

	def addFront(self, value):
		newNode = Node(value)
		self.storage[value] = newNode
		newNode.previous = self.head
		newNode.next = self.head.next
		self.head.next.previous = newNode
		self.head.next = newNode

	def remove(self, value):
		toRemove = self.storage[value]
		toRemove.previous.next = toRemove.next
		toRemove.next.previous = toRemove.previous
		del self.storage[value]

	def removeFirst(self):
		if (len(self.storage) == 0):
			return None
		returnVal = self.head.next.value
		self.remove(returnVal)
		return returnVal

	def printList(self):
		curr = self.head.next
		while (curr != self.tail):
			print curr.value
			curr = curr.next
		print ''

def main():
	cases = int(raw_input())
	for case in range(cases):
		commands = int(raw_input())
		container = Buffer()
		for j in range(commands):
			line = raw_input()
			if (line == 'DELETE'):
				val = container.removeFirst()
				if (val == None):
					print 'NONE'
				else:
					print val
			else:
				action, person = line.split()
				if (action != 'SEND' and action != 'RECEIVE'):
					raise Exception('Unexpected value ' + action)
				if (container.contains(person)):
					container.remove(person)
				container.addFront(person)
		print('')

main()


