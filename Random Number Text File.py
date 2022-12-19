
import random     #import random library

def  randoms_to_file(n,n1,n2,filename):
    #function to generate n random numbers
    with open(filename, "w") as f: #write mode 
        for i in range(n):      
            f.write(str(random.randint(n1,n2)) + "\n")   
            
def read_file_and_process():    
    #function to read 
    while True:
        try:
            filename = input("The name of the file contaning the random number? ")
            with open(filename, "r") as f:
                random_numbers = f.readlines()  
            break
        except:
            print("File name incorrect, try again! ")  #error message
     #calculations       
    random_numbers = [int(x) for x in random_numbers]    
    maximum = max(random_numbers)           
    minimum = min(random_numbers)           
    num_of_int = len(random_numbers)        
    average = sum(random_numbers)/len(random_numbers) 
    return [minimum,maximum,num_of_int,average] #return the list of elements

def main():   #main function
    while True :    #loop function
        try:        #try block
            #inputs
            n = int(input("How many random  random numbers? ")) 
            n1 = int(input("Possible minimum random number? ")) 
            n2 = int(input("Possible maximum random number? "))
            filename = input("Filename for saving the random numbers: ")    
            break
        
        except ValueError:  #error exception
            print("Provide integer as your input!") #error message
    randoms_to_file(n,n1,n2,filename)   #call the function 
    output = read_file_and_process()
    
    #print statements
    print("The returned list is: ")   
    print(output)  
    print("That means :")   
    print("The lowest number is ",output[0],"the largest number is ",output[1]) 
    print("There are ",output[2],"number and their average is ",output[3])  
    
#main
if __name__ == "__main__":  
    main()
