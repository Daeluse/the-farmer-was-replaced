def Get_Seed_Cost(seed):
	plot_count = get_world_size() * get_world_size()
	cost = get_cost(seed)
	for item in cost:
		cost[item] = cost[item] * plot_count
	return cost
	
def Get_Seeds(item):
	cost = Get_Seed_Cost(item)
	for item in cost:
		while num_items(item) < cost[item]:
			Grow(item)

def Grow(item):
	if (item == Items.Hay):
		Grow_Grass()
	elif (item == Items.Wood):
		Grow_Wood()
	elif (item == Items.Carrot):
		Get_Seeds(Items.Carrot_Seed)
		Grow_Carrots()
	elif (item == Items.Gold):
		Get_Seeds(Items.Fertilizer)
		Spawn_Maze()
	elif (item == Items.Cactus):
		Get_Seeds(Items.Cactus_Seed)
		Grow_Cacti()
	elif (item == Items.Power):
		Get_Seeds(Items.Sunflower_Seed)
		Grow_Sunflowers()
	elif (item == Items.Bones):
		Get_Seeds(Items.Egg)
		Grow_Dinosaur()
	elif (item == Items.Pumpkin):
		Get_Seeds(Items.Pumpkin_Seed)
		Grow_Pumpkins()
		
def Do_Harvest(use_fertilizer):
	Move_To(0, 0)
	for y in range(get_world_size()):
		for x in range(get_world_size()):
			while (get_entity_type() != None and not can_harvest()):
				if (use_fertilizer):
					trade(Items.Fertilizer)
					use_item(Items.Fertilizer)
				else:
					Do_Nothing()
			harvest()
			move(North)
		move(East)