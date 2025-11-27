
import random
import string
import csv

# Генеруємо рядок із рандомних літер (a–z, A–Z)
# def generate_random_letter():
#     return random.choice(string.ascii_letters)

# N:int = 10_000
# file_to_save: str = "task_1.txt"

# with open(file_to_save, 'w', encoding='utf-8') as file:
#     for i in range(N):
#         random_letters = generate_random_letter()
#         file.write('\n' + random_letters)
  

#---------------------------------------------

# Task 3. Calculate stat letters - display in format A: 100, B:50, etc

# def count_letters(data):
#     d = {}
#     list_data = data.strip().split() 
#     for i in list_data:
#             d[i] = list_data.count(i)
#     return d

# with open(file_to_save, 'r', encoding='utf-8') as file:
#     data = file.read()

# print(count_letters(data))

#-------------------------------------------------

# Task 1. Read first 3 rows from amazon.csv, display columns 

url = "amazon.csv"

with open(url, 'r') as file:
     reader = csv.DictReader(file, delimiter=',')

count = 0
result = []
for row in reader:
     if count < 3:
          result.append(row)
          count += 1    
print(result)     
        

#  Task 2. Calculate image_url and display stats