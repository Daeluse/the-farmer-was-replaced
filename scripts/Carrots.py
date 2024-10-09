def Harvest_Carrots():
	if (get_entity_type() == Entities.Carrots):
		if (can_harvest()):
			harvest()
			Plant_Carrots()
	else:
		Plant_Carrots()

def Plant_Carrots():
	Make_Ground_Soil()
	Trade(Items.Carrot_Seed, 1)
	plant(Entities.Carrots)
	
def Grow_Carrots():
	Move_To_Origin()
	clear()
	For_Each_Tile(Plant_Carrots)
	Do_Harvest(False)
