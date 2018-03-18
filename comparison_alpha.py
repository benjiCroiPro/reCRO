# import relevant packages for use in this script
from pathlib import Path
import json, recro_functions

# set user_profile and product database file paths
user_profile_json = Path("databases/user_profile.json")
products_json = Path("databases/products.json")
# check if user profile and product database exists
if products_json.is_file() and user_profile_json.is_file():
	# success message
	print ("Databases exist")

	# open user profile
	with open("databases/user_profile.json", 'r') as user:
		# relevant messaging
		user_profile = json.load(user)
		user_id = user_profile['user_id']
		user_journey = user_profile["user_journey"]
		user_page = user_profile["current_page"]
		# open product database
		with open("databases/products.json", 'r') as prods:
			# relevant messaging
			p_json = json.load(prods)
			products = p_json["products"]
			# find journey similarity
			for product in products:
				if product["product_url"] == user_page:
					current_product = product
					products.remove(product)
			
			for product in products:
				journey_similarity = recro_functions.journey_comparison(product, user_journey)
				print (journey_similarity)
				for pj in product["user_journeys"]:
					for js in journey_similarity:
						pj["journey_similarity"] = js["similarity"]
						pj["journey_conversion_rate"] = js["conversion_rate"]

				product_relevance = recro_functions.product_relevance(product, current_product)
				product["product_relevance"] = product_relevance

			print(json.dumps(products, indent=4))
