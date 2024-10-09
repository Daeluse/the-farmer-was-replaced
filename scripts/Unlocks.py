def Can_Unlock(unlockable):
	upgradeable_unlocks = {
		Unlocks.Auto_Unlock: 1,
		Unlocks.Benchmark: 1,
		Unlocks.Cactus: 3,
		Unlocks.Carrots: 4,
		Unlocks.Costs: 1,
		Unlocks.Debug: 1,
		Unlocks.Debug_2: 1,
		Unlocks.Dictionaries: 1,
		Unlocks.Dinosaurs: 2,
		Unlocks.Expand: 10,
		Unlocks.Fertilizer: 1,
		Unlocks.Functions: 1,
		Unlocks.Grass: 5,
		Unlocks.Leaderboard: 1,
		Unlocks.Lists: 1,
		Unlocks.Loops: 1,
		Unlocks.Mazes: 2,
		Unlocks.Multi_Trade: 1,
		Unlocks.Operators: 1,
		Unlocks.Plant: 1,
		Unlocks.Polyculture: 1,
		Unlocks.Pumpkins: 2,
		Unlocks.Senses: 1,
		Unlocks.Speed: 10,
		Unlocks.Sunflowers: 2,
		Unlocks.Trees: 2,
		Unlocks.Utilities: 1,
		Unlocks.Variables: 1,
		Unlocks.Watering: 1,
	}
	return not num_unlocked(unlockable) == upgradeable_unlocks[unlockable]

def Get_Unlock_Cost(unlockable):
	weights = {
		Items.Hay: 1,
		Items.Wood: 2,
		Items.Carrot: 4,
		Items.Pumpkin: 8,
		Items.Power: 16,
		Items.Gold: 32,
		Items.Cactus: 64,
		Items.Bones: 128,
	}
	total = 0
	cost = get_cost(unlockable)
	for item in cost:
		if Is_Unlocked(item): 
			total = total + (weights[item] * cost[item])
		else:
			total = total + 1000000
	return total
		
def Get_Next_Unlock():
	necessary_unlocks = [
		Unlocks.Cactus,
		Unlocks.Carrots,
		Unlocks.Dinosaurs,
		Unlocks.Expand,
		Unlocks.Fertilizer,
		Unlocks.Grass,
		Unlocks.Leaderboard,
		Unlocks.Mazes,
		Unlocks.Plant,
		Unlocks.Pumpkins,
		Unlocks.Speed,
		Unlocks.Sunflowers,
		Unlocks.Trees,
	]
	result = None
	result_cost = None
	for unlockable in necessary_unlocks:
		if Can_Unlock(unlockable):
			unlock_cost = Get_Unlock_Cost(unlockable)
			if result == None or unlock_cost < result_cost:
				result = unlockable
				result_cost = unlock_cost
	return result
		
def Is_Unlocked(unlockable):
	return num_unlocked(unlockable) > 0

def Unlock(unlockable):
	cost = get_cost(unlockable)
	
	if unlockable == Unlocks.Expand and num_unlocked(Unlocks.Speed) == 0:
		Unlock(Unlocks.Speed)
	elif unlockable == Unlocks.Pumpkins and num_unlocked(Unlocks.Expand) == 0:
		Unlock(Unlocks.Expand)
	elif unlockable == Unlocks.Cactus and num_unlocked(Unlocks.Senses) == 0:
		Unlock(Unlocks.Senses)
	elif unlockable == Items.Gold and num_unlocked(Unlocks.Fertilizer) == 0:
		Unlock(Unlocks.Fertilizer)
	elif unlockable == Items.Power and num_unlocked(Unlocks.Trees) == 0:
		Unlock(Unlocks.Trees)
	elif unlockable == Items.Wood and num_unlocked(Unlocks.Speed) == 0:
		Unlock(Unlocks.Speed)
		
	for item in cost:
		while num_items(item) < cost[item]:
			Unlock_Item(item)
			Grow(item)
		unlock(unlockable)

def Unlock_Item(item):
	if item == Items.Pumpkin and num_unlocked(Unlocks.Pumpkins) == 0:
		if num_unlocked(Unlocks.Expand) == 0:
			Unlock(Unlocks.Expand)
		Unlock(Unlocks.Pumpkins)
	elif item == Items.Bones and num_unlocked(Unlocks.Dinosaurs) == 0:
		Unlock(Unlocks.Dinosaurs)
	elif item == Items.Cactus and num_unlocked(Unlocks.Cactus) == 0:
		if num_unlocked(Unlocks.Senses) == 0:
			Unlock(Unlocks.Senses)
		Unlock(Unlocks.Cactus)
	elif item == Items.Carrot and num_unlocked(Unlocks.Carrots) == 0:
		Unlock(Unlocks.Carrots)
	elif item == Items.Gold and num_unlocked(Unlocks.Mazes) == 0:
		if num_unlocked(Unlocks.Fertilizer) == 0:
			Unlock(Unlocks.Fertilizer)
		Unlock(Unlocks.Mazes)
	elif item == Items.Power and num_unlocked(Unlocks.Sunflowers) == 0:
		if num_unlocked(Unlocks.Trees) == 0:
			Unlock(Unlocks.Trees)
		Unlock(Unlocks.Sunflowers)
	elif item == Items.Wood and num_unlocked(Unlocks.Plant) == 0:
		if num_unlocked(Unlocks.Speed) == 0:
			Unlock(Unlocks.Speed)
		Unlock(Unlocks.Plant)