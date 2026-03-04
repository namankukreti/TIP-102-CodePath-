In the extended universe of fictional bears, Goldilocks finds an enticing list of numbers in the Three Bears' house. She doesn't want to take a number that's too high or too low - she wants a number that's juuust right. Write a function goldilocks_approved() that takes in the list of distinct positive integers nums and returns any number from the list that is neither the minimum nor the maximum value in the array, or -1 if there is no such number.

Return the selected integer.

def goldilocks_approved(nums):
    pass
Example Usage

nums = [3, 2, 1, 4]
goldilocks_approved(nums)

nums = [1, 2]
goldilocks_approved(nums)

nums = [2, 1, 3]
goldilocks_approved(nums)
Example Output:

2
-1
2


Understand:
	I - Inputs
		Array of integers		
	O - Outputs
		Single element of the array (integer)
	C - Constraints
		return -1 if the integer doesn't exist. return neither the min or the max 
	E - Edge cases
		empty array, 2 integer array, duplicate elements (several maxes or several mins, could have an array of all the same number)
Plan:
	if statement that checks length
	variable that stores min or max, then iterate through it and if an element isn't equal to the min or max, return it
	I think that python just has a min or max function for arrays, if not you can just iterate through it
Implement:
	See python file
