#import text file in from command line
#format the text so that it's splittable - take out white space
#split into bi-grams
#Initialize an empty dictionary
#store the bigrams in tuples, these tuples into a dictionary, the value an emptly list
#while/for loop to go through, collect the words following each bi-gram, append them to list in dictionary
#initialize empty string or list to keep track of our new text
#pick random key to start
#while loop, if else statement looking for if key in dictionary
#adding random value (word in list) for key (bi-gram) to new string/list (new text) if key in dictionary
#make new bi-gram to feed into (function?)/while loop to generate another value/word.
#in while loop - else: if cannot find key in dictionary, break
#print the new text/string/ 

import sys

text_filename = sys.argv[1]
source_text = open(text_filename)
source_string = ""

for line in source_text:
    source_line = line.rstrip()
    source_string += source_line + " "

markov_dict = {}

def make_chains(corpus):
    """Takes input text as string; returns dictionary of markov chains."""

    source_list = source_string.split(" ")
    source_list.pop()

    for i in range(len(source_list)-1):
        if (source_list[i], source_list[i+1]) not in markov_dict:
            markov_dict[(source_list[i], source_list[i+1])] = []    
            if i <= len(source_list)-3:
                markov_dict[(source_list[i], source_list[i+1])].append(source_list[i+2])
        else:
            if i <= len(source_list)-3:
                markov_dict[(source_list[i], source_list[i+1])].append(source_list[i+2])

    return markov_dict


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    return "Here's some random text."


# Change this to read input_text from a file, deciding which file should
# be used by examining the `sys.argv` arguments (if neccessary, see the
# Python docs for sys.argv)

# input_text = "Some text"

# # Get a Markov chain
chain_dict = make_chains(source_string)

# # Produce random text
# random_text = make_text(chain_dict)

# print random_text
print chain_dict
