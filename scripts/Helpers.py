def Do_Nothing():
	return

def For_Each_Tile(callback):
	Move_To(0,0)
	world_size = get_world_size()
	for x in range(world_size):
		for y in range(world_size):
			callback()
			move(North)
		move(East)
		
def Has_Empty_Tiles():
	status = False
	Move_To(0,0)
	world_size = get_world_size()
	for x in range(world_size):
		for y in range(world_size):
			if (get_entity_type() == None or not can_harvest()):
				status = True
			move(North)
		move(East)
	return status

def Chunk(l, n):
	result = []
	inner_result = []
	while len(l) > 0:
		inner_result.append(l.pop(0))
		if len(inner_result) == n:
			result.append(inner_result)
			inner_result = []
	if len(inner_result) > 0:
		result.append(inner_result)
	return result
