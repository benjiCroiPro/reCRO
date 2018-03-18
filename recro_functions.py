def journey_comparison(product, user_journey):
	similar_journeys = []
	journeys = product["user_journeys"]
	product_id = product["product_id"]

	for journey in journeys:
		x = 0
		similarity_points = 0
		pages = journey["pages"]
		for page in pages:
			if pages[page] == user_journey[str(x)]:
				similarity_points+=1
			x+=1;
		similarity = similarity_points/x
		conversion_rate = int(journey["journey_conversions"])/int(journey["journey_count"])
		if similarity > 0.1 and conversion_rate:
			similar_journeys.append({"path_id": journey["path_id"], "similarity": similarity, "conversion_rate": conversion_rate })

	similar_journeys = sorted(similar_journeys, key=lambda x: (x["path_id"], x["conversion_rate"]), reverse=True)
	return similar_journeys[:3]