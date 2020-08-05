
#@@@@@@@@@@@@@@@@@@@@@@ README!!!! @@@@@@@@@@@@@@@@@@@@@@#
#(C)Copyright Date:2019-07-18 11:17:35                   #                                       
#Author       Danny Chela                                #
#Notes        Delete When Done                           #
#Script       test_this_out_0002.py                      #
#                                                        #
#@@@@@@@@@@@@@@@@@@@@@@ README!!!! @@@@@@@@@@@@@@@@@@@@@@#


##########################################################
#                   DECLARE FUNCTIONS
##########################################################

def if_low_display_red():
    mess="STATUS RED...............WARNING........VISIT PETROL STATION"
    return mess

def if_not_low_display_green():
    mess="STATUS GREEN.......ALL OK.......CONTINUE DRIVING"
    return mess
    
def eop():
    mess="THIS PROGRAM HAS NOW ENDED............."    
    return mess

##########################################################
#                   DECLARE ATTRIBUTES
##########################################################


am_i_red=  False

am_i_green=False

fuelCapacity=145

##########################################################
#                   MAIN STARTS HERE
##########################################################


from random import randint

fuelAmount=randint(1,145)


print("Your Fuel Gauge Is Showing",fuelAmount,"Litres")

if(fuelAmount<=fuelCapacity*0.10):
    am_i_red=True
    
if(fuelAmount>fuelCapacity*0.10):
    am_i_green=True

    

if(am_i_red):
    print(if_low_display_red())
else:
    if(am_i_green):
        print(if_not_low_display_green())
    
    
##########################################################
#                   CALL FUNCTIONS
##########################################################  

def main():
    print(eop())
    
    
main()    
    
    
    
        
    
    
    
