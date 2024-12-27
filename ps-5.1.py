my_dict = { "aam":"mango" , "baal":"hair","phool":"flowers","lakdi":"stick"}
a = int(input("do you wat to check the dicionary ? if yes enter 1 orelse enter 0 !"))
if a==1 :
    key =str(input("enter the key you want o search :"))
    value = my_dict.get(key)
    if value == None :
        print("I dont know!!")
    else :
        print(f"The value for {key} is {value}")
elif a==0 :
    print("THANK YOU!!")            