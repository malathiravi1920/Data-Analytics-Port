import re
text="python is easy"
res=re.search('matha',text)
res=re.findall('python',text)
print(res)

text="sql power bi"
new=re.sub("power bi","powerbi",text)
print(new)

import re
text="1,2,3,4,5,6,7,8,9"
data=re.findall(r"\d",text)
print(data)

import re
text="sales:500  profit:100"
data=re.findall(r"\d+",text)
print(data)

import re
mail1="join123@gmail.com"
mail2="web@gmail.com"
mail3="123@gmail"

data=re.search(r"\w+@+\w+\w",mail1)
data=re.search(r"\w+@+\w+\w",mail2)
data=re.search(r"\w+@+\w+\w",mail3)
print(data)


import re
text="99234156122"
text1="73t38rtt328"
data=re.search(r"\d+{10}",text)
print(data)
