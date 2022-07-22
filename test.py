
def digitin(a, b):
    digit = 1
    while b > 1:
        digit *= 10
        b -= 1
    digit = (a/digit) % 10
    return int(digit)


print (digitin(1594,8))