import hashlib

i = 1
while True:
	str2hash = "yzbqklnj" + str(i)

	result = hashlib.md5(str2hash.encode()) 
	s = result.hexdigest()
	if s.startswith('000000'):
		print s
		print i
		exit(0)
	i += 1
