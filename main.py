from bs4 import BeautifulSoup
import d
# print(len("/watch?v=_ZvnD73m40o"))
# exit()
# Load the HTML file
with open('a.html', 'r',encoding="utf-8") as file:
    html_content = file.read()

# Parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Find all anchor tags
anchor_tags = soup.find_all('a')

# Extract href attributes
hrefs = [tag.get('href') for tag in anchor_tags]

a=set()
# Print the extracted hrefs
for href in hrefs:
    if(href != None):
        if(len(href)>22):
            if("/watch" == href[:6]):
                if("&index" in href ):
                # print(href)
                    a.add('https://www.youtube.com'+href)


# print(len(hrefs))
print(len(a))
count =0
for i in a:
    print(count)
    d.download_video(i)
    count =count +1
# print(a)

