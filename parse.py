with open('games.txt') as f:
    games = f.read().split('\n\n\n') 

for i, game_str in enumerate(games):
    game = game_str.splitlines() 
    try: 
        d = {}
        d['Event'] = game[0].split('\"')[1]
        d['Site'] = game[1].split('\"')[1]
        d['Date'] = game[2].split('\"')[1]
        d['Round'] = game[3].split('\"')[1]
        d['White'] = game[4].split('\"')[1]
        d['Black'] = game[5].split('\"')[1]
        d['Result'] = game[6].split('\"')[1]
        d['UTCDate'] = game[7].split('\"')[1]
        d['UTCTime'] = game[8].split('\"')[1]
        d['WhiteElo'] = game[9].split('\"')[1]
        d['BlackElo'] = game[10].split('\"')[1]

        if 'WhiteRatingDiff' in game_str:
            d['WhiteRatingDiff'] = game[11].split('\"')[1]
            d['BlackRatingDiff'] = game[12].split('\"')[1]
            d['Variant'] = game[13].split('\"')[1]
            d['TimeControl'] = game[14].split('\"')[1]
            d['ECO'] = game[15].split('\"')[1]
            d['Termination'] = game[16].split('\"')[1]

            if 'Chess960' in game_str:
                d['FEN'] = game[17].split('\"')[1]
                d['Setup'] = game[18].split('\"')[1]
                d['Moves'] = game[20]

            else:
                d['Moves'] = game[18]
        else:
            d['Variant'] = game[11].split('\"')[1]
            d['TimeControl'] = game[12].split('\"')[1]
            d['ECO'] = game[13].split('\"')[1]
            d['Termination'] = game[14].split('\"')[1]
            d['Moves'] = game[16]

        games[i] = d

    except: 
        print(game_str) 

victories = 24*[0]
losses = 24*[0]
draws = 24*[0]

def is_victory(game):
    return (game['Result'] == '0-1' and game['Black'] == 'aitotumainen') or (game['Result'] == '1-0' and game['White'] == 'aitotumainen')

def is_draw(game):
    return game['Result'] == '1/2-1/2'

for i, game in enumerate(games):
    time = game['UTCTime'].split(':')[0]

    if is_victory(game):
        victories[int(time)] += 1
    elif is_draw(game):
        draws[int(time)] += 1
    else:
        losses[int(time)] += 1

win_rate = [victories[i]/(victories[i]+losses[i]+draws[i])
        for i in range(24)]

import matplotlib.pyplot as plt
# TODO only for 10 standard games
# TODO plot weighted straight line 
plt.plot(victories)
plt.plot(losses)
#plt.plot(range(7,24),win_rate[7:])
plt.savefig('wins_and_losses.png')
