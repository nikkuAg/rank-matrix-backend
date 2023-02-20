from rank_matrix.constants.default import DEFAULT_NULL


def get_rank_color_code(user_rank, prediction_rank:int, delta:int):
	color = None
	if(user_rank == DEFAULT_NULL):
		color = "null"	
	else:
		user_rank = int(user_rank)
		if(user_rank <= round((1 - (delta / 100)) * prediction_rank)):
			color = 'green'
		elif ((user_rank > round((1 - (delta / 100)) * prediction_rank)) and (user_rank <= round(prediction_rank))):
			color = 'yellow'
		elif (user_rank > round(prediction_rank) and user_rank <= round((1 + (delta / 100)) * prediction_rank)):
			color = 'orange'
		elif (user_rank > round((1 + (delta / 100)) * prediction_rank)):
			color = 'red'

	return color