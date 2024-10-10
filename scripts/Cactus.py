def Plant_Cactus():
	Make_Ground_Soil()
	Trade(Items.Cactus_Seed, 1)
	plant(Entities.Cactus)
		
def Can_Swap_North():
	curr = measure()
	y = get_pos_y()
	if y < get_world_size() - 1 and curr > measure(North):
		return True
	return False

def Can_Swap_East():
	curr = measure()
	x = get_pos_x()
	if x < get_world_size() - 1 and curr > measure(East):
		return True
	return False
	
def Can_Swap_South():
	curr = measure()
	y = get_pos_y()
	if y > 0 and curr < measure(South):
		return True
	return False
	
def Can_Swap_West():
	curr = measure()
	x = get_pos_x()
	if x > 0 and curr < measure(West):
		return True
	return False

def Can_Swap():
	return Can_Swap_North() or Can_Swap_East() or Can_Swap_South() or Can_Swap_West()
		
def Do_Swap():
	while Can_Swap():
		prev_x = get_pos_x()
		prev_y = get_pos_y()
		while Can_Swap():
			if Can_Swap_North():
				swap(North)
				move(North)
			elif Can_Swap_East():
				swap(East)
				move(East)
			elif Can_Swap_South():
				swap(South)
				move(South)
			elif Can_Swap_West():
				swap(West)
				move(West)
		Move_To(prev_x, prev_y)

def Grow_Cacti():
	clear()
	For_Each_Tile(Plant_Cactus)
	For_Each_Tile(Do_Swap)
	while not can_harvest():
		Do_Nothing()
	harvest()