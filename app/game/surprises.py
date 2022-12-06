def get_300(player):
    player.money += 300
    return 'player {} just credited with free 300$'.format(player.id)


def lose_300(player):
    player.money -= 300
    return 'player {} just debited with 300$'.format(player.id)


SURPRISES = [lose_300, get_300]