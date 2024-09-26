import requests
import base64
import json

# WooCommerce API credentials
consumer_key = "Key_"
consumer_secret = "Key_"

# URL for WooCommerce API
url = "https://tossonlibrary.com/wp-json/wc/v3/products"

def AutoGenPro(ProductName, Price, Description, ShortDescription, ID):
    # Extract the first word of the product name (SEO focus word)
    seo_focus_word = ProductName.split()[0]

    # Basic authentication header
    header = {
        "Authorization": f"Basic {base64.b64encode(f'{consumer_key}:{consumer_secret}'.encode()).decode()}",
        "Content-Type": "application/json"
    }

    # Product data with Rank Math Focus Keyword in meta_data
    data = {
        "name": ProductName,
        "type": "simple",
        "regular_price": Price,
        "description": Description,
        "short_description": ShortDescription,
        "images": [{"id": ID}],
        "categories": [{"id": 99}],
        "meta_data": [
            {
                "key": "rank_math_focus_keyword",
                "value": seo_focus_word
            }
        ]
    }

    # Send the POST request to create the product
    r = requests.post(url, headers=header, json=data)
    
    if r.status_code == 201:  # Product created successfully
        product_id = r.json()['id']
        print(f"Product created with ID: {product_id}")

        # Update the SEO focus keyword for the newly created product
        print(f"\nUpdating SEO focus keyword for Product ID: {product_id}")

        # Prepare the meta field for Rank Math SEO focus keyword
        meta_update = {
            "meta_data": [
                {
                    "key": "rank_math_focus_keyword",
                    "value": seo_focus_word
                }
            ]
        }

        # Send the PUT request to update the product's SEO focus keyword
        update_url = f"{url}/{product_id}"
        wp_update = requests.put(update_url, headers=header, json=meta_update)

        if wp_update.status_code == 200:
            print("Rank Math SEO focus keyword updated successfully!")
        else:
            print("Failed to update SEO focus keyword:", wp_update.status_code, wp_update.text)
    else:
        print("Failed to create product:", r.status_code, r.text)
