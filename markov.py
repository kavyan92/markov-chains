"""Generate Markov text from text files."""
import random
from random import choice

def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    file = open(file_path).read()

    return file

def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """
    #split up long string into a list of individual words
    text = text_string.split()


    #loop over each word (i) in list 'text' and create tuples
    
    chains = {}

    for i in range(len(text) - 2):
        #create tuple from text list
        bigram = (text[i], text[i + 1])

        # #check if key is in chains dict, if not, add as new key
        if bigram not in chains:
            # add each bigram/key to dict, with empty list as value 
            chains[bigram] = []
        # append values to empty list for each key
        chains[bigram].append(text[i + 2])

    return chains
            

    #...get values for each tuple that are all the words that could come 
    #...after that tuple and add as values to chains dict
    

def make_text(chains):
    """Return text from chains."""
    #create list to add in all text that we'll string together at the end
    words = []

    # pull out first key from dict
    key1, value1 = list(chains.items())[0]

    #pick random value from key
    random_value = random.choice(value1)
    
    #create new key with first key and random value
    new_key = (key1[1], random_value)
    
    # add key to words list
    words.append(key1[0])
    words.append(new_key[0])
    words.append(new_key[1])
    
    
# create a new key with the second word in key + random value
        
    while True:

        #if the new key just created is in the dictionary chains
        if new_key in chains.keys():
        
            #assign value associated with new_key
            next_value_list = chains.get(new_key, 0)
            
            #choose a random value from value list
            next_value = random.choice(next_value_list)
            
            #add chosen value into words list
            words.append(next_value)
            
            #make newest pair the new_key
            new_key = (words[-2], words[-1])                
        
        #once the new_key is no longer in dict, end loop  
        else:
            break
    
    #convert list of words into a string
    return ' '.join(words)

 

input_path = 'green-eggs.txt'

# # # Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# # # Get a Markov chain
chains = make_chains(input_text)

# # Produce random text
random_text = make_text(chains)

print(random_text)

