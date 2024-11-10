![Header](https://www.dropbox.com/scl/fi/kmuhyettn4t5h1ts1qa7w/ReadmeHeader.png?rlkey=rse5lb2rt6zlybx7y1xijmt55&raw=1)

# eSports data visualization

<br/>

<span style="font-size: 20px;"> In this project, I built a SQL database and used Python, SQL, Matplotlib, HTML and CSS to analyze and visualize in-depth data from 2,000 eSports games.</span>
<br/>


## Intro
Starcraft is the biggest eSport in history. While its popularity peaked between 2007 and 2011, it remains a widely played game to this day, with a sizeable following and tournaments with 5-figure (USD) prize pools. In spite of this, information about tournament results, game dynamics and player performance remains sporadic and scattered. When I noticed that a lot of data is openly available but poorly organized, I decided to take the opportunity to hone my skills in **data structuring, database/SQL querying, and data visualization**.

You can view the final product here:
<br/>

### [Stats from the ASL/KSL era of Starcraft 1](https://jackyvso.github.io/Starcraft) 
<br/>

All you need to know about Starcraft before you click:
- Each player chooses one of three **races** to play: **Terran**, **Protoss**, or **Zerg**. Each has its advantages and disadvantages. 
- A **matchup** refers to games between any two of these races (for example, if one player in a game plays as Terran and his opponent plays as Protoss, the matchup is Terran vs Protoss, or "TvP" for short)
- The two most prestigious Starcraft **tournaments** are called **ASL** and **KSL**

The webpage went live in October 2023 and was, two days later, [featured on the Twitch stream of Artosis](https://www.youtube.com/watch?v=prfbNBOraGg) - the most popular English-language Starcraft streamer.
<br/><br/>

![Starcraft crowd](https://www.dropbox.com/scl/fi/2eppzl5723sb8b1783ybg/SCcrowd.jpg?rlkey=4cgxe0cjulx5jwsfq7z5sy1d1&raw=1)

*Starcraft tournament in Seoul at the peak of the game's popularity* 
<br/><br/>

# How it works

The following is a behind-the-scenes tour of how I created this webpage using Python, SQL, matplotlib and HTML/CSS.

## 1. Structuring the database

What the architecture needed to do was allow querying for all relevant insights using as few loops as possible (to preserve time-efficiency) while also avoiding redundancy and being simple and legible.  
This is the schema I opted for:

![Database architecture](https://www.dropbox.com/scl/fi/scofstox9w93z4r2w9t63/databasevisualized.png?rlkey=ebyza9h5b7szybsmmyoikkco2&raw=1)

Having become wiser through the project, there are some things I would change if I was designing it now. The "Players" table, which stores the players involved in each game and the races they played as, was made in a misguided attempt to keep the "games" table lean. Having the races in a separate table from the rest of the data for each game necessitated some pretty hairy joins when I had to write queries for some of the insights later. But that at least had the effect of heightening my SQL query abilities !

While the "seasons" table (storing a player's performance in a tournament) should probably exist, I would have kept info about group stage groups in a separate table to allow for easier analysis of group outcomes.

Other than that, this schema served me well. It has very few redundant relationships and mostly conforms to best practices.

## 2. Collecting the data

To collect the data I wanted, I had to go to two sources. One was the "Wikipedia of Starcraft", Liquipedia, where all game results, tournament results, details about game maps and biographical data on players is stored. However, in order to get some of the really crucial data that would enable me to provide the kind of insights I knew people were really interested in, I needed to go to another source, which was YouTube videos of all the tournament dates. This would enable me to add information to the database about how long each game lasted and where on the map each player started out. If all the relevant data had been available on Liquipedia, I might have been able to write a web scraping script to funnel it all into my database automatically. But as it was, I instead created an input interface which would at least allow me to input the data quickly, with all SQL statements being automated.

This script is kind of funny because I wrote it before I knew about [SQLAlchemy](https://www.sqlalchemy.org/) and therefore ended up kind of reinventing the wheel with this:  
(code snippet)

```python
def getinputtype():
    inputtype = ""
    while inputtype not in INPUTTYPES and inputtype != "quit":
        inputtype = input("Input type (person/map/game/player/handle/season/series) or quit (quit): ")
    return inputtype

inputtype = ""

while inputtype != "quit":
    execstring = """db.execute("INSERT INTO """
    dictionary = getdict(getinputtype())
    if inputtype == "quit":
        return

def process (dictionary, table, execstring, db):
    qs = ""
    values = ""
    columns = "("
    valuelist = []
    execstring += table

    for k,v in dictionary.items():
        data = input(f"{k}: ")
    
    for value in valuelist:
        qs += "?, "
        columns += value[0] + ", "
        try:
            int(value[1])
            value = value[1]
        except:
            value = str(value[1])
            if value[0] != '"' and value[-1] != '"':
                value = '"' + value + '"'
        values += str(value) + ", "
        
    if len(valuelist) > 0:
        columns = columns[:-2] + ") VALUES ("
        qs = qs[:-2] + ''')", '''
        values = values[:-2] + ")"
        execstring += columns + qs + values
        return execstring
    else:
        return 'print("No row added.")'

execstring = process(dictionary, table, execstring, db)
print("Adding row: " + execstring)
exec(execstring)
```

The above code simply pieces together an "INSERT INTO" SQL statement according to the values inputted by the user, and then executes it at the end. The full code for this input interface also includes a lot of little automations not shown above, such as translating abbreviated inputs and automatically inserting data into other tables in the database if the received input mandates it.

Interface view:

![Interface view](https://www.dropbox.com/scl/fi/4w0xvvcffr5gzwqxr4tpo/inputsscreenshot.png?rlkey=gtrxmttg7g948gdmi7lyqpi11&raw=1)

Once the tedious work of collecting all the data was well over with and the database had been checked for consistency and inevitable errors corrected, it was time for the much more fun job of querying for insights and serializing them.

## 3. Extracting the key insights from the database

With the database in order, I was now able to answer questions about pro Starcraft by writing SQL queries to the database. However, I didn't just want to have my questions answered. I wanted to visualize my insights. For this purpose, I needed them stored neatly in spreadsheets. I also wanted to gather some insights that required a bit of processing beyond SQL queries.  

Out of 22 insights that I chose to visualize in tables or graphs for this project, some were very easy to pull from the database, while others required a quite a bit of Python code. This stage is also the "data transformation" stage where I prepare and reformat the raw data from the database for human consumption. I found Python a splendidly suitable tool for this, again much more versatile than desktop apps like Excel or Power BI, although more specialized apps also exist that could enhance this process even further. 

Here are two examples of how I extracted, transformed and serialized the data. The first example concerns the "maps" that the games are played on. I wanted to rank the maps according to how fair they are (a fair map does not advantage any race over any other), which I was able calculate statistically by looking at win ratios for each race on each map. This is how I did it:

```python
def mapbalance():
    # Get list of maps to loop through
    rows = db.execute("SELECT id, name FROM maps")
    maps = []
    
    # Initialize final data list
    mapdata = []
    
    for row in rows:
        maps.append(row)
    # Loop through all maps in database
    for map in maps:
        # Initialize data dictionary for current map
        thismap = {"Map": map['name']}
        # For each map, get all games played on this map. Exclude mirror matchup games (e.g. Terran vs Terran)
        # because this insight is about whether matches between DIFFERENT races are balanced on each map or not
        nonmirrorgamesonmap = db.execute("SELECT COUNT(id) FROM games WHERE map_id = ?", map['id'])[0]['COUNT(id)']
        # Skip maps that too few games have been played on to draw any meaningful conclusions about them
        if nonmirrorgamesonmap < 40:
            continue
        # Store amount of games played on map
        thismap['Total games'] = nonmirrorgamesonmap
        # For each of the three non-mirror matchups (Terran vs Protoss, Terran vs Zerg, and Protoss vs Zerg), compare the amount of wins for each race on the current map
        for matchup in ("TvP", "TvZ", "PvZ"):
            # Derive the races involved in the matchup, for use in the next database query
            # (this is the kind of minor workaround I wouldn't have needed if I had abandoned the "Players" table in the database and instead put race data in the "Games" table)
            if matchup == "TvP":
                races = ["Terran", "Protoss"]
            elif matchup == "TvZ":
                races = ["Terran", "Zerg"]
            elif matchup == "PvZ":
                races = ["Protoss", "Zerg"]
            # Query the database for the amount of wins for each race in the current matchup on the current map
            race1wins = db.execute("SELECT COUNT(*) FROM games JOIN players ON games.id = players.game_id AND games.winner_id = players.player_id WHERE matchup = ? AND race = ? AND map_id = ?", matchup, races[0], map['id'])[0]['COUNT(*)']
            race2wins = db.execute("SELECT COUNT(*) FROM games JOIN players ON games.id = players.game_id AND games.winner_id = players.player_id WHERE matchup = ? AND race = ? AND map_id = ?", matchup, races[1], map['id'])[0]['COUNT(*)']
            # Store the winrate percentage for each matchup in the data dictionary
            thismap[matchup] = round(race1wins / (race1wins + race2wins) * 100, 1)
       
        # Add this map's data dictionary to the overall list
        mapdata.append(thismap)

    # Now that we have the winrates for each matchup for each map, we can score the maps according to how balanced they are
    import math
    for mapstats in mapdata:
        error = 0
        # Increment error for current map according to how far it is from perfect balance (50% winrate) in each matchup
        for winrate in [mapstats['TvP'], mapstats['TvZ'], mapstats['PvZ']]:
            # Using RMSE in order to punish strong deviance in a single matchup harder than moderate deviance in multiple matchups
            error += (abs(winrate - 50) * abs(winrate - 50)) / 3
        # Store balance score as 100 minus the error
        mapstats['Balance score'] = round(100 - math.sqrt(error), 1)
    # Sort the maps according to their balance score
    mapdata.sort(key = lambda x: x['Balance score'], reverse=True)

    # Save the map balance score sheet to csv
    fieldnames = ['Map', 'Total games', 'TvP', 'TvZ', 'PvZ', 'Balance score']
    with open('data/8mapbalance.csv', 'w', newline='') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(mapdata)
    print(colored(f"Map balance sheet saved to csv.", 'green'))
```


Writing the SELECT statement to fetch the winrate data for each race was a challenge to my SQL abilities:
```sql
SELECT COUNT(*) FROM games 
JOIN players ON games.id = players.game_id AND games.winner_id = players.player_id 
WHERE matchup = ? AND race = ? AND map_id = ?
```

It only worked once I realized I needed to do a double join.

The second example combines winrate data with game duration to reveal which players do significantly better or worse depending on how long the game goes on. For this purpose, I also needed to write a clustering function that would divide each player's games into five intervals with an equal number of games in each, to allow legitimate comparison.
<br/><br/>

```python
# K-means clustering
def cluster(k, dataset):
    size = len(dataset)
    previous = 0
    intervals = []
    for i in range(size // k, size, size // k):
        interval = (previous, dataset[i]['duration'])
        # Avoid single minute intervals
        if interval[0] >= interval[1]:
            interval = (previous, previous+1)
        previous = dataset[i]['duration'] + 1
        # Avoid overlaps
        if interval not in intervals:
            intervals.append(interval)
    # Make the last interval open-ended (50 represents a value just higher than the highest game duration value in the database)
    intervals[-1] = (intervals[-1][0], 50)
    return intervals

def playerwinratesbyduration():
    # Initialize final data list
    pwbyduration = []

    # Loop through list of players
    for player in playerids:
        # Skip players who have less than 50 games in the database, 
        # as it would be impossible to make meaningful statistics about those
        if db.execute("SELECT COUNT(*) FROM players WHERE player_id = ?", player)[0]['COUNT(*)'] < 50:
            continue
        # Get the player's name
        handle = db.execute("SELECT handle FROM handles WHERE id = ?", player)[0]['handle']
        # Initialize data dictionary for player
        thisplayer = {'Intervals': [], 'Winrates': [], 'name': handle}
        # Get the duration of all of this players games
        dataset = db.execute("SELECT duration FROM games WHERE winner_id = ? OR loser_id = ? ORDER BY duration", player, player)
        # Using k-means clustering, generate five duration intervals for the current player 
        # which each represents an even share of his total games 
        intervals = cluster(5, dataset)
        # Calculate this player's winrate for games with duration falling in each of these five intervals
        for interval in intervals:
            wins = db.execute("SELECT COUNT(*) FROM games WHERE games.winner_id = ? AND duration BETWEEN ? AND ?", player, interval[0], interval[1])[0]['COUNT(*)']
            losses = db.execute("SELECT COUNT(*) FROM games WHERE games.loser_id = ? AND duration BETWEEN ? AND ?", player, interval[0], interval[1])[0]['COUNT(*)']
            # Store intervals as text and winrates as float
            thisplayer['Intervals'].append(str(interval[0]) + '-' + str(interval[1])) 
            thisplayer['Winrates'].append(round(wins / (wins + losses) * 100, 2))
        
        # Search for players with high variance across the different time intervals 
        # (those will be the interesting ones, since they'll contradict the null hypothesis)
        total = 0
        count = 0
        # Calculate variance
        for v in thisplayer['Winrates']:
            total += v
            count += 1
        mean = total / count
        variance = 0
        for v in thisplayer['Winrates']:
            variance += abs(mean - v)
        # Store variance
        thisplayer['variance'] = variance
        # Add player's data dictionary to final data list
        pwbyduration.append(thisplayer)

    # Having calculated interval winrates and variance for all players, 
    # sort them by variance and save data for the 10 players with highest variance
    pwbyduration.sort(key=lambda x: x['variance'], reverse=True)
    for playerdata in pwbyduration[:10]:
        with open('data/PWbyduration/13' + playerdata['name'] + 'pwbd.csv', 'w', newline='') as outfile:
            # Strip player name (since that's now stored in the filename) and variance (since that has already served its purpose as the sorting criterion)
            del playerdata['name']
            del playerdata['variance']
            # Write data to csv
            writer = csv.writer(outfile)
            writer.writerow(['Intervals', 'Winrates'])
            for row in zip(playerdata['Intervals'], playerdata['Winrates']):
                writer.writerow(row)
    print(colored("Winrate by duration graphs for players with high variance saved to csv (one file for each player)", 'green'))

```

I have a very long file called "queries.py" with this kind of scripts that extract figures from the database and store them as spreadsheets. I later realized that in this particular project, there was no necessity of storing the files as csv spreadsheets before plotting them (see next section). This is because the plot of each insight needed a sufficient amount of customization that I ended up writing a separate plot script for each of them anyway, which might as well have been appended at the end of each query script without the need for an intermediate csv file. In real life situations, however, it's usually good practice to store data in spreadsheet format (or other formats where applicable) because it might need to be handled by other people, used for several different purposes, or returned to at a much later time. 



## 4. Visualizing the insights

With a folder of neatly ordered csv spreadsheet files at the ready, it was now time to make the insights as clear as possible with charts and tables. All along, knowing that this would be studied with a lot of curiosity by thousands of Starcraft players and followers around the world was a great motivation to present everything as succinctly and beautifully as possible.

I looked at a range of software options for the visualization stage including Power BI, Tableau, Google Charts and Data Wrapper but found that, honestly, these were all less flexible and harder to use than Matplotlib - the most popular plotting library for Python. Using Matplotlib, I was able to customize each graph exactly to my needs. For data that was better presented in table form, I decided to write Python scripts to generate HTML and CSS code. This would, again, allow me to leverage the power of Python instead of relying on pre-programmed options or graphics in programs like Excel. The Pandas library has a convenient method called "to_html" which converts a dataframe into an HTML table but at the end of the day, I abandoned this method and wrote it all by hand, as that was the only way to get the design flexibility I wanted.

I enlisted the help of ChatGPT a lot in this stage of the project. I found this a great time to use AI because my problems were all very simple and therefore easy to explain (for example: "How can I draw a horizontal line through the middle of a graph?" or "How can I position the labels inside the chart bars instead of outside?") but the solutions depended on knowing the relevant Matplotlib methods and arguments from memory. ChatGPT is less useful when coding in raw Python because there, the real challenge is usually to even find out exactly what it is you need to do. Once you've managed to formulate a clear question, the answer is usually embedded in the question.

For the table plots, I wrote a basic script that would allow me to color code table cells according to their values or to their values relative to other values in the same column, like this:

![Table with color codes](https://www.dropbox.com/scl/fi/b5784ae7h0rxdvpxsvagj/colorcodes.png?rlkey=zseqifacor5ys8zmlgk66qcfu&raw=1)

This script reads the contents of a csv spreadsheet into memory as a Pandas dataframe, adds a ranking column, generates style settings for the table, sets parameters, and then iterates through the Dataframe, generating a table row for each dataframe row according to the parameters, then saves the table as HTML:

```python
# Read CSV data into a Pandas DataFrame
df = pd.read_csv('data/12playerspeeds.csv')

# Add ranking (and place it to the left)
df['Rank'] = range(1, len(df) + 1)
df = df[['Rank', 'Name', 'Race', 'Avg. game duration']]

# Style settings
html = """<style>
    .table {
    font-family: 'IBM Plex Mono', sans-serif;
    width: 80%;
    ... [shortened for readability]
    }
</style>
"""

# Parameters: Define columns to color code and columns to put in bold
colorgrading = {}
racecolors = {'Name': 'Name'} # Columns may also be color coded according to the values of other columns
bold = ['Name']

startbold = ''
endbold = ''

# Set background color, font color and race colors
bgcolor = '#d2dfee'
fontcolor = '#000000'
colors = {'Terran': '#1578da', 'Protoss': '#d3a514', 'Zerg': '#d73529'}

# Initialize color scales for color coding
scales = {
        'blue': {'max': (17, 80, 238), 'min': (223, 225, 238)}, 
        'full': {'max': (67, 130, 238), 'min': (238, 111, 76)},
        'red': {'max': (238, 61, 26), 'min': (238, 225, 223)}
}

# Color code a cell according to its value relative to the other cells in the same column
def colorgrade(value, vmax, vmin, scale='blue'):
    rgbcolor = (round(scales[scale]['max'][0] + ((scales[scale]['min'][0] - scales[scale]['max'][0]) * (1 - ((value - vmin) / (vmax - vmin))))), round(scales[scale]['max'][1] + ((scales[scale]['min'][1] - scales[scale]['max'][1]) * (1 - ((value - vmin) / (vmax - vmin))))), round(scales[scale]['max'][2] + ((scales[scale]['min'][2] - scales[scale]['max'][2]) * (1 - ((value - vmin) / (vmax - vmin))))))
    hexcolor = '#' + hex(rgbcolor[0])[2:] + hex(rgbcolor[1])[2:] + hex(rgbcolor[2])[2:]
    return hexcolor

# Write title
html += f"""<table border="1" class="dataframe table table-striped table-bordered">
    <thead>
    <tr>
    <th colspan="4" style="font-size: 24px; text-align: center;">Average game duration by player</th>
</tr>"""

# Write header
html += '<tr style="text-align: right;">'
for column in df:
    html += ("<th>" + column + "</th>")
html += """    </tr>
    </thead>
    <tbody>
    """

# Write body (incl. optional color coding and bold text)
i = 0
for index, row in df.iterrows():
    # Apply alternating row colors
    bgcolor = '#d2dfee' if i % 2 == 0 else '#e2effe'

    html += """<tr>
    """
    for column in df:
        # Text in bold (if needed)
        if column in bold:
            startbold = '<b>'
            endbold = '</b>'
        # Color player names according to the race they play as (if needed)
        if column in racecolors:
            rows = db.execute("SELECT mainrace FROM people WHERE id IN (SELECT id FROM handles WHERE handle = ?)", row[column])
            fontcolor = colors[rows[0]['mainrace']]
        # Color code cells according to relative value (if needed)
        if column in colorgrading:
            max = df[colorgrading[column]].max()
            min = df[colorgrading[column]].min()
            value = df[colorgrading[column]].values[i]
            bgcolor = colorgrade(value, max, min, scale='blue')
        # Write row
        html += (f'<td style="background-color: {bgcolor};"><span style="color: {fontcolor};">' + startbold + str(row[column]) + endbold + "</span></td>")
        # Reset font color and text formatting
        fontcolor = '#000000'
        startbold = ''
        endbold = ''
    i += 1
    html += """
    </tr>"""


html += """  </tbody>
</table>"""

# Save the HTML code to a file or display it as needed
with open(f'graphs/12playerspeeds.html', 'w') as file:
    file.write(html)
```

In hindsight, I could have saved some lines of code by loading in the style settings, basic colors settings and the colorgrade function from an external file, since I used the same style settings for every table.

For the line, bar and pie charts, I was faced with another range of problems. As one example, I wanted to created this arm-wrestling style strength-meter for each matchup:

![Matchup winrate](https://www.dropbox.com/scl/fi/44xz5omp88jxdcj2yyi8t/A11PvZoverallwinrate.png?rlkey=ckopqt8gwc1i0gxrwy6qop79g&raw=1)

But that proved harder than expected because Matplotlib - while generally giving me an experience of making anything I desired possible - has no semicircle plot functionality. So the above chart is actually a normal pie chart disguised as a meter. There's a fake pie slice with the same color as the background filling out the bottom half of the pie, and a small circle in the middle also colored like the background. This kind of "creative" solutions can sometimes save a lot of time and effort. But they should only be used in isolated cases because they inevitably begin to cause problems if you need to change something. For example, when I tried to add automatic labels to this, the values were half of what they should have been because the fake slice made up the last 50%. So I had to add the labels manually as text instead.

The remaining data lent itself to a variety of different kinds of charts, including bar charts:

![TvZ bar chart](https://www.dropbox.com/scl/fi/t3n8zm8025cwnrv58sscf/7TvZspawns.png?rlkey=60two1gqn5lkuopjpk679uj30&raw=1)

...line charts with shading to indicate discrepancy size:

![TvP over time](https://www.dropbox.com/scl/fi/udhmrcrvcb4x9bbv365rh/6TvPwinrates.png?rlkey=7yxpqb77tr908xz9ejzvqeq7k&raw=1)

...and multiline charts:

![Elo development](https://www.dropbox.com/scl/fi/zrr1zssg8axxchbflyqlx/5elotimeseries.png?rlkey=6k3z084sadxevzifcm812jryb&raw=1)

With the power of Matplotlib, each graph is customized in terms of font, colors, labels, size, extents of x and y axes, ticks along the axes and legend placement.


## 5. Presenting it nicely
With 22 graphs and tables and some further microinsights now at hand, there remained only the question of how to present it all to the world. This is a crucial aspect of data analysis as a whole because the ultimate purpose is to make a difference out in the world. This requires that the data is not merely available but that it's actually studied and taken in by the relevant people. This is why I'm so pleased that this data has already been delivered to at least 14,000 viewers on Artosis' channel alone, in addition to an unknown number of visitors to my page from other sources - not because Starcraft fans understanding the dynamics of the game better is going to save the world but because it proves that the methods I've used in this project really can leverage the power of data.

I opted to publish the data on a page on Github Pages, which offered me the convenience of updating automatically from my Github repository, which I could in turn push to from my local machine. I wrote the document in Markdown but including a lot of raw HTML for customization. Again, I used ChatGPT to instruct me about things like CSS rulesets, as I have some nightmarish memories from the pre-AI era of the exquisite frustration of trying to align containers and images and different kinds of content on a website and adapting it to varying screen sizes. Each insight as accompanied by my analysis of the data including notes and caveats about the statistical implications - or lack thereof - of each figure. (Since this project is primarily for entertainment, I have not been as strict with my statistical analysis as I would definitely need to be if import decisions were riding on my data).

![Page screenshot](https://www.dropbox.com/scl/fi/soxxld8w6uzurct411ioh/headerscreenshot.png?rlkey=r4f2h7hfla5w90yxokf8dyz84&raw=1)

*Screenshot of the page as it appears on a big screen*


## 6. In conclusion
This project has taught me about:

- Database design 
- SQL queries
- Combining Python and SQL to extract the relevant individual insights from a comprehensive dataset
- Visualizing data with Matplotlib
- Setting up web content with HTML and CSS
- Github Pages
- K-means clustering
- How to use AI assistance efficiently
- Improved raw Python skills

You can view the finished webpage here:

[Stats from the ASL/KSL era of Starcraft 1](https://jackyvso.github.io/Starcraft)


