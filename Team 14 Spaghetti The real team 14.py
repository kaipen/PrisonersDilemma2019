Team member = "Iori and Finn"

team_name = '[CENSORED]'
team_strat = 'B niCe'
strat_desc = 'If they betray then we betray, if not, then we collude'



def move(my_history, their_history, my_score, their_score):
  if len(my_history) == 0:
    return 'c'
  elif len(my_history) > 0:
    if (their_history[-1]) == 'b':
      return 'b'
    else:
      return 'c'

print move('b','c',100,200)
