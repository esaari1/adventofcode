import math

total = 0

def processOperator(typeID, vals):
    if typeID == 0: # sum
        return sum(vals)
    if typeID == 1: # product
        return math.prod(vals)
    if typeID == 2: # min
        return min(vals)
    if typeID == 3: # max
        return max(vals)
    if typeID == 5: # gt
        if vals[0] > vals[1]:
            return 1
        else:
            return 0
    if typeID == 6: # lt
        if vals[0] < vals[1]:
            return 1
        else:
            return 0
    if typeID == 7: # eq
        if vals[0] == vals[1]:
            return 1
        else:
            return 0

    return 0

def readPacket(bits, prefix):
    global total
    version = int(bits[0:3], 2)
    typeID = int(bits[3:6], 2)

    total += version

    print(prefix, version, typeID)
    if typeID == 4:
        print(prefix, 'LITERAL')
        bit = 6
        valbits = ''
        while bits[bit] != '0':
            valbits += bits[bit+1:bit+5]
            bit += 5

        valbits += bits[bit+1:bit+5]
        bit += 5
        return bit, int(valbits, 2)

    else:
        print(prefix, 'OPERATOR', typeID)
        lengthType = bits[6]
        print(prefix, 'LTYPE', lengthType)
        vals = []
        if lengthType == '0':
            # read next 15 bits
            packetLen = int(bits[7:22], 2)
            print(prefix, packetLen)
            print(prefix, bits[22:22 + packetLen])
            bit = 0
            while bit < packetLen:
                (b, val) = readPacket(bits[22 + bit:22 + bit + packetLen], prefix + '     ')
                bit += b
                vals.append(val)
                print(prefix, 'bit', bit)

            return bit + 22, processOperator(typeID, vals)

        elif lengthType == '1':
            # read next 11 bits
            packetCount = int(bits[7:18], 2)
            print(prefix, 'PACKET COUNT', packetCount)

            bit = 18
            for c in range(packetCount):
                print(prefix, 'PACKET', c)
                (b, val) = readPacket(bits[bit:], prefix + '     ')
                bit += b
                vals.append(val)

            return bit, processOperator(typeID, vals)

        else:
            print(prefix, 'WHAT?')
            exit(0)

hexmap = {
'0': '0000',
'1': '0001',
'2': '0010',
'3': '0011',
'4': '0100',
'5': '0101',
'6': '0110',
'7': '0111',
'8': '1000',
'9': '1001',
'A': '1010',
'B': '1011',
'C': '1100',
'D': '1101',
'E': '1110',
'F': '1111'
}

input = '620D7800996600E43184312CC01A88913E1E180310FA324649CD5B9DA6BFD107003A4FDE9C718593003A5978C00A7003C400A70025400D60259D400B3002880792201B89400E601694804F1201119400C600C144008100340013440021279A5801AE93CA84C10CF3D100875401374F67F6119CA46769D8664E76FC9E4C01597748704011E4D54D7C0179B0A96431003A48ECC015C0068670FA7EF1BC5166CE440239EFC226F228129E8C1D6633596716E7D4840129C4C8CA8017FCFB943699B794210CAC23A612012EB40151006E2D4678A4200EC548CF12E4FDE9BD4A5227C600F80021D08219C1A00043A27C558AA200F4788C91A1002C893AB24F722C129BDF5121FA8011335868F1802AE82537709999796A7176254A72F8E9B9005BD600A4FD372109FA6E42D1725EDDFB64FFBD5B8D1802323DC7E0D1600B4BCDF6649252B0974AE48D4C0159392DE0034B356D626A130E44015BD80213183A93F609A7628537EB87980292A0D800F94B66546896CCA8D440109F80233ABB3ABF3CB84026B5802C00084C168291080010C87B16227CB6E454401946802735CA144BA74CFF71ADDC080282C00546722A1391549318201233003361006A1E419866200DC758330525A0C86009CC6E7F2BA00A4E7EF7AD6E873F7BD6B741300578021B94309ABE374CF7AE7327220154C3C4BD395C7E3EB756A72AC10665C08C010D0046458E72C9B372EAB280372DFE1BCA3ECC1690046513E5D5E79C235498B9002BD132451A5C78401B99AFDFE7C9A770D8A0094EDAC65031C0178AB3D8EEF8E729F2C200D26579BEDF277400A9C8FE43D3030E010C6C9A078853A431C0C0169A5CB00400010F8C9052098002191022143D30047C011100763DC71824200D4368391CA651CC0219C51974892338D0'
#input = '9C0141080250320F1802104A08'

bits = ''

for c in input:
    bits += hexmap[c]

print(bits)

version = int(bits[0:3], 2)
typeID = int(bits[3:6], 2)

(b, value) = readPacket(bits[0:], '')
print(value)
#print(total)
