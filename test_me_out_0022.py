#@@@@@@@@@@@@@@@@@@@@@@ README!! @@@@@@@@@@@@@@@@@@@@@@
#(C)Copyright Date 2019-07-10 11:45:23                #
#Author       Danny Chela                             #
#Instructions Delete When Finished                    #
#Script       test_me_out_0022.py                     #
#@@@@@@@@@@@@@@@@@@@@@@ README!! @@@@@@@@@@@@@@@@@@@@@@


#######################################################
#                 CREATE FUNCTIONS
#######################################################


def eop():
    mess="THIS PROGRAM HAS ENDED................."
    return mess
    
    
    
#######################################################
#                 DECLARE ATTRIBUTES
#######################################################  

was_the_user_right=False

os_name="Sally Be Right_88"

#######################################################
#                 MAIN STARTS HERE
#######################################################



print("Enter Linux Pass Word:",end="")

the_pass=input()

if(the_pass==os_name):
    was_the_user_right=True
    
    
if( was_the_user_right):
    print("Well Done You Got It Right First Attempt")
    
else:
    print("Wrong Try Again:",end="")
    the_pass=input()
    was_the_user_right=False
    
    if(the_pass==os_name):
        was_the_user_right=True
        
    if( was_the_user_right):
        print("Well Done You Got It Right Second Attempt")
        
    else:
        print("Account Now Locked")
        
        
            
        
        
    
    
    
    
    
        
    


