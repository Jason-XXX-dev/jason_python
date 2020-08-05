#@@@@@@@@@@@@@@@@@@@@@@@ README @@@@@@@@@@@@@@@@@@@@@@@@#
#                                                       #
#(C)Copyright Date:2019-04-27 11:12:16                  #
#      Author Danny Chela                               #
#      Notes  Delete When Finished For Testing Purposes #
#      Script test_me_out_0002                          #
#                                                       #
#@@@@@@@@@@@@@@@@@@@@@@@@ README @@@@@@@@@@@@@@@@@@@@@@@#


############################################
#         DECLARE FUNCTIONS
############################################


def up_and_down(num):
    for i in range(10):
        print("{0:.5f}".format(num))
        num=3.7*num*(1-num)
    
    
def eop():
    mess="THIS PROGRAM HAS NOW ENDED............."
    return mess
    
    
    
############################################
#         MAIN STARTS HERE
############################################ 


print("Enter A Number Between 0 And 1:",end="")

num=eval(input())

def main():
    up_and_down(num)

############################################
#         CALL FUNCTIONS
############################################ 


main()

print()
print(eop())





      