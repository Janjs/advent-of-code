first_res = 0

with open('input.txt', 'r') as file:
  for line in file:
    line_numbers = line.split()
    for exclude in range(len(line_numbers)):
      safe = True
      asc = None
      numbers = line_numbers[:exclude] + line_numbers[exclude+1:]
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
      if safe:
        print(line, exclude)
        first_res += safe
        break

print(f'first result: {first_res}')

