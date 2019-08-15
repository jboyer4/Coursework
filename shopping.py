#Family Knapsack
#Author: Justin Boyer
#Input: Requires the input file passed as an argument.  The input file cotnains information
#  about the itmes, family and weights. The proper format is detailed in the readme
#Output: written to results.txt
#Outside references: geeksforgeeks.org

import sys
import math

#Class table cell holds info about 2 things: 1) the optimum value for a given item number and weight combination. 
#2) The corrisponding items making up that optimum value 
class Cell:
    def __init__(self):
        self.optVal = 0
        self.itemList = ""
        

def knapsackTable(W, vList, wList):
  items = len(vList)
  #initialize table cells to -1
  valTable = [[Cell() for x in range(W+1)] for x in range(items +1)]
  
  for item in range(items+1):
    for curWeight in range(W+1):
        
        #3 cases:
        #1)Base case: if the weight is 0 or the item number is 0 then the cell has a value of 0 (Cell defaults to this)
        if item == 0 or curWeight == 0:
            pass
            #valTable[item][curWeight] = 0
        #2)Current item fits in the bag. Check if it is better with or without the new item
        #use i - 1 when getting info from the arrays to account for the 0 col in the table
        elif wList[item-1] <= curWeight:
            newVal = vList[item-1] + valTable[item-1][curWeight - wList[item-1]].optVal
            oldOpt = valTable[item-1][curWeight].optVal
            if newVal > oldOpt:
                #update the opt value
                valTable[item][curWeight].optVal = vList[item-1] + valTable[item-1][curWeight - wList[item-1]].optVal
                #update the item list
                valTable[item][curWeight].itemList = valTable[item-1][curWeight - wList[item-1]].itemList  + str(item) + " "

            #if the oldOptimum is better, just keep that
            else:
              #update the opt value
              valTable[item][curWeight].optVal = valTable[item-1][curWeight].optVal
              #update the item list
              valTable[item][curWeight].itemList = valTable[item-1][curWeight].itemList

        #3)The current item does not fit - just use the optimum value from the previous column
        else:
            #update the opt value
            valTable[item][curWeight].optVal = valTable[item-1][curWeight].optVal
            #update the item list
            valTable[item][curWeight].itemList = valTable[item-1][curWeight].itemList

       # print("ValTable[item][curWeight] ", item, curWeight)
       # print("optVal: ",  valTable[item][curWeight].optVal)
       # print("itemList: ",  valTable[item][curWeight].itemList)
       # print()

  return valTable;


def main():
  #Ensure that the input file is included
  if(len(sys.argv) < 2):
    print("Please include the file containing lists to sort as an argument")
    quit()

  #if the input file is included, continue setting up in/out files
  inFile = sys.argv[1]
  readFile = open(inFile, "r")
  writeFile = open("results.txt","w")

  #The first line is the number of test cases T where T in (1:100)
  Tcount = int(readFile.readline())
  for case in range(Tcount):
    #For each case, reinitialize the arrays to send to the knapsack function
    carryCaps = []
    itemWeight = []
    itemValue = []
    
    #for each test case, seperate the different parts
	#first get number of items
    itemCount = int(readFile.readline())
    	
    
    #Next circle through the items to build value and weight arrays
    for item in range(itemCount):
      VandW = readFile.readline()
      VandW = VandW.rstrip().split()
      itemValue.append(int(VandW[0]))
      itemWeight.append(int(VandW[1]))
  
	#After that get the number of family members
    #and add their carrying capacities to the carryCaps array
    famCount = int(readFile.readline())
    for person in range(famCount):
      carryCaps.append(int(readFile.readline()))
 
    #Arrays are filled for the current case: itemValue, item Weight, and carryCaps
    #Build the table for the item set and then get optimum solutions for each family member's carryCap
    maxWeight = max(carryCaps)
    table = knapsackTable(maxWeight, itemValue, itemWeight)
    
    #reset the max value for each case
    maxVal = 0
    indItemLists = []
    for person in range(famCount):
      #optimum value for a given family member is found with table[value][weight]
      maxVal = maxVal + table[len(itemValue)][carryCaps[person]].optVal
      indItemLists.append(table[len(itemValue)][carryCaps[person]].itemList)

    #Write Case info to file
    writeFile.write("Test Case %d \n" % (case +1))
    writeFile.write("Total Price %d \n" % (maxVal))
    writeFile.write("Member Items\n")
    count  = 1
    for i in indItemLists:
      #print(i)
      writeFile.write("   %d: " % (count))
      writeFile.write(indItemLists[count-1])
      writeFile.write("\n")
      count = count+1

    writeFile.write("\n")
    print("Case %d complete" % (case+1))
        
  writeFile.close()
  readFile.close()
  return;

main()
print("Finished")


