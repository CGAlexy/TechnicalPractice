def fizzbuzz(vals):
    for val in vals: 
        if(val%3==0 and val%5==0): 
            print("FizzBuzz")
        elif(val%3==0): 
            print("Buzz")
        elif(val%5==0): 
            print("Fizz")
        else: 
            print(val)

fizzbuzz([1,2,3,4,5,6,7,8,9,15,30])