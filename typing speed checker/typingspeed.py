from time import *
import random as r



def mistake(partest,usertest):
     error = 0
     for i in range(len(partest)):
        try :
             if partest[i] != usertest[i] :
                 error = error + 1
        except:
            error = error + 1
     return error

def speed_time(time_S,time_e,userinput):
    time_delay = time_e -time_S

    time_r = round(time_delay,2)   
    speed = len(userinput)/time_r
    return round(speed)


while True : 
    ck =input("ready to test : yes or no : ")
    if ck =="yes" :

        
        
        test=["the black brown fox jumping over the lazy dog" , "my name is anothny gonswalis me duniya me akela hu" , "mere raske kamar tune phlinazar jab " ]
        test1= r.choice(test)
        
        print("***typing test****")
        print(test1)
        
        print()
        print()
        
        
        
        time1 = time()
        
        testinput=input("enter : ")
        
        time2= time()
        
        print("speed :", speed_time(time1,time2,testinput),"w/sec" )
        print("error: ", mistake(test1,testinput))
        
    elif  ck == "no":
            print("thank you ")
         

    else :
           print("wrong input")     