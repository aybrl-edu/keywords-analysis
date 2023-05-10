import time

import requests
import json
from kafka import KafkaProducer


# Categories and Keywords
categories_and_seed_keywords = [
    ("Apparel Accessories", ["shirts", "dresses", "shoes", "handbags", "jewelry"]),
    ("Automotive", ["car parts", "tires", "auto repair", "car insurance", "used cars"]),
    ("Baby Children's Products", ["diapers", "baby clothes", "toys", "strollers", "car seats"]),
    ("Consumer Electronics", ["smartphones", "laptops", "TVs", "headphones", "cameras"]),
    ("Financial Services", ["credit cards", "loans", "mortgages", "banking", "investment"]),
    ("Health Wellness", ["vitamins", "supplements", "fitness equipment", "weight loss", "health insurance"]),
    ("Home Garden", ["furniture", "appliances", "home decor", "lawn care", "gardening tools"]),
    ("Real Estate", ["homes for sale", "rentals", "real estate agents", "mortgage rates", "home valuation"]),
    ("Software Apps", ["antivirus software", "mobile apps", "project management tools", "photo editing", "accounting software"]),
    ("Sports Fitness", ["sporting goods", "athletic wear", "exercise equipment", "fitness classes", "outdoor gear"]),
    ("Travel", ["flights", "hotels", "car rentals", "vacation packages", "travel insurance"]),
]

# Set up Kafka producer
KAFKA_TOPIC = 'seo_keywords_topic'
producer = KafkaProducer(bootstrap_servers='172.31.253.254:9092',
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))

# API credentials
API_TOKEN = ''
RELATED_KW_URL = f"https://api.keyword.io/related_keywords?api_token={API_TOKEN}&"


def keywords_data():

    for category in categories_and_seed_keywords:

        print(f"Getting keywords of category {category[0]}")

        list_keywords = []

        for keyword in category[1]:
            url = f'{RELATED_KW_URL}q={keyword}'

            response = requests.get(url)

            if response.status_code == 200:
                print(f"Request for keyword '{keyword}' was successful.")
                data = response.json()
                for kw in data['keywords']:
                    list_keywords.append(kw)
            else:
                print(f"Request for category '{category}' failed. Status code: {response.status_code}")

            time.sleep(12)

        message = {
            'category_name': category[0],
            'keywords': list_keywords
        }
        print("sending message to kafka...")

        producer.send(KAFKA_TOPIC, message)

        print("waiting for 30 seconds")

        time.sleep(30)

    producer.close()

