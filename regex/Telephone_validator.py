# https://regex101.com/r/DfXYXM/1/

import re

phone_numbers = re.compile(
    r"(?:\s*\+?\d{1,3}\s*(?:\d{3}-?){3})|(?:\s*\(?\+?(?:\d{1,3})\)?\s*)(?:\d{3}-*){3}|\s*(?:\d{3}-*){3}",
    flags=re.M
)

test_str = """
(351) 974-789-988
(351)974-789-988
(1)      387987765
 (+21) 987-986-234
 +21 987-986-234
351 987-876-876
765449888
   876-987-987   
"""

for phone_number in phone_numbers.findall(test_str):
    print(phone_number)
