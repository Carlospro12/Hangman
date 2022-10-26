import random
Words = []

def Run():
    Choose_Word()

def Choose_Word ():
    with open(r'./data.txt','r', encoding="utf-8") as data:
        for line in data:
            Words.append(line)
                  
        word = random.choice(Words)
        word = list(word)
        if '\n' in word:
            word.remove('\n')
        for i ,letra in enumerate(word):

            if letra == 'á':
                word[i]= 'a'
    
            if letra == 'é':
                word[i] = 'e'
    
            if letra == 'í':
               word[i] = 'i'

            if letra == 'ó':
                word[i] = 'o'
    
            if letra == 'ú':
                word[i] = 'u'   
    return word     

if __name__ == "__main__":
    Run()
    
  


