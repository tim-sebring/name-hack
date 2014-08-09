#!/bin/env python
""" http://www.reddit.com/r/dailyprogrammer/comments/2cld8m/8042014_challenge_174_easy_thuemorse_sequences/ """

mycount = 6
mystr = "0"
newstr = ""
anotherstr = ""

def togglebit(bit):
    """ Returns a 0 for 1 and a 1 for 0 """
    if bit == "0":
        return "1"
    else:
        return "0"


def togglestring(str):
    """ uses togglebit to toggle a whole string """
    newstr = ""
    for c in str:
        newstr = newstr + togglebit(c)
    return newstr

I = 0
while I <= mycount:
    
    print("Iteration %d is %s" % (I,mystr))
    newstr = togglestring(mystr)
    mystr = mystr + newstr
    I+=1





