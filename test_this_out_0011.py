#@@@@@@@@@@@  README!!!    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
# (C)Copyright  Date 2019-06-14 11:12:44                 #
# Author        Danny Chela                              #
# Notes         Delete When Finished                     #
# ScriptName    test_this_out_0011                       #
#@@@@@@@@@@@  README!!!    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#



"""
Ask The User To Guess The Password
Only Five Attempts After That Account Is Locked
Contact Administrator To Unlock Account (No Loops Are To Be Used Use Nested Else)
"""


#############################################
#        DECLARE ALL ATTRIBURTES
#############################################

did_i_guess_right=False

def eop():
    mess="THIS PROGRAM HAS ENDED....................."
    return mess

#############################################
#        MAIN STARTS HERE
#############################################

print("Enter Password:",end="")

pass_word=input()

if(pass_word=="SallyComeHome!!"):
    did_i_guess_right=True
    
    

if(did_i_guess_right):
    print("Welcome To System Linux Red Hat Log Off When You Are Finished")  #### Attempt ONE
    
else:
    print("Wrong Password Enter Password:",end="")
    pass_word=input()
    
    if(pass_word=="SallyComeHome!!"):
        did_i_guess_right=True
    
    if(did_i_guess_right):
        print("Welcome To System Linux Red Hat Log Off When You Are Finished") #### Attempt TWO
    
    else:
        print("Wrong Password Enter Password:",end="")
        pass_word=input()
    
        if(pass_word=="SallyComeHome!!"):
            did_i_guess_right=True
    
        if(did_i_guess_right):
            print("Welcome To System Linux Red Hat Log Off When You Are Finished") #### Attempt THREE
            
        else:
             print("Wrong Password Enter Password:",end="")
             pass_word=input()
    
             if(pass_word=="SallyComeHome!!"):
                 did_i_guess_right=True
    
             if(did_i_guess_right):
                 print("Welcome To System Linux Red Hat Log Off When You Are Finished") #### Attempt FOUR
                 
             else:
                 print("Wrong Password Enter Password:",end="")
                 pass_word=input()
    
                 if(pass_word=="SallyComeHome!!"):
                     did_i_guess_right=True
    
                 if(did_i_guess_right):
                     print("Welcome To System Linux Red Hat Log Off When You Are Finished") #### Attempt FIVE
                     
                 else:
                     print("After Five Attemps Your Account Is Locked Contact Your System Administrator On 07987343434")
                         
                     
#############################################
#         CALL FUNCTIONS
#############################################  


def main():
    print(eop())
    
 
main() 
              
            
            
            
        
        
        
    
    
        
     
    
    