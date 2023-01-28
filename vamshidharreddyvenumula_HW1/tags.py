import re

def match_html_tag(input_str):
    html_tag_regex = r'<[/]?\w+>'
    match = re.search(html_tag_regex, input_str)
    if match:
        print('Found : ',match.group())
    