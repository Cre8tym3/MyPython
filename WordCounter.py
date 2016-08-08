# Write a program that given a phrase can count the occurrences of each word in that phrase.

words = 'olly olly in come free'

wordcount={}

for word in words.split():
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1

for k,v in wordcount.items():
    print (k, v)
    #print (wordcount)

