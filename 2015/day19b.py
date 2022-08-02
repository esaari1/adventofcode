import pdb

replacements = {}
states = {}

def process(s, steps):
	global states

	if s == 'e':
		print(steps)
		exit(0)
		return

	if s in states:
		return

	states[s] = 1

	for k in replacements:
		idx = 0
		while idx > -1:
			idx = s.find(k, idx)
			if idx >= 0:
				s2 = s[:idx] + replacements[k] + s[idx+len(k):]
				idx += 1
				process(s2, steps + 1)

		#print('Done with ', k, steps)

f = open('input.txt', 'r')

line = f.readline()
while line:
    line = line.strip()
    parts = line.split(' ')
    p2 = parts[2].replace('Rn', '').replace('Ar', '')
    replacements[p2] = parts[0]
    line = f.readline()

f.close()

str = 'CRnCaSiRnBSiRnFArTiBPTiTiBFArPBCaSiThSiRnTiBPBPMgArCaSiRnTiMgArCaSiThCaSiRnFArRnSiRnFArTiTiBFArCaCaSiRnSiThCaCaSiRnMgArFYSiRnFYCaFArSiThCaSiThPBPTiMgArCaPRnSiAlArPBCaCaSiRnFYSiThCaRnFArArCaCaSiRnPBSiRnFArMgYCaCaCaCaSiThCaCaSiAlArCaCaSiRnPBSiAlArBCaCaCaCaSiThCaPBSiThPBPBCaSiRnFYFArSiThCaSiRnFArBCaCaSiRnFYFArSiThCaPBSiThCaSiRnPMgArRnFArPTiBCaPRnFArCaCaCaCaSiRnCaCaSiRnFYFArFArBCaSiThFArThSiThSiRnTiRnPMgArFArCaSiThCaPBCaSiRnBFArCaCaPRnCaCaPMgArSiRnFYFArCaSiThRnPBPMgAr'
str = str.replace('Rn', '')
str = str.replace('Ar', '')
process(str, 0)
