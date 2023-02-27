import sys
import threading
import numpy

def compute_height(n, parents):
    # Write this function
    max_height = 0
    # Your code here
    tree = numpy.array(parents)
    max_height = max(next(tree, n), max_height)
    return max_height

def next(tree, n):
    for i in range(n):
        height = 1
        element = tree[i]
        while(element != -1 ):
            element = tree[element]
            height += 1
    return height + 1

def main():
    txt=input()
    if "F" in txt:
        filename=input()
        if "a" not in filename:
            with open(filename, mode="r") as fails:
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