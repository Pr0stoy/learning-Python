my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
to_find = int(input("what do you want to find?: "))
found = False
for i in range(len(my_list)):
    if my_list[i] == to_find:
        print(f"index is {i}")
        break
else:
    print("absent")
