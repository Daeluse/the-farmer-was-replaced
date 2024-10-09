def Plant_Dinosaur():
	Make_Ground_Soil()
	Trade(Items.Egg, 1)
	use_item(Items.Egg)

def Find_Dino(type):
	Move_To(0,0)
	for x in range(get_world_size()):
		for y in range(get_world_size()):
			move(North)
		move(East)

def Sort_Dinosaur():
	for x in range(get_world_size()):
		for y in range(get_world_size()):
			dino_type = measure()
			if dino_type == 1:
				Swap_To(0, get_pos_y())
			elif dino_type == 2:
				Swap_To(get_pos_x(), 0)
			elif dino_type == 3:
				Swap_To(get_world_size() - 1, get_pos_y())
			elif dino_type == 4:
				Swap_To(get_pos_x(), get_world_size() - 1)
			move(North)
		move(East)

def Grow_Dinosaur():
	Move_To_Origin()
	clear()
	For_Each_Tile(Plant_Dinosaur)
	Sort_Dinosaur()
	Do_Harvest(False)