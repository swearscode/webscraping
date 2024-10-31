from bs4 import BeautifulSoup
import json

# Path to your local HTML file
file_path = 'Iphone.html'

# Open and read the local HTML file
with open(file_path, 'r', encoding='utf-8') as file:
    soup = BeautifulSoup(file, 'html.parser')

# Find all product containers
products = soup.find_all('div', class_='sg-col-4-of-24 sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 sg-col s-widget-spacing-small sg-col-4-of-20')

# List to hold product data
product_data = []

# Loop through each product and extract the required information
for product in products:
    title = product.find('h2', class_='a-size-mini a-spacing-none a-color-base s-line-clamp-4')
    title_text = title.get_text(strip=True) if title else 'N/A'

    image = product.find('img', class_='s-image')
    image_url = image['src'] if image else 'N/A'

    rating = product.find('span', class_='a-icon a-icon-star-small a-star-small-4')
    rating_text = rating.get_text(strip=True) if rating else 'N/A'

    price = product.find('span', class_='a-price-whole')
    price_text = price.get_text(strip=True) if price else 'N/A'

    # Append the data to the list
    product_data.append({
        'title': title_text,
        'image_url': image_url,
        'rating': rating_text,
        'price': price_text
    })

# Save the data to a JSON file
with open('Products.json', 'w') as json_file:
    json.dump(product_data, json_file, indent=4)

print('Data has been scraped and saved to data.json.')