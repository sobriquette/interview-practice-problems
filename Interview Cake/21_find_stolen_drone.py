def findStolenDrone(drones):
	unique_delivery_id = 0

	for deliv_id in drones:
		unique_delivery_id ^= deliv_id

	return unique_delivery_id