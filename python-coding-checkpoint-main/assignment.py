# Name: Kathy Nguyen
# Period: PM
# Python Skills Check — Slides 1–60

# ============================================================
# DIRECTIONS
# ============================================================
# - I recommend you create a repo first and clone it.
# - Drag this folder into your repo and then push when you are done.
#
#
# Complete each task underneath its directions.
# 
#
# RULES:
# - Use ONLY concepts we have learned in class.
# - Use the EXACT variable names provided.
# - Do not delete the directions.
# - Your entire Python file must run without errors.
# - Do NOT manually type an answer that Python should calculate.
# - Read carefully. Some questions are intentionally tricky.


# ============================================================
# SECTION 1 — COMMENTS & PRINTING
# ============================================================

# TASK 1:
# Below this comment, write a SINGLE-LINE comment that says:
# This is my first comment
# This is my first comment



# TASK 2:
# Below, use print() to display:
print("Python Skills Check")
# Python Skills Check
#
# Make sure Python treats the words as text.



# TASK 3:
# Write THREE separate print() statements.
#
# Print:
print("Kathy")
print("Poke")
print("5")
# Your first name
# Your favorite food
# A number between 1 and 100
#
# IMPORTANT:
# The first two should be text.
# The third should be a number.



# ============================================================
# SECTION 2 — CREATING VARIABLES
# ============================================================

# TASK 4:
# Below, create a variable named:
student_name = "Kathy"
# student_name
#
# Store YOUR name inside the variable.



# TASK 5:
# Create a variable named:
#
# student_age
student_age = int(17)
# Store your age as an INTEGER.
#
# Do NOT put quotation marks around the value.



# TASK 6:
# Create a variable named:
account_balance = float(125.75)
# account_balance
#
# Give it the value:
#
# 125.75
#
# Think about what type of data this is.



# TASK 7:
# Create a variable named:
#
# is_learning_python
is_learning_python = True
# Store the Boolean value True inside it.
#
# Be careful with capitalization and quotation marks.



# TASK 8:
# Print all FOUR variables you created in Tasks 4–7.
#
# Use four separate print() statements.
print(student_name)
print(student_age)
print(account_balance)
print(is_learning_python)
# IMPORTANT:
# Print the VALUES stored in the variables,
# not the names of the variables.



# ============================================================
# SECTION 3 — DATA TYPES
# ============================================================

# TASK 9:
# Create these FOUR variables:
#
# whole_number
# decimal_number
# message
# answer
whole_number = int(8)
decimal_number = float(3.1415)
message = "yoohoo"
answer = False
# Store a DIFFERENT type of data in each:
#
# whole_number should store an Integer.
# decimal_number should store a decimal.
# message should store a String.
# answer should store a Boolean.
#
# You choose the values.



# TASK 10:
# Create a variable named:
#
# tricky_number
tricky_number = "500"
# Store:
#
# "500"
#
# EXACTLY as shown above.
#
# THINK:
# Is tricky_number storing a number that Python can currently
# perform arithmetic with, or is it storing a String?



# TASK 11:
# Print tricky_number.
print(tricky_number)
actual_number = int(500)
print(actual_number)
# Then, directly underneath it, create another variable named:
#
# actual_number
#
# Store the INTEGER 500 inside actual_number.
#
# Print actual_number.
#
# The output may look similar, but the two variables
# should NOT contain the same data type.



# ============================================================
# SECTION 4 — ARITHMETIC WITH VARIABLES
# ============================================================

# TASK 12:
# Create:
#
# number_one = 45
# number_two = 17
number_one = 45
number_two = 17
# Create another variable named:
total = number_one + number_two
# total
#
# Use number_one and number_two to calculate their sum.
#
# Do NOT write:
#
# total = 62
#
# Python must perform the calculation.



# TASK 13:
# Using the SAME number_one and number_two variables,
# create:
#
# difference
difference = number_one - number_two
# Store the result of subtracting number_two
# from number_one.



# TASK 14:
# Using the SAME variables again, create:
#
# product
product = number_one * number_two
# Store the result of multiplying the two numbers.



# TASK 15:
# Using the SAME variables again, create:
#
# quotient
quotient = number_one/number_two
# Store the result of dividing number_one by number_two.



# TASK 16:
# Print:
print(total)
print(difference)
print(product)
print(quotient)
# total
# difference
# product
# quotient
#
# Use four separate print statements.



# ============================================================
# SECTION 5 — CALCULATIONS THAT REQUIRE THINKING
# ============================================================

