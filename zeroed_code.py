def zeroed_code(numbers):
	if len(numbers) >= 2:
		numbers[0] = 0 
		numbers[-1] = 0;
		return numbers;	
	


print(zeroed_code([2, 5, 7, 8, 9]));