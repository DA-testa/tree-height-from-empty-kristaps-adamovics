import sys
import threading
import numpy

def compute_height(n, parents):
    # Write this function
    max_height = 0
    # Your code here
    len = numpy.zeros(n)
    tree = numpy.array(parents)
    check = numpy.zeros(n)
    
    for i in range(n):
        check[i] = 1
        len[i] = 1
        element = tree[i]
        if(check[element] != 1):
            while(element!=-1):
                element = tree[element]
                len[len!=0] += 1
                len[element]=1
                check[element] = 1
    for i in range(n):
        if(len[i] > max_height):
            max_height = int(len[i])
    return max_height

def main():
    txt=input()
    if "F" in txt:
        filename=input()
        if "a" not in filename:
            with open(str("test/"+filename), mode="r") as fails:
                count = int(fails.readline())
                elements = list(map(int, fails.readline().split()))
        else:
            print("error")
    elif "I" in txt:
        count=int(input())
        elements = list(map(int, input().split()))
    else:
        print("Input error")
    print(compute_height(count, elements))
   
sys.setrecursionlimit(10**7)
threading.stack_size(2**27)
threading.Thread(target=main).start()