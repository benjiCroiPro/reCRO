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
		# open product database
		with open("databases/products.json", 'r') as prods:
			# relevant messaging
			p_json = json.load(prods)
			products = p_json["products"]
			# find journey similarity
			for product in products:
				journey_similarity = recro_functions.journey_comparison(product, user_journey)
				product["journey_similarity"] = journey_similarity

			print(json.dumps(products, indent=4))
