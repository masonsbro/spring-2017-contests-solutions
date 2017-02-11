import random
import string

test_cases = 10

print test_cases

# # Multiname with domestic issues travel
# # Expected output:
# # 
# # IMPOSSIBLE
# # 0
# # 0
# # IMPOSSIBLE
# # IMPOSSIBLE
# # IMPOSSIBLE
# # 1
# # 0
# print '6 4 8'
# print 'MOSCOW JAPAN TO PARIS FRANCE'
# print 'MOSCOW FRANCE TO PARIS FRANCE'
# print 'MOSCOW FRANCE TO PARIS JAPAN'
# print 'PARIS JAPAN TO MOSCOW JAPAN'
# print 'MOSCOW JAPAN TO MOSCOW FRANCE'
# print 'PARIS FRANCE TO PARIS JAPAN'
# print 'FRANCE NO JAPAN'
# print 'NORWAY NO SWEDEN'
# print 'SWEDEN NO NORWAY'
# print 'CHINA NO FRANCE'
# print 'FRANCE PARIS FRANCE TO MOSCOW FRANCE'
# print 'FRANCE MOSCOW FRANCE TO PARIS FRANCE'
# print 'CANADA MOSCOW JAPAN TO MOSCOW FRANCE'
# print 'FRANCE MOSCOW JAPAN TO NYC USA'
# print 'USA NYC USA TO PARIS JAPAN'
# print 'FRANCE MOSCOW FRANCE TO MOSCOW JAPAN'
# print 'JAPAN MOSCOW FRANCE TO MOSCOW JAPAN'
# print 'CHINA MOSCOW FRANCE TO PARIS FRANCE'

# # Test for differentiating between city and country
# # Expected:
# # 1
# # IMPOSSIBLE
# # 1
# print '4 0 3'
# print 'R USSIA TO PARIS FRANCE'
# print 'RU SSIA TO PARIS FRANCE'
# print 'PARIS FRANCE TO RU SSIA'
# print 'PARIS FRANCE TO RUSS IA'
# print 'CHINA R USSIA TO RU SSIA'
# print 'CHINA RU SSIA TO R USSIA'
# print 'CHINA RU SSIA TO RUSS IA'

# cities = []
# for i in range(50):
# 	cities.append(''.join(random.choice(string.ascii_uppercase) for _ in range(5)))
# countries = []
# for i in range(50):
# 	countries.append(''.join(random.choice(string.ascii_uppercase) for _ in range(5)))

# # Long line with a few restrictions
# print '49 4 49'
# for j in range(49):
# 	print cities[j] + ' ' + countries[j] + ' TO ' + cities[j + 1] + ' ' + countries[j + 1]
# for i in range(4):
# 	print countries[i * 10] + ' NO ' + countries[(i + 1) * 10]
# for i in range(49):
# 	print countries[i] + ' ' + cities[i] + ' ' + countries[i] + ' TO ' + cities[49] + ' ' + countries[49]

# # Completely connected with no restrictions
# # Should be all zeroes 
# print str(50 * 49) + ' 0 ' + str(100)
# for i in range(50):
# 	for j in range(50):
# 		if (i != j):
# 			print cities[i] + ' ' + countries[i] + ' TO ' + cities[j] + ' ' + countries[j]

# for i in range(100):
# 	choice_one = random.randint(0, 49)
# 	choice_two = random.randint(0, 49)
# 	if (choice_one == choice_two):
# 		if (choice_one == 49):
# 			choice_one -= 1
# 		else:
# 			choice_one += 1
# 	nat = random.choice(countries)
# 	print nat + ' ' + cities[choice_one] + ' ' + countries[choice_one] + ' TO ' + cities[choice_two] + ' ' + countries[choice_two]

def gen_pairs(num_countries, num_nodes):
	countries = []
	for i in range(num_countries):
		countries.append(''.join(random.choice(string.ascii_uppercase) for _ in range(1)))

	country = []
	city = []
	for j in range(num_nodes):
		country.append(random.choice(countries))
		city.append(''.join(random.choice(string.ascii_uppercase) for _ in range(1)))

	return countries, country, city

