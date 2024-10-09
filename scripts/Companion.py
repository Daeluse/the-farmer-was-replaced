def Plant_Random_Companion():
	types = [Plant_Grass, Plant_Bushes, Plant_Trees, Plant_Carrots]
	index = random() * len(types)
	types[index]()

def Grow_Companion():
	Move_To(0,0)
	clear()
	For_Each_Tile(till)
	Move_To(0,0)
	for x in range(get_world_size()):
		for y in range(get_world_size()):
			if get_entity_type() == None:
				Plant_Random_Companion()
			companion = get_companion()
			if (companion != None):
				prev_x = get_pos_x()
				prev_y = get_pos_y()
				Move_To(companion[1], companion[2])
				if (get_entity_type() == None):
					if (companion[0] == Entities.Grass):
						Plant_Grass()
					elif (companion[0] == Entities.Bush):
						Plant_Bushes()
					elif (companion[0] == Entities.Tree):
						Plant_Trees()
					elif (companion[0] == Entities.Carrots):
						Plant_Carrots()
				Move_To(prev_x, prev_y)
			move(North)
		move(East)
	Do_Harvest(True)
						