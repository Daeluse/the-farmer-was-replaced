def Trade(item, count):
	cost = get_cost(item)
	for cost_item in cost:
		while num_items(cost_item) < cost[cost_item]:
			Grow(cost_item)
	if Is_Unlocked(Unlocks.Multi_Trade):
		trade(item, count)
	else:
		for i in range(count):
			trade(item)