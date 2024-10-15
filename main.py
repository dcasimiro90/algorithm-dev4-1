def find_min_value(numbers):
    minium = numbers[0]
    
    for number in numbers[1:]:
        if number < minium:
            minium = number
    return minium

example_list = [12, 4, 9, 21, 7]


min_value = find_min_value(example_list)

print(f"The minium value in the list is: {min_value}")