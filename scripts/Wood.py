def Harvest_Wood():
	if (get_entity_type() == Entities.Bush):
		if (can_harvest()):
			harvest()
			Plant_Bushes()
	elif (get_ground_type() == Entities.Tree):
		if (can_harvest()):
			harvest()
			Plant_Trees()
	else:
		Plant_Wood()

def Plant_Wood():
	if not Is_Unlocked(Entities.Tree):
		Plant_Bushes()
	else:
		if (get_pos_y() % 2 == 0 and get_pos_x() % 2 == 0):
			Plant_Bushes()
		elif (get_pos_y() % 2 == 1 and get_pos_x() % 2 == 1):
			Plant_Bushes()
		else:
			Plant_Trees()	

def Plant_Bushes():
	Make_Ground_Soil()
	plant(Entities.Bush)

def Plant_Trees():
	Make_Ground_Soil()
	plant(Entities.Tree)
	
def Grow_Wood():
	Move_To_Origin()
	clear()
	For_Each_Tile(Plant_Wood)
	Do_Harvest(False)