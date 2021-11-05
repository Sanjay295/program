#5. Take a range from 0 – 100, find the digits that are repeated twice like 33, 77,etc and store them in an array 
def main():
     
    arr = [ 10,20,30,40,50,60,70,30,80,40,70]
     
    numberMap = {}
     
    max = len(arr)
    for i in arr:
        if not i in numberMap:
            numberMap[i] = True
             
        else:
            print("Repeating =", i)
     
    for i in range(1, max + 1):
        if not i in numberMap:
            print("Missing =", i)
main()
 