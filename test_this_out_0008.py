#@@@@@@@@@@@@@@@@@@@@@@@@@@@ README!! @@@@@@@@@@@@@@@@@@@@@@@@@@@@
#(C)Copyright   Date 2019-06-22 17:19:14                         #
#      Author   Danny Chela                                      #
#      Notes    Delete When Finished                             #
#      Script   test_this_out_0008.py                            #
#@@@@@@@@@@@@@@@@@@@@@@@@@@@ README!! @@@@@@@@@@@@@@@@@@@@@@@@@@@@


##################################################################
#                     CREATE FUNCTIONS
##################################################################

def eop():
    display_message="THIS PROGRAM HAS NOW ENDED................."
    return display_message
    
def con():
    mess="WELL DONE EXCELLENT STUDENT!!!"
    return mess
    
        
def non_con():
    mess="NEED TO PUT MORE EFFORT INTO YOUR STUDIES!!!"
    return mess  


##################################################################
#                     DECLARE ATTRIBUTES
##################################################################

do_you_need_to_be_congratulated=False

##################################################################
#                     MAIN STARTS HERE
##################################################################

my_scores=input("Enter Your Three Scores:")   # Use Split Method To Turn String Into A List Of Numbers

num1=int(my_scores.split()[0])

num2=int(my_scores.split()[1])

num3=int(my_scores.split()[2])


avg_score=(num1+num2+num3)/3

if(avg_score>=9.2):
    do_you_need_to_be_congratulated=True
      
##################################################################
#                     CALL FUNCTIONS
##################################################################

    
if(do_you_need_to_be_congratulated):
    print(con())
else:
    print(non_con())



def main():
    print(eop())
    
    
main()

    