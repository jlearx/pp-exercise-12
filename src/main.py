'''
Created on Aug 29, 2017

@author: jlearx
'''

def NewList(oldlist):
    newlist = oldlist[1:len(oldlist) - 1]
    return newlist

if __name__ == '__main__':
    oldlist = []
    
    while (len(oldlist) == 0):
        listIn = input("Please enter a list of numbers inside []: ")
        start = listIn.find("[")
        finish = listIn.find("]")
        
        if ((start >= 0) and (finish > 0) and (finish != start + 1)):
            listIn = listIn[start + 1:finish]
            listIn = listIn.replace(" ", "")
            listStr = listIn.split(",")
            oldlist = listStr
            break
    
    newlist = NewList(oldlist)
    length = len(newlist)
    
    print("Here is the new list:")
    
    for i in range(0, length):
        if (i < length - 1):
            print(newlist[i], end=', ')
        else:
            print(newlist[i])
    