#
# Name: Steven Taruc
# Student ID: 013665908
# Date (last modified): 9/21/18
# 
# Lab 0
# Section 13/14
# Purpose of Lab: Environment, Python, and Testing!
# https://polylearn.calpoly.edu/AY_2018-2019/pluginfile.php/243868/mod_resource/content/0/lab00.pdf

# Takes integer earth weight as input from input() and converts it to Mars and Jupiter weight
def weight_on_planets():
    weight = int(input("What do you weigh on earth? "))
    print("\nOn Mars you would weigh {} pounds.\nOn Jupiter you would weigh {} pounds.".format(weight*0.38, weight*2.34))
   
   
if __name__ == '__main__':
   weight_on_planets()