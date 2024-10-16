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

def Get_Power(number):
	if Is_Unlocked(Unlocks.Sunflowers):
		while num_items(Items.Power) < number:
			Grow(Items.Power)

def Grow(item):
	if num_items(Items.Wood) > 500 and num_items(Items.Water_Tank) < 50:
		trade(Items.Empty_Tank)
	if (item == Items.Hay or item == Items.Wood or item == Items.Carrot):
		if Is_Unlocked(Unlocks.Polyculture):
			Grow_Companion()
		elif (item == Items.Hay):
			Grow_Grass()
		elif (item == Items.Wood):
			Grow_Wood()
		elif (item == Items.Carrot):
			Get_Seeds(Items.Carrot_Seed)
			Grow_Carrots()
	elif (item == Items.Gold):
		Get_Power(1000)
		Get_Seeds(Items.Fertilizer)
		Spawn_Maze()
	elif (item == Items.Cactus):
		Get_Power(1000)
		Get_Seeds(Items.Cactus_Seed)
		Grow_Cacti()
	elif (item == Items.Power):
		Get_Seeds(Items.Sunflower_Seed)
		Grow_Sunflowers()
	elif (item == Items.Bones):
		Get_Power(1000)
		Get_Seeds(Items.Egg)
		Grow_Dinosaur()
	elif (item == Items.Pumpkin):
		Get_Power(1000)
		Get_Seeds(Items.Pumpkin_Seed)
		Grow_Pumpkins()
		
def Do_Harvest():
	while (get_entity_type() != None and not can_harvest()):
		Do_Nothing()
	harvest()