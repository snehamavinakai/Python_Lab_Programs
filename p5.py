class StringReverser:
    def reverse_words(self,input_string):
        words = input_string.split()
        reversed_words = words[::-1]
        reversed_string = "".join(reversed_words)
        return reversed_string
    
if __name__ == "__main__":
    input_string = "Hello World"
    reverser = StringReverser()
    reversed_result = reverser.reverse_words(input_string)
    print("Original String : ",input_string)
    print("Reversed String : ",reversed_result)