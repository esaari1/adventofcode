inst = ['set a 1',
'add a 2',
'mul a a',
'mod a 5',
'snd a',
'set a 0',
'rcv a',
'jgz a -1',
'set a 1',
'jgz a -2']

inst = [
'set i 31',
'set a 1',
'mul p 17',
'jgz p p',
'mul a 2',
'add i -1',
'jgz i -2',
'add a -1',
'set i 127',
'set p 952',
'mul p 8505',
'mod p a',
'mul p 129749',
'add p 12345',
'mod p a',
'set b p',
'mod b 10000',
'snd b',
'add i -1',
'jgz i -9',
'jgz a 3',
'rcv b',
'jgz b -1',
'set f 0',
'set i 126',
'rcv a',
'rcv b',
'set p a',
'mul p -1',
'add p b',
'jgz p 4',
'snd a',
'set a b',
'jgz 1 3',
'snd b',
'set f 1',
'add i -1',
'jgz i -11',
'snd a',
'jgz f -16',
'jgz a -19'
]

inst2 = [
'snd 1',
'snd 2',
'snd p',
'rcv a',
'rcv b',
'rcv c',
'rcv d'
]

q0 = []
q1 = []

class Program:

    def __init__(self, p):
        self.pos = 0
        self.id = p
        self.reg = {
            'a': 0,
            'p': p
        }

        self.sent = 0

    def run(self):
        global q0
        global q1
        if self.pos >= len(inst):
            return False
        p = inst[self.pos].split()

        if p[0] == 'set':
            val = p[2]
            if val in self.reg:
                val = self.reg[val]
            self.reg[p[1]] = int(val)
            self.pos += 1

        elif p[0] == 'add':
            val = p[2]
            if val in self.reg:
                val = self.reg[val]
            self.reg[p[1]] = self.reg.get(p[1], 0) + int(val)
            self.pos += 1

        elif p[0] == 'mul':
            val = p[2]
            if val in self.reg:
                val = self.reg[val]
            self.reg[p[1]] = self.reg.get(p[1], 0) * int(val)
            self.pos += 1

        elif p[0] == 'mod':
            val = p[2]
            if val in self.reg:
                val = self.reg[val]
            self.reg[p[1]] = self.reg.get(p[1], 0) % int(val)
            self.pos += 1

        elif p[0] == 'snd':
            val = p[1]
            if val in self.reg:
                val = self.reg[val]
            if self.id == 0:
                q1.append(int(val))
            else:
                q0.append(int(val))
            self.sent += 1
            self.pos += 1

        elif p[0] == 'rcv':
            #print(self.id, p, q0, q1)
            val = p[1]
            if self.id == 0:
                if len(q0) == 0:
                    return False
                self.reg[val] = q0[0]
                q0 = q0[1:]
            else:
                if len(q1) == 0:
                    return False
                self.reg[val] = q1[0]
                q1 = q1[1:]

            self.pos += 1

        elif p[0] == 'jgz':
            val = p[1]
            if val in self.reg:
                val = self.reg[val]
            val2 = p[2]
            if val2 in self.reg:
                val2 = self.reg[val2]
            val = int(val)
            val2 = int(val2)
            if val != 0:
                self.pos += val2
            else:
                self.pos += 1

        return self.pos < len(inst)

p0 = Program(0)
p1 = Program(1)

run0 = True

while True:
    print(p0.sent, p1.sent)
    while run0:
        run0 = p0.run()

    run1 = True
    while run1:
        run1 = p1.run()

    run0 = p0.run()
    if not run0:
        break

print(p1.sent)
