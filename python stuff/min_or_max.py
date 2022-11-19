num_list = []
while True:
    num = input("Please enter a number to add to the list (type q to quit): ")
    if num == 'q':
        break
    else:
        num_list.append(float(num))
while True:
    find = input("Do you want to find the minimum or maximum? ")
    if find == 'min':
        item = min(num_list)
        break
    elif find == 'max':
        item = max(num_list)
        break
    else:
        print("Invalid input")
print(f"Here is our list: {num_list}")
if find == 'min':
        print(f"And here is the minimum item: {item}")
elif find == 'max':
        print(f"And here is the maximum item: {item}")
