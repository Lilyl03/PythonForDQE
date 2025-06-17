import random as rnd

#Create a python script:

#1.create list of 100 random numbers from 0 to 1000

rand_nums= [rnd.randint(0,1000) for i in range(1000)]

#2.sort list from min to max (without using sort())
sorted_rand_nums=[]

while rand_nums != []:
    sorted_rand_nums.append(min(rand_nums))
    rand_nums.remove(min(rand_nums))
    
#3.calculate average for even and odd numbers
even_sum=0
even_count=0
odd_sum=0
odd_count=0


for i in sorted_rand_nums:
    if i%2==0 :
        even_sum+=i
        even_count+=1
    else:
        odd_sum+=i
        odd_count+=1

even_avg=even_sum/even_count
odd_avg=odd_sum/odd_count

#4.print both average result in console 
print("Even Average: ", even_avg)
print("Odd Average: ", odd_avg)
