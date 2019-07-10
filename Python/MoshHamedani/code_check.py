# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 18:38:34 2019

@author: ddutta8
"""
##########################################################################
###
### This file is to be used to test out various tweaking of the codes
###
##########################################################################

print(" ")
print(" ")
print(" ")
print('Testing miltiple line text printing and stopping the new line appending at the end ')
print("---------------------------------------------------------------")
print("""
The text to be printed has to be enclosed by \"""
Every line of the \"print\" function statement for a multiline statement get's printed \"as is\" in a new line
until the last \""" is encountered.
     """)
print('Sample below  :::-')
print("""
     This is a multiline
message and
   spans accross 3 lines
""", end='\t')
print("---------------------------------------------------------------")

print('The following code does not work since the multiline text is enclosed by \"" and not \""" ')
print(
"""
print(""This is a multiline
message and
   spans accross 3 lines"", end='\t')
print('again')
"""
)

# s1 = 'string1'
# s2 = 'string2'
#
#
# def expand(str1, str2):
#     loopcount = 3
#     for i in loopcount:
#         res = ''
#         res = res + str1 + str2
#
# expand(s1,s2)
