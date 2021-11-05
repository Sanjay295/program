#2. Extend the above program to sort the array and then find the 2nd largest and the 2nd smallest element. 
def print2largest(arr, arr_size):
    

 
    # There should be atleast
    # two elements
    if (arr_size < 2):
        print(" Invalid Input ");
        return;
 
    largest = second = -2454635434;
 
    # Find the largest element
    for i in range(0, arr_size):
        largest = max(largest, arr[i]);
 
    # Find the second largest element
    
    for i in range(0, arr_size):
        if (arr[i] != largest):
            second = max(second, arr[i]);
            
 
    if (second == -2454635434):
        print("There is no second " +
              "largest element");
    else:
        print("The second largest " +
              "element is \n", second);
 
# Driver code
if __name__ == '__main__':
   
    arr = [90,45, 60,
           100, 340, 869,1299];
    n = len(arr);
    print2largest(arr, n);
   
 