# TASK 17:
# Create:
#
# price = 14
# quantity = 7
price = 14
quantity = 14
# Create:
purchase_total = price * quantity
# purchase_total
#
# Determine what arithmetic operation should be used
# to calculate the cost of buying 7 items.
#
# Do NOT manually type the answer.



# TASK 18:
# Create:
#
# money = 500
# people = 8
#
# Create:
#
# money_per_person
money = 500
people = 8
money_per_person = money/people
# Imagine the money is divided equally between everyone.
#
# Determine the correct calculation yourself.



# TASK 19:
# Create:
#
# starting_balance = 850
# amount_spent = 237
starting_balance = 850
amount_spent = 237
remaining_balance = starting_balance - amount_spent
# Create:
#
# remaining_balance
#
# Determine how much money remains.
#
# Use the variables in your calculation.



# TASK 20:
# Create:
#
# boxes = 12
# items_per_box = 24
boxes = 12
items_per_box = 24
total_items = boxes * items_per_box
# Create:
#
# total_items
#
# Calculate the total number of items.
#
# Do NOT manually calculate the answer.



# ============================================================
# SECTION 6 — REUSING VARIABLES
# ============================================================

# TASK 21:
# Create:
#
# hourly_pay = 20
# hours_worked = 8
#
# Create:
#
# daily_pay
hourly_pay = 20
hours_worked = 8
daily_pay = hourly_pay * hours_worked
# Calculate one day's pay.



# TASK 22:
# Now create:
#
# weekly_pay
weekly_pay = 5 * daily_pay
# Assume the person works 5 days.
#
# REQUIREMENT:
# You MUST use daily_pay in your calculation.
#
# Do NOT redo the calculation from Task 21.



# TASK 23:
# Create:
#
# monthly_pay
#
# For this question, assume there are 4 work weeks
# in a month.
#
# REQUIREMENT:
# Use weekly_pay.
monthly_pay = 4 * weekly_pay
# Do NOT use hourly_pay or hours_worked in this calculation.



# TASK 24:
# Create:
#
# yearly_pay
#
# For this question, assume there are 12 months in a year.
yearly_pay = 12 * monthly_pay
# REQUIREMENT:
# Your calculation may ONLY use:
#
# monthly_pay
#
# and one number.



# ============================================================
# SECTION 7 — STRINGS
# ============================================================

# TASK 25:
# Create:
first_name = "Kathy"
last_name = "Nguyen"
# first_name
# last_name
#
# Store your first and last name as Strings.



# TASK 26:
# Create:
#
# full_name
full_name = first_name + " " + last_name
# Combine first_name and last_name together.
#
# There MUST be a space between the names.
#
# REQUIREMENT:
# Use the two variables.
#
# Do NOT manually type your full name again.



# TASK 27:
# Print full_name.
print(full_name)


# TASK 28:
# Create:
#
# word_one = "Python"
# word_two = "Programming"
#
# Create:
word_one = "Python"
word_two = "Programming"
course_name = word_one + " " + word_two
# course_name
#
# Combine the two variables so the result displays:
#
# Python Programming
#
# You may NOT manually type "Python Programming"
# into course_name.



# ============================================================
# SECTION 8 — USER INPUT
# ============================================================

# TASK 29:
# Create:
#
# user_name
user_name = input("What is your username?: ")
# Ask the user to enter their name.
#
# Store their answer inside user_name.



# TASK 30:
# Print a message that says:
#
# Hello [their name]

print("Hello,", user_name)
# REQUIREMENT:
# Use user_name.
#
# The program must work no matter what name is entered.



# TASK 31:
# Create:
#
# favorite_food
favorite_food = input("What is your favorite food?: ")
# Ask the user for their favorite food.



# TASK 32:
# Create a personalized message using:
#
# user_name
# favorite_food
#
# Your output should use BOTH answers.
print(user_name + " " + "enjoys eating" + " " + favorite_food)
# Example idea:
#
# Alex likes pizza.
#
# Do NOT manually type the user's answers.



# ============================================================
# SECTION 9 — INPUT + DATA CONVERSION
# ============================================================

# TASK 33:
# Ask the user:
#
# How old are you?
#
# Store the answer inside:
user_age =  int(input("How old are you?: "))
# user_age
#
# IMPORTANT:
# You are going to perform arithmetic with this value.
#
# Remember that input() gives you a String.
# Figure out what conversion is needed.



