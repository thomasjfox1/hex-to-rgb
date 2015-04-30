filename = 'hex.txt'

def main(filename):
    i = 0
    with open(filename, "r") as f:
        for line in f:
            translate(line, i)
            i = i + 1

def translate(hex, inc):
    r = hex[:2]
    g = hex[2:4]
    b = hex[4:]

    '''print(r+g+b)'''
    r = str(hexToDecimal(r))
    g = str(hexToDecimal(g))
    b = str(hexToDecimal(b))

    print('new int[]{255,' + r + ',' + g + ',' + b + ','+ str(inc) +'},')


def hexToDecimal(hexNum):
    return int(hexNum, 16)

main(filename)
