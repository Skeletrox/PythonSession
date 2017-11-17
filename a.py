import sys
#sys.stdout.write("installing xxx")


            
i=0
text = {'A': '.-',   'B': '-...',   'C': '-.-.', 
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
     	  'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',
        
        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.' 
        }
morse= {'..-.': 'F', '-..-': 'X',
                 '.--.': 'P', '-': 'T', '..---': '2',
                 '....-': '4', '-----': '0', '--...': '7',
                 '...-': 'V', '-.-.': 'C', '.': 'E', '.---': 'J',
                 '---': 'O', '-.-': 'K', '----.': '9', '..': 'I',
                 '.-..': 'L', '.....': '5', '...--': '3', '-.--': 'Y',
                 '-....': '6', '.--': 'W', '....': 'H', '-.': 'N', '.-.': 'R',
                 '-...': 'B', '---..': '8', '--..': 'Z', '-..': 'D', '--.-': 'Q',
                 '--.': 'G', '--': 'M', '..-': 'U', '.-': 'A', '...': 'S', '.----': '1'}
def conmorse(sub):
     sys.stdout.write(morse[sub])
        

ch=int(input("enter your choice \n1. encrypt\n2. decrypt \n"))

if(ch==1):
        strin=input("enter the string \n")
        while(i<len(strin)):
            sys.stdout.write(text[strin[i]]+" ")
            i=i+1
else:
    strin=input("enter the morse code \n")
    j=0; 
    while(i<len(strin)):
        if(strin[i]==' '):
            conmorse(strin[int(j):int(i)])
            j=i+1
        i=i+1
    if(i==len(strin) and j!=i):
        conmorse(strin[int(j):int(i)])
