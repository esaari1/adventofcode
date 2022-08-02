replacements = {}
m = {}

f = open('input.txt', 'r')

line = f.readline()
while line:
    line = line.strip()
    parts = line.split(' ')
    if parts[0] not in replacements:
        replacements[parts[0]] = []
    replacements[parts[0]].append(parts[2])
    line = f.readline()

f.close()


for k in replacements:
    for val in replacements[k]:
        idx = 0
        while True:
            s = 'CRnCaSiRnBSiRnFArTiBPTiTiBFArPBCaSiThSiRnTiBPBPMgArCaSiRnTiMgArCaSiThCaSiRnFArRnSiRnFArTiTiBFArCaCaSiRnSiThCaCaSiRnMgArFYSiRnFYCaFArSiThCaSiThPBPTiMgArCaPRnSiAlArPBCaCaSiRnFYSiThCaRnFArArCaCaSiRnPBSiRnFArMgYCaCaCaCaSiThCaCaSiAlArCaCaSiRnPBSiAlArBCaCaCaCaSiThCaPBSiThPBPBCaSiRnFYFArSiThCaSiRnFArBCaCaSiRnFYFArSiThCaPBSiThCaSiRnPMgArRnFArPTiBCaPRnFArCaCaCaCaSiRnCaCaSiRnFYFArFArBCaSiThFArThSiThSiRnTiRnPMgArFArCaSiThCaPBCaSiRnBFArCaCaPRnCaCaPMgArSiRnFYFArCaSiThRnPBPMgAr'

            idx = s.find(k, idx)
            if idx == -1:
                break
            s = s[:idx] + val + s[idx+len(k):]
            m[s] = 1
            idx += 1


print(len(m))