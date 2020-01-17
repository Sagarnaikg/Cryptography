'''
    This the programme which usees a concept of cryptography to secure a communication between two object in the presence of third party.
'''
def encrpto(sentence,key):

    reverseMessage=""
    temp=""
    i=len(sentence)-1

    #first layer of encryption (reversing the message)
    while i>=0 :
        reverseMessage=reverseMessage+sentence[i]
        i=i-1

    sentence=reverseMessage
    #second order encryption changing each char with another char with constant position
    for letter in sentence:
        l=ord(letter) - key
        temp=temp+chr(l)

    sentence=temp
    
    display(sentence,key)


#display function
def display(code,key):
    print("The cipher text = ")
    print(code)
    print("The private key = ")
    print(key)

    

#main func
def main():
    #user will enter the text data
    sentence=""
    sentence=input("Enter the sentence that you wanted to encrypt = ")
    p=int(input("Enter a 1st prime number = "))
    q=int(input("Enter a 2nd prime number = "))
    encrpto(sentence,p*q)

if __name__ == '__main__' :
    main()
