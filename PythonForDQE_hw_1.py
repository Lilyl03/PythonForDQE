# This is a sample Python script.
import random as rnd


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


rand_nums= [rnd.randint(0,1000) for i in range(1000)]
sorted_rand_nums=[]

while rand_nums != []:
    sorted_rand_nums.append(min(rand_nums))
    rand_nums.remove(min(rand_nums))

print(len(sorted_rand_nums))
print(rand_nums)
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