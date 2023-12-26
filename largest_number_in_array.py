def largest_number_in_array(array):
    largest_num = 0

    for collect in range(len(array)):
        print()
        array[collect] = int(input("OYA BOSS SHARPLY ENTER ANY INTEGER: "))
        if array[collect] > largest_num:
            largest_num = array[collect]

    return largest_num


#if __name__ == "__main__":
my_array = [0] * 5

print("I WILL BE HELPING YOU CHOOSE CORRECTLY THE LARGEST INPUT FROM YOUR CHOICE OF THREE INTEGERS:")
print()
print("The Highest Number Amongst All Three Choice From User Input is thus:", largest_number_in_array(my_array))
