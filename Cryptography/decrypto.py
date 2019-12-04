

def decrpto(result,key):
   
    end_string = ""

    #second layer encryption
    for letter in result:
            l=ord(letter)+key
            l=chr(l)
            end_string=end_string+l
    
    display(end_string)

def display(message):

    reverseMessage = ""

    #firstlayer encryption
    i=len(message)-1
    while i>=0 :
        reverseMessage=reverseMessage+message[i]
        i=i-1

    message=reverseMessage

    print("Your decrpted message = ")
    print(message)

def main():
    result =" "
    result=input("Enter the code data = ")
    key=int(input("Enter the private key = "))
    decrpto(result,key)

if __name__ == '__main__' :
    main()