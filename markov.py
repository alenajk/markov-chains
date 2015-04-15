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
import random

text_filename = sys.argv[1]
source_text = open(text_filename)
source_string = ""


for line in source_text:
    source_line = line.rstrip()
    source_string += source_line + " "

markov_dict = {}

def make_chains(corpus):
    """Takes input text as string; returns dictionary of markov chains."""

    source_list = corpus.split(" ")
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
    
starter_string = ""

def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""
    
    #Start with a random bi-gram
    bi_gram = random.choice(chains.keys())
    
    #Start output_string with our first bi-gram
    output_string = starter_string + " ".join(bi_gram)

    #Continue generating random text, concatonating to output_string, and creating new bi-grams as we go
    while True:
        if bi_gram in chains and chains[bi_gram] != []:
            new_word = random.choice(chains[bi_gram])
            output_string += " " + new_word
            bi_gram = (bi_gram[1], new_word)
        else:
            break

    return output_string


# # Get a Markov chain
chain_dict = make_chains(source_string)

# # Produce random text
random_text = make_text(markov_dict)

print random_text