import date
import currency
import phone_numbers
import tags

f = open('input.txt','r')
for li in f:
    print(li)
    phone_numbers.is_valid_phone_number(li)
    tags.match_html_tag(li)
    currency.is_valid_currency(str(li))
    date.is_valid_date(str(li))