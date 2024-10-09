def Harvest_Pumpkins():
	if (get_entity_type() == Entities.Pumpkin):
		if (can_harvest()):
			harvest()
			Plant_Pumpkins()
	else:
		Plant_Pumpkins()

def Plant_Pumpkins():
	if (get_entity_type() != Entities.Pumpkin):
		Make_Ground_Soil()
		Trade(Items.Pumpkin_Seed, 1)
		plant(Entities.Pumpkin)
	
def Grow_Pumpkins():
	Move_To(0, 0)
	clear()
	For_Each_Tile(Plant_Pumpkins)
	while Has_Empty_Tiles():
		For_Each_Tile(Plant_Pumpkins)
		Do_Nothing()
		Do_Nothing()
		Do_Nothing()
	while not can_harvest():
		Do_Nothing()
	harvest()
	
		