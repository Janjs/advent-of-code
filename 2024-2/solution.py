first_res = 0

with open('input.txt', 'r') as file:
  for line in file:
    safe = True
    asc = None
    numbers = line.split()
    for i in range(1, len(numbers)):
      prev_num = int(numbers[i-1])
      curr_num = int(numbers[i])
      diff = abs(prev_num - curr_num)
      
      if not (diff >= 1 and diff <= 3):
        safe = False
        continue

      if asc == None:
        asc = curr_num > prev_num
      else: 
        if asc: 
          if curr_num < prev_num:
            safe = False
            continue
        else:
          if curr_num > prev_num:
            safe = False
            continue
    first_res += safe

print(f'first result: {first_res}')

