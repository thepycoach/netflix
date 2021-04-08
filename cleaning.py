import re
def clean_transcripts(text):
    #if it has more than 100 group of '4 upper-cased words in a row' then most likely the whole
    #transcript is in upper case. If so, do NOT remove the dialogues' names
    if len(re.findall('[A-Z]{2,} [A-Z]{2,} [A-Z]{2,} [A-Z]{2,}', text)) > 100:
        text = text.lower()
        text = re.sub("'s", ' s', text) #splitting possesion e.g. "Andy's toys" -> "Andy s toys". it helps in vocabulary coverage. gives 's'. Count Vectorizer will ignore it
        text = re.sub("'re", ' re', text)  # gives 're'. Count Vectorizer will NOT ignore it
        text = re.sub("'d", ' d', text)  # gives 'd'. Count Vectorizer will ignore it
        text = re.sub("can't", 'cannot', text)
        text = re.sub("won't", 'will not', text)
        text = re.sub("n't", ' not', text)
        text = re.sub("'ll", ' will', text)
        text = re.sub("'ve", ' have', text)
        text = re.sub("'m", ' am', text)
        text = re.sub('-',' ',text) #must include this one in next rounf !!!
        text = re.sub('\[.*?\]','',text) #get rid of words inside square brackets + sq. brackets
        text = re.sub('\(.*?\)','',text) #get rid of words inside parentheses + parentheses
        text = re.sub('[^\w\s]','',text) #get rid of punctuation
        text = re.sub('\w*\d\w*','',text) #remove digits or words containing digits
        text = re.sub('_','', text) #transcript contains this: __hello
        text = re.sub(r'\w*([a-z])\1{2,}\w*','', text) # repetitive letters aah ohhhh: you don't need \b cause it needs 3 repetitive letters together
    else:
        text = re.sub('[A-Z]{2,}', '', text)  # get rid of dialogues' names e.g. WOODY: bla bla bla. BUZZ: bla
        text = text.lower()
        text = re.sub("'s", ' s', text) #splitting possesion e.g. "Andy's toys" -> "Andy s toys". it helps in vocabulary coverage. gives 's'. Count Vectorizer will ignore it
        text = re.sub("'re", ' re', text)  # gives 're'. Count Vectorizer will NOT ignore it
        text = re.sub("'d", ' d', text)  # gives 'd'. Count Vectorizer will ignore it
        text = re.sub("can't", 'cannot', text)
        text = re.sub("won't", 'will not', text)
        text = re.sub("n't", ' not', text)
        text = re.sub("'ll", ' will', text)
        text = re.sub("'ve", ' have', text)
        text = re.sub("'m", ' am', text)
        text = re.sub('-',' ',text) #must include this one in next rounf !!!
        text = re.sub('\[.*?\]','',text) #get rid of words inside square brackets + sq. brackets
        text = re.sub('\(.*?\)','',text) #get rid of words inside parentheses + parentheses
        text = re.sub('[^\w\s]','',text) #get rid of punctuation
        text = re.sub('\w*\d\w*','',text) #remove digits or words containing digits
        text = re.sub('_','', text) #transcript contains this: __hello
        text = re.sub(r'\w*([a-z])\1{2,}\w*','', text) # repetitive letters aah ohhhh: you don't need \b cause it needs 3 repetitive letters together
    return text