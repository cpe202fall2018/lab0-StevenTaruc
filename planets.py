#
# Name: Steven Taruc
# Student ID: 013665908
# Date (last modified): 9/21/18
# 
# Lab 0
# Section 13/14
# Purpose of Lab: Environment, Python, and Testing!
# Additional Comments

def weight_on_planets():
    weight = int(input())
    # print("What do you weigh on earth? {}\n\nOn Mars you would weigh {} pounds.\nOn Jupiter you would weigh {} pounds.".format(weight, weight*0.38, weight*2.34))
    print("What do you weigh on earth? \nOn Mars you would weigh {} pounds.\nOn Jupiter you would weigh {} pounds.".format(weight*0.38, weight*2.34))
    # write your code here
    # Passes Unit test. The commented out print statement matches the lab specs from polylearn

   
   
if __name__ == '__main__':
   weight_on_planets()