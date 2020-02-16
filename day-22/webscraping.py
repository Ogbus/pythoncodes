import requests
from bs4 import BeautifulSoup

# The url to scrape
url = 'http://mlr.cs.umass.edu/ml/datasets.html'
response = requests.get(url)

# to get the status code of the request
status = response.status_code
print(status)

# we get all the content from the website
content = response.content
# beautiful soup will give a chance to parse
soup = BeautifulSoup(content, 'html.parser')
# <title>UCI Machine Learning Repository: Data Sets</title>
print(soup.title)

# UCI Machine Learning Repository: Data Sets
# print(soup.title.get_text())
# gives the whole page on the website
# print(soup.body)

tables = soup.find_all('table', {'cellpadding':'3'})
# We are targeting the table with cellpadding attribute and the attribute value
# We can select using id, class or HTML tag , for more information check the beautifulsoup doc
table = tables[0] # the result is list, we are taking out from the list
for td in table.find('tr').find_all('td'):
    print(td.json())
