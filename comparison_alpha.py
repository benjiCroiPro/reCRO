# import relevant packages for use in this script
from pathlib import Path
import json

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
			similar_journeys = []

			for product in products:
				journeys = product["user_journeys"]
				for journey in journeys:
					x = 0
					similarity_points = 0
					pages = journey["pages"]
					for page in pages:
						if pages[page] == user_journey[str(x)]:
							similarity_points+=1
						x+=1;
					similarity = similarity_points/x
					if similarity > 0.1:
						similar_journeys.append([journey["path_id"], similarity])
			similar_journeys = sorted(similar_journeys, key=lambda x: x[1], reverse=True)
			print (similar_journeys)