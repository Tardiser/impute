mystr = "<url>https://xcd32112.smart_meter.com</url>"
mystr2 = "<url>http://xcd32112.smart_meter.com</url>"

import re
print(re.split("<url>|</url>|https://|http://", mystr)[2])
print(re.split("<url>|</url>|https://|http://", mystr2)[2])