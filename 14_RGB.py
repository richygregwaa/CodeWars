
# My Solution
# I lacked knowledge with format {0:x} and could have used {:02X} meaning I wouldn't need zfill(2)
def rgb(r, g, b):
    r = val_range(r)
    g = val_range(g)
    b = val_range(b)
    txt = "{0:x}"
    ret = txt.format(r).zfill(2) + txt.format(g).zfill(2) + txt.format(b).zfill(2)
    return ret.upper()


def val_range(value):
    if value not in range(1, 256):
        if value > 255:
            return 255
        else:
            return 0
    return value


# Alternative Solution 1
def rgb1(r, g, b):
    round = lambda x: min(255, max(x, 0))
    return ("{:02X}" * 3).format(round(r), round(g), round(b))


# Alternative Solution 2
# See how 3 variables are formatted, range checked and concatenated in one return line
def limit(num):
    if num < 0:
        return 0
    if num > 255:
        return 255
    return num


def rgb2(r, g, b):
    return "{:02X}{:02X}{:02X}".format(limit(r), limit(g), limit(b))


print (rgb(148,0,211))
print (rgb1(148,0,211))
print (rgb2(0,0,0))

# rgb(255, 255, 255) # returns FFFFFF
# rgb(255, 255, 300) # returns FFFFFF
# rgb(0,0,0) # returns 000000
# rgb(148, 0, 211) # returns 9400D3
