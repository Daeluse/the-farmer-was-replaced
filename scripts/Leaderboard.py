def Run_Leaderboard():
	while num_unlocked(Unlocks.Leaderboard) == 0:
		Unlock(Get_Next_Unlock())
	timed_reset()