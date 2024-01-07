
# Vending Machine Sales with Python


## Introduction with Business Problem

Fast Snacks had some concerns based on their delivery workers stating that they kept stocking the same products week after week at each location. Management then approached a data consulting company to see if they can help better track how many producs they sell at each location so they can determine what sells and what does not.

This project analyzes sales data from Fast Snacks (vending machine company) to identify trends, popular products, and ways to improve sales for next year.

## Authors

- [@MalcolmQSmith](https://github.com/MalcolmQSmith)


## License

[Vending Machine Sales Dataset from Kaggle](https://www.kaggle.com/datasets/awesomeasingh/vending-machine-sales)


## Features

- Exploratory Data Analysis (EDA) via Python
- Data Cleaning
- Data Visualization via matplotlib and plotly


## Installation

The following libraries will be needed to execute this project
```bash
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    import plotly.graph_objs as go
    from plotly.subplots import make_subplots
    import zipfile
    import kaggle
```
    
## Analysis Questions

#### Question 1: What is the best selling vending machine location? 

Gutten Plans with $7,945.75, followed by EB Public Library with $7744
    
#### Question 2: What is the best selling product category in our vending machines?

Food with $10,938.50 followed by drinks with Carbonated drinks with $5290.75

#### Question 3: What is the best selling month from our vending machines?

July with $2,529 (peak summertime)

#### Question 4: What were the top selling products during our best selling month?

Monster Energy Original was first with $223, followed by Kit Kat and Coke Zero with $151.75 and $119.50

#### Question 5: What are the top selling beverage products?

Monster Energy Original was first with $1583, followed by Coca Cola - Zero Sugar with $1081

#### Question 6: What are the top selling food products?

KitKat was first with $750.25, followed by Wonderful Pistachios - Variety $467

#### Question 7: What were the lowest selling products?

Nature's Valley Crunchy and Chewy Granola Bar are tied with $1.25, followed by Orchard Bar - Cranberry Orange & Walnut with $2

## Actionable Plan to Increase Sales

1. To start, make sure all vending machines are updated to be able to take cash, coins, card, and tap to pay options. If not, all will need to be updated to ensure all customers have an opportunity to pay for their item .
2. Locations with the highest sales will get two sets of additional machines, with the lower performing locations will maintain their current machine count.
3. To make sure our customers never encounter an empty vending machine, all products - especially at our highest selling products - must be restocked two to three times per month.
4. During the summer, make sure beverage vending machines are stocked to capacity, especially water 
5. The top ten lowest selling products will be replaced with equal distribution of the top ten highest selling products
   

