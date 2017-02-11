import string
import random

test_cases = 9
STRING_LEN = 10
max_commands = 100000

valid_opens = ['SEND', 'RECEIVE']
valid_all = ['SEND', 'RECEIVE', 'DELETE']

print test_cases

bank_10000 = []
for i in range(10000):
	bank_10000.append(''.join(random.choice(string.ascii_uppercase) for _ in range(5)))


# Check single empty case
print str(1)
print 'DELETE'

# Hand case
# Expected:
# CAMERON
# CAMERON
# ARNAV
# JENNY
# TAYLOR
print str(15)
print 'SEND JENNY'
print 'SEND ARNAV'
print 'SEND CAMERON'
print 'SEND CAMERON'
print 'RECEIVE CAMERON'
print 'DELETE'
print 'RECEIVE CAMERON'
print 'DELETE'
print 'DELETE'
print 'SEND JENNY'
print 'DELETE'
print 'RECEIVE CAMERON'
print 'SEND ARNAV'
print 'SEND TAYLOR'
print 'DELETE'

# Test single person 
# Expected output: 
# JENNY
# NONE
print str(max_commands)
for i in range(max_commands - 2):
	print random.choice(valid_opens) + ' JENNY'
print 'DELETE'
print 'DELETE'

# Test back and forth between two people.
# Expected Output:
# CHRIS
# JENNY
# ^^ ten times total
print str(10000)
for i in range(10):
	for j in range(998 / 2):
		print random.choice(valid_opens) + ' JENNY'
		print random.choice(valid_opens) + ' CHRIS'
	print 'DELETE'
	print 'DELETE'

# Test half and half
print str(max_commands)
for i in range(max_commands / 2 - 1):
	print random.choice(valid_opens) + ' JENNY'
for j in range(max_commands / 2 - 1):
	print random.choice(valid_opens) + ' CHRIS'
print 'DELETE'
print 'DELETE'

# Test 50000 random adds followed by 10,000 deletes
print str(100000 + 10000)
for name in bank_10000:
	print random.choice(valid_opens) + ' ' + name
for i in range(100000 - 10000):
	print random.choice(valid_opens) + ' ' + random.choice(bank_10000)
for i in range(10000):
	print 'DELETE'

# 1 completely randomized
for j in range(1):
	print str(max_commands)
	for i in range(max_commands):
		c = random.choice(valid_all)
		if (c == 'DELETE'):
			print c
		else:
			print c + ' ' + random.choice(bank_10000)

# Double delete at the end
print str(max_commands / 2)
for i in range((max_commands) / 2 - 2):
	print random.choice(valid_opens) + ' ' + random.choice(bank_10000)
print 'DELETE'
print 'DELETE'

# Lots of adds, relatively few deletes
print str(max_commands)
for i in range(max_commands):
	choice = random.randint(1, 20)
	if (choice == 20):
		print 'DELETE'
	else:
		print random.choice(valid_opens) + ' ' + random.choice(bank_10000)

