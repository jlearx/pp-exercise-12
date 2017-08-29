'''
Created on Aug 29, 2017

@author: jlearx
'''

def NewList(oldlist):
    newlist = []
    return newlist

if __name__ == '__main__':
    oldlist = []
    
    while (len(oldlist) == 0):
        listIn = input("Please enter a list of numbers inside []: ")
        start = listIn.find("[")
        finish = listIn.find("]")
        
        if ((start >= 0) and (finish > 0) and (finish != start + 1)):
            listStr = listIn.split(",")
            print(listStr)
            break
    
    print(NewList(oldlist))