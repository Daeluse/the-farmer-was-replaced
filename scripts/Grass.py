def Harvest_Grass():
	if (get_entity_type() == Entities.Grass):
		if (can_harvest()):
			harvest()
			Plant_Grass()
	else:
		Plant_Grass()

def Plant_Grass():
	Make_Ground_Turf()
	
def Grow_Grass():
	clear()
	For_Each_Tile(Do_Harvest)