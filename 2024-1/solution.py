first_list = []
second_list = []

with open('input.txt', 'r') as file:
  for line in file:
    first_found = False
    first_number = ''
    second_number = ''
    for char in line:
      if char.isdigit():
        if not first_found:
          first_number += char
        else:
          second_number += char
      else:
        if len(first_number) > 0:
          first_found = True
    
    first_list.append(int(first_number))
    second_list.append(int(second_number))

first_list.sort()
second_list.sort()

first_res = 0
for i, _ in enumerate(first_list):
  diff = abs(first_list[i] - second_list[i])  
  first_res += diff

print(f'first solution {first_res}')

second_res = 0
for num in first_list:
  second_res += num * second_list.count(num)

print(f'second result: {second_res}')
