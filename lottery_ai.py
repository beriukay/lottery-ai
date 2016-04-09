def main():
	# http://www.huffingtonpost.com/ronald-l-wasserstein/chances-of-winning-powerball-lottery_b_3288129.html
	chance_to_win_powerball = 1.0 / 175223510
	# Borrowed from Go AI: if chance of winning < 20%, give up.
	if chance_to_win_powerball < 0.2:
		print "Don't play"
	else:
		# TODO add logic here. Not a high priority at this time.
		print "pick from this list: ", 
		for i in range(100):
			print i,	







main()
