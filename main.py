
# Input & Output in Python
FirstName = input('First Name : ')
LastName = input('Last Name : ')

print(FirstName +' '+ LastName)

def InputNumber():
    input_number = input('Enter the number : ')
    PostiveNumber(input_number)
def PostiveNumber(input_number):
    if int(input_number) % 4:
        print(input_number)

InputNumber()