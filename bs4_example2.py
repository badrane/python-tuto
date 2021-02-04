from bs4 import BeautifulSoup
import re

# ecological pyramid example

with open("ecologicalpyramid.html") as ecological_pyramid:
    soup = BeautifulSoup(ecological_pyramid, "html.parser")
producer_entries = soup.find("ul")
print(producer_entries.li.div.string)

tag_li = soup.find("li")
print(type(tag_li))

#search for text
search_for_stringonly = soup.find(text="fox")
print(search_for_stringonly)

# finding css class using attr
css_class = soup.find(attrs={"class": "primaryconsumerlist"})
print(css_class)
# finding css class using class_

css_class = soup.find(class_="primaryconsumers")


# find using pre defined functions

def is_secondary_consumers(tag):
    return tag.has_attr("id") and tag.get("id") == "secondaryconsumers"


secondary_consumer = soup.find(is_secondary_consumers)
print(secondary_consumer.li.div.string)

# example for find_all
all_tertiaryconsumers = soup.find_all(class_="tertiaryconsumerslist")
print(type(all_tertiaryconsumers))

# searching all text

all_texts = soup.find_all(text=True)
print(all_texts)

# searching group of string

all_texts_in_list = soup.find_all(text=["plants", "algae"])
print(all_texts_in_list)

# finding all div and li tags

div_li_tags = soup.find_all(["div", "li"])

# findign all css classes

all_css_class = soup.find_all(class_=["producerlist", "primaryconsumerlist"])

# find all using recursive

div_li_tags = soup.find_all(["div", "li"], recursive=True)
print(div_li_tags)

# Regular expression example.

email_id_example = """<br/>
<div>The below HTML has the information that has email ids.</div>
abc@example.com
<div>xyz@example.com</div>
<span>foo@example.com</span>
 """
soup = BeautifulSoup(email_id_example, "html.parser")
emailid_regexp = re.compile("\w+@\w+\.\w+")
first_email_id = soup.find(text=emailid_regexp)
print(first_email_id)

# searching using find_all based on reg exp

email_ids = soup.find_all(text=emailid_regexp)
print(email_ids)

# using limit in find_all

email_ids_limited = soup.find_all(text=emailid_regexp, limit=2)
print(email_ids_limited)

# using custom attrs

customattr = """<p data-custom="custom">custom attribute example</p>"""
customsoup = BeautifulSoup(customattr, "html.parser")
using_attrs = customsoup.find(attrs={"data-custom": "custom"})
print(using_attrs)

# searching for combinations

html_identical = """<p class="identical">
Example of p tag with class identical
</p>
<div class="identical">
Example of div tag with class identical
</div>"""
soup = BeautifulSoup(html_identical, "html.parser")
identical_div = soup.find("div", class_="identical")
print(identical_div)


li = soup.find('li', {'class': 'text'})
children = li.findChildren()
for child in children:
    print(child)