def Plant_Dinosaur():
	dino_list = [0, 0, 0, 0]
	for x in range(get_world_size()):
		for y in range(get_world_size()):
			Make_Ground_Turf()
			Trade(Items.Egg, 1)
			use_item(Items.Egg)
			type = measure()
			dino_list[type] = dino_list[type] + 1
			move(North)
		move(East)
	return dino_list

def Grow_Dinosaur():
	Move_To_Origin()
	clear()
	dino_list = Plant_Dinosaur()
	Move_To(0,0)
	Do_Harvest(False)