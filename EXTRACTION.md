## Liste des KW Seeds (Grains)
```python
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
```
## Logs de l'extraction
```
Getting keywords of category Apparel Accessories
Request for keyword 'shirts' was successful.
Request for keyword 'dresses' was successful.
Request for keyword 'shoes' was successful.
Request for keyword 'handbags' was successful.
Request for keyword 'jewelry' was successful.
sending message to kafka...
waiting for 30 seconds
Getting keywords of category Automotive
Request for keyword 'car parts' was successful.
Request for keyword 'tires' was successful.
Request for keyword 'auto repair' was successful.
Request for keyword 'car insurance' was successful.
Request for keyword 'used cars' was successful.
sending message to kafka...
waiting for 30 seconds
Getting keywords of category Baby Children's Products
Request for keyword 'diapers' was successful.
Request for keyword 'baby clothes' was successful.
Request for keyword 'toys' was successful.
Request for keyword 'strollers' was successful.
Request for keyword 'car seats' was successful.
sending message to kafka...
waiting for 30 seconds
Getting keywords of category Consumer Electronics
Request for keyword 'smartphones' was successful.
Request for keyword 'laptops' was successful.
Request for keyword 'TVs' was successful.
Request for keyword 'headphones' was successful.
Request for keyword 'cameras' was successful.
sending message to kafka...
waiting for 30 seconds
Getting keywords of category Financial Services
Request for keyword 'credit cards' was successful.
Request for keyword 'loans' was successful.
Request for keyword 'mortgages' was successful.
Request for keyword 'banking' was successful.
Request for keyword 'investment' was successful.
sending message to kafka...
waiting for 30 seconds
Getting keywords of category Health Wellness
Request for keyword 'vitamins' was successful.
Request for keyword 'supplements' was successful.
Request for keyword 'fitness equipment' was successful.
Request for keyword 'weight loss' was successful.
Request for keyword 'health insurance' was successful.
sending message to kafka...
waiting for 30 seconds
Getting keywords of category Home Garden
Request for keyword 'furniture' was successful.
Request for keyword 'appliances' was successful.
Request for keyword 'home decor' was successful.
Request for keyword 'lawn care' was successful.
Request for keyword 'gardening tools' was successful.
sending message to kafka...
waiting for 30 seconds
Getting keywords of category Real Estate
Request for keyword 'homes for sale' was successful.
Request for keyword 'rentals' was successful.
Request for keyword 'real estate agents' was successful.
Request for keyword 'mortgage rates' was successful.
Request for keyword 'home valuation' was successful.
sending message to kafka...
waiting for 30 seconds
Getting keywords of category Software Apps
Request for keyword 'antivirus software' was successful.
Request for keyword 'mobile apps' was successful.
Request for keyword 'project management tools' was successful.
Request for keyword 'photo editing' was successful.
Request for keyword 'accounting software' was successful.
sending message to kafka...
waiting for 30 seconds
Getting keywords of category Sports Fitness
Request for keyword 'sporting goods' was successful.
Request for keyword 'athletic wear' was successful.
Request for keyword 'exercise equipment' was successful.
Request for keyword 'fitness classes' was successful.
Request for keyword 'outdoor gear' was successful.
sending message to kafka...
waiting for 30 seconds
Getting keywords of category Travel
Request for keyword 'flights' was successful.
Request for keyword 'hotels' was successful.
Request for keyword 'car rentals' was successful.
Request for keyword 'vacation packages' was successful.
Request for keyword 'travel insurance' was successful.
sending message to kafka...
```
## Echantillon d'un résultat sur le topic Kafka
```json
{
  "category_name": "Apparel Accessories", 
  "keywords": [
    {
        "kw": "shirts", 
        "n": 823000, 
        "monthly": [823000, 823000, 823000, 673000, 823000, 1000000, 1000000, 823000, 823000, 1000000, 823000, 823000], 
        "c": 0.9936, 
        "sb": 0.0, 
        "headiness": 1.0, 
        "con": 9.4
    }
  ]
}
```