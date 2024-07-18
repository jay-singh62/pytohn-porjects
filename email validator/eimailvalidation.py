# in these we our going to check the following condition of our emails 
# 1 is that our email should not be less than 6 characters 
# 2 nd is that our fist inedx or charater of our email should be alphabet
# 3  is thers should be @ is ther in our gmail and only one @ is there
# 4 there shuld be . at the place of 3rd  and 4th from the last of email

email= input("enter your gmail -")
k=0
j=0
d=0
if len(email)>=6:
    if email[0].isalpha():
        if ("@" in email )and (email.count("@")==1):
            if (email[-4]==".")^(email[-3]=="."):
                 for i in email:
                      if i==i.isspace():
                          k=1
                      elif i.isalpha():
                           if i==i.upper():
                                 j=1        
                      elif i.isdigit():
                          continue
                      elif i=="_" or i=="." or i=="@":
                          continue
                      else:
                          d=1
                        


                 if k==1 or j==1 or d==1: 
                     print("wrong email 5")   
                 else:
                     print("right email")          
            else:
                print("wrong emial 4")

        else:
            print ("wrong email 3")

    else :
        print("wront email 2")
else :
   print ("wrong email 1")
