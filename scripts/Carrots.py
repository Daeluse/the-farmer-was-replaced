def Plant_Carrots():
	Make_Ground_Soil()
	Trade(Items.Carrot_Seed, 1)
	plant(Entities.Carrots)
	
def Grow_Carrots():
	clear()
	For_Each_Tile(Plant_Carrots)
	For_Each_Tile(Do_Harvest)
