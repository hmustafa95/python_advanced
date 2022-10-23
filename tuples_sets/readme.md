Unique Usernames
Write a program that reads from the console a sequence of N usernames and keeps a collection only of the unique ones. On the first line, you will receive an integer N. On the next N lines, you will receive a username. Print the collection on the console (the order does not matter):
Examples

Sets of Elements
Write a program that prints a set of elements. On the first line, you will receive two numbers - n and m, separated by a single space - representing the lengths of two separate sets. On the next n + m lines, you will receive n numbers, which are the numbers in the first set, and m numbers, which are in the second set. Find all the unique elements that appear in both and print them on separate lines (the order does not matter).
For example:
Set with length n = 4: {1, 3, 5, 7}
Set with length m = 3: {3, 4, 5}
Set that contains all the elements that repeat in both sets -> {3, 5}
Examples

Periodic Table
Write a program that keeps all the unique chemical elements. On the first line, you will be given a number n - the count of input lines that you will receive. On the following n lines, you will be receiving chemical compounds separated by a single space. Your task is to print all the unique ones on separate lines (the order does not matter):
Examples

Count Symbols
Write a program that reads a text from the console and counts the occurrences of each character in it. Print the results in alphabetical (lexicographical) order.  
Examples

Longest Intersection
Write a program that finds the longest intersection. You will be given a number N. On each of the next N lines you will be given two ranges in the format: "{first_start},{first_end}-{second_start},{second_end}". You should find the intersection of these two ranges. The start and end numbers in the ranges are inclusive. 
Finally, you should find the longest intersection of all N intersections, print the numbers that are included and its length in the format: "Longest intersection is [{longest_intersection_numbers}] with length {length_longest_intersection}"
Note: in each range, there will always be an intersection. If there are two equal intersections, print the first one.
Examples

Battle of Names
You will receive a number N. On the following N lines, you will be receiving names. You should sum the ASCII values of each letter in the name and integer divide it by the number of the current row (starting from 1). Save the result to a set of either odd or even numbers, depending on if the resulting number is odd or even. After that, sum the values of each set.
If the sums of the two sets are equal, print the union of the values, separated by ", ". 
If the sum of the odd numbers is bigger than the sum of the even numbers, print the different values, separated by ", ".
If the sum of the even numbers is bigger than the sum of the odd numbers, print the symmetric-different values, separated by ", ".
NOTE: On every operation, the starting set should be the odd set
Examples



Count Same Values
You will be given numbers separated by a space. Write a program that prints the number of occurrences of each number in the format "{number} - {count} times". The number must be formatted to the first decimal point.
Examples

Students' Grades
Write a program that reads students' names and their grades and adds them to the student record.
On the first line, you will receive the number of students – N. On the following N lines, you will be receiving a student's name and their grade. For each student print all his/her grades and finally his/her average grade, formatted to the second decimal point in the format: "{student's name} -> {grade1} {grade2} ... {gradeN} (avg: {average_grade})".
The order in which we print the result does not matter.
Examples

Record Unique Names
Write a program, which will take a list of names and print only the unique names in the list.
The order in which we print the result does not matter.
Examples

Parking Lot
Write a program that:
Records a car number for every car that enters the parking lot
Removes a car number when the car leaves the parking lot
On the first line, you will receive the number of commands - N. On the following N lines, you will receive the direction and car's number in the format: "{direction}, {car_number}". The direction could only be "IN" or "OUT". Print the car numbers which are still in the parking lot. Keep in mind that all car numbers must be unique. If the parking lot is empty, print "Parking Lot is Empty".
Note: The order in which we print the result does not matter.
Examples

SoftUni Party
There is a party at SoftUni. Many guests are invited, and there are two types of them: Regular and VIP. When a guest comes, check if they exist on any of the two reservation lists.
On the first line, you will receive the number of guests – N. On the following N lines, you will be receiving their reservation codes. All reservation codes are 8 characters long, and all VIP numbers will start with a digit. Keep in mind that all reservation numbers must be unique.
After that, you will be receiving guests who came to the party until you read the "END" command.
In the end, print the number of guests who did not come to the party and their reservation numbers:
The VIP guests must be first.
Both the VIP and the Regular guests must be sorted in ascending order.
Examples

Summation Pairs
On the first line, you will receive a sequence of numbers separated by space. On the second line, you'll receive a target number. Your task is to find the pairs of numbers whose sum equals the target number. For each found pair print "{number} + {number} = {target_number}". You may NOT use the same element twice.
Can you come up with an algorithm that has less time complexity?
Examples

