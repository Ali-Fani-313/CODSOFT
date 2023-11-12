# Task 1 (Design a simple Calculator)
Continue=1
while (Continue==1):
  op_selction = int (input (print ("Which operation do you want to perform : \n 1 for additon\n 2 for substraction \n 3 for division \n 4 for multiply")))

  if op_selction==1:
    print ("<<<<<<<addition>>>>>>>>>\n")
    idx= int(input("how many numbers do you want to add :"))
    lst=[]
   
    for i in range (idx):
         elem= float(input("Please enter the {}st Number : ".format(i+1)))
         lst.append(elem)

    total=float(0)  
    for num in lst:
         total=num+total
    print("The Sum of all Numbers is : " , total)     

  if op_selction==2:
     print("<<<<<<Substraction>>>>>>> \n")
     main_num = float(input(print("Please enter a Number from which you will subtract : " )))

     idx=int(input("How many numbers do you want to SUBSTRACT from it : "))
     lst=[]
     for i in range(idx):
         elem= float(input("Please enter the {}st Number : ".format(i+1)))
         lst.append(elem)
        
     after_sub= main_num
     for num in lst:
          after_sub=main_num-num
    
     print("After Substraction : ", after_sub)

  if op_selction==3:
     print("<<<<<<<<Division>>>>>>\n")
     dividend=float(input("Enter the number which is to be divided : "))
     divisor= float(input("Enter the number which is the divisor : "))
     quotient= float(dividend/divisor)
     reminder=float(dividend % divisor)
     print ("The Quotient is : " , quotient)
     print("The Reminder is : ", reminder)
                
  if op_selction==4:
     print("<<<<<<<<<Mutiplication>>>>>>>>>\n")
     idx=int(input("How many numbers do you want to multiply togather : "))
     lst=[]
     for i in range(idx):
        num=float(input("Enter the {}st Number : ".format(i+1)))
        lst.append(num)

     net_multiple= float(1)

     for num in lst:
        net_multiple=num*net_multiple

     print("The net multiple is : " , net_multiple)


     Continue=int (input(" <<<<<<< Press 1 for another Calculation >>>>>> : "))
                
                    

      
     
     
    