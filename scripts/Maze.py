def Spawn_Maze():
	clear()
	Move_To(0,0)
	Plant_Bushes()
	while not can_harvest():
		Do_Nothing()
	while get_entity_type() != Entities.Hedge and get_entity_type() != Entities.Treasure:
		Trade(Items.Fertilizer, 1)
		use_item(Items.Fertilizer)
	Solve_Maze()

def Solve_Maze():
	orientation = 0
	while get_entity_type() != Entities.Treasure:
		if not Move_Forward(orientation):
			orientation = Rotate(orientation, True)
		else:
			orientation = Rotate(orientation, False)
	harvest()
	
def Move_Forward(orientation):
	if (orientation == 0):
		return move(North)
	elif (orientation == 1):
		return move(East)
	elif (orientation == 2):
		return move(South)
	elif (orientation == 3):
		return move(West)

def Rotate(orientation, clockwise):
	if clockwise:
		orientation = orientation + 1
	else:
		orientation = orientation - 1
	if orientation > 3:
		orientation = 0
	elif orientation < 0:
		orientation = 3
	return orientation