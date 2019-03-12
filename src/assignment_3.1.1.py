largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" : break

    try:
        largest = 10
        smallest = 2

    except:
        if num == "done" : break
print('Invalid input')
print("Maximum", largest)
print("Minimum", smallest) 
