print(" ANANDHU V POOVANKAL")
print(" 23mca015")
def gen_ngrams(text,wordsToCombine):
    words=text.split()
    output=[]
    for i in range(len(words)-wordsToCombine+1):
        output.append(words[i:i+wordsToCombine])
    return output
x=gen_ngrams(text='Using the iris data set,impliments the KNN algorithm',wordsToCombine=3)
print(x)