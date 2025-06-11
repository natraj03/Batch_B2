input_strr = "Welcome to Python"
# output = "emocleW ot nohtyP"

split_str = input_strr.split()
print("split_str",split_str)
def revfunc(inp1):
        rev_word = ""
        for char in inp1:
            rev_word = char + rev_word
        return rev_word

print(revfunc(input_strr))

finalStr = ""
for word in split_str:
    print("word",word)
    # finalStr = finalStr + " "+  word
    finalStr = finalStr+ " " + revfunc(word)

print("Rreverse of word",finalStr)