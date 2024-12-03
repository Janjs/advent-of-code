with open("input.txt", "r") as file:
  data = file.read()
  
res = 0
last_char = ''
first_num_str = ''
second_num_str = ''
first_num = 0
second_num = 0
enabled = True
start_computation = False

def compute_mul():
  global res
  print(f'enabled {enabled} {first_num} * {second_num}')
  if enabled:
    res += first_num * second_num
  reset()

def reset():
  global last_char 
  last_char = ''
  global first_num_str 
  first_num_str = ''
  global second_num_str
  second_num_str = ''
  global first_num 
  first_num = 0
  global second_num
  second_num = 0
  global start_computation
  start_computation = False

for i, char in enumerate(data):
  if char == 'm':
    if last_char == '':
      last_char = char
      start_computation = True
    else:
      reset()
  elif char == 'u':
    if last_char == 'm':
      last_char = char
    else:
      reset()
  elif char == 'l':
    if last_char == 'u':
      last_char = char
    else:
      reset()
  elif char == '(':
    if last_char == 'l':
      last_char = char
    else:
      reset()
  elif char.isdigit():
    if first_num_str != '':
      first_num_str += char
    elif last_char == '(':
      first_num_str += char
    elif second_num_str != '':
      second_num_str += char
    elif last_char == ',':
      second_num_str += char
    else:
      reset()
  elif char == ',':
    if first_num_str != '':
      first_num = int(first_num_str)
      first_num_str = ''
      last_char = ','
    else:
      reset()
  elif char == ')':
    if second_num_str != '':
      second_num = int(second_num_str)
      compute_mul()
    else: 
      reset()
  elif char == 'd':
    if data[i+1] == 'o' and data[i+2] == '(' and data[i+3] == ')':
      enabled = True
    elif data[i+1] == 'o' and data[i+2] == 'n' and data[i+3] == "'"  and data[i+4] == 't' and data[i+5] == '(' and data[i+6] == ')':
      enabled = False
    if start_computation:
      reset()
  else:
    reset()

print(f'Result: {res}')
  
