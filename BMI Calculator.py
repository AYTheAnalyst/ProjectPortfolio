#!/usr/bin/env python
# coding: utf-8

# # BMI Calculator

# In[9]:


Name = input("Enter your Name: ")

Weight = int(input("Please enter your weight in kilograms: "))

Height = int(input("Please enter your height in inches: "))

BMI = (((Weight * 2.205) * 703)/ (Height * Height))

print(round(BMI))

if BMI>0:
    if (BMI<18.5):
        print(Name +" You are underwight, please eat some food asap.")
    elif (BMI<= 24.9):
        print(Name +" You are normal weight, keep up the good work.")
    elif (BMI<= 29.9):
        print(Name +" You are over weight, get off the damn couch and start exercising.")   
    elif (BMI<= 34.9):
        print(Name +" You are obese, enough with the chips already.")
    elif (BMI<= 39.9):
        print(Name +" You are severly obese, stop eating right away and go for a walk.")
    else:
        print(Name +" You are morbidly obese, if you dont stop eating now you will die soon.")
        
else:
    print("Enter Valid Input")


# In[ ]:



    
        


# In[ ]:




