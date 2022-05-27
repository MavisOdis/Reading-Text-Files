# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content():
    # [assignment] Add your code here 
    with open("story.txt" , 'r') as f:
        var = f.read()
        print(var)
        f.close()



def count_words():
    text = read_file_content("story.txt")
    # [assignment] Add your code here
    count = 0
    for word in text:
        count += 1
        return {"as": 10, "would": 20}

# print(count_words)
# read_file_content()

with open("read.txt", 'r') as f:
    var = f.read()
    print(var)
    f.close()