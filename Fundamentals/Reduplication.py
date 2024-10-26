#Bryan Chora 9/25/2024 Kattis: Reduplication

'''
This function will reduplicate the same string and return it 
param: the word to be repeated, the n times no be repeated
return: (string) newString : this is the new string created after reduplication
'''
def reduplication(string,times):
    #Initileze new string
    newString = ""

    #This will replicate the n times
    for _ in range(times):
        newString += string

    #Return the new string   
    return newString


#This program will repeat the same string in n times as a single string
def main():
    #string: the word to be repeated
    word = input()
  
    #int : the n times to repeat
    n = int(input())

    #Check if there is any reduplication possible
    if n > 0 and word != "":
        #if is possible print the reduplication
        print(reduplication(word,n))
    else:
        #otherwise print empty
        print('')
#execute main program
main()