def Move_To_Origin():
	Move_To(0,0)
		
def Move_To(x, y):
	world_size = get_world_size() - 1
	if x < 0:
		x = 0
	if y < 0:
		y = 0
	if x > world_size:
		x = world_size
	if y > world_size:
		y = world_size
	while get_pos_x() > x:
		move(West)
	while get_pos_x() < x:
		move(East)
	while get_pos_y() > y:
		move(South)
	while get_pos_y() < y:
		move(North)

def Swap_To(x, y):
	prev_x = get_pos_x()
	prev_y = get_pos_y()
	world_size = get_world_size() - 1
	if x < 0:
		x = 0
	if y < 0:
		y = 0
	if x > world_size:
		x = world_size
	if y > world_size:
		y = world_size
	while get_pos_x() > x:
		swap(West)
		move(West)
	while get_pos_x() < x:
		swap(East)
		move(East)
	while get_pos_y() > y:
		swap(South)
		move(South)
	while get_pos_y() < y:
		move(North)
	Move_To(prev_x, prev_y)
		