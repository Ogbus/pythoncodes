import re
from collections import Counter
# Clean the following text. After cleaning, count three most frequent words in the string.
sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''
rex_pattern = r'[%$#@&]'
match_replace = re.sub(rex_pattern, '', sentence)
print(match_replace)

paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'
word = r'\w+'
matched_pattern = re.findall(word, paragraph)
Counter = Counter(matched_pattern)
most_occur = Counter.most_common()
print(most_occur)

counts = 0 
for words in matched_pattern:
    counts = counts + 1
print(counts)
print(list(words))