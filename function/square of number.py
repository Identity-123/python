# Define a function
def square(x):
    return x ** 2


# Create a list of numbers
numbers = [1, 2, 3, 4, 5]

# Use map() to apply the square function to each element in the list
squared_numbers = map(square, numbers)
# inside variable x I wrote what we have done one line 10
x = ''' 
  map(square, numbers): This is using the map() function. The map() function takes two arguments - a function 
  (square in this case) and an iterable (numbers in this case). It applies the specified function (square)
   to each item in the iterable (numbers), producing an iterator of the results.
 '''

result_list = list(squared_numbers)
# Convert the result to a list (since map() returns an iterable)

print(result_list)