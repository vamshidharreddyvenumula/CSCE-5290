import re

def is_valid_phone_number(phone_number):
    pattern = r'^\+[1-9]{1} [0-9]{3}-[0-9]{3}-[0-9]{4}$'
    phone_number_pattern = r"^[2-9]\d{9}$"
    p1 = r'^\([0-9]{3}\)[-]?[0-9]{3}[-]?[0-9]{4}$'
    p2 = r'^0?0?[1-9]{1}[-]{1}[0-9]{3}[-]{1}[0-9]{3}[-]{1}[0-9]{4}$'
    a = re.match(pattern, phone_number)
    b = re.match(phone_number_pattern, phone_number)
    c = re.match(p1, phone_number)
    d = re.match(p2, phone_number)
    if re.match(pattern, phone_number):
      print('Found : ',a.group())
    if re.match(phone_number_pattern, phone_number):
      print('Found : ',b.group())
    if re.match(p1, phone_number):
      print('Found : ',c.group())
    if re.match(p2, phone_number):
      print('Found : ',d.group())
    
# is_valid_phone_number('6012664949')
# is_valid_phone_number('+1 601 266-4949')
# is_valid_phone_number('(601)-266-4949')
# is_valid_phone_number('001-601-266-4949')
  