# TASK 34:
# Create:
#
# age_next_year
#
# Calculate how old the user will be next year.
age_next_year = user_age + 1
# REQUIREMENT:
# Use user_age.
#
# Do NOT ask for their age again.



# TASK 35:
# Create:
#
# age_in_ten_years
age_in_ten_years = user_age + 10
# Calculate how old the SAME user will be 10 years from now.
#
# Do NOT ask another question.



# ============================================================
# SECTION 10 — MULTIPLE USER INPUTS
# ============================================================

# TASK 36:
# Ask the user to enter a whole number.
#
# Store it inside:
first_user_number = int(input("Enter in a whole number: "))
# first_user_number
#
# Make sure Python can perform arithmetic with it.



# TASK 37:
# Ask the user for another whole number.

second_user_number = int(input("Enter in another whole number: "))
# Store it inside:
#
# second_user_number



# TASK 38:
# Using ONLY those two variables, create:
#
# user_sum
# user_difference
# user_product
# user_quotient
user_sum = first_user_number + second_user_number
user_difference = first_user_number - second_user_number
user_product = first_user_number * second_user_number
user_quotient = first_user_number/second_user_number
#
# Each variable should contain the result of a
# DIFFERENT arithmetic operation.



# TASK 39:
# Print all four answers.
print(user_sum)
print(user_difference)
print(user_product)
print(user_quotient)

# Your program must work with different numbers entered
# by different users.



# ============================================================
# SECTION 11 — HARDER MULTI-STEP CALCULATIONS
# ============================================================

# TASK 40:
# Ask the user how many hours they work in ONE day.
#
# Store the answer in:
work_hours = int(input("How many hours do you work in ONE day?: "))
# work_hours



# TASK 41:
# Ask the user how much money they earn PER HOUR.
#
# Store the answer in:
hourly_rate = float(input("How much do you earn per hour?: $"))
# hourly_rate
#
# THINK:
# A pay rate could contain cents.



# TASK 42:
# Create:
#
# one_day_pay
one_day_pay = hourly_rate * work_hours
# Calculate how much the person earns in one day.



# TASK 43:
# Create:
#
# five_day_pay
five_day_pay = one_day_pay * 5
# Calculate how much the person earns after working
# five days.
#
# REQUIREMENT:
# Use one_day_pay.
#
# Do NOT repeat your previous calculation.



# TASK 44:
# Create:
#
# money_after_spending
money_after_spending = float(input("How much money did you spend?: $"))

# Ask the user how much money they spent.
current_money = five_day_pay - money_after_spending
# Subtract that amount from five_day_pay.
#
# You will need to decide whether another variable
# is necessary before you can perform the calculation.



# ============================================================
# SECTION 12 — REVERSE THINKING
# ============================================================

# TASK 45:
# Create:
#
# total_cost = 360
# number_of_items = 12
total_cost = 360
number_of_items = 12
# Create:
#
# cost_per_item
cost_per_item = total_cost/number_of_items
# You know the TOTAL and the NUMBER OF ITEMS.
#
# Determine the price of ONE item.



# TASK 46:
# Create:
total_distance = 450
# total_distance = 450
# hours = 6
hours = 6
# Create:
distance_per_hour = total_distance * hours
# distance_per_hour
#
# Determine how many miles were traveled during
# each hour.



# TASK 47:
# Create:
#
# total_students = 120
# classrooms = 5
total_students = 120
classrooms = 5
# Create:
#
# students_per_classroom
students_per_classroom = total_students/classrooms
# Assume students are divided equally.



# ============================================================
# SECTION 13 — MORE ADVANCED VARIABLE REUSE
# ============================================================

# TASK 48:
# Create:
#
# item_price = 18
# number_purchased = 5
item_price = 18
number_purchased = 5
# Create:
subtotal = item_price * number_purchased
# subtotal
#
# Calculate the subtotal.



# TASK 49:
# Create:
#
# shipping_cost = 12
shipping_cost = 12
# Then create:
#
# total_with_shipping
total_with_shipping = subtotal + shipping_cost
# REQUIREMENT:
# Use subtotal and shipping_cost.



# TASK 50:
# Create:
#
# amount_paid = 150
amount_paid = 150
# Then create:
change_received = amount_paid - total_with_shipping
# change_received
#
# Determine how much change should be returned.
#
# REQUIREMENT:
# Use total_with_shipping.
#
# Do NOT redo either of the previous calculations.



# ============================================================
# SECTION 14 — STRING + NUMBER CHALLENGE
# ============================================================

