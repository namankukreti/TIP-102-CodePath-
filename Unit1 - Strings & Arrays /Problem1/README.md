Problem 1: Reverse Sentence
Write a function reverse_sentence() that takes in a string sentence and returns the sentence with the order of the words reversed. The sentence will contain only alphabetic characters and spaces to separate the words. If there is only one word in the sentence, the function should return the original string.

def reverse_sentence(sentence):
    pass
Example Usage:

sentence = "tubby little cubby all stuffed with fluff"
reverse_sentence(sentence)

sentence = "Pooh"
reverse_sentence(sentence)
Example Output:

"fluff with stuffed all cubby little tubby"
"Pooh"
Understand:
	I - Inputs
		Sentence in the form of a string		
	O - Outputs
		String output that is the reversed input
	C - Constraints
		If there's only one word, you return the og string 
	E - Edge cases
		If you have an empty string, there could potentially be errors depending on		   methodology?
		
Plan:
	Two ways I can see you do this:
	Two pointer: Left and Right pointer that swaps the elements
	Use pythons built in [::-1]

	Another way:
	Put the elements into a stack, and then pop the stack into a new string
Implement:
	See python file
	


