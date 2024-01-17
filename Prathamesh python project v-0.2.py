#!/usr/bin/env python
# coding: utf-8

# In[10]:


def Area_of_Room():
    #Area of Room
    print("Calculate area of room")
    #ask user to width and leghth of the room
    width=float(input("Please Enter your Width here: "))
    length=float(input("Please Enter your length here: "))
    Area=width*length
    print(f"The area of room is {Area}squ feet")

def Area_of_field():
    #Famer's Area of field in acres
    print("Calculate the famer's area of field in acres")
    squ_feet=43560
    #ask user to width and length of the farmer's field
    width=float(input("Please Enter your width here: "))
    length=float(input("Please Enter your length here: "))
    acre=width*length/squ_feet
    print(f"The area of the farmer's field {round(acre,2)} acres")

def Bottle_deposit():
    #Bottle deposits
    print("Calculate the refund of the drink containers")
    less=0.10
    more=0.25
    #ask user to the drink containers of the which is less than one liter and more thna n one liter
    less1=int(input("please Enter the drink containers less than 1 liter or eqauol to on eliter do you have?"))
    more1=int(input("Please Enter the drink containers more than liter which do you have"))
    refund=less*less1+more*more1
    print(f"The refund amount is in ${round(refund,2)}%")

def Tax_and_Tip():    
    #Tax and tip
    print("Calculate tha Tax and tip of the total meal")
    tax=0.05
    tip=0.18
    #now ask user to the Enter the amount of meal
    amount=int(input("Please Enter your meal amount here: "))
    tax1=amount*tax
    tip1=amount*tip
    total=amount+tax1+tip1
    print(f"The Tax amount of the meal is {tax1} \nThe tip amount of the meal is {tip1} \n The total amount of the meal is {total}")

def Sum_of_first_n_positive_integers():
    #Sum of the first n positive integers
    print("Calculate the sum of first n positive integers")
    n=int(input("Please Enter your input here:"))
    #now we have formula to calculate sum of the first n positive inte=gers
    sum1=n*(n+1)/2
    print(f"The sum of the first n positive integers is {round(sum1)}")

def widgets_and_gizoms():
    #Widgets and gizoms
    print("Calculare the total weight of the order")
    widgets=75
    gizmos=112
    #ask user to take inputs of widgets and gizmos
    widgets1=int(input("Please Enter your widgets here: "))
    gizmos1=int(input("Please Enter your gizmos here: "))
    a=widgets*widgets
    b=gizmos*gizmos1
    total=a+b
    print(f"The total weight of the order is {total}gm")

def compound_intrest():
    #compound intrest
    print("calculare the compound intrest")
    initial_deposit=float(input("Please Enter initial deposit amount: "))
    #set the intrest rate
    intrest_rate=0.4
    #set the number of years
    years=3
    #calculate and display the saving balalnce for 1,2 and 3 years
    for year in range(1,1+years):
        intrest=initial_deposit+intrest_rate/100
        initial_deposit+=intrest
        print(f"After {year} years,the saving account balance is:Rs.{initial_deposit:.2f}")

def Even_and_odd():
    #Even and odd numbers
    print("WElcome to the choice the number even or odd bot!")
    num=int(input("Please Enter your number here: "))
    if (num%2)==0:
        print("This number is even")
    else:
        print("This number is odd")

def vowel_or_constants():
    #vowels or constants
    print("Welcome to the show the vowels or constants in a alphabets ")
    letter=input("Please Enter your alphabet here: ")
    if letter=="a" or letter=="e" or letter=="i" or letter=="o" or letter=="u":
        print("Vowel")
    else:
        print("constant")

def letter_grade_to_grade_points():
    #letters grade to grade points
    A=4.0
    A_PLUS=4.0
    A_MINUS=3.7
    B_PLUS=3.3
    B=3.0
    B_MINUS=2.7
    C_PLUS=2.3
    C=2.0
    C_MINUS=1.7
    D_PLUS=1.3
    D=1.0
    F=0
    letter=input("Please enter your Grade here: ")
    letter=letter.upper()
    if letter=="A" or letter=="A+":
        print(f"The grade of letter A+ is {A}")
    elif letter=="A-":
        print(f"The grade of letter A- is {A_MINUS}")

    elif letter=="B+":
        print(f"The grade of letter B+ is {B_plus}")
    elif letter=="B":
        print(f"The grade of letter B is {B}")
    elif letter=="B-":
        print(f"The grade of letter B- is {B_MINUS}")
    elif letter=="C+":
        print(f"The grade of letter C+ is {C_PLUS}")
    elif letter=="C":
        print(f"The grade of letter C is {c}")
    elif letter=="C-":
        print(f"The grade of letter c- is {c_MINUS}")
    elif letter=="D":
        print(f"The grade of letter D is {D}")
    elif letter=="D+":
        print(f"The grade of letter D+  is {D_PLUS}")
    elif letter=="F":
        print(f"The grade of letter F is {F}")
    else:
        print("Invalid Grade")



def identify_triangle():

    #Name that triangle
    print("Classify the triangle as per their length")
    len1=int(input("Please Enter your length here: "))
    len2=int(input("Please Enter your length here: "))
    len3=int(input("Please Enter your length here: "))
    if len1==len2==len3:
        print("This triangle is equilateral triangle")
    elif len1!=len2==len3 or len1==len2!=len3:
        print("This triangle is isosceles triangle")
    else:
        print("This triangle is scalene triangle")


# In[ ]:





# In[12]:


#importing tkinter library
import tkinter as tk
#creating main window
window=tk.Tk()
#change the title
window.title("Prathamesh Palve")
#Size 
window.geometry("750x550")
#label
tk.Label(window,text="Python Project",font=("helvetics",21),bg="black",fg="white").place(x=270,y=50)
tk.Label(window,text="Made by:Prathamesh",font=("helvetics",18,'bold')).place(x=240,y=100)
#Button
tk.Button(window,text="Area_of_Room",command=Area_of_Room).place(x=50,y=150,width=220,height=25)
tk.Button(window,text="Area_of_field",command=Area_of_field).place(x=270,y=150,width=220,height=25)
tk.Button(window,text="Bottle_deposit",command=Bottle_deposit).place(x=490,y=150,width=220,height=25)
tk.Button(window,text="Tax_and_Tip",command=Tax_and_Tip).place(x=50,y=200,width=220,height=25)
tk.Button(window,text="Sum_of_the_first_n_positive_integers",command=Sum_of_first_n_positive_integers).place(x=270,y=200,width=220,height=25)
tk.Button(window,text="widgets_and_gizoms",command=widgets_and_gizoms).place(x=490,y=200,width=220,height=25)
tk.Button(window,text="compound_intrest",command=compound_intrest).place(x=50,y=250,width=220,height=25)
tk.Button(window,text="Even_and_odd",command=Even_and_odd).place(x=270,y=250,width=220,height=25)
tk.Button(window,text="vowel_or_constants",command=vowel_or_constants).place(x=490,y=250,width=220,height=25)
tk.Button(window,text="letter_grade_to_grade_points",command=letter_grade_to_grade_points).place(x=50,y=300,width=220,height=25)
tk.Button(window,text="identify_triangle",command=identify_triangle).place(x=270,y=300,width=220,height=25)


#this is necessary to write
window.mainloop()


# In[ ]:





# In[ ]:




