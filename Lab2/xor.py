a = bytearray(b"U.ìS.].è®.Úÿ.Àp.  ")
b = bytearray(b"4yn142cf")
for i in range(len(a)):
    d = a[i]^b[i]
    if 48 <= d < 59:
        print(chr(d), end='')
        continue
    if 97 <= d <= 123:
        print(chr(d), end='')
        continue
    if 80 <= d <= 89:
        print(d-80, end='')
        continue
    else:
        print(chr(ord('a')-1+d), end='')
        continue