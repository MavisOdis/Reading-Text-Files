# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}



def read_file_content(filename):
     
    with open("story.txt" , 'r') as filename:

        story = filename.read()
        
        return story
        

def count_words():
    text = read_file_content("./story.txt")
    words = text.split()
    occurance = dict()
 
    for i in words:

        if i in occurance:
            occurance[i] += 1

        else:
            occurance[i] = 1

    return occurance        

        

print(count_words())
