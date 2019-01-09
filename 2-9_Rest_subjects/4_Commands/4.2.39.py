sentence=input('enter the sentence: ')
sentlist=sentence.split(sep=' ')
newlist = [i for i in sentlist if i.find('Б')
+i.find('Е')+i.find('б')+i.find('е')==-4]
print(' '.join(newlist))
