# Assignment A4
# CS 1400
# Starter code by David Johnson
# Assignment completed by Jason Nguyen

# The multiply function computes the product of two factors with repeated adding
def multiply(factor1, factor2):
    product = 0
    for counter in range(factor2):
        product += factor1
    return product

#ADD YOUR FUNCTIONS BELOW HERE (AND REMOVE THIS LINE)
 #Choose larger func
# def choose_larger(num1,num2):
#     if num1 >= num2:
#         return num1
#     else:
#         return num2
# # Input numbers for num1-2
# choose_number = choose_larger(1, 20)
# print(choose_number)

# Describe number func
# def describe_number(number):
#     if number ==0:
#         return "zero"
#     elif number > 0:
#         return "positive"
#     elif number < 0:
#         return "negative"
# # Input 0 to test code
# input_number = describe_number(0)
# print(input_number)

# # Adding "a" or "an" func
# def add_a_or_an_to_word(word):
#     if word == 'a' or word == 'e' or word == 'i' or word == 'u':
#         return "an " + word
#     else:
#         return "a " + word
# # Test by printing words
# print(add_a_or_an_to_word("apple"))
# print(add_a_or_an_to_word("phone"))
#
# # Adding punc func.
# def collect_punctuation(sentence):
#     punctuation = ""
#     for char in sentence:
#         if char == '.' or char == ',' or char == '!' :
#             punctuation += char
#     return punctuation
# # test func
# print("""Testing collect_punctuation("Hey! I'm good, are you?"). Expecting a result of "!',." and computed a result of""", collect_punctuation("Hey! I'm good, are you?"))

# pirate word func
def translate_pirate_word (word):
# pirate words list
    pirate_words = {"my": "me","you": "ye","is": "be","are": "be","hello": "ahoy","yes": "arr","friend": "matey"}
    if word in pirate_words:
        return pirate_words[word]
    else:
        return word
# Test translate pirate word
print(translate_pirate_word("are"))

def translate_to_pirate(sentence):
    # Add a space to the end of the sentence
    sentence += " "
    translated_sentence = ""  # Initialize the translated sentence
    current_word = ""  # Initialize the current word being built

    # Loop over each character in the sentence
    for char in sentence:
        # If the character is a space, it indicates the end of a word
        if char == " ":
            # Translate the current word using translate_pirate_word function
            translated_word = translate_pirate_word(current_word)
            # Add the translated word and a space to the translated sentence
            translated_sentence += translated_word + " "
            # Reset the current word for the next word
            current_word = ""
        else:
            # Add the character to the current word being built
            current_word += char

    # Remove the trailing space and return the translated sentence
    return translated_sentence[:-1]
print(translate_to_pirate("hello friend"))

# ADD YOUR (FUNCTIONS) ABOVE HERE (AND REMOVE THIS LINE)

# Main tests all the functions and reports on their results
def main():
    print("Testing the multiply function")
    print("Testing multiply(2,3). Expecting a result of 6 and computed a result of", str(multiply(2,3)) + ".")
    print("Testing multiply(5,6). Expecting a result of 30 and computed a result of", str(multiply(5,6)) + ".")
    print()

if __name__=="__main__":
    main()