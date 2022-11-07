import colorama 
from colorama import Fore 
def encryption(txt:str): 
    l= len(txt)
    print('  hi, this is a Encrypter ')
    a= input('choose a symbol to encrypt  a msg: 1. * \n 2.# \n 3.^  4. random or type r  ')
    if a ==" *" : 
        print ( Fore.GREEN , 'your encrypted msg is ' , l * ' * '   )
    elif a ==" #" : 
        print ( Fore.RED, 'your encrypted msg is ' , l * ' # '   )
    elif a ==" ^ " : 
        print ( Fore.CYAN  , 'your encrypted msg is ' , l * '^  '   )
    elif a == 'random' or a== 'r': 
        lk= l // 2 
        print(Fore.BLACK, 'your encrpteed msg is  ' , lk * '@%'  )
    else :
        print('invalid input : ')
if __name__== '__main__ ': 
    s= str(input('enter your text : '))
    print(encryption(s))
    