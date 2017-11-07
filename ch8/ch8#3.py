secret_key = {'A':'@','B':'!','C':'#','D':'%','E':'^','F':'*','G':'&','H':'+','I':'=','J':'{','K':'~','L':'`','M':'/',
              'N':'?','O':'[','P':']','Q':'6','R':'8','S':'9','T':'5','U':'1','V':'2','W':'3','X':'4','Y':'7','Z':'-',' ':'\\','.':'|'}
decode_key = {'@':'A','!':'B','#':'C','%':'D','^':'E','*':'F','&':'G','+':'H','=':'I','{':'J','~':'K','`':'L','/':'M',
              '?':'N','[':'O',']':'P','6':'Q','8':'R','9':'S','5':'T','1':'U','2':'V','3':'W','4':'X','7':'Y','-':'Z','\\':' ','|':'.'}
var = ''
def print_menu():       
    print (30 * '-' , 'MENU' , 30 * '-')
    print ('1 - Encode a Message.')
    print ('2 - Decode The Message.')
    print ('3 - Display Encoded Message.')
    print ('4 - Exit')
    print (67 * '-')
    
def encode():
    or_message = input('Please enter your sentence here:\n')
    message = or_message.upper()
    mess = list(message)
    var = ''
    global var
    for key in mess:
       if key in secret_key:
           var += secret_key[key]
    print(var)
    
def decode():
    global var
    final = ''
    mess = list(var)
    for key in mess:
       if key in decode_key:
           final += decode_key[key]
    finals = final.lower()
    print(finals)
    
while True:
    print_menu()    
    choice = int(input("Enter your choice [1-4]: "))
    
    if choice==1:     
        encode()
    elif choice==2:
         decode()
    elif choice==3:
        print(var)
    elif choice==4:
         break 
    else:
        input("Wrong option selection.")


