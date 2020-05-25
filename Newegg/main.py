from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pandas as pd
import requests
import time,re
from all_links import *
import warnings

start = time.time()
options = Options()
options.add_argument('--log-level=3')
options.add_argument('--headlesss')
warnings.filterwarnings("ignore")

products  = []
prices    = []
reviews   = []
brands    = []

df = pd.DataFrame()

items = ('Cpu','Gpu','Ram','Power-supply','Motherboard','Ssd','Hdd','Fans')
allowed_brands = ('Intel','AMD')
possible_locations = ('External','Internal')


def NewEgg(product,amount=int,price=True,review=False,brand=False,
		   default_brand='Intel',location='Internal'):
	"""Params:
		Item: Must choose one item of the list not case sensitive.
		Amount: Right now, amount set to less than 900 items.
		Price: Set True by default. If False, it will not display prices.
		Review: Set False by default. If True, it will display reviews and stars.
		Brand: Set False by default. If True, it will display brand of item.
		default_brand: Brand for motherboard. Set to Intel by default.
		location: Location for SSD. Set to Internal by default."""

	if product.capitalize() not in items:
		raise Exception('Please choose one of these items: {}'.format([item for item in items]))
	else:
		print('-'*60)
		print('\n Looking for product: {:>37}'.format(product.upper()))

	if default_brand.capitalize() not in allowed_brands:
		raise Exception('Please choose one these brands: {}'.format([v for v in allowed_brands]))

	if location.capitalize() not in possible_locations:
		raise Exception('Please choose either one of these locations for your SSD: {}'.format(possible_locations))

	if amount > 900 or amount < 1:
		raise Exception('Please choose a number between 1 and 900')
	else:
		print(' Searching for {:>38} items\n'.format(amount))

	for boolean in (price,review,brand):
		if boolean == 0 or boolean == 1:
			pass
		else:
			raise Exception('Must be set to True of False.')

	pages = round(amount/40)
	if pages < 1: pages = 1
	if pages > 15: pages = 15

	print(' Priceset to:   {:>43}\n'.format(price),
	      'Review set to: {:>43}\n'.format(review),
	      'Brand set to:  {:>43}\n'.format(brand),
	      'Default brand for motherboard set to: {:>20}\n'.format(default_brand),
	      'Default location for SSD set to:      {:>20}'.format(location))
	print('-'*60)

	time.sleep(1)

	number = 0

	driver = webdriver.Chrome('../../Chromedriver/chromedriver.exe')

	try:
		for i in range(1,pages+1): #Change this
			if i == 1:
				print('\n Going to page {}\n'.format(i))
			else:
				print(' \n Going to page {}\n'.format(i))
			website_link = choose_what_product(product.capitalize(),default_brand,location)
			driver.get(website_link.format(i))
			time.sleep(1)
			main = WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.CLASS_NAME, "page-content")))
			all_items = main.find_elements_by_class_name("item-container")
			for item in all_items:
				number += 1
				all_names = item.find_element_by_class_name("item-title")
				products.append(all_names.text)

				if price:
					all_prices = item.find_element_by_class_name('price-current')
					try:
						all_prices = all_prices.text.split()[0]
					except:
						go_to_price = item.find_element_by_class_name('item-buying-choices')
						go_to_price_1 = go_to_price.find_element_by_class_name('item-buying-choices-price')
						all_prices = go_to_price_1.text

					prices.append(all_prices)
				else:
					pass

				if review:
					all_reviews = item.find_element_by_class_name('item-branding')
					all_reviews = (re.sub("[^\w]", "", all_reviews.text))
					reviews.append(all_reviews)
				else:
					pass

				if brand:
					all_brands = all_names.text.split()[0]
					brands.append(all_brands)
				else:
					pass

				if number >= amount:

					time.sleep(1)

					print('-'*60)

					df['Products'] = products
					print(' Total number of items: {:>35}'.format(len(df['Products'])))

					if prices:
						df['Prices'] = prices
						print(' Total number of prices: {:>34}'.format(len(df['Prices'])))

					if reviews:
						df['Reviews'] = reviews
						print(' Total number of reviews: {:>33}'.format(len(df['Reviews'])))

					if brands:
						df['Brand'] = brands
						print(' Total number of brands: {:>34}'.format(len(df['Brand'])))


					df.to_csv('all_names.csv',index=False, header=True)
					driver.quit()
					elapsed_time = time.time() - start
					print(' \n Time taken: ', time.strftime("%H:%M:%S", time.gmtime(elapsed_time)))
					print('-'*60)
					quit()

	finally:
		pass

NewEgg(product='SSD',amount=70,price=True,review=True,brand=True,location='External')