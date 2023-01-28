from pickle import FALSE
import re

def is_valid_currency(string):
    pattern = "^[+-]?\$(([1-9][0-9]{0,2}(,[0-9]{3})*[\.][0-9]{1,2})|([1-9][0-9]{0,2}(,[0-9]{3})*)|[0-9]+(\.[0-9]{1,2})?)([M|B|K]?|[A-Z]{3})?$"
    pattern1 = "^[A-Z]{3}[0-9]+(M|B|K)?$"
    a = re.match(pattern, string)
    b = re.match(pattern1, string)
    if a: 
      print('Found : ',a)
    if b:
      print('Found : ',b)
    
    

print(is_valid_currency("$954.49"))
print(is_valid_currency("$10,724.00"))
print(is_valid_currency("$1,000,000,023.45"))
print(is_valid_currency("-$250,000,456"))
print(is_valid_currency("+$234,922.99"))
print(is_valid_currency("USD45M"))
print(is_valid_currency("$25K"))
print(is_valid_currency("$4B"))