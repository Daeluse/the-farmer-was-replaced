def Plant_Pumpkins():
	if (get_entity_type() != Entities.Pumpkin):
		Make_Ground_Soil()
		Trade(Items.Pumpkin_Seed, 1)
		plant(Entities.Pumpkin)
	
def Grow_Pumpkins():
	clear()
	For_Each_Tile(Plant_Pumpkins)
	while Has_Empty_Tiles():
		For_Each_Tile(Plant_Pumpkins)
	harvest()