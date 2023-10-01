import json
from bs4 import BeautifulSoup

# Read the Amazon HTML file
with open('amazon.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(html_content, 'lxml')

# Find all div elements with the specified class
results = soup.find_all('div', class_='sg-col-4-of-24 sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 AdHolder sg-col s-widget-spacing-small sg-col-4-of-20')

# Initialize a list to store the extracted data
data_list = []

# Loop through each result div
for result in results:
    # Extract the image link (if available)
    img_tag = result.find('img', class_='s-image')
    link = img_tag['src'] if img_tag else ''

    # Extract the title (if available)
    title_tag = result.find('span', class_='a-size-base-plus a-color-base')
    title = title_tag.text if title_tag else ''

    # Extract the rating (if available)
    rating_tag = result.find('span', class_='a-size-base puis-normal-weight-text')
    rating = rating_tag.text if rating_tag else ''

    # Extract the price (if available)
    price_tag = result.find('span', class_='a-price-whole')
    price = price_tag.text if price_tag else ''

    # Create a dictionary for each item and add it to the data list
    item_data = {
        'link': link,
        'title': title,
        'rating': rating,
        'price': price,
    }
    data_list.append(item_data)

# Write the data to a JSON file
with open('data.json', 'w', encoding='utf-8') as json_file:
    json.dump(data_list, json_file, ensure_ascii=False, indent=4)

print('Data extraction and writing to data.json completed.')
