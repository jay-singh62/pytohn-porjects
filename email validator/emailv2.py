# thse is email validation by using regex
# a-z
# 0-9
# . and _ should be ocuur at one time
# @ only one time
# . in gmail should be at the last third or fouth position (ie.  .in , .com)

import re
# we have imported regex
# now we can add alll above conditon in varible thorugh regex

# starting in rege we have to use (^) thse symbol than we have to give range in brackets like. [a-z] than + will add another conditon \ is used to seacrh our given item item here is (._) than it will be [\._] ,after that  we add ? here qestion mark means that brakets items will be ither come in zero times or one time only  , than we write range of alphbets and numbers [a-z 0-9] than we add another conditons by using + another conditon is [@] than we use \w thse will search that @ in our gmail now we give[.] and again add \w
# and after that we give the index of (.) in curly barces {2,3} htan we use $ thse is to search (.)from right to left 
email_conditon = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"

user_email=input("write your email -")

if re.search(email_conditon,user_email):
    print("right email")
else :
    print("wrong emial")