# TASK 51:
# Create:
#
# current_year = 2026
current_year = 2026
# Ask the user what year they were born.
birth_year = int(input("What year were you born?: "))
# Store their answer inside:
#
# birth_year
#
# Make sure you can perform arithmetic with it.



# TASK 52:
# Create:
approximate_age = current_year - birth_year
# approximate_age
#
# Calculate the user's approximate age.



# TASK 53:
# Create a variable named:
#
# age_as_string
age_as_string = (approximate_age)
# Convert approximate_age into a String.
#
# Do NOT manually type their age as text.



# TASK 54:
# Create:
#
# age_message
#
# Using STRING CONCATENATION, make age_message contain:
print("You are approximateley", approximate_age, "years old")
# You are approximately [age] years old.
#
# REQUIREMENTS:
#
# - Use approximate_age somewhere in the process.
# - Use string concatenation.
# - Do NOT manually type the calculated age.
#
# Think carefully about the data types involved.



# ============================================================
# SECTION 15 — FINAL CHALLENGES
# ============================================================

# TASK 55:
# Ask the user for THREE whole numbers.
#
# Store them in:
#
# number1
# number2
# number3
number1 = int(input("Enter in a whole number: "))
number2 = int(input("Enter in a whole number: "))
number3 = int(input("Enter in a whole number: "))

combined_total = number1 + number2 + number3
# Create:
#
# combined_total
#
# Add all three numbers together.



# TASK 56:
# Create:
#
# average
#
# Calculate the average of the THREE numbers.
average = combined_total/3
# REQUIREMENT:
# Use combined_total in your calculation.
#
# Do NOT add number1, number2, and number3 together again.



# TASK 57:
# Create:
#
# doubled_average
doubled_average = 2 * average
# Make its value TWO TIMES the average.
#
# REQUIREMENT:
# Use average.



# TASK 58:
# Create:
#
# final_answer
final_answer = doubled_average - number1
# Subtract number1 from doubled_average.
#
# You may ONLY use:
#
# doubled_average
# number1
#
# in this calculation.



# ============================================================
# SECTION 16 — FIND THE PROBLEM
# ============================================================

# TASK 59:
# The programmer wanted score to store the NUMBER 95.
#
# Fix the line below so score stores the correct DATA TYPE.

score = int(95)



# TASK 60:
# The programmer wants to add 10 to the user's number.
#
# The code below will cause a problem.
#
# FIX IT.
#
# Do not replace the user's input with a number.

user_number = int(input("Enter a number: "))
answer = user_number + 10
print(answer)



# TASK 61:
# The programmer wants the output:
#
# 15

# Fix the code WITHOUT changing the values 10 and 5.

first = int(10)
second = int(5)
total = first + second
print(total)



# TASK 62:
# The programmer wants to print the VALUE stored in student.
#
# Fix the print statement.

student = "Alex"

print(student)



# ============================================================
# FINAL BOSS — CHECK FOR UNDERSTANDING
# ============================================================

# TASK 63:
#
# Ask the user for:
#
# - Their first name
# - Their last name
# - Their birth year
# - Their favorite number
their_first_name = (input("What is your first name?: "))
their_last_name = (input("What is your last name?: "))
their_birth_year = int(input("What is your birth year?: "))
their_favorite_number = int(input("What is your favorite nubmer?: "))
# You decide what variables to create.
#
# Then your program must:
#
# 1. Combine their first and last name into ONE variable.
# 2. Calculate their approximate age using 2026.
# 3. Multiply their favorite number by their approximate age.
# 4. Store EVERY calculated result inside a variable.
# 5. Print a personalized message containing their full name.
# 6. Print their approximate age.
# 7. Print the result of their favorite number multiplied by their age.

their_full_name = their_first_name + " " + their_last_name
their_approximate_age = current_year - their_birth_year
number_age = their_favorite_number * approximate_age

print("Hello,", their_full_name, "Here's a little bit about you")
print("Your approximately", their_approximate_age, "years old" )
print("Your favroite number multiplied by your age is ", number_age)
# IMPORTANT:
#
# You are NOT being given the variable names for this problem.
# Choose clear and descriptive variable names yourself.
#
# Your program must work for ANY user.
#
# You may ONLY use concepts from slides 1–60.



# ============================================================
# GIT CHECK
# ============================================================

# When you are completely finished:
#
# 
# 1. Save your file.
# 2. Run your ENTIRE program.
# 3. Fix all errors.
# 4. Make sure you can explain your code.
#
#
# Then use:
#
# git status
# git add .
# git commit -m "Complete Python skills check"
# git push
