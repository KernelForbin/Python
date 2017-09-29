__author__ = 'Kenny Mitchell'
#Problem 4
print('Welcome to Rock-Paper-Scissors Cheater!\nI hope you have fun!')

win_input = input('\nDo you want to win or lose? ')
wants_to_win = 0
if win_input == 'win':
	wants_to_win = True
elif win_input == 'lose':
    wants_to_win = False
else:
    print('You didn\'t choose "win" or "lose"! Defaulting to "win"...')
    wants_to_win = True

opp_choice = input('What did your opponent do? Enter r, p, or s. ')

if opp_choice == 'r':
	if wants_to_win:
		print('You should play "paper"')
	else:
		print('You should play "scissors"')
elif opp_choice == 'p':
	if wants_to_win:
		print('You should play "scissors"')
	else:
		print('You should play "rock"')
elif opp_choice == 's':
	if wants_to_win:
	    print('You should play "rock"')
	else:
	    print('You should play "paper"')
elif opp_choice == "":
		print('You didn\'t input anything!')
else:
	print('You didn\'t choose one of the options...')
print("\nHope you enjoyed! Run me again any time!\n")
input('Press the Enter Key To Exit...\n\n\n')
exit()
