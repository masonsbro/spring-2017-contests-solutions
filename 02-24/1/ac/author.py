cases = int(raw_input())
for i in range(cases):
	c, g = map(int, raw_input().split())
	if (g < c):
		print 'LEFT'
	else:
		print 'RIGHT'