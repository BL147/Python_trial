"""
1. Take 4 letters as input

2.Break the word into letters

3. Convert letters to numbers

4.Increase each by 1

5.Convert these numbers to letters

6.Combine the 4 shifted letters
"""
word = input("Type a 4 letter word")
a = word[0]
b = word[1]
c = word[2]
d = word[3]

print(str(a)+" "+str(b)+" "+str(c)+" "+str(d))

a1 = ord(a)
b1 = ord(b)
c1 = ord(c)
d1 = ord(d)

print(str(a1)+" "+str(b1)+" "+str(c1)+" "+str(d1))

a1 = a1+1
b1 = b1+1
c1 = c1+1
d1 = d1+1

print(str(a1)+" "+str(b1)+" "+str(c1)+" "+str(d1))


a2 = chr(a1)
b2 = chr(b1)
c2 = chr(c1)
d2 = chr(d1)

print(a2+b2+c2+d2)
