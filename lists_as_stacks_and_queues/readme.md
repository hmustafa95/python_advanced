Exercise: Lists as Stacks and Queues Problems for exercise and homework for the Python Advanced Course @SoftUni.

1. Reverse Numbers

Write a program that reads a string with N integers from the console, separated by a single space, and reverses them using a stack. Print the reversed integers on one line, separated by a single space.

2. Stacked Queries

You have an empty stack. You will receive an integer – N. On the next N lines, you will receive queries. Each query is one of these four types:

· '1 {number}' – push the number (integer) into the stack

· '2' – delete the number at the top of the stack

· '3' – print the maximum number in the stack

· '4' – print the minimum number in the stack

It is guaranteed that each query is valid.

After you go through all the queries, print the stack from top to bottom in the following format:

"{n}, {n1}, {n2}, ... {nn}"

3. Fast Food

You have a fast-food restaurant, and the food you are offering is previously prepared.

Write a program that checks if you have enough food to serve lunch to all your customers. You also want to know who the client with the biggest order for that day is.

First, you will be given the quantity of the food you have for the day (an integer number). Next, you will be given a sequence of integers (separated by a single space), each representing the quantity of food in each order. Keep the orders in a queue.

Find the biggest order and print it. Next, you will begin servicing your clients from the first one that came. Before each order, check if you have enough food left to complete it:

· If you have, remove the order from the queue and reduce the quantity of food in the restaurant.

· Otherwise, stop serving.

Input

· On the first line, you will be given the quantity of your food - an integer in the range [0, 1000]

· On the second line, you will receive a sequence of integers, representing each order, separated by a single space

Output

· On the first line, print the quantity of the biggest order

· On the second line:

If you succeeded in servicing all your clients, print: "Orders complete".

Otherwise, print: "Orders left: {order1} {order2} .... {orderN}".

Constraints

· The input will always be valid

4. Fashion Boutique

You own a fashion boutique and receive a delivery of a huge box of clothes, represented as a sequence of integers. On the following line, you will be given an integer representing the capacity for one rack in your store.

You must arrange the clothes in the store and use the racks to hang up every piece of clothing. You start from the last piece of clothing on the top of the pile to the first one at the bottom. Use a stack for this purpose. Each piece of clothing has its value (an integer). You must sum their values while you take them out of the box:

· If the sum becomes equal to the capacity of the current rack, you must take a new one for the next clothes (if there are any left in the box).

· If the sum becomes greater than the capacity, do not hang the piece of clothing on the current rack. Take a new rack and then hang it up.

In the end, print how many racks you have used to hang up the clothes.

Input

· On the first line, you will be given a sequence of integers representing the clothes in the box, separated by a single space.

· On the second line, you will be given an integer representing the capacity of a rack.

Output

· Print the number of racks needed to hang up the clothes from the box.

Constraints

· The values of the clothes will be integers in the range [0,20]

· There will never be more than 50 clothes in a box

· The capacity will be an integer in the range [0,20]

· None of the integers from the box will be greater than the value of the capacity

5. Truck Tour

There is a circle road with N petrol pumps. The petrol pumps are numbered 0 to (N−1) (both inclusive). For each petrol pump, you will receive two pieces of information (separated by a single space):

The amount of petrol the petrol pump will give you

The distance from that petrol pump to the next petrol pump (kilometers)

You are a truck driver, and you want to go all around the circle. You know that the truck consumes 1 liter of petrol per 1 kilometer, and its tank has infinite petrol capacity

In the beginning, the tank is empty, but you start your journey at a petrol pump so you can fill it with the given amount of petrol.

Your task is to calculate the first petrol pump from where the truck will be able to complete the circle. You never miss filling its tank at a petrol pump.

Input

· On the first line, you will receive the number of petrol pumps - N

· On the next N lines, you will receive the amount of petrol that each petrol pump will give and the distance between that petrol pump and the next petrol pump, separated by a single space

Output

· An integer which will be the smallest index of a petrol pump from which you can start the tour

Constraints

· 1 ≤ N ≤ 1000001

· 1 ≤ amount of petrol, distance ≤ 1000000000

· You will always have at least one point from where the truck will be able to complete the circle

6. Balanced Parentheses

You will be given a sequence consisting of parentheses. Your job is to determine whether the expression is balanced. A sequence of parentheses is balanced if every opening parenthesis has a corresponding closing parenthesis that occurs after the former. There will be no interval symbols between the parentheses. You will be given three types of parentheses: (), {}, and [].

{[()]} - Parentheses are balanced.

(){}[] - Parentheses are balanced.

{[(])} - Parentheses are NOT balanced.

Input

· On a single line, you will receive a sequence of parentheses.

Output

· For each test case, print on a new line "YES" if the parentheses are balanced.

· Otherwise, print "NO"

Constraints

· 1 ≤ lens ≤ 1000, where the lens is the length of the sequence

· Each character of the sequence will be one of {, }, (, ), [, ]

