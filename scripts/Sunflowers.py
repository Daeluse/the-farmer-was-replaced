def Plant_Sunflowers():
	plant_locations = {15:[], 14:[], 13:[], 12:[], 11:[], 10:[], 9:[], 8:[], 7:[]}
	world_size = get_world_size()
	for x in range(world_size):
		for y in range(world_size):
			Make_Ground_Soil()
			Trade(Items.Sunflower_Seed, 1)
			plant(Entities.Sunflower)
			petal_count = measure()
			plant_locations[petal_count].append([get_pos_x(), get_pos_y()])
			move(North)
		move(East)
	return plant_locations
	
def Grow_Sunflowers():
	clear()
	plant_locations = Plant_Sunflowers()
	for petal_count in plant_locations:
		for coords in plant_locations[petal_count]:
			Move_To(coords[0], coords[1])
			while not can_harvest():
				Do_Nothing()
			harvest()