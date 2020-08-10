
import numpy as np
a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])

# 1. How many negative numbers are there?

len(a[a < 0])

# 2. How many positive numbers are there?

len(a[a > 0])

# 3. How many even positive numbers are there?

a = a[a > 0]
a = a[a % 2 == 0]
print(len(a))

#Even Numbers
(a % 2 == 0)
#Positive Numbers
(a > 0)
#Even and Positive
a[(a % 2 == 0) & (a > 0)]
#Count(shape) Even and Positive
a[(a % 2 == 0) & (a > 0)].shape

# 4. If you were to add 3 to each data point, how many positive numbers would there be?

a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])
a = a + 3
a = a[a > 0]
print(len(a))


# 5. If you squared each number, what would the new mean and standard deviation be?

a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])
a.mean()
a.std()
a = a ** 2
a
a.mean()
a.std()

# 6. A common statistical operation on a dataset is centering. This means to adjust the data such that the center of the data is at 0. 
#    This is done by subtracting the mean from each data point. Center the data set.

a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])
result = a - int(a.mean())
result

# 7. Calculate the z-score for each data point. Recall that the z-score is given by:
#     Z = (x - mean ) / SD

a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])
z_score = ((a - a.mean()) / a.std())
z_score

#8. More Numpy Exercises - Part 1

import numpy as np

## Setup 1
# Life w/o numpy to life with numpy
aa = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Use python's built in functionality/operators to determine the following:
# Exercise 1 - Make a variable called sum_of_a to hold the sum of all the numbers in above list

# sum_of_a = a.sum()
# sum_of_a

total = 0
for n in aa:
    total += n
sum_of_a = total
print(sum_of_a)

# Exercise 2 - Make a variable named min_of_a to hold the minimum of all the numbers in the above list

# min_of_a = a.min()
# min_of_a

a.sort()
min_of_a = a[0]
print(min_of_a)

# Exercise 3 - Make a variable named max_of_a to hold the max number of all the numbers in the above list

# max_of_a = a.max()
# max_of_a

max_of_a = max(a)

# Exercise 4 - Make a variable named mean_of_a to hold the average of all the numbers in the above list

# mean_of_a = a.mean()
# mean_of_a

mean_of_a = (sum_of_a /len(a))
print(mean_of_a)

# Exercise 5 - Make a variable named product_of_a to hold the product of multiplying all the numbers in the above list together

# product_of_a = a.prod()
# product_of_a

total = 1
for n in aa:
    total *= n
product_of_a = total
print(product_of_a)


# Exercise 6 - Make a variable named squares_of_a. It should hold each number in a squared like [1, 4, 9, 16, 25...]

# squares_of_a = np.square(a)
# squares_of_a

squares_of_a = [(n ** 2) for n in aa]
print(squares_of_a)

# Exercise 7 - Make a variable named odds_in_a. It should hold only the odd numbers

# odds_in_a = a[a % 2 != 0]
# odds_in_a

oddlist = [] 
for n in aa: 
    if (n % 2 != 0): 
         oddlist.append(n) 
    odds_in_a = oddlist
print(oddlist)

# Exercise 8 - Make a variable named evens_in_a. It should hold only the evens.

# evens_in_a = a[a % 2 == 0]
# evens_in_a

evenlist = [] 
for n in aa: 
    if (n % 2 == 0): 
         evenlist.append(n) 
    even_in_a = evenlist
print(evenlist)

## What about life in two dimensions? A list of lists is matrix, a table, a spreadsheet, a chessboard...
## Setup 2: Consider what it would take to find the sum, min, max, average, sum, product, and list of squares for this list of two lists.

b = np.array([[3, 4, 5],
              [6, 7, 8]])
b

# Exercise 1 - refactor the following to use numpy. Use sum_of_b as the variable. 
#              **Hint, you'll first need to make sure that the "b" variable is a numpy array**

sum_of_b = 0
for row in b:
    sum_of_b += sum(row)
print(sum_of_b)

sum_of_b = b.sum()
sum_of_b

# Exercise 2 - refactor the following to use numpy. 

