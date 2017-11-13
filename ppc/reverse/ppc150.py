print ("Input your flag")
flag= input ()
if (len (flag )==22 and flag [9 :3 :-1 ]=="yz4rc_"and sum ([ord (O00O0OOOOOO0O0000 )for O00O0OOOOOO0O0000 in flag ])//2==967 and ''.join ([chr (ord (OOOOOO0O0O000O0O0 )^42 )for OOOOOO0O0O000O0O0 in flag [10 :15 ]])=='uibou'and ''.join ([chr ((ord (O0OOO00OOOO0O0OO0 )-65+8 ) +ord ('a'))for O0OOO00OOOO0O0OO0 in flag [20 :14 :-1 ]])=='s'*4 +'{'*2 ):
    print ("Success")#line:5
else :#line:6
    print ("Wrong")