def tree(num_nodes, num_blacklist, num_queries, num_countries):
	# It's a bird, it's a plane, it's a treeeeeeeeeeeeeeeeeeee
	num_connections = (num_nodes - 1) * 2
	print str(num_connections) + ' ' + str(num_blacklist) + ' ' + str(num_queries)

	countries, country, city = gen_pairs(num_countries, num_nodes)

	# Print connections
	for j in range(num_nodes):
		if (j == 0):
			continue;
		predecessor = random.randint(0, j - 1)
		str_one = str(city[j]) + ' ' + str(country[j])
		str_two = str(city[predecessor]) + ' ' + str(country[predecessor])
		print str_one + ' TO ' + str_two
		print str_two + ' TO ' + str_one

	# Print blacklist
	for k in range(num_blacklist):
		first, second = '', ''
		while (first == second):
			first, second = random.choice(countries), random.choice(countries)
		print first + ' NO ' + second

	# Print queries
	for j in range(num_queries):
		nat = random.choice(countries)
		start = 0
		finish = 0
		while (start == finish):
			start, finish = random.randint(0, num_nodes - 1), random.randint(0, num_nodes - 1)
		str_one = city[start] + ' ' + country[start]
		str_two = city[finish] + ' ' + country[finish]
		print str(nat) + ' ' + str_one + ' TO ' + str_two

# # Tree with no blacklist
# tree(100, 0, 100, 10)

# # Bigger tree with no blacklist
# tree(500, 0, 500, 20)

# Tree with a blacklist
for i in range(10):
	tree(10, 5, 10, 10)

# # Bigger tree with a blacklist
# for i in range(5):
# 	tree(500, 10, 500, 20)


# #### Random gen
# max_cities = 500
# max_countries = 20
# for i in range(2):
# 	num_countries = random.randint(2, max_countries)
# 	mapping = {}
# 	for i in range(num_countries):
# 		mapping[''.join(random.choice(string.ascii_uppercase) for _ in range(5))] = []

# 	num_cities = random.randint(2, max_cities)
# 	countries = mapping.keys()
# 	for j in range(num_cities):
# 		country = random.choice(countries)
# 		mapping[country].append(''.join(random.choice(string.ascii_uppercase) for _ in range(5)))

# 	num_connections = random.randint(num_cities, num_cities * (num_cities - 1) / 4)
# 	num_blacklist = random.randint(1, num_countries * (num_countries - 1) / 2)
# 	num_queries = random.randint(num_cities, 500)

# 	print str(num_connections) + ' ' + str(num_blacklist) + ' ' + str(num_queries)

# 	connected = {}

# 	for i in range(num_connections):
# 		done = False
# 		while (not done):
# 			country_one, country_two = random.choice(countries), random.choice(countries)
# 			if (len(mapping[country_one]) == 0 or len(mapping[country_two]) == 0):
# 				continue;
# 			city_one, city_two = random.choice(mapping[country_one]), random.choice(mapping[country_two])
# 			if (country_one == country_two and city_one == city_two):
# 				continue
# 			str_one = str(city_one) + ' ' + str(country_one)
# 			str_two = str(city_two) + ' ' + str(country_two)
# 			if str_one not in connected:
# 				connected[str_one] = []
# 			if str_two not in connected[str_one]:
# 				print str_one + ' TO ' + str_two
# 				done = True

# 	blacklist = {}
# 	for i in range(num_blacklist):
# 		done = False
# 		while (not done):
# 			country_one, country_two = random.choice(countries), random.choice(countries)
# 			if (country_one == country_two):
# 				continue;
# 			if country_one not in blacklist:
# 				blacklist[country_one] = []
# 			if country_two not in blacklist[country_one]:
# 				print country_one + ' NO ' + country_two
# 				done = True

# 	for i in range(num_queries):
# 		done = False
# 		while not done:
# 			nationality = random.choice(countries)
# 			country_one, country_two = random.choice(countries), random.choice(countries)
# 			if (len(mapping[country_one]) == 0 or len(mapping[country_two]) == 0):
# 				continue;
# 			city_one, city_two = random.choice(mapping[country_one]), random.choice(mapping[country_two])
# 			if (country_one == country_two and city_one == city_two):
# 				continue
# 			print nationality + ' ' + city_one + ' ' + country_one + ' TO ' + city_two + ' ' + country_two 
# 			done = True





