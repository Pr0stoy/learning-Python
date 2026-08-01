my_list = []
length = int(input("How many elements do you want to sort? : "))
for i in range(length):
      el = int(input("Add number to the list : "))
      my_list.append(el)
print(my_list)
  # It's a little fake, we need it to enter the while loop.
def fun(x):
    swapped = True
    while swapped:
        swapped = False  # no swaps so far
        for i in range(len(x)-1):
            if x[i] > x[i + 1]:
                swapped = True  # a swap occurred!
                x[i], x[i + 1] = x[i + 1], x[i]
    
    return x
print(fun(my_list))