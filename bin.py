def e(t):
    return ' '.join(format(ord(c), '08b') for c in t)

def d(b):
    b_vals = b.split(' ')
    return ''.join(chr(int(bv, 2)) for bv in b_vals)

o = input("1) Encode, \n2) Decode: ")

if o == '1':
    t = input("Enter text to encode: ")
    b = e(t)
    print("Encoded:", b)
elif o == '2':
    b_in = input("Enter binary to decode: ")
    t_decoded = d(b_in)
    print("Decoded:", t_decoded)
else:
    print("Invalid option")
