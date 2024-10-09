def Make_Ground_Turf():
	if (get_ground_type() != Grounds.Turf):
		till()
		
def Make_Ground_Soil():
	if (get_ground_type() != Grounds.Soil):
		till()
	if (get_water() == 0):
		use_item(Items.Water_Tank)