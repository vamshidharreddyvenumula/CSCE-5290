# from pickle import FALSE
import re

def is_valid_date(string):
    date_regex = r'(January|February|March|April|May|June|July|August|September|October|November|December) \d{2}, \d{4}'
    pattern1 = r'\d{1,2}/\d{1,2}/\d{2}'
    p2 = r'\d{2}-(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec), \d{4}'
    p3 = "^\d{4}-(0[1-9]|1[0-9]|2[0-9]|3[0-1])-(0[1-9]|1[0-2])$"
    a = re.match(date_regex, string)
    b = re.match(pattern1, string)
    c = re.match(p2, string)
    d = re.match(p3, string)
    if re.match(date_regex, string): 
      print('Found : ',a.group())
    if re.match(pattern1, string):
      print('Found : ',b.group())
    if re.match(p2, string):
      print('Found : ',c.group())
    if re.match(p3, string):
      print('Found : ',d.group())
    
    

# print(is_valid_date("2021-20-01"))
# print(is_valid_date("04-Jul, 2004"))
# print(is_valid_date("January 05, 1960"))
# print(is_valid_date("6/1/00"))