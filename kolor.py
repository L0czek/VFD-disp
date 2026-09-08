blue = int(input(), 2)
green = int(input(), 2)
red = int(input(), 2)
g = int(input(), 2)

def get(color, bit):
    return (color >> (bit - 1)) & 1

bitlist = [get(blue, 3), get(green, 3), get(red, 3), 0, get(blue, 4), 
 get(green, 4), get(red, 4), 0, get(blue, 5), get(green, 5), 
 get(red, 5), 0, get(blue, 6), get(green, 6), get(red, 6), 
 0, get(blue, 7), get(green, 7), get(red, 7), 0, 
 get(blue, 1), get(green, 1), get(red, 1), 0, get(blue, 2), 
 get(green, 2), get(red, 2), 0, 0, 0, 
 0, get(g, 1), get(g, 2), get(g, 3), get(g, 4), 
 get(g, 5), 0, 0, 0, 0]

out = 0 
for bit in bitlist:
    out = (out << 1) | bit
print(bin(out))
