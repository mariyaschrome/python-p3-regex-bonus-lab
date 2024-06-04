import re

my_pattern = r"It's such a lovely day today\.|Some weather we're having today, huh\?|Maybe today's just not my day\."
my_regex = re.compile(my_pattern)

test_strings = [
    "It's such a lovely day today.",
    "Some weather we're having today, huh?",
    "Maybe today's just not my day."
]

for test_string in test_strings:
    print(f"Testing: {test_string}")
    match = my_regex.fullmatch(test_string)
    print("Match:", match)


FINDALL_STRING = """
    It's such a lovely day today.
    Where'd all the time go?
    Some weather we're having today, huh?
    Tomorrow never knows!
    Maybe today's just not my day.
    It's clobbering time!
"""
found_matches = my_regex.findall(FINDALL_STRING)
print("Found Matches:", found_matches)







