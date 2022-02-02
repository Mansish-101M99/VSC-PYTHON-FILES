def verify_prime(num):
    pm = True
    #Take numbers from 2 to the num
    if num > 1:
        for i in range(2,num//2 + 1):
#Traversing from each integer and dividing num with all of them lying b/w 2 to num//2. we did num//2 because in the mid of that num, the 1st 1/2 will be from 2 to num//2 and the 2nd 1/2 will be n//2 + 1 to num. the 2nd 1/2 will not be exactly divisible and will be in decimal. 
            if ((i % 2) == 0):
                pm = False
                break          
                #Breaking after we found another factor
            
        if pm is True:
            print("The number ",num," is a prime number.")
        else:
            print("The number ",num," is not a prime number.")
    
#Python program to check if a number is prime or not

n = int(input("Enter a number : "))
vr = verify_prime(n)
print(vr)