min_of_b = min(b[0]) if min(b[0]) <= min(b[1]) else min(b[1])
min_of_b  

min_of_b = b.min()
min_of_b

# Exercise 3 - refactor the following maximum calculation to find the answer with numpy.

max_of_b = max(b[0]) if max(b[0]) >= max(b[1]) else max(b[1])
max_of_b

max_of_b = b.max()
max_of_b

# Exercise 4 - refactor the following using numpy to find the mean of b

mean_of_b = (sum(b[0]) + sum(b[1])) / (len(b[0]) + len(b[1]))
mean_of_b

mean_of_b = b.mean()
mean_of_b

# Exercise 5 - refactor the following to use numpy for calculating the product of all numbers multiplied together.

product_of_b = 1
for row in b:
    for number in row:
        product_of_b *= number
product_of_b 

product_of_b = b.prod()
product_of_b 

# Exercise 6 - refactor the following to use numpy to find the list of squares 

squares_of_b = []
for row in b:
    for number in row:
        squares_of_b.append(number**2)
squares_of_b

squares_of_b = np.square(b)
squares_of_b

# Exercise 7 - refactor using numpy to determine the odds_in_b

odds_in_b = []
for row in b:
    for number in row:
        if(number % 2 != 0):
            odds_in_b.append(number)
odds_in_b 

odds_in_b = b[b % 2 != 0]
odds_in_b 

# Exercise 8 - refactor the following to use numpy to filter only the even numbers

evens_in_b = []
for row in b:
    for number in row:
        if(number % 2 == 0):
            evens_in_b.append(number)
evens_in_b 

evens_in_b = b[b % 2 == 0]
evens_in_b 

# Exercise 9 - print out the shape of the array b.

print(np.shape(b))

# Exercise 10 - transpose the array b.

np.transpose(b)

# Exercise 11 - reshape the array b to be a single list of 6 numbers. (1 x 6)

b = np.reshape(np.ravel(b), (1, 6))
b

# Exercise 12 - reshape the array b to be a list of 6 lists, each containing only 1 number (6 x 1)

b = np.reshape(np.ravel(b), (6, 1))
b

## Setup 3
c = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])
c

# HINT, you'll first need to make sure that the "c" variable is a numpy array prior to using numpy array methods.
# Exercise 1 - Find the min, max, sum, and product of c.

min_val = c.min()
max_val = c.max()
sum_val = c.sum()
product = np.product(c)
print(f"\n Minimum C Value: {min_val}\n Maximum C Value: {max_val}\n Sum Value of C: {sum_val}\n Total Product of C: {product}")

# Exercise 2 - Determine the standard deviation of c.

std_c = c.std()
std_c

# Exercise 3 - Determine the variance of c.

var_c = np.var(c)
var_c

# Exercise 4 - Print out the shape of the array c

print(np.shape(c))

# Exercise 5 - Transpose c and print out transposed result.
t_c = np.transpose(c)
print(t_c)

# Exercise 6 - Get the dot product of the array c with c. 

dot_product = np.dot(c,t_c)
dot_product

# Exercise 7 - Write the code necessary to sum up the result of c times c transposed. Answer should be 261

(c * t_c).sum()

# Exercise 8 - Write the code necessary to determine the product of c times c transposed. Answer should be 131681894400.

## Setup 4
d = [
    [90, 30, 45, 0, 120, 180],
    [45, -90, -30, 270, 90, 0],
    [60, 45, -45, 90, -45, 180]
]

# Exercise 1 - Find the sine of all the numbers in d

# Exercise 2 - Find the cosine of all the numbers in d

# Exercise 3 - Find the tangent of all the numbers in d

# Exercise 4 - Find all the negative numbers in d

# Exercise 5 - Find all the positive numbers in d

# Exercise 6 - Return an array of only the unique numbers in d.

# Exercise 7 - Determine how many unique numbers there are in d.

# Exercise 8 - Print out the shape of d.

# Exercise 9 - Transpose and then print out the shape of d.

# Exercise 10 - Reshape d into an array of 9 x 2


