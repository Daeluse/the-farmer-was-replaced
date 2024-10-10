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
	clear()
	For_Each_Tile(Plant_Wood)
	For_Each_Tile(Do_Harvest)