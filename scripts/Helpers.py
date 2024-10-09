def Do_Nothing():
	do_a_flip()

def For_Each_Tile(callback):
	for y in range(get_world_size()):
		for x in range(get_world_size()):
			callback()
			move(North)
		move(East)
		
def Has_Empty_Tiles():
	status = False
	Move_To(0, 0)
	for y in range(get_world_size()):
		for x in range(get_world_size()):
			if (get_entity_type() == None):
				status = True
			move(North)
		move(East)
	return status