#@@@@@@@@@@@@@@@@    README!!    @@@@@@@@@@@@@@@#
#(C)Copyright :Date 2019-04-17 11:56:12         #
#Author       :Danny Chela                      #
#Instructions :Delete When Finished             #
#Script       :Displays Prime Numbers           #
#Name         :test_me_out_0002                 #
#@@@@@@@@@@@@@@@@    README!!    @@@@@@@@@@@@@@@#


###########################
# DECLARE FUNCTION
###########################

def eop():
    mess="THIS PROGRAM HAS NOW ENDED.................."
    return mess
    
    

###########################
# DECLARE ATTRIBUTES
###########################


count=0 # Number Is A Prime If It Has No Divisors Other Than 1 And Itself


###########################
#      MAIN STRATS HERE
###########################

print("Enter A Number Is It A Prime?:",end="")

your_number=eval(input())

for i in range(1,your_number+1):
    if(your_number%i==0):
        count+=1
        
        
if(count==2):
    print("{0} Is A Prime Number".format(your_number))
    
else:
    print("{0} Is Not A Prime Number".format(your_number))
    

###########################
#      CALL FUNCTIONS
########################### 

print(eop())
 
                
                