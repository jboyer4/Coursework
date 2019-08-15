Readme shopping.py
Author: Justin Boyer
Last edit: 7/15/19

This program uses the knapsack dynamic programing algorithm
to determine the optimum carry load for each member of a family
out shopping.

**How to run:
python3 shopping.py shopping.txt

**Input:
The input file is passed as an argument in the command line (shopping.txt)
The formating description from the assignment reads as follows:
T (1 ≤ T ≤ 100) is given on the first line of the input file.

	* Each test case begins with a line containing a single integer number N that indicates the number
	of items (1 ≤ N ≤ 100) in that test case
	
	* Followed by N lines, each containing two integers: P and W. The first integer (1 ≤ P ≤ 5000)
	corresponds to the price of object and the second integer (1 ≤ W ≤ 100) corresponds to the
	weight of object.

	*The next line contains one integer (1 ≤ F ≤ 30) which is the number of people in that family.
	
	* The next F lines contains the maximum weight (1 ≤ M ≤ 200) that can be carried by the i
	th person in the family (1 ≤ i ≤ F).

Sample Input
2
3
72 17
44 23
31 24
1
26
6
64 26
85 22
52 4
99 18
39 13
54 9
4
23
20
20
36

**Output: output is written to a file call results.txt.
From the assignement description:
    For each test case your program should output the
	maximum total price of all goods that the family can carry out during their shopping spree and for each
	the family member, numbered 1 ≤ i ≤ F, list the item numbers 1 ≤ N ≤ 100 that they should select. 

Sample Output:
Test Case 1
Total Price 72
Member Items
 1: 1

Test Case 2
Total Price 568
Member Items
 1: 3 4
 2: 3 6
 3: 3 6
 4: 3 4 6
