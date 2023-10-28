from cs50 import SQL
import csv
from datetime import date
import pandas as pd
from termcolor import colored
import numpy as np

db = SQL("sqlite:///asl.db")
totalgames = db.execute("SELECT COUNT(*) FROM games")[0]['COUNT(*)']

playerids = []
rows = db.execute("SELECT id FROM people")
for dct in rows:
    playerids.append(dct['id'])

gameids = []
rows = db.execute("SELECT id FROM games")
for dct in rows:
    gameids.append(dct['id'])

baseday = (2016, 1, 1)

#Helpers
def datetoday(today, base):
    now = date(*today)
    then = date(*base)
    delta = now - then
    return delta.days

#K-means clustering
def cluster(k, dataset):
    size = len(dataset)
    previous = 0
    intervals = []
    for i in range(size // k, size, size // k):
        interval = (previous, dataset[i]['duration'])
        #Avoid single minute intervals
        if interval[0] >= interval[1]:
            interval = (previous, previous+1)
        previous = dataset[i]['duration'] + 1
        #Avoid overlaps
        if interval not in intervals:
            intervals.append(interval)
    #Make the last interval open-ended (50 represents a value just higher than the highest game duration value in the database)
    intervals[-1] = (intervals[-1][0], 50)
    return intervals

def duration2minsec(duration):
    totalseconds = (int(duration) * 60 + 30) + (int((duration - int(duration)) * 60))
    minutes = totalseconds // 60
    seconds = totalseconds % 60
    return (minutes, seconds)
    

#Queries
def mostgames():
    gamecounts = []
    for player in playerids:
        handle = db.execute("SELECT handle FROM handles WHERE id = ?", player)[0]['handle']
        gamecount = db.execute("SELECT count(id) FROM players WHERE player_id = ?", player)[0]['count(id)']
        gamecounts.append((handle, gamecount))
    gamecounts.sort(key=lambda x: x[1], reverse=True)

    with open('data/1mostgames.csv', 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(('Player', 'Games'))
        writer.writerows(gamecounts)
    print(colored("Most games ranking saved to csv.", 'green'))

def mostgamesASLONLY():    
    gamecounts = []
    for player in playerids:
        handle = db.execute("SELECT handle FROM handles WHERE id = ?", player)[0]['handle']
        gamecount = db.execute("SELECT count(id) FROM players WHERE player_id = ? AND game_id IN (SELECT id FROM games WHERE tournament = 'ASL')", player)[0]['count(id)']
        gamecounts.append((handle, gamecount))
    gamecounts.sort(key=lambda x: x[1], reverse=True)

    with open('data/2mostgamesASLONLY.csv', 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(('Player', 'Games'))
        writer.writerows(gamecounts)
    print(colored("Most games (ASL only) saved to csv.", 'green'))

def playerwinrates():
    winrates = {}
    winrates['Total'] = {}
    winratelist = []
    for player in playerids:
        winrates['Total'][player] = {}
        handle = db.execute("SELECT handle FROM handles WHERE id = ?", player)[0]['handle']
        winrates['Total'][player]['Name'] = handle
        wins = db.execute("SELECT count(id) FROM games WHERE winner_id = ?", player)[0]['count(id)']
        losses = db.execute("SELECT count(id) FROM games WHERE loser_id = ?", player)[0]['count(id)']
        if wins + losses > 14:
            winrate = round((wins / (wins + losses)) * 100, 2)
            winrates['Total'][player]['Games'] = wins + losses
            winrates['Total'][player]['Winrate'] = winrate
            winratelist.append(winrates['Total'][player])

    winratelist.sort(key = lambda x: x['Winrate'], reverse=True)
    for i, item in enumerate(winratelist):
        item['Rank'] = i + 1
    
    fieldnames = ['Rank', 'Name', 'Games', 'Winrate']
    with open('data/3playerwinratesTotal.csv', 'w', newline='') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(winratelist)
    print(colored('Total player winrates saved to csv.', 'green'))

    for mirror in ['TvT', 'PvP', 'ZvZ']:
        winrates[mirror] = {}
        winratelist = []
        for player in playerids:
            winrates[mirror][player] = {}
            handle = db.execute("SELECT handle FROM handles WHERE id = ?", player)[0]['handle']
            winrates[mirror][player]['Name'] = handle
            wins = db.execute("SELECT count(id) FROM games WHERE winner_id = ? AND matchup = ?", player, mirror)[0]['count(id)']
            losses = db.execute("SELECT count(id) FROM games WHERE loser_id = ? AND matchup = ?", player, mirror)[0]['count(id)']
            if wins + losses > 10:
                winrate = (wins / (wins + losses)) * 100
                winrates[mirror][player]['Games'] = wins + losses
                winrates[mirror][player]['Winrate'] = round(winrate, 2)
                winratelist.append(winrates[mirror][player])
        
        winratelist.sort(key = lambda x: x['Winrate'], reverse=True)
        for i, item in enumerate(winratelist):
            item['Rank'] = i + 1
        
        fieldnames = ['Rank', 'Name', 'Games', 'Winrate']
        with open('data/3playerwinrates' + mirror + '.csv', 'w', newline='') as outfile:
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(winratelist)
        print(colored(f'{mirror} player winrates saved to csv.', 'green'))

    for matchup in (('TvP', 'PvT', 'Terran', 'Protoss'), ('TvZ', 'ZvT', 'Terran', 'Zerg'), ('PvZ', 'ZvP', 'Protoss', 'Zerg')):
        winratelists = {matchup[0]: [], matchup[1]: []}
        winrates[matchup[0]] = {}
        winrates[matchup[1]] = {}
        for player in playerids:
            winrates[matchup[0]][player] = {}
            winrates[matchup[1]][player] = {}
            handle = db.execute("SELECT handle FROM handles WHERE id = ?", player)[0]['handle']
            winrates[matchup[0]][player]['Name'] = handle
            winrates[matchup[1]][player]['Name'] = handle

            wins = db.execute("SELECT id FROM games WHERE winner_id = ? AND matchup = ?", player, matchup[0])
            race1wins = race2wins = 0
            for row in wins:
                race = db.execute("SELECT race FROM players WHERE game_id = ? AND player_id = ?", row['id'], player)[0]['race']
                if race == matchup[2]:
                    race1wins += 1
                elif race == matchup[3]:
                    race2wins += 1
                else:
                    raise Exception("Race not belonging in matchup found")

            losses = db.execute("SELECT id FROM games WHERE loser_id = ? AND matchup = ?", player, matchup[0])
            race1losses = race2losses = 0
            for row in losses:
                race = db.execute("SELECT race FROM players WHERE game_id = ? AND player_id = ?", row['id'], player)[0]['race']
                if race == matchup[2]:
                    race1losses += 1
                elif race == matchup[3]:
                    race2losses += 1
                else:
                    raise Exception("Race not belonging in matchup found")
            
            if race1wins + race1losses > 9:
                winrates[matchup[0]][player]['Games'] = race1wins + race1losses
                if race1losses > 0:
                    winrate1 = (race1wins / (race1wins + race1losses)) * 100
                    winrates[matchup[0]][player]['Winrate'] = round(winrate1, 2)
                elif race1losses == 0 and race1wins > 0:
                    winrate1 = 100
                    winrates[matchup[0]][player]['Winrate'] = round(winrate1, 2)
                else:
                    winrates[matchup[0]][player]['Winrate'] = None
            
            if race2wins + race2losses > 9:
                winrates[matchup[1]][player]['Games'] = race2wins + race2losses
                if race2losses > 0:
                    winrate2 = (race2wins / (race2wins + race2losses)) * 100
                    winrates[matchup[1]][player]['Winrate'] = round(winrate2, 2)
                elif race2losses == 0 and race2wins > 0:
                    winrate2 = 100
                    winrates[matchup[1]][player]['Winrate'] = round(winrate2, 2)
                else:
                    winrates[matchup[1]][player]['Winrate'] = None

            if 'Winrate' in winrates[matchup[0]][player]:
                winratelists[matchup[0]].append(winrates[matchup[0]][player])
            if 'Winrate' in winrates[matchup[1]][player]:
                winratelists[matchup[1]].append(winrates[matchup[1]][player])
        
        for i in [0, 1]:
            winratelists[matchup[i]].sort(key = lambda x: x['Winrate'], reverse=True)
            for j, item in enumerate(winratelists[matchup[i]]):
                item['Rank'] = j + 1
            
            fieldnames = ['Rank', 'Name', 'Games', 'Winrate']
            with open('data/3playerwinrates' + matchup[i] + '.csv', 'w', newline='') as outfile:
                writer = csv.DictWriter(outfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(winratelists[matchup[i]])
            print(colored(f'{matchup[i]} player winrates saved to csv.', 'green'))

def maxminwinrates():
    winratelist = []
    for player in playerids:
        winrates = {}
        handle = db.execute("SELECT handle FROM handles WHERE id = ?", player)[0]['handle']
        winrates['Name'] = handle
        wins = db.execute("SELECT count(id) FROM games WHERE winner_id = ?", player)[0]['count(id)']
        losses = db.execute("SELECT count(id) FROM games WHERE loser_id = ?", player)[0]['count(id)']
        if wins + losses < 15:
            continue
        if losses > 0:
            winrate = (wins / (wins + losses)) * 100

        winrates['Total'] = round(winrate, 2)

        for mirror in ('TvT', 'PvP', 'ZvZ'):
            mwins = db.execute("SELECT count(id) FROM games WHERE matchup = ? AND winner_id = ?", mirror, player)[0]['count(id)']
            mlosses = db.execute("SELECT count(id) FROM games WHERE matchup = ? AND loser_id = ?", mirror, player)[0]['count(id)']
            if mwins + mlosses > 14:
                mwinrate = (mwins / (mwins + mlosses)) * 100
                winrates[mirror] = round(mwinrate, 2)
            else:
                winrates[mirror] = None            
        
        for matchup in (('TvP', 'PvT', 'Terran', 'Protoss'), ('TvZ', 'ZvT', 'Terran', 'Zerg'), ('PvZ', 'ZvP', 'Protoss', 'Zerg')):
            wins = db.execute("SELECT id FROM games WHERE winner_id = ? AND matchup = ?", player, matchup[0])
            race1wins = race2wins = 0
            for row in wins:
                race = db.execute("SELECT race FROM players WHERE game_id = ? AND player_id = ?", row['id'], player)[0]['race']
                if race == matchup[2]:
                    race1wins += 1
                elif race == matchup[3]:
                    race2wins += 1
                else:
                    raise Exception("Race not belonging in matchup found")

            losses = db.execute("SELECT id FROM games WHERE loser_id = ? AND matchup = ?", player, matchup[0])
            race1losses = race2losses = 0
            for row in losses:
                race = db.execute("SELECT race FROM players WHERE game_id = ? AND player_id = ?", row['id'], player)[0]['race']
                if race == matchup[2]:
                    race1losses += 1
                elif race == matchup[3]:
                    race2losses += 1
                else:
                    raise Exception("Race not belonging in matchup found")
            
            if race1wins + race1losses > 14:
                winrate1 = (race1wins / (race1wins + race1losses)) * 100
                winrates[matchup[0]] = round(winrate1, 2)
            else:
                winrates[matchup[0]] = None

            if race2wins + race2losses > 14:
                winrate2 = (race2wins / (race2wins + race2losses)) * 100
                winrates[matchup[1]] = round(winrate2, 2)
            else:
                winrates[matchup[1]] = None

        winratelist.append(winrates)

    matchups = ['TvT', 'PvP', 'ZvZ', 'TvP', 'PvT', 'TvZ', 'ZvT', 'PvZ', 'ZvP']
    array = np.zeros((len(winratelist), 9))
    for i, player in enumerate(winratelist):
        for j, matchup in enumerate(matchups):
            array[i,j] = player[matchup]
    
    import copy
    toparray = copy.deepcopy(array)
    top5 = []
    for n in range(5):
        highest = 0
        for i in range(len(winratelist)):
            for j in range(9):
                if toparray[i,j] > highest:
                    highest = toparray[i,j]
                    ind = (i,j)
        top5.append(ind)
        toparray[ind[0], ind[1]] = 0

    bottomarray = copy.deepcopy(array)
    bottom5 = []
    for n in range(5):
        lowest = 101
        for i in range(len(winratelist)):
            for j in range(9):
                if bottomarray[i,j] < lowest:
                    lowest = bottomarray[i,j]
                    ind = (i,j)
        bottom5.append(ind)
        bottomarray[ind[0], ind[1]] = 101
    print(bottom5)
    
    toplist = []
    for i, idx in enumerate(top5):
        record = {}
        record['Rank'] = i + 1
        record['Name'] = winratelist[idx[0]]['Name']
        record['Matchup'] = matchups[idx[1]]
        record['Winrate'] = winratelist[idx[0]][matchups[idx[1]]]
        toplist.append(record)

    with open('data/3playerwinratesAnyMatchupBest.csv', 'w', newline='') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=['Rank', 'Name', 'Matchup', 'Winrate'])
        writer.writeheader()
        writer.writerows(toplist)
    print(colored("Top winrates across matchups saved to csv.", 'green'))

    bottomlist = []
    for i, idx in enumerate(bottom5):
        record = {}
        record['Rank'] = i + 1
        record['Name'] = winratelist[idx[0]]['Name']
        record['Matchup'] = matchups[idx[1]]
        record['Winrate'] = winratelist[idx[0]][matchups[idx[1]]]
        bottomlist.append(record)

    with open('data/3playerwinratesAnyMatchupWorst.csv', 'w', newline='') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=['Rank', 'Name', 'Matchup', 'Winrate'])
        writer.writeheader()
        writer.writerows(bottomlist)
    print(colored("Bottom winrates across matchups saved to csv.", 'green'))

def racesmostgames():
    terran = db.execute("SELECT count(id) FROM games WHERE matchup = 'TvP' OR matchup = 'TvZ' OR matchup = 'TvT'")[0]['count(id)']
    protoss = db.execute("SELECT count(id) FROM games WHERE matchup = 'PvP' OR matchup = 'PvZ' OR matchup = 'TvP'")[0]['count(id)']
    zerg = db.execute("SELECT count(id) FROM games WHERE matchup = 'PvZ' OR matchup = 'TvZ' OR matchup = 'ZvZ'")[0]['count(id)']
    print("Games involving at least one player of race:")
    print(f"Terran: {terran}")
    print(f"Protoss: {protoss}")
    print(f"Zerg: {zerg}")

def racestotalwinrates():
    for cuttop in ['n', 'y']: 
        if cuttop == 'y':
            condition = [4,10,23]
            spec = ' without top player'
        else:
            condition = [50,50,50]
            spec = ''
        for race in [['Terran', 'TvZ', 'TvP'], ['Protoss', 'TvP', 'PvZ'], ['Zerg', 'TvZ', 'PvZ']]:
            wins = db.execute("SELECT COUNT(*) FROM games JOIN players ON games.id = players.game_id AND games.winner_id = players.player_id WHERE race = ? AND (matchup = ? OR matchup = ?) AND games.winner_id != ? AND games.winner_id != ? AND games.winner_id != ?", race[0], race[1], race[2], *condition)[0]['COUNT(*)']
            losses = db.execute("SELECT COUNT(*) FROM games JOIN players ON games.id = players.game_id AND games.loser_id = players.player_id WHERE race = ? AND (matchup = ? OR matchup = ?) AND games.loser_id != ? AND games.loser_id != ? AND games.loser_id != ?", race[0], race[1], race[2], *condition)[0]['COUNT(*)']
            print(f"Total {race[0]} winrate{spec}: {round(wins / (wins + losses) * 100, 2)}%")

def elo():
    ratings = {}
    timeseries = {}
    k = 30
    for player in playerids:
         ratings[player] = {}
         handle = db.execute("SELECT handle FROM handles WHERE id = ?", player)[0]['handle']
         ratings[player]['Name'] = handle
         ratings[player]['Games'] = 0
         ratings[player]['Rating'] = 1600
         timeseries[player] = {}
         timeseries[player]['Name'] = handle
         timeseries[player][0] = None

    for game in gameids:
        rows = db.execute("SELECT winner_id, loser_id, gameday, gamemonth, gameyear FROM games WHERE id = ?", game)
        day = datetoday((rows[0]['gameyear'], rows[0]['gamemonth'], rows[0]['gameday']), baseday)        
        ratings[rows[0]['winner_id']]['Games'] += 1
        ratings[rows[0]['loser_id']]['Games'] += 1
        ra = ratings[rows[0]['winner_id']]['Rating']
        rb = ratings[rows[0]['loser_id']]['Rating']
        ea = 1 / (1 + pow(10, (rb - ra) / 400))
        eb = 1 / (1 + pow(10, (ra - rb) / 400))
        ratings[rows[0]['winner_id']]['Rating'] += k * (1 - ea)
        ratings[rows[0]['loser_id']]['Rating'] += k * (0 - eb)
        timeseries[rows[0]['winner_id']][day] = round(ratings[rows[0]['winner_id']]['Rating'])
        timeseries[rows[0]['loser_id']][day] = round(ratings[rows[0]['loser_id']]['Rating'])

    ratinglist = []
    for primary,nested in ratings.items():
        if nested['Games'] > 19:
            nested['Rating'] = round(nested['Rating'])
            ratinglist.append(nested)
    ratinglist.sort(key = lambda x: x['Rating'], reverse=True)

    with open('data/4elo.csv', 'w', newline='') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=['Name', 'Games', 'Rating'])
        writer.writeheader()
        writer.writerows(ratinglist)
    print(colored("Elo ranking list saved to csv.", 'green'))
    
    for player in playerids:
        timeseries[player][0] = None
        for d in range(1, day+1):
            if d not in timeseries[player]:
                timeseries[player][d] = timeseries[player][d-1]

    fieldnames = ['Name'] + list(range(0, day+1))
    timeserieslist = []
    for primary, nested in timeseries.items():
        timeserieslist.append(nested)
    timeserieslist.sort(key = lambda x: (x[day] is not None, x[day]), reverse=True)

    with open('data/5elotimeseries.csv', 'w', newline='') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(timeserieslist)
    print(colored("Elo time series saved to csv.", 'green'))

def seriesgames():
    rows = db.execute("SELECT * FROM series")
    reversesweeps = {}
    for f in [5,7]:
        game1wins = 0
        game2wins = 0
        game3wins = 0
        game4wins = 0
        total = 0
        reversesweeps[f] = 0
        rtotal = 0
        for row in rows:
            reversesweep = 1
            if row['format'] != f:
                continue
            winner = row['winner_id']
            games = db.execute("SELECT winner_id FROM games WHERE id > ? ORDER BY id LIMIT ?", row['firstgame'] - 1, row['format'])
            if winner == games[0]['winner_id']:
                game1wins += 1
            if winner == games[1]['winner_id']:
                game2wins += 1
            if winner == games[2]['winner_id']:
                game3wins += 1
            if f == 7 and winner == games[3]['winner_id']:
                game4wins += 1
            
            winners = set()
            for i in range(0,f-3):
                winners.add(games[i]['winner_id'])
                if games[i]['winner_id'] == winner:
                    reversesweep = 0
                if i == f-4 and len(winners) == 1:
                    rtotal += 1
            reversesweeps[f] += reversesweep
            total += 1

        for i, game in enumerate([game1wins, game2wins, game3wins, game4wins]):
            print(f"In {total} best of {f} series, winner of game {i+1} was series winner {round(game / total * 100, 2)}% of the time")
        print(f"Probability of reverse sweep in best of {f}: {round(reversesweeps[f] / rtotal * 100, 2)}")

def mapselection():
    df = pd.DataFrame(db.execute("SELECT winner_id, loser_id, mapchoice, gamenumber, tournament, matchup FROM games WHERE mapchoice IS NOT NULL AND mapchoice != 'none' AND mapchoice != ''"))
    df['mapchoice'] = df['mapchoice'].astype(int)
    df['tournament'].replace({"ASL": 0, "KSL": 1}, inplace=True)
    df['matchup'].replace({"TvT": 1, "PvP": 1, "ZvZ": 1, "TvP": 0, "TvZ": 0, "PvZ": 0}, inplace=True)

    lost = df.loc[(df['loser_id'] == df['mapchoice']) & (df['tournament'] == 0)].shape[0]
    won = df.loc[(df['winner_id'] == df['mapchoice']) & (df['tournament'] == 0)].shape[0]
    print(f"Map chooser won {round(won / (won + lost) * 100, 2)}% of the time")
    
    lost1 = df.loc[(df['loser_id'] == df['mapchoice']) & (df['gamenumber'] == 1)].shape[0]
    won1 = df.loc[(df['winner_id'] == df['mapchoice']) & (df['gamenumber'] == 1)].shape[0]
    print(f"Game 1 chooser won {round(won1 / (won1 + lost1) * 100, 2)}% of the time")

    lost = df.loc[(df['loser_id'] == df['mapchoice']) & (df['matchup'] == 0) & (df['tournament'] == 0)].shape[0]
    won = df.loc[(df['winner_id'] == df['mapchoice']) & (df['matchup'] == 0) & (df['tournament'] == 0)].shape[0]
    print(f"In non-mirror matchups, map chooser won {round(won / (won + lost) * 100, 2)}% of the time")

    lost1 = df.loc[(df['loser_id'] == df['mapchoice']) & (df['matchup'] == 0) & (df['gamenumber'] == 1)].shape[0]
    won1 = df.loc[(df['winner_id'] == df['mapchoice']) & (df['matchup'] == 0) & (df['gamenumber'] == 1)].shape[0]
    print(f"In non-mirror matchups, game 1 chooser won {round(won1 / (won1 + lost1) * 100, 2)}% of the time")

def matchupwinrates():
    fieldnames = ['Race'] + list(range(2016, 2024))
    
    for cuttop in ['n', 'y']: 
        if cuttop == 'y':
            condition = [4,10,23]
            extension = 'NoTopPlayers'
            spec = ' without top players'
        else:
            condition = [50,50,50]
            extension = ''
            spec = ''

        for matchup in ("TvP", "TvZ", "PvZ"):
            matchupyears = {}
            overall = {}
            if matchup == "TvP":
                races = ["Terran", "Protoss"]
            elif matchup == "TvZ":
                races = ["Terran", "Zerg"]
            elif matchup == "PvZ":
                races = ["Protoss", "Zerg"]
            overall[races[0]] = overall[races[1]] = 0
            
            matchupyears[races[0]] = {"Race": races[0]}
            matchupyears[races[1]] = {"Race": races[1]}
            for year in range(2016, 2024):
                race1wins = db.execute("SELECT COUNT(*) FROM games JOIN players ON games.id = players.game_id AND games.winner_id = players.player_id WHERE matchup = ? AND race = ? AND gameyear = ? AND games.winner_id != ? AND games.winner_id != ? AND games.winner_id != ?", matchup, races[0], year, *condition)[0]['COUNT(*)']
                race2wins = db.execute("SELECT COUNT(*) FROM games JOIN players ON games.id = players.game_id AND games.winner_id = players.player_id WHERE matchup = ? AND race = ? AND gameyear = ? AND games.winner_id != ? AND games.winner_id != ? AND games.winner_id != ?", matchup, races[1], year, *condition)[0]['COUNT(*)']
                matchupyears[races[0]][year] = round(race1wins / (race1wins + race2wins) * 100, 2)    
                matchupyears[races[1]][year] = round(race2wins / (race1wins + race2wins) * 100, 2)
                overall[races[0]] += race1wins
                overall[races[1]] += race2wins
            
            with open('data/6' + matchup + 'timeseries' + extension + '.csv', 'w', newline='') as outfile:
                writer = csv.DictWriter(outfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerow(matchupyears[races[0]])
                writer.writerow(matchupyears[races[1]])

            print(f"Overall {matchup} winrate: \n{races[0]}: {round(overall[races[0]] / (overall[races[0]] + overall[races[1]]) * 100, 2)}%\n{races[1]}: {round(overall[races[1]] / (overall[races[0]] + overall[races[1]]) * 100, 2)}%")
            print(colored(f"{matchup} yearly winrates{spec} saved to csv", 'green'))

def matchupfrequency():
    matchups = {}
    for matchup in ("TvP", "TvZ", "PvZ", "TvT", "PvP", "ZvZ"):
        matchups[matchup] = {}
        matchups[matchup]['count'] = db.execute("SELECT COUNT(*) FROM games WHERE matchup = ?", matchup)[0]['COUNT(*)']
        matchups[matchup]['percentage'] = round(matchups[matchup]['count'] / totalgames * 100, 2)
        print(f"{matchups[matchup]['count']} games, or {matchups[matchup]['percentage']}% of all games, were {matchup}")

def mapfeatures():
    for feature in ("size", "spawns", "island", "highgroundmain"):
        featuredata = []
        fieldnames = [feature, "Matchup", "Terran", "Protoss", "Zerg"]
        features = db.execute(f"SELECT DISTINCT({feature}) FROM maps ORDER BY ?", feature)

        for featurecount in features:
            for matchup in ("TvP", "TvZ", "PvZ"):
                thismatchup = {feature: featurecount[feature], "Matchup": matchup}
                if matchup == "TvP":
                    races = ["Terran", "Protoss"]
                elif matchup == "TvZ":
                    races = ["Terran", "Zerg"]
                elif matchup == "PvZ":
                    races = ["Protoss", "Zerg"]
            
                race1wins = db.execute(f"SELECT COUNT(*) FROM games JOIN players ON games.id = players.game_id AND games.winner_id = players.player_id WHERE matchup = ? AND race = ? AND map_id IN (SELECT id FROM maps WHERE {feature} = ?)", matchup, races[0], featurecount[feature])[0]['COUNT(*)']
                race2wins = db.execute(f"SELECT COUNT(*) FROM games JOIN players ON games.id = players.game_id AND games.winner_id = players.player_id WHERE matchup = ? AND race = ? AND map_id IN (SELECT id FROM maps WHERE {feature} = ?)", matchup, races[1], featurecount[feature])[0]['COUNT(*)']
                thismatchup[races[0]] = round(race1wins / (race1wins + race2wins) * 100, 2)
                thismatchup[races[1]] = round(race2wins / (race1wins + race2wins) * 100, 2)
                print(f"On {feature}: {featurecount[feature]} maps, in {matchup}, {races[0]} won {race1wins} games, while {races[1]} won {race2wins} games.")
                
                featuredata.append(thismatchup)
        
            with open('data/7' + feature + '.csv', 'w', newline='') as outfile:
                writer = csv.DictWriter(outfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(featuredata)
            print(colored(f"Matchup winrates by map {feature} saved to csv.", 'green'))
        
def tilesets():
    tilesets = db.execute("SELECT DISTINCT(tileset) FROM maps")
    tilesetfrequency = {}
    for tileset in tilesets:
        tileset = tileset['tileset']
        tilesetfrequency[tileset] = {}
        tilesetfrequency[tileset]['gamecount'] = db.execute("SELECT COUNT(*) FROM games WHERE map_id IN (SELECT id FROM maps WHERE tileset = ?)", tileset)[0]['COUNT(*)']
        tilesetfrequency[tileset]['gamepercentage'] = round(tilesetfrequency[tileset]['gamecount'] / totalgames * 100, 2)
        print(f"{tilesetfrequency[tileset]['gamecount']} games, or {tilesetfrequency[tileset]['gamepercentage']}% of all games, were played on {tileset} tileset.")

def mapbalance():
    #Get list of maps to loop through
    rows = db.execute("SELECT id, name FROM maps")
    maps = []
    
    #Initialize final data list
    mapdata = []
    
    for row in rows:
        maps.append(row)
    #Loop through all maps in database
    for map in maps:
        #Initialize data dictionary for current map
        thismap = {"Map": map['name']}
        #For each map, get all games played on this map. Exclude mirror matchup games (e.g. Terran vs Terran) because this insight is about whether matches between DIFFERENT races are balanced on each map or not
        nonmirrorgamesonmap = db.execute("SELECT COUNT(id) FROM games WHERE map_id = ?", map['id'])[0]['COUNT(id)']
        #Skip maps that too few games have been played on to draw any meaningful conclusions about them
        if nonmirrorgamesonmap < 40:
            continue
        #Store amount of games played on map
        thismap['Total games'] = nonmirrorgamesonmap
        #For each of the three non-mirror matchups (Terran vs Protoss, Terran vs Zerg, and Protoss vs Zerg), compare the amount of wins for each race on the current map
        for matchup in ("TvP", "TvZ", "PvZ"):
            #Derive the races involved in the matchup, for use in the next database query (this is the kind of minor workaround I wouldn't have needed if I had abandoned the "Players" table in the database and instead put race data in the "Games" table)
            if matchup == "TvP":
                races = ["Terran", "Protoss"]
            elif matchup == "TvZ":
                races = ["Terran", "Zerg"]
            elif matchup == "PvZ":
                races = ["Protoss", "Zerg"]
            #Query the database for the amount of wins for each race in the current matchup on the current map
            race1wins = db.execute("SELECT COUNT(*) FROM games JOIN players ON games.id = players.game_id AND games.winner_id = players.player_id WHERE matchup = ? AND race = ? AND map_id = ?", matchup, races[0], map['id'])[0]['COUNT(*)']
            race2wins = db.execute("SELECT COUNT(*) FROM games JOIN players ON games.id = players.game_id AND games.winner_id = players.player_id WHERE matchup = ? AND race = ? AND map_id = ?", matchup, races[1], map['id'])[0]['COUNT(*)']
            #Store the winrate percentage for each matchup in the data dictionary
            thismap[matchup] = round(race1wins / (race1wins + race2wins) * 100, 1)
       
        #Add this map's data dictionary to the overall list
        mapdata.append(thismap)

    #Now that we have the winrates for each matchup for each map, we can score the maps according to how balanced they are
    import math
    for mapstats in mapdata:
        error = 0
        #Increment error for current map according to how far it is from perfect balance (50% winrate) in each matchup
        for winrate in [mapstats['TvP'], mapstats['TvZ'], mapstats['PvZ']]:
            #Using RMSE in order to punish strong deviance in a single matchup harder than moderate deviance in multiple matchups
            error += (abs(winrate - 50) * abs(winrate - 50)) / 3
        #Store balance score as 100 minus the error
        mapstats['Balance score'] = round(100 - math.sqrt(error), 1)
    #Sort the maps according to their balance score
    mapdata.sort(key = lambda x: x['Balance score'], reverse=True)

    #Save the map balance score sheet to csv
    fieldnames = ['Map', 'Total games', 'TvP', 'TvZ', 'PvZ', 'Balance score']
    with open('data/8mapbalance.csv', 'w', newline='') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(mapdata)
    print(colored(f"Map balance sheet saved to csv.", 'green'))

def seeds():
    seedavg = db.execute("SELECT AVG(result) FROM seasons WHERE tier = 0")[0]['AVG(result)']
    nonseedavg = db.execute("SELECT AVG(result) FROM seasons WHERE player_id IN (SELECT DISTINCT(player_id) FROM seasons WHERE tier = 0) AND tier != 0")[0]['AVG(result)']
    print(f"Average result of seeded player: {round(seedavg, 3)}.\nAverage result of non-seeded player: {round(nonseedavg, 3)}")

    seed2seed = db.execute("SELECT COUNT(id) FROM seasons WHERE tier = 0 AND result <= 4")[0]['COUNT(id)']
    seed2nonseed = db.execute("SELECT COUNT(id) FROM seasons WHERE tier = 0 AND result > 4")[0]['COUNT(id)']
    nonseed2seed = db.execute("SELECT COUNT(id) FROM seasons WHERE tier != 0 AND player_id IN (SELECT DISTINCT(player_id) FROM seasons WHERE tier = 0) AND result <= 4")[0]['COUNT(id)']
    nonseed2nonseed = db.execute("SELECT COUNT(id) FROM seasons WHERE tier != 0 AND player_id IN (SELECT DISTINCT(player_id) FROM seasons WHERE tier = 0) AND result > 4")[0]['COUNT(id)']
    print(f"Probability of gaining seed as already seeded player: {round(seed2seed / (seed2seed + seed2nonseed) * 100, 2)}%.\nProbability of gaining seed as non-seeded player: {round(nonseed2seed / (nonseed2seed + nonseed2nonseed) * 100, 2)}%")
    
    print("Note: Both figures calculated comparing the same set of players - those who have played as seeded players in at least one season.")

def winnerslosers():
    loserswinners = db.execute("SELECT COUNT(*) FROM games LEFT JOIN series ON series.firstgame = games.id WHERE series.firstgame IN (SELECT id FROM games WHERE matchtype = 'decider') AND EXISTS (SELECT * FROM series AS series2 WHERE firstgame IN (SELECT id FROM games AS games2 WHERE games.tournament = games2.tournament AND games.round = games2.round AND games.season_id = games2.season_id AND matchtype = 'losers') AND series2.winner_id = series.winner_id)")[0]['COUNT(*)']
    winnerslosers = db.execute("SELECT COUNT(*) FROM games LEFT JOIN series ON series.firstgame = games.id WHERE series.firstgame IN (SELECT id FROM games WHERE matchtype = 'decider') AND EXISTS (SELECT * FROM series AS series2 WHERE firstgame IN (SELECT id FROM games AS games2 WHERE games.tournament = games2.tournament AND games.round = games2.round AND games.season_id = games2.season_id AND matchtype = 'winners') AND series2.loser_id = series.winner_id)")[0]['COUNT(*)']

    print(f"Winners' loser won {round(winnerslosers / (winnerslosers + loserswinners) * 100, 1)}% of decider matches, whereas losers' winner won {round(loserswinners / (winnerslosers + loserswinners) * 100, 1)}%")
            
def shortestlongestgames():
    rows = {}
    rows['shortest'] = db.execute("SELECT matchup, winner_id, loser_id, map_id, gameday, gamemonth, gameyear, tournament, season_id, duration FROM games ORDER BY duration LIMIT 10")
    rows['longest'] = db.execute("SELECT matchup, winner_id, loser_id, map_id, gameday, gamemonth, gameyear, tournament, season_id, duration FROM games ORDER BY duration DESC LIMIT 10")

    gamelists = {'longest': [], 'shortest': []}

    for key in rows:
        for row in rows[key]:
            thisrow = {}
            thisrow['Matchup'] = row['matchup']
            thisrow['Winner'] = db.execute("SELECT handle FROM handles WHERE id = ?", row['winner_id'])[0]['handle']
            thisrow['Loser'] = db.execute("SELECT handle FROM handles WHERE id = ?", row['loser_id'])[0]['handle']
            thisrow['Map'] = db.execute("SELECT name FROM maps WHERE id = ?", row['map_id'])[0]['name']
            thisrow['Date'] = f"{row['gameyear']}-{row['gamemonth']}-{row['gameday']}"
            thisrow['Tournament'] = row['tournament']
            thisrow['Season'] = row['season_id']
            thisrow['Duration'] = str(row['duration']) + ' minutes'
            gamelists[key].append(thisrow)
        
        fieldnames = []
        for k in gamelists[key][0]:
            fieldnames.append(k)
        with open('data/9' + key + 'games.csv', 'w', newline='') as outfile:
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(gamelists[key])
        print(colored(f"{key} games saved to csv.", 'green'))

def longestbymatchup():
    longestgames = []
    for matchup in ["TvP", "TvZ", "PvZ", "TvT", "PvP", "ZvZ"]:
        thisrow = {}
        rows = db.execute("SELECT winner_id, loser_id, map_id, gameday, gamemonth, gameyear, tournament, season_id, duration FROM games WHERE matchup = ? ORDER BY duration DESC LIMIT 1", matchup)[0]
        thisrow['Matchup'] = matchup
        thisrow['Winner'] = db.execute("SELECT handle FROM handles WHERE id = ?", rows['winner_id'])[0]['handle']
        thisrow['Loser'] = db.execute("SELECT handle FROM handles WHERE id = ?", rows['loser_id'])[0]['handle']
        thisrow['Map'] = db.execute("SELECT name FROM maps WHERE id = ?", rows['map_id'])[0]['name']
        thisrow['Date'] = f"{rows['gameyear']}-{rows['gamemonth']}-{rows['gameday']}"
        thisrow['Tournament'] = rows['tournament']
        thisrow['Season'] = rows['season_id']
        thisrow['Duration'] = str(rows['duration']) + ' minutes'
        longestgames.append(thisrow)

    fieldnames = []
    for k in longestgames[0]:
        fieldnames.append(k)
    with open('data/10longestgamesbymatchup.csv', 'w', newline='') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(longestgames)
        print(colored("Longest game by matchup saved to csv.", 'green'))

def matchupavgduration():
    minutes, seconds = duration2minsec(db.execute("SELECT AVG(duration) FROM games")[0]['AVG(duration)'])
    print(f"Average duration of all games in database: {minutes} minutes, {seconds} seconds")
    for matchup in ["TvP", "TvZ", "PvZ", "TvT", "PvP", "ZvZ"]:
        minutes, seconds = duration2minsec(db.execute("SELECT AVG(duration) FROM games WHERE matchup = ?", matchup)[0]['AVG(duration)'])
        print(f"Average duration of {matchup} games: {minutes} minutes {seconds} seconds")

def matchupwinratesbyduration():
    for matchup in ["TvP", "TvZ", "PvZ"]:
        thismatchup = {}
        if matchup == "TvP":
            races = ["Terran", "Protoss"]
        elif matchup == "TvZ":
            races = ["Terran", "Zerg"]
        elif matchup == "PvZ":
            races = ["Protoss", "Zerg"]
        thismatchup[races[0]] = {"Interval": races[0]}
        thismatchup[races[1]] = {"Interval": races[1]}

        dataset = db.execute("SELECT duration FROM games WHERE matchup = ? ORDER BY duration", matchup)
        intervals = cluster(12, dataset)
        for interval in intervals:
            race1wins = db.execute("SELECT COUNT(*) FROM games JOIN players ON games.id = players.game_id AND games.winner_id = players.player_id WHERE matchup = ? AND race = ? AND duration BETWEEN ? AND ?", matchup, races[0], interval[0], interval[1])[0]['COUNT(*)']
            race2wins = db.execute("SELECT COUNT(*) FROM games JOIN players ON games.id = players.game_id AND games.winner_id = players.player_id WHERE matchup = ? AND race = ? AND duration BETWEEN ? AND ?", matchup, races[1], interval[0], interval[1])[0]['COUNT(*)']

            thismatchup[races[0]][str(interval[0]) + '-' + str(interval[1])] = round(race1wins / (race1wins + race2wins) * 100, 2)
            thismatchup[races[1]][str(interval[0]) + '-' + str(interval[1])] = round(race2wins / (race1wins + race2wins) * 100, 2)
        fieldnames = []
        for k in thismatchup[races[0]]:
            fieldnames.append(k)
        with open('data/11' + matchup + 'WinratesByDuration.csv', 'w', newline='') as outfile:
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow(thismatchup[races[0]])
            writer.writerow(thismatchup[races[1]])

    print(colored("Matchup winrates by game duration saved to csv (one file for each non-mirror matchup)", 'green'))

def fastestslowestplayers():
    playerspeeds = []
    for player in playerids:
        handle = db.execute("SELECT handle FROM handles WHERE id = ?", player)[0]['handle']
        race = db.execute("SELECT mainrace FROM people WHERE id = ?", player)[0]['mainrace']
        rows = db.execute("SELECT COUNT(*), AVG(duration) FROM games JOIN players ON games.id = players.game_id WHERE winner_id = ? OR loser_id = ? AND EXISTS (SELECT * FROM players AS p2 WHERE p2.game_id = games.id AND p2.player_id = ? AND race = ?)", player, player, player, race)
        if rows[0]['COUNT(*)'] > 20:
            playerspeeds.append([handle, race, rows[0]['AVG(duration)']])

    playerspeeds.sort(key=lambda x: x[2])
    for player in playerspeeds:
        player[2] = str(duration2minsec(player[2])[0]) + ":" + (str(duration2minsec(player[2])[1]) if duration2minsec(player[2])[1] > 9 else '0' + str(duration2minsec(player[2])[1]))
    
    with open('data/12playerspeeds.csv', 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(['Name', 'Race', 'Avg. game duration'])
        writer.writerows(playerspeeds)
    print(colored("Player speeds saved to csv.", 'green'))

def playerwinratesbyduration():
    #Initialize final data list
    pwbyduration = []

    #Loop through list of players
    for player in playerids:
        #Get the player's name
        handle = db.execute("SELECT handle FROM handles WHERE id = ?", player)[0]['handle']
        #Skip players who have less than 50 games in the database, as it would be impossible to make meaningful statistics about those
        if db.execute("SELECT COUNT(*) FROM players WHERE player_id = ?", player)[0]['COUNT(*)'] < 50:
            continue
        #Initialize data dictionary for player
        thisplayer = {'Intervals': [], 'Winrates': [], 'name': handle}
        #Get the duration of all of this players games
        dataset = db.execute("SELECT duration FROM games WHERE winner_id = ? OR loser_id = ? ORDER BY duration", player, player)
        #Using k-means clustering, generate five duration intervals for the current player which each represents an even share of his total games 
        intervals = cluster(5, dataset)
        #Calculate this player's winrate for games with duration falling in each of these five intervals
        for interval in intervals:
            wins = db.execute("SELECT COUNT(*) FROM games WHERE games.winner_id = ? AND duration BETWEEN ? AND ?", player, interval[0], interval[1])[0]['COUNT(*)']
            losses = db.execute("SELECT COUNT(*) FROM games WHERE games.loser_id = ? AND duration BETWEEN ? AND ?", player, interval[0], interval[1])[0]['COUNT(*)']
            #Store intervals as text and winrates as float
            thisplayer['Intervals'].append(str(interval[0]) + '-' + str(interval[1])) 
            thisplayer['Winrates'].append(round(wins / (wins + losses) * 100, 2))
        
        #Search for players with high variance across the different time intervals (those will be the interesting ones, since they'll contradict the null hypothesis)
        total = 0
        count = 0
        #Calculate variance
        for v in thisplayer['Winrates']:
            total += v
            count += 1
        mean = total / count
        variance = 0
        for v in thisplayer['Winrates']:
            variance += abs(mean - v)
        #Store variance
        thisplayer['variance'] = variance
        #Add player's data dictionary to final data list
        pwbyduration.append(thisplayer)

    #Having calculated interval winrates and variance for all players, sort them by variance and save data for the 10 players with highest variance
    pwbyduration.sort(key=lambda x: x['variance'], reverse=True)
    for playerdata in pwbyduration[:10]:
        with open('data/PWbyduration/13' + playerdata['name'] + 'pwbd.csv', 'w', newline='') as outfile:
            #Strip player name (since that's now stored in the filename) and variance (since that has already served is purpose as the sorting criterion)
            del playerdata['name']
            del playerdata['variance']
            #Write data to csv
            writer = csv.writer(outfile)
            writer.writerow(['Intervals', 'Winrates'])
            for row in zip(playerdata['Intervals'], playerdata['Winrates']):
                writer.writerow(row)
    print(colored("Winrate by duration graphs for players with high variance saved to csv (one file for each player)", 'green'))

def crossspawnsduration():
    crossspawns = []
    overall = {}
    avgcross = db.execute("SELECT AVG(duration) FROM games WHERE crossspawns = 1")[0]['AVG(duration)']
    avgnocross = db.execute("SELECT AVG(duration) FROM games WHERE crossspawns = 0 AND map_id IN (SELECT id FROM maps WHERE spawns = 4)")[0]['AVG(duration)']

    overall['Matchup'] = "Overall"
    overall['Adjacent spawns'] = f"{duration2minsec(avgnocross)[0]}m{duration2minsec(avgnocross)[1]}s"
    overall['Cross spawns'] = f"{duration2minsec(avgcross)[0]}m{duration2minsec(avgcross)[1]}s"
    overall['Difference'] = round((avgcross - avgnocross) / avgnocross * 100, 2)

    crossspawns.append(overall)

    for matchup in ("TvP", "TvZ", "PvZ", "TvT", "PvP", "ZvZ"):
        thismatchup = {}
        avgcross = db.execute("SELECT AVG(duration) FROM games WHERE crossspawns = 1 AND matchup = ?", matchup)[0]['AVG(duration)']
        avgnocross = db.execute("SELECT AVG(duration) FROM games WHERE crossspawns = 0 AND map_id IN (SELECT id FROM maps WHERE spawns = 4) AND matchup = ?", matchup)[0]['AVG(duration)']

        thismatchup['Matchup'] = matchup
        thismatchup['Adjacent spawns'] = f"{duration2minsec(avgnocross)[0]}m{duration2minsec(avgnocross)[1]}s"
        thismatchup['Cross spawns'] = f"{duration2minsec(avgcross)[0]}m{duration2minsec(avgcross)[1]}s"
        thismatchup['Difference'] = round((avgcross - avgnocross) / avgnocross * 100, 2)

        crossspawns.append(thismatchup)

    fieldnames = ["Matchup", "Adjacent spawns", "Cross spawns", "Difference"]
    with open('data/14crossspawnsduration.csv', 'w', newline='') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(crossspawns)

    print(colored("Cross spawns duration table saved to csv.", 'green'))

def crossspawnswinrates():
    for matchup in ("TvP", "TvZ", "PvZ"):
        matchupspawns = {}
        if matchup == "TvP":
            races = ["Terran", "Protoss"]
        elif matchup == "TvZ":
            races = ["Terran", "Zerg"]
        elif matchup == "PvZ":
            races = ["Protoss", "Zerg"]
        
        matchupspawns[races[0]] = {"Race": matchup + races[0]}
        matchupspawns[races[1]] = {"Race": matchup + races[1]}
        for spawns in [(0, "Adjacent spawns"), (1, "Cross spawns")]:
            race1wins = db.execute("SELECT COUNT(*) FROM games JOIN players ON games.id = players.game_id AND games.winner_id = players.player_id WHERE matchup = ? AND race = ? AND crossspawns = ? AND map_id IN (SELECT id FROM maps WHERE spawns = 4)", matchup, races[0], spawns[0])[0]['COUNT(*)']
            race2wins = db.execute("SELECT COUNT(*) FROM games JOIN players ON games.id = players.game_id AND games.winner_id = players.player_id WHERE matchup = ? AND race = ? AND crossspawns = ? AND map_id IN (SELECT id FROM maps WHERE spawns = 4)", matchup, races[1], spawns[0])[0]['COUNT(*)']
            matchupspawns[races[0]][spawns[1]] = round(race1wins / (race1wins + race2wins) * 100, 2)    
            matchupspawns[races[1]][spawns[1]] = round(race2wins / (race1wins + race2wins) * 100, 2)

        print(f"In {matchup}, the winrate with adjacent spawns was {matchupspawns[races[0]]['Adjacent spawns'] if matchupspawns[races[0]]['Adjacent spawns'] > matchupspawns[races[1]]['Adjacent spawns'] else matchupspawns[races[1]]['Adjacent spawns']}% for {races[0] if matchupspawns[races[0]]['Adjacent spawns'] > matchupspawns[races[1]]['Adjacent spawns'] else races[1]}, whereas with cross spawns, it was {matchupspawns[races[0]]['Cross spawns'] if matchupspawns[races[0]]['Cross spawns'] > matchupspawns[races[1]]['Cross spawns'] else matchupspawns[races[1]]['Cross spawns']}% for {races[0] if matchupspawns[races[0]]['Cross spawns'] > matchupspawns[races[1]]['Cross spawns'] else races[1]}.")
    
