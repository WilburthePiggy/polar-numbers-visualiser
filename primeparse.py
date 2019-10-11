# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 01:30:05 2019

@author: Alexander
"""
def main():
    f = open("prime.txt","r")
    workingline = f.read().replace("      ",",")
    workingline = workingline.replace(" \n","")
    workingline = workingline.replace("     ",",")
    workingline = workingline.replace("    ",",")
    workingline = workingline.replace("   ",",")
    workingline = workingline.replace("  ",",")
    workingline = workingline.replace(" ",",")

    f.close
    
    print(workingline)
    
    return (workingline);
    
remember = main()
g = open("clean.txt","w")
g.write(remember)
g.close

    