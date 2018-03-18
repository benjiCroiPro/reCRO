def journey_comparison(product, user_journey):
	similar_journeys = []
	journeys = product["user_journeys"]
	product_id = product["product_id"]

	for journey in journeys:
		x = 0
		similarity_points = 0
		pages = journey["pages"]
		for page in pages:
			for uj in user_journey:
				if pages[page] == uj:
					similarity_points+=1
			x+=1;
		similarity = similarity_points/x
		conversion_rate = int(journey["journey_conversions"])/int(journey["journey_count"])
		if similarity > 0.1 and conversion_rate:
			similar_journeys.append({"path_id": journey["path_id"], "similarity": similarity, "conversion_rate": conversion_rate })

	similar_journeys = sorted(similar_journeys, key=lambda x: (x["path_id"], x["conversion_rate"]), reverse=True)
	return similar_journeys[:3]

def product_relevance(productA, productB):
	productA_categories = productA["product_categories"]
	productA_related_products = productA["related_products"]

	productB_categories = productB["product_categories"]
	productB_related_products = productB["related_products"]

	primary_match = 0
	secondary_match = 0
	
	if productA_categories["primary"] == productB_categories["primary"]:
		primary_match += 1
	elif productA_categories["primary"] == productB_categories["secondary"]:
		primary_match += 1
	
	if productA_categories["secondary"] == productB_categories["primary"]:
		secondary_match += 1
	elif productA_categories["secondary"] == productB_categories["secondary"]:
		secondary_match += 1

	relevance = primary_match + (secondary_match / 2)

	return relevance