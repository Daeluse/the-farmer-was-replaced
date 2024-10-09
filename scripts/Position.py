def Move_To_Origin():
	while get_pos_x() > 0:
		move(West)
	while get_pos_y() > 0:
		move(South)
		
def Move_To(x, y):
	world_size = get_world_size()
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