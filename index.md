---
layout: default
title: Stats from the remastered era of pro Starcraft 1
---
<p style="margin: 0px 0px;">
<br/><br/>
</p>

# Stats from the ASL/KSL era
#### by Jacob Stubbe Østergaard / JackyVSO  

## Introduction
The following is a set of insights gleaned from data on offline Starcraft 1 tournament games at the pro level between 2016 and 2024. It includes combined insights related to:

- Game duration
- Matchup dynamics
- Player winrates and ratings
- Map balance
- Spawn locations
- Player and matchup development over time

...and much more.

The dataset comprises all 18 seasons of ASL/SSL and all 4 seasons of KSL for a total of <span style="font-size: 18px;"><b><u>2,107 games</u></b></span>. This is enough to make lots of statistically significant inferences but also few enough that more fine-grained insights that build on a small subset of the games come with a lot of uncertainty.

Data for each game includes players, outcome, date, duration, spawn locations, map details, map selection and tournament context. I have personally compiled the data in a SQL database which I have then queried for the insights. Most of the data has been collected from <a href="https://liquipedia.net/starcraft/Main_Page">Liquipedia</a>, while game duration and spawn location has been collected from the AfreecaTV VODs.

It should be noted that since the dataset consists exclusively of top level games, the insights in this article apply only to Starcraft played at the very highest skill level. Different dynamics may be at play at other levels. For analysis of ladder game data instead of ASL/KSL, check out <a href="https://tl.net/forum/brood-war/617209-data-analysis-on-8-million-games">Kraekkling's recent work</a>.

Making these stats available is my attempt to give something back to the community. I hope you find them interesting. Let me know if you have further questions that may be answered from this dataset, and I'll get back to you.

## Table of contents
The article is divided into four main parts: Matchups, Maps, Players and Tournament Stats. For the casuals, I recommend using this menu to find the stats you're interested in. For the nerds, I recommend diving right in and reading the article from end to end.

### 1. [Matchups](#Matchups)
- [Frequency of each matchup](#A5)
- [Overall winrate for each race](#A2)
- [Overall winrates for each non-mirror matchup](#A11)
- [Matchup winrates by year](#6)
- [Average duration of each matchup](#A9)
- [Longest games by matchup](#10)
- [Matchup winrates by game duration](#11)
- [Effect of cross spawns on game duration for each matchup](#14)
- [Effect of cross spawns on winrate for each matchup](#A10)



### 2. [Maps](#Maps)
- [Matchup winrates by number of spawn locations](#7)
- [Balance ranking of popular maps](#8)


### 3. [Players](#Players)
- [Games played by each player](#1)
- [Player winrates](#3)
- [Elo ranking list](#4)
- [Elo graphs of top players](#5)
- [Player winrates by game duration](#13)
- [Average game duration by player](#12)



### 4. [Tournament Stats](#TournamentStats)
- [Longest and shortest games in ASL/KSL history](#9)
- [Bo5/Bo7 win probabilities by game outcomes](#A3)
- [Map selection advantage](#A4)
- [Relative advantage of being a seeded player](#A7)
- [Group decider matches: winners' loser vs. losers' winner](#A8)
<br/><br/>


<h1 class="h1" id="Matchups"> 1. Matchups</h1>
The distribution of matchups of games in the database is as follows:
<h4 id="A5"></h4>
<img src="images/A5matchupfrequency.png" alt="Distribution of matchups">

We can see that mirror matchups are quite rare, which is only logical. The comparative scarcity of TvPs can be explained by a slight overrepresentation of Zergs in ASL and KSL in general (see the figures for total games played by each race in the table below) but that leaves no obvious explanation for why there have then been more TvTs than ZvZs. Maybe Zergs try to avoid each other in group selections. Maybe ZvZ series are generally more one-sided and therefore shorter than TvTs series. I don't know. Now let's move on to matchup winrates. The numbers still nominally indicate that Protoss is the best performing race.

This table shows the overall winrate for each race across both its non-mirror matchups:

<table border="1" class="dataframe table table-striped table-bordered">
  <thead>
    <tr style="text-align: right;"><table border="1" class="dataframe table table-striped table-bordered">
    <thead>
    <tr>
    <th colspan="3" style="font-size: 24px; text-align: center;">Overall race winrates</th>
</tr><tr style="text-align: right;"><th>Race</th><th>Total games</th><th>Overall winrate</th>    </tr>
    </thead>
    <tbody>
    <tr>
    <td style="background-color: #d2dfee;"><span style="color: #1578da;">Terran</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">1242</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">49.76</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #d3a514;">Protoss</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">1166</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">50.6</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #d73529;">Zerg</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">1260</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">49.68</span></td>
    </tr>  </tbody>
</table>

 Protoss is the best performing race by a margin of 0.8 percentage points over Terran. It also seems that Terran is the 2nd best performing race. But since Artosis often points out that Terran only appears to be doing well because Flash is so good, I decided to check what the winrates would be without Flash. To make a fair comparison, I also removed the statistically best performing player for each of the other races (Rain for Protoss and Soulkey for Zerg), and this is what the updated figures look like:

<table border="1" class="dataframe table table-striped table-bordered">
  <thead>
    <tr style="text-align: right;"><table border="1" class="dataframe table table-striped table-bordered">
    <thead>
    <tr>
    <th colspan="3" style="font-size: 24px; text-align: center;">Overall race winrates</th>
</tr><tr style="text-align: right;"><th>Race</th><th>Total games</th><th>Overall winrate</th>    </tr>
    </thead>
    <tbody>
    <tr>
    <td style="background-color: #d2dfee;"><span style="color: #1578da;">Terran</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">1126</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">47.66</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #d3a514;">Protoss</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">984</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">49.83</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #d73529;">Zerg</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">1016</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">46.7</span></td>
    </tr>  </tbody>
</table>

So Terran does do noticeably worse without Flash, but still better than Zerg without Soulkey. So while there's still a tiny bit of fuel for the "Protoss is OP" argument, there isn't much left for the "Terran has it hardest" argument - at least not in this dataset.

(While this was all a fun exercise, I should really emphasize that it means very little. The Protoss winrate advantage of 50.6 vs 49.76 over Terran amounts to an advantage of no more than six games, which makes it statistically insignificant by any reasonable standards. There is really only one thing that these numbers show very clearly, and that is that **Starcraft is an eerily well balanced game** - at least when played on carefully designed maps)  

Now let's look at the winrates for the individual non-mirror matchups. The numbers confirm the well-known pattern of T > Z > P > T but suggest that Zerg's advantage over Protoss is slightly smaller than Terran's advantage over Zerg and Protoss' advantage over Terran:  

<h4 id="A11"></h4>
<img src="./images/A11TvPoverallwinrate.png" alt="TvP overall winrate" width="255" height="auto" margin=0 style="display: inline;">
<img src="./images/A11TvZoverallwinrate.png" alt="TvZ overall winrate" width="255" height="auto" margin=0 style="display: inline;">
<img src="./images/A11PvZoverallwinrate.png" alt="PvZ overall winrate" width="255" height="auto" margin=0 style="display: inline;">

While these figures are very unsurprising, the story becomes a lot more interesting when we go into some more detail. For starters, let's take a look at the development of the matchup winrates year on year:

<h4 id="6"></h4>

<img src="./images/6TvPwinrates.png" alt="TvP winrate year on year" class="wide-image">
<img src="./images/6TvZwinrates.png" alt="TvZ winrate year on year" class="wide-image">
<img src="./images/6PvZwinrates.png" alt="PvZ winrate year on year" class="wide-image">

These graphs tell quite a different story than the overall winrates. The power distributions have actually fluctuated greatly as the races have struggled for the upper hand in the metagame. The picture becomes still more nuanced when we take game duration and spawn locations into consideration.  
First, let's look at how game duration correlates to matchup winrates. 

<span style="font-size: 12px;">*Note:because of the limited data available (only 500 tournament games played in each non-mirror matchup since 2016), I have created these graphs using 10 automatically clustered intervals, which means the intervals are of different length but each represent roughly the same amount of games (20-50 games per interval). Using any more intervals than this, let alone setting a point for every single minute, would leave some intervals with way too few data points, which would make the graphs noisy/random. The presented graphs represent a compromise between that and a very coarse version with only a few intervals but more certainty. Their minor details do not represent reality but their major trends are accurate.*</span>

Looking at winrates across game duration intervals, the trend is that

<h3 id="11"><i>Zerg rules the early game but struggles in the midgame. The late game is balanced.</i></h3>

<img src="./images/11TvPwinratesbyduration.png" alt="TvP winrate by game duration" class="wide-image">
<img src="./images/11TvZwinratesbyduration.png" alt="TvZ winrate by game duration" class="wide-image">
<img src="./images/11PvZwinratesbyduration.png" alt="PvZ winrate by game duration" class="wide-image">

We can see that if the game ends quickly, that bodes well for Zerg. In TvZ, there is a clear trend of early victories being Zerg, midgame victories being Terran, and the late game being very even. Long games are quite evenly split in all three matchups. PvZ has a similar trend but with semi-long games being once again Zerg-favored.

Moving on to spawn locations, we come to one of the most unambiguous findings of this study:

<h3 id="A10"><i>Cross spawns is VERY BAD for Terran</i></h3>
... and amazing for Protoss.

<table border="1" class="dataframe table table-striped table-bordered">
    <thead>
    <tr>
    <th colspan="8" style="font-size: 24px; text-align: center;">Effect of cross spawns in each matchup</th>
</tr><tr style="text-align: right;"><th>Matchup</th><th>Adjacent spawns winrate</th><th>Cross spawns winrate</th><th>Net effect</th>    </tr>
    </thead>
    <tbody>
    <tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">TvP</span></td><td style="background-color: #e2effe;"><span style="color: #1578da;">Terran +14</span></td><td style="background-color: #e2effe;"><span style="color: #d3a514;">Protoss +7</span></td><td style="background-color: #e2effe;"><span style="color: #d3a514;"><b>Protoss +21</b></span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">TvZ</span></td><td style="background-color: #e2effe;"><span style="color: #1578da;">Terran +14</span></td><td style="background-color: #e2effe;"><span style="color: #1578da;">Terran +2</span></td><td style="background-color: #e2effe;"><span style="color: #d73529;"><b>Zerg +12</b></span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">PvZ</span></td><td style="background-color: #e2effe;"><span style="color: #d73529;">Zerg +13</span></td><td style="background-color: #e2effe;"><span style="color: #d3a514;">Protoss +4</span></td><td style="background-color: #e2effe;"><span style="color: #d3a514;"><b>Protoss +17</b></span></td>
    </tr>  </tbody>
</table>

Such strong discrepancies across 200+ games in each matchup on 4-player maps is unlikely to have happened randomly. This table begins to reveal how the overall winrate of each matchup is really just an average of a range of varied winrates under specific conditions. TvP in general might be slightly Protoss-favored but TvP on a 4 player map with adjacent spawns is strongly Terran-favored.

If that table began to reveal how circumstance-dependent the power dynamics between the races are, these charts should drive the point home. They show how matchup winrates are affected by whether it's a 2-player, 3-player or 4-player map:

<h4 id="7"></h4>
<img src="images/7TvPspawns.png" alt="TvP winrates by number of spawn locations">
<img src="images/7TvZspawns.png" alt="TvZ winrates by number of spawn locations">
<img src="images/7PvZspawns.png" alt="PvZ winrates by number of spawn locations">

The most notable thing here is just how lopsided TvP on 2-player maps is. Out of 133 games in the database, Terran has won 46 and Protoss has won 87. If TvP was never played on 2-player maps, it would be a Terran-favored matchup. Terran also fares better with more spawning locations against Zerg, although this is far less pronounced. This is consistent with another finding in the data, which was that *the bigger the map (by size in tiles), the better for Terran*. I have not included that figure here because it shows the same as the above but less markedly.
PvZ seems hardly to be affected by the number of spawning locations on the map. There's a slight advantage for Protoss on 3-player maps and for Zerg on 2- and 4-player maps but it's small enough to be random. I'll leave it to more accomplished players to explain why this matchup is the least affected.  
<br/><br/>
<h1 class="h1" id="Maps"> 2. Maps</h1>

Now let's keep our focus on the maps for a bit before we move on to stats about players. No less than 78 different maps have been used in ASL and KSL: 22 2-player maps (603 games), 15 3-player maps (425 games), and 41 4-player maps (1079 games).

Since most of these maps have been in use for only one or two seasons, it isn't really possible to glean any statistical insights from them. However, for the most popular maps which have been played across many seasons, it should be possible to make meaningful comparisons. I thought it might be interesting to devise a metric to score these maps according to how balanced they are. The following balance ranking of the 13 most played maps was calculated using RMSE (root mean squared error) across the three matchups, with 50.0% as the target value.

<span style="font-size: 12px;">*Note: Using RMSE instead of MAE (mean absolute error) means that a strong bias in one matchup is punished more than a moderate bias across all matchups. Whether to use one or the other is a question of what one's idea of balance really is. I'm using RMSE because I personally think a map that is perfectly balanced in two matchups but has a 75% bias in the third one is less balanced than one that has scores of, say, 57/40/58.*</span>

<h4 id="8"></h4>
<table border="1" class="dataframe table table-striped table-bordered">
    <thead>
    <tr>
    <th colspan="7" style="font-size: 24px; text-align: center;">Most to least balanced maps</th>
</tr><tr style="text-align: right;"><th>Rank</th><th>Map</th><th>Total games</th><th>TvP</th><th>TvZ</th><th>PvZ</th><th>Balance score</th>    </tr>
    </thead>
    <tbody>
    <tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">1</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">Sylphid</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">141</span></td><td style="background-color: #eee1df;"><span style="color: #000000;">47.1</span></td><td style="background-color: #eeccc5;"><span style="color: #000000;">47.1</span></td><td style="background-color: #eea79a;"><span style="color: #000000;">58.8</span></td><td style="background-color: #2261ff;"><span style="color: #000000;">94.4</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">2</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">Retro</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">44</span></td><td style="background-color: #eeddda;"><span style="color: #000000;">53.8</span></td><td style="background-color: #eeb8ad;"><span style="color: #000000;">44.4</span></td><td style="background-color: #eeb2a7;"><span style="color: #000000;">42.9</span></td><td style="background-color: #2361fe;"><span style="color: #000000;">94.3</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">3</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">Eddy</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">55</span></td><td style="background-color: #eed9d6;"><span style="color: #000000;">54.5</span></td><td style="background-color: #eea091;"><span style="color: #000000;">58.8</span></td><td style="background-color: #eecbc5;"><span style="color: #000000;">46.7</span></td><td style="background-color: #2761fb;"><span style="color: #000000;">94.0</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">4</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">Butter</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">41</span></td><td style="background-color: #eed4d0;"><span style="color: #000000;">44.4</span></td><td style="background-color: #ee8570;"><span style="color: #000000;">37.5</span></td><td style="background-color: #eee1df;"><span style="color: #000000;">50.0</span></td><td style="background-color: #3c5fe6;"><span style="color: #000000;">92.1</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">5</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">Polypoid</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">77</span></td><td style="background-color: #eedfdd;"><span style="color: #000000;">53.3</span></td><td style="background-color: #ee745d;"><span style="color: #000000;">64.7</span></td><td style="background-color: #eec3bc;"><span style="color: #000000;">54.5</span></td><td style="background-color: #4a5ed8;"><span style="color: #000000;">90.9</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">6</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">Eclipse</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">94</span></td><td style="background-color: #eeaca0;"><span style="color: #000000;">36.0</span></td><td style="background-color: #eecfca;"><span style="color: #000000;">52.4</span></td><td style="background-color: #eeb5aa;"><span style="color: #000000;">43.3</span></td><td style="background-color: #4a5ed8;"><span style="color: #000000;">90.9</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">7</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">Vermeer</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">46</span></td><td style="background-color: #eeb3a8;"><span style="color: #000000;">62.5</span></td><td style="background-color: #ee7760;"><span style="color: #000000;">64.3</span></td><td style="background-color: #eee1df;"><span style="color: #000000;">50.0</span></td><td style="background-color: #605cc3;"><span style="color: #000000;">89.0</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">8</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">Circuit Breaker</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">149</span></td><td style="background-color: #eea99c;"><span style="color: #000000;">64.7</span></td><td style="background-color: #eea495;"><span style="color: #000000;">58.3</span></td><td style="background-color: #ee8f7c;"><span style="color: #000000;">62.5</span></td><td style="background-color: #6d5bb7;"><span style="color: #000000;">87.9</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">9</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">Fighting Spirit</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">105</span></td><td style="background-color: #eebfb7;"><span style="color: #000000;">40.0</span></td><td style="background-color: #ee907e;"><span style="color: #000000;">60.9</span></td><td style="background-color: #ee7c66;"><span style="color: #000000;">34.6</span></td><td style="background-color: #6f5ab5;"><span style="color: #000000;">87.7</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">10</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">Benzene</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">48</span></td><td style="background-color: #eecdc7;"><span style="color: #000000;">42.9</span></td><td style="background-color: #ee5335;"><span style="color: #000000;">30.8</span></td><td style="background-color: #eeab9e;"><span style="color: #000000;">58.3</span></td><td style="background-color: #755aaf;"><span style="color: #000000;">87.2</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">11</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">Heartbreak Ridge</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">48</span></td><td style="background-color: #ee907e;"><span style="color: #000000;">30.0</span></td><td style="background-color: #eea799;"><span style="color: #000000;">57.9</span></td><td style="background-color: #eebcb3;"><span style="color: #000000;">55.6</span></td><td style="background-color: #755aaf;"><span style="color: #000000;">87.2</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">12</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">Transistor</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">41</span></td><td style="background-color: #eea090;"><span style="color: #000000;">66.7</span></td><td style="background-color: #ee8570;"><span style="color: #000000;">37.5</span></td><td style="background-color: #ee735b;"><span style="color: #000000;">33.3</span></td><td style="background-color: #935793;"><span style="color: #000000;">84.6</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">13</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">Overwatch 2</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">54</span></td><td style="background-color: #eeb3a8;"><span style="color: #000000;">37.5</span></td><td style="background-color: #ee5335;"><span style="color: #000000;">69.2</span></td><td style="background-color: #ee5a3d;"><span style="color: #000000;">70.6</span></td><td style="background-color: #ae5578;"><span style="color: #000000;">82.2</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">14</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">Gladiator</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">47</span></td><td style="background-color: #ee3d1a;"><span style="color: #000000;">12.5</span></td><td style="background-color: #eee1df;"><span style="color: #000000;">50.0</span></td><td style="background-color: #ee6348;"><span style="color: #000000;">69.2</span></td><td style="background-color: #f94e31;"><span style="color: #000000;">75.7</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">15</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">Dark Origin</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">48</span></td><td style="background-color: #ee6f56;"><span style="color: #000000;">23.1</span></td><td style="background-color: #ee3d1a;"><span style="color: #000000;">27.8</span></td><td style="background-color: #ee3d1a;"><span style="color: #000000;">25.0</span></td><td style="background-color: #ff4e2b;"><span style="color: #000000;">75.2</span></td>
    </tr>  </tbody>
</table>

*The winrates displayed are for the first race mentioned in the matchup (e.g. Sylphid has a 47.1% winrate for T in TvP, 47.1% for T in TvZ and 58.8% for P in PvZ)*
<br/><br/>

So Sylphid appears to be the most balanced map yet made, closely followed by Retro, whereas Dark Origin is the least balanced - being very Zerg favored (and Protoss favored in TvP). Looking at the scores for Vermeer, Polypoid and Circuit Breaker, we can see that what is sometimes termed "standard maps" are actually clearly Terran-favored, whereas more unusual maps might be less comfortable for Terran.

<br/><br/>
<h1 id="Players">3. Players</h1>
In this section, we'll abandon the bird's eye view and instead zoom in on how the individual Starcraft 1 pros have been faring against each other. A total of 80 players have qualified for ASL and/or KSL at least once (29 Terran, 27 Zerg, 24 Protoss). Here they are, listed according to how many tournament games they've played:

<h4 id="1"></h4>
<table border="1" class="dataframe table table-striped table-bordered">
    <thead>
    <tr>
    <th colspan="3" style="font-size: 24px; text-align: center;">Total games played (ASL+KSL)</th>
</tr><tr style="text-align: right;"><th>Rank</th><th>Player</th><th>Games</th>    </tr>
    </thead>
    <tbody>
    <tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">1</span></td><td style="background-color: #d2dfee;"><span style="color: #d73529;">SoulKey</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">244</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">2</span></td><td style="background-color: #e2effe;"><span style="color: #d3a514;">Mini</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">216</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">3</span></td><td style="background-color: #d2dfee;"><span style="color: #1578da;">Sharp</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">191</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">4</span></td><td style="background-color: #e2effe;"><span style="color: #1578da;">Light</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">191</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">5</span></td><td style="background-color: #d2dfee;"><span style="color: #d3a514;">Snow</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">187</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">6</span></td><td style="background-color: #e2effe;"><span style="color: #d73529;">hero</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">186</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">7</span></td><td style="background-color: #d2dfee;"><span style="color: #d3a514;">Rain</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">182</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">8</span></td><td style="background-color: #e2effe;"><span style="color: #d3a514;">Best</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">175</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">9</span></td><td style="background-color: #d2dfee;"><span style="color: #1578da;">Rush</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">157</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">10</span></td><td style="background-color: #e2effe;"><span style="color: #d73529;">Queen</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">143</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">11</span></td><td style="background-color: #d2dfee;"><span style="color: #d3a514;">Bisu</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">129</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">12</span></td><td style="background-color: #e2effe;"><span style="color: #d73529;">Action</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">124</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">13</span></td><td style="background-color: #d2dfee;"><span style="color: #1578da;">FlaSh</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">118</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">14</span></td><td style="background-color: #e2effe;"><span style="color: #1578da;">Mind</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">118</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">15</span></td><td style="background-color: #d2dfee;"><span style="color: #1578da;">Last</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">117</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">16</span></td><td style="background-color: #e2effe;"><span style="color: #d73529;">Larva</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">113</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">17</span></td><td style="background-color: #d2dfee;"><span style="color: #d73529;">Soma</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">101</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">18</span></td><td style="background-color: #e2effe;"><span style="color: #d3a514;">Shuttle</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">100</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">19</span></td><td style="background-color: #d2dfee;"><span style="color: #1578da;">JyJ</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">100</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">20</span></td><td style="background-color: #e2effe;"><span style="color: #d3a514;">Stork</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">99</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">21</span></td><td style="background-color: #d2dfee;"><span style="color: #d73529;">Jaedong</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">97</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">22</span></td><td style="background-color: #e2effe;"><span style="color: #1578da;">RoyaL</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">86</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">23</span></td><td style="background-color: #d2dfee;"><span style="color: #d73529;">Shine</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">79</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">24</span></td><td style="background-color: #e2effe;"><span style="color: #d73529;">EffOrt</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">74</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">25</span></td><td style="background-color: #d2dfee;"><span style="color: #1578da;">Mong</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">65</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">26</span></td><td style="background-color: #e2effe;"><span style="color: #1578da;">Sea</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">61</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">27</span></td><td style="background-color: #d2dfee;"><span style="color: #1578da;">BarrackS</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">51</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">28</span></td><td style="background-color: #e2effe;"><span style="color: #1578da;">sSak</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">48</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">29</span></td><td style="background-color: #d2dfee;"><span style="color: #d73529;">MIsO</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">47</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">30</span></td><td style="background-color: #e2effe;"><span style="color: #d73529;">Sacsri</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">43</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">31</span></td><td style="background-color: #d2dfee;"><span style="color: #d3a514;">Horang2</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">42</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">32</span></td><td style="background-color: #e2effe;"><span style="color: #d73529;">Modesty</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">40</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">33</span></td><td style="background-color: #d2dfee;"><span style="color: #d3a514;">Movie</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">38</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">34</span></td><td style="background-color: #e2effe;"><span style="color: #1578da;">Ample</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">34</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">35</span></td><td style="background-color: #d2dfee;"><span style="color: #d3a514;">Jaehoon</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">32</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">36</span></td><td style="background-color: #e2effe;"><span style="color: #d3a514;">free</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">31</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">37</span></td><td style="background-color: #d2dfee;"><span style="color: #d3a514;">GuemChi</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">31</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">38</span></td><td style="background-color: #e2effe;"><span style="color: #d73529;">Killer</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">31</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">39</span></td><td style="background-color: #d2dfee;"><span style="color: #1578da;">Leta</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">25</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">40</span></td><td style="background-color: #e2effe;"><span style="color: #d73529;">Calm</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">24</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">41</span></td><td style="background-color: #d2dfee;"><span style="color: #1578da;">Piano</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">19</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">42</span></td><td style="background-color: #e2effe;"><span style="color: #d73529;">ggaemo</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">17</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">43</span></td><td style="background-color: #d2dfee;"><span style="color: #1578da;">ForGG</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">17</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">44</span></td><td style="background-color: #e2effe;"><span style="color: #d73529;">beast</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">17</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">45</span></td><td style="background-color: #d2dfee;"><span style="color: #d73529;">Hyuk</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">15</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">46</span></td><td style="background-color: #e2effe;"><span style="color: #d73529;">HyuN</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">12</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">47</span></td><td style="background-color: #d2dfee;"><span style="color: #1578da;">Speed</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">12</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">48</span></td><td style="background-color: #e2effe;"><span style="color: #d3a514;">nOOb</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">11</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">49</span></td><td style="background-color: #d2dfee;"><span style="color: #d73529;">ZeLoT</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">9</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">50</span></td><td style="background-color: #e2effe;"><span style="color: #d73529;">815</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">9</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">51</span></td><td style="background-color: #d2dfee;"><span style="color: #d3a514;">Brain</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">8</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">52</span></td><td style="background-color: #e2effe;"><span style="color: #d3a514;">Ss1nz</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">8</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">53</span></td><td style="background-color: #d2dfee;"><span style="color: #d3a514;">YSC</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">7</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">54</span></td><td style="background-color: #e2effe;"><span style="color: #d3a514;">Ruin</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">7</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">55</span></td><td style="background-color: #d2dfee;"><span style="color: #1578da;">HiyA</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">6</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">56</span></td><td style="background-color: #e2effe;"><span style="color: #d3a514;">Pusan</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">5</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">57</span></td><td style="background-color: #d2dfee;"><span style="color: #d3a514;">Sky</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">5</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">58</span></td><td style="background-color: #e2effe;"><span style="color: #d3a514;">Tyson</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">5</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">59</span></td><td style="background-color: #d2dfee;"><span style="color: #1578da;">BishOp</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">5</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">60</span></td><td style="background-color: #e2effe;"><span style="color: #d3a514;">Lazy</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">4</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">61</span></td><td style="background-color: #d2dfee;"><span style="color: #1578da;">firebathero</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">4</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">62</span></td><td style="background-color: #e2effe;"><span style="color: #1578da;">ByuL</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">4</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">63</span></td><td style="background-color: #d2dfee;"><span style="color: #1578da;">Scan</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">4</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">64</span></td><td style="background-color: #e2effe;"><span style="color: #1578da;">Iris</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">3</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">65</span></td><td style="background-color: #d2dfee;"><span style="color: #1578da;">NaDa</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">3</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">66</span></td><td style="background-color: #e2effe;"><span style="color: #d73529;">Yoon</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">3</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">67</span></td><td style="background-color: #d2dfee;"><span style="color: #1578da;">TY</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">3</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">68</span></td><td style="background-color: #e2effe;"><span style="color: #d3a514;">Hint</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">2</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">69</span></td><td style="background-color: #d2dfee;"><span style="color: #d3a514;">Maru</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">2</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">70</span></td><td style="background-color: #e2effe;"><span style="color: #d73529;">Force(Name)</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">2</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">71</span></td><td style="background-color: #d2dfee;"><span style="color: #d73529;">Terror</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">2</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">72</span></td><td style="background-color: #e2effe;"><span style="color: #d73529;">PURPOSE</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">2</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">73</span></td><td style="background-color: #d2dfee;"><span style="color: #1578da;">Tinkle</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">2</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">74</span></td><td style="background-color: #e2effe;"><span style="color: #1578da;">soso</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">2</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">75</span></td><td style="background-color: #d2dfee;"><span style="color: #d73529;">JJabNewDa</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">2</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">76</span></td><td style="background-color: #e2effe;"><span style="color: #d73529;">ivOry</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">2</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">77</span></td><td style="background-color: #d2dfee;"><span style="color: #1578da;">TaeNgGu</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">2</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">78</span></td><td style="background-color: #e2effe;"><span style="color: #1578da;">1127</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">2</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">79</span></td><td style="background-color: #d2dfee;"><span style="color: #d3a514;">Motive</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">2</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">80</span></td><td style="background-color: #e2effe;"><span style="color: #d73529;">Yerim2</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">0</span></td>
    </tr>  </tbody>
</table>

In terms of winrates, these are the overall standings:

<table border="1" class="dataframe table table-striped table-bordered">
      <thead>
      <tr>
        <th colspan="4" style="font-size: 24px; text-align: center;">Total</th>
    </tr><tr style="text-align: right;"><th>Rank</th><th>Name</th><th>Games</th><th>Winrate</th></tr>
      </thead>
      <tbody>
      <tr>
        <td style="background-color: #d2dfee;"><span style="color: #000000;">1</span></td><td style="background-color: #d2dfee;"><span style="color: #1578da;">FlaSh</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">118</span></td><td style="background-color: #4382ee;"><span style="color: #000000;">74.58</span></td>
        </tr><tr>
        <td style="background-color: #e2effe;"><span style="color: #000000;">2</span></td><td style="background-color: #e2effe;"><span style="color: #d3a514;">Rain</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">182</span></td><td style="background-color: #647ecf;"><span style="color: #000000;">63.74</span></td>
        </tr><tr>
        <td style="background-color: #d2dfee;"><span style="color: #000000;">3</span></td><td style="background-color: #d2dfee;"><span style="color: #d73529;">SoulKey</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">244</span></td><td style="background-color: #6a7ec9;"><span style="color: #000000;">61.48</span></td>
        </tr><tr>
        <td style="background-color: #e2effe;"><span style="color: #000000;">4</span></td><td style="background-color: #e2effe;"><span style="color: #1578da;">Last</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">117</span></td><td style="background-color: #6f7dc4;"><span style="color: #000000;">59.83</span></td>
        </tr><tr>
        <td style="background-color: #d2dfee;"><span style="color: #000000;">5</span></td><td style="background-color: #d2dfee;"><span style="color: #d73529;">EffOrt</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">74</span></td><td style="background-color: #707dc3;"><span style="color: #000000;">59.46</span></td>
        </tr><tr>
        <td style="background-color: #e2effe;"><span style="color: #000000;">6</span></td><td style="background-color: #e2effe;"><span style="color: #d3a514;">Mini</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">216</span></td><td style="background-color: #7c7cb8;"><span style="color: #000000;">55.56</span></td>
        </tr><tr>
        <td style="background-color: #d2dfee;"><span style="color: #000000;">7</span></td><td style="background-color: #d2dfee;"><span style="color: #1578da;">Light</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">191</span></td><td style="background-color: #7c7cb8;"><span style="color: #000000;">55.5</span></td>
        </tr><tr>
        <td style="background-color: #e2effe;"><span style="color: #000000;">8</span></td><td style="background-color: #e2effe;"><span style="color: #d73529;">Soma</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">101</span></td><td style="background-color: #7c7cb8;"><span style="color: #000000;">55.45</span></td>
        </tr><tr>
        <td style="background-color: #d2dfee;"><span style="color: #000000;">9</span></td><td style="background-color: #d2dfee;"><span style="color: #d73529;">hero</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">186</span></td><td style="background-color: #7d7cb7;"><span style="color: #000000;">55.38</span></td>
        </tr><tr>
        <td style="background-color: #e2effe;"><span style="color: #000000;">10</span></td><td style="background-color: #e2effe;"><span style="color: #d3a514;">Bisu</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">129</span></td><td style="background-color: #807bb4;"><span style="color: #000000;">54.26</span></td>
        </tr><tr>
        <td style="background-color: #d2dfee;"><span style="color: #000000;">11</span></td><td style="background-color: #d2dfee;"><span style="color: #d3a514;">Snow</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">187</span></td><td style="background-color: #827bb2;"><span style="color: #000000;">53.48</span></td>
        </tr><tr>
        <td style="background-color: #e2effe;"><span style="color: #000000;">12</span></td><td style="background-color: #e2effe;"><span style="color: #d73529;">Queen</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">143</span></td><td style="background-color: #837bb1;"><span style="color: #000000;">53.15</span></td>
        </tr><tr>
        <td style="background-color: #d2dfee;"><span style="color: #000000;">13</span></td><td style="background-color: #d2dfee;"><span style="color: #d3a514;">Best</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">175</span></td><td style="background-color: #877aae;"><span style="color: #000000;">52.0</span></td>
        </tr><tr>
        <td style="background-color: #e2effe;"><span style="color: #000000;">14</span></td><td style="background-color: #e2effe;"><span style="color: #d73529;">Larva</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">113</span></td><td style="background-color: #897aac;"><span style="color: #000000;">51.33</span></td>
        </tr><tr>
        <td style="background-color: #d2dfee;"><span style="color: #000000;">15</span></td><td style="background-color: #d2dfee;"><span style="color: #1578da;">Sharp</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">190</span></td><td style="background-color: #8d7aa8;"><span style="color: #000000;">50.0</span></td>
        </tr><tr>
        <td style="background-color: #e2effe;"><span style="color: #000000;">16</span></td><td style="background-color: #e2effe;"><span style="color: #1578da;">Mind</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">118</span></td><td style="background-color: #8d7aa8;"><span style="color: #000000;">50.0</span></td>
        </tr><tr>
        <td style="background-color: #d2dfee;"><span style="color: #000000;">17</span></td><td style="background-color: #d2dfee;"><span style="color: #1578da;">JyJ</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">100</span></td><td style="background-color: #8d7aa8;"><span style="color: #000000;">50.0</span></td>
        </tr><tr>
        <td style="background-color: #e2effe;"><span style="color: #000000;">18</span></td><td style="background-color: #e2effe;"><span style="color: #1578da;">Rush</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">157</span></td><td style="background-color: #8e7aa7;"><span style="color: #000000;">49.68</span></td>
        </tr><tr>
        <td style="background-color: #d2dfee;"><span style="color: #000000;">19</span></td><td style="background-color: #d2dfee;"><span style="color: #1578da;">RoyaL</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">86</span></td><td style="background-color: #9079a5;"><span style="color: #000000;">48.84</span></td>
        </tr><tr>
        <td style="background-color: #e2effe;"><span style="color: #000000;">20</span></td><td style="background-color: #e2effe;"><span style="color: #1578da;">Leta</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">25</span></td><td style="background-color: #9379a2;"><span style="color: #000000;">48.0</span></td>
        </tr><tr>
        <td style="background-color: #d2dfee;"><span style="color: #000000;">21</span></td><td style="background-color: #d2dfee;"><span style="color: #d73529;">Action</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">123</span></td><td style="background-color: #9379a2;"><span style="color: #000000;">47.97</span></td>
        </tr><tr>
        <td style="background-color: #e2effe;"><span style="color: #000000;">22</span></td><td style="background-color: #e2effe;"><span style="color: #d3a514;">Shuttle</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">100</span></td><td style="background-color: #9679a0;"><span style="color: #000000;">47.0</span></td>
        </tr><tr>
        <td style="background-color: #d2dfee;"><span style="color: #000000;">23</span></td><td style="background-color: #d2dfee;"><span style="color: #d73529;">Jaedong</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">97</span></td><td style="background-color: #98799e;"><span style="color: #000000;">46.39</span></td>
        </tr><tr>
        <td style="background-color: #e2effe;"><span style="color: #000000;">24</span></td><td style="background-color: #e2effe;"><span style="color: #1578da;">Sea</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">61</span></td><td style="background-color: #99789c;"><span style="color: #000000;">45.9</span></td>
        </tr><tr>
        <td style="background-color: #d2dfee;"><span style="color: #000000;">25</span></td><td style="background-color: #d2dfee;"><span style="color: #d3a514;">Stork</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">99</span></td><td style="background-color: #9e7898;"><span style="color: #000000;">44.44</span></td>
        </tr><tr>
        <td style="background-color: #e2effe;"><span style="color: #000000;">26</span></td><td style="background-color: #e2effe;"><span style="color: #d3a514;">Jaehoon</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">32</span></td><td style="background-color: #a07896;"><span style="color: #000000;">43.75</span></td>
        </tr><tr>
        <td style="background-color: #d2dfee;"><span style="color: #000000;">27</span></td><td style="background-color: #d2dfee;"><span style="color: #d73529;">Shine</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">79</span></td><td style="background-color: #a67791;"><span style="color: #000000;">41.77</span></td>
        </tr><tr>
        <td style="background-color: #e2effe;"><span style="color: #000000;">28</span></td><td style="background-color: #e2effe;"><span style="color: #d73529;">Calm</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">24</span></td><td style="background-color: #a67790;"><span style="color: #000000;">41.67</span></td>
        </tr><tr>
        <td style="background-color: #d2dfee;"><span style="color: #000000;">29</span></td><td style="background-color: #d2dfee;"><span style="color: #1578da;">Ample</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">34</span></td><td style="background-color: #a7778f;"><span style="color: #000000;">41.18</span></td>
        </tr><tr>
        <td style="background-color: #e2effe;"><span style="color: #000000;">30</span></td><td style="background-color: #e2effe;"><span style="color: #1578da;">BarrackS</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">51</span></td><td style="background-color: #a7778f;"><span style="color: #000000;">41.18</span></td>
        </tr><tr>
        <td style="background-color: #d2dfee;"><span style="color: #000000;">31</span></td><td style="background-color: #d2dfee;"><span style="color: #d3a514;">Horang2</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">42</span></td><td style="background-color: #a9778d;"><span style="color: #000000;">40.48</span></td>
        </tr><tr>
        <td style="background-color: #e2effe;"><span style="color: #000000;">32</span></td><td style="background-color: #e2effe;"><span style="color: #1578da;">sSak</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">48</span></td><td style="background-color: #ac768a;"><span style="color: #000000;">39.58</span></td>
        </tr><tr>
        <td style="background-color: #d2dfee;"><span style="color: #000000;">33</span></td><td style="background-color: #d2dfee;"><span style="color: #d3a514;">GuemChi</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">31</span></td><td style="background-color: #af7688;"><span style="color: #000000;">38.71</span></td>
        </tr><tr>
        <td style="background-color: #e2effe;"><span style="color: #000000;">34</span></td><td style="background-color: #e2effe;"><span style="color: #d73529;">Sacsri</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">43</span></td><td style="background-color: #b37684;"><span style="color: #000000;">37.21</span></td>
        </tr><tr>
        <td style="background-color: #d2dfee;"><span style="color: #000000;">35</span></td><td style="background-color: #d2dfee;"><span style="color: #1578da;">Mong</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">65</span></td><td style="background-color: #b47583;"><span style="color: #000000;">36.92</span></td>
        </tr><tr>
        <td style="background-color: #e2effe;"><span style="color: #000000;">36</span></td><td style="background-color: #e2effe;"><span style="color: #d3a514;">free</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">31</span></td><td style="background-color: #b8757f;"><span style="color: #000000;">35.48</span></td>
        </tr><tr>
        <td style="background-color: #d2dfee;"><span style="color: #000000;">37</span></td><td style="background-color: #d2dfee;"><span style="color: #d3a514;">Movie</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">38</span></td><td style="background-color: #bc757b;"><span style="color: #000000;">34.21</span></td>
        </tr><tr>
        <td style="background-color: #e2effe;"><span style="color: #000000;">38</span></td><td style="background-color: #e2effe;"><span style="color: #d73529;">Hyuk</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">15</span></td><td style="background-color: #bf7479;"><span style="color: #000000;">33.33</span></td>
        </tr><tr>
        <td style="background-color: #d2dfee;"><span style="color: #000000;">39</span></td><td style="background-color: #d2dfee;"><span style="color: #d73529;">Modesty</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">40</span></td><td style="background-color: #c17476;"><span style="color: #000000;">32.5</span></td>
        </tr><tr>
        <td style="background-color: #e2effe;"><span style="color: #000000;">40</span></td><td style="background-color: #e2effe;"><span style="color: #d73529;">Killer</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">31</span></td><td style="background-color: #c27476;"><span style="color: #000000;">32.26</span></td>
        </tr><tr>
        <td style="background-color: #d2dfee;"><span style="color: #000000;">41</span></td><td style="background-color: #d2dfee;"><span style="color: #d73529;">MIsO</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">47</span></td><td style="background-color: #c37475;"><span style="color: #000000;">31.91</span></td>
        </tr><tr>
        <td style="background-color: #e2effe;"><span style="color: #000000;">42</span></td><td style="background-color: #e2effe;"><span style="color: #1578da;">Piano</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">19</span></td><td style="background-color: #c47474;"><span style="color: #000000;">31.58</span></td>
        </tr><tr>
        <td style="background-color: #d2dfee;"><span style="color: #000000;">43</span></td><td style="background-color: #d2dfee;"><span style="color: #d73529;">ggaemo</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">17</span></td><td style="background-color: #cb736d;"><span style="color: #000000;">29.41</span></td>
        </tr><tr>
        <td style="background-color: #e2effe;"><span style="color: #000000;">44</span></td><td style="background-color: #e2effe;"><span style="color: #d73529;">beast</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">17</span></td><td style="background-color: #cb736d;"><span style="color: #000000;">29.41</span></td>
        </tr><tr>
        <td style="background-color: #d2dfee;"><span style="color: #000000;">45</span></td><td style="background-color: #d2dfee;"><span style="color: #1578da;">ForGG</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">17</span></td><td style="background-color: #ee6f4c;"><span style="color: #000000;">17.65</span></td>
        </tr>  </tbody>
    </table>

Even with Soulkey's dominance as of late, FlaSh still shows a winrate that suggests he's on his own level as the best player in this era of Starcraft. However, FlaSh hasn't played since 2020, and when, in a moment, we'll check a ranking that privileges more recent performance, it's a different story.

Now let's take a look at the top players in each matchup:

<h4 id="3"></h4>
<div class="table-container">

<table border="1" class="dataframe table table-striped table-bordered">
      <thead>
      <tr>
        <th colspan="4" style="font-size: 24px; text-align: center;">TvT</th>
    </tr><tr style="text-align: right;"><th>Rank</th><th>Name</th><th>Games</th><th>Winrate</th></tr>
      </thead>
      <tbody>
      <tr>
        <td style="background-color: #d2dfee;"><span style="color: #000000;">1</span></td><td style="background-color: #d2dfee;"><span style="color: #1578da;">FlaSh</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">27</span></td><td style="background-color: #4382ee;"><span style="color: #000000;">77.78</span></td>
        </tr><tr>
        <td style="background-color: #e2effe;"><span style="color: #000000;">2</span></td><td style="background-color: #e2effe;"><span style="color: #1578da;">Last</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">25</span></td><td style="background-color: #5780db;"><span style="color: #000000;">72.0</span></td>
        </tr><tr>
        <td style="background-color: #d2dfee;"><span style="color: #000000;">3</span></td><td style="background-color: #d2dfee;"><span style="color: #1578da;">Sharp</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">57</span></td><td style="background-color: #877aad;"><span style="color: #000000;">57.89</span></td>
        </tr><tr>
        <td style="background-color: #e2effe;"><span style="color: #000000;">4</span></td><td style="background-color: #e2effe;"><span style="color: #1578da;">Light</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">38</span></td><td style="background-color: #877aad;"><span style="color: #000000;">57.89</span></td>
        </tr><tr>
        <td style="background-color: #d2dfee;"><span style="color: #000000;">5</span></td><td style="background-color: #d2dfee;"><span style="color: #1578da;">sSak</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">16</span></td><td style="background-color: #8d7aa8;"><span style="color: #000000;">56.25</span></td>
        </tr><tr>
        <td style="background-color: #e2effe;"><span style="color: #000000;">6</span></td><td style="background-color: #e2effe;"><span style="color: #1578da;">Rush</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">49</span></td><td style="background-color: #9179a4;"><span style="color: #000000;">55.1</span></td>
        </tr><tr>
        <td style="background-color: #d2dfee;"><span style="color: #000000;">7</span></td><td style="background-color: #d2dfee;"><span style="color: #1578da;">RoyaL</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">22</span></td><td style="background-color: #a27794;"><span style="color: #000000;">50.0</span></td>
        </tr><tr>
        <td style="background-color: #e2effe;"><span style="color: #000000;">8</span></td><td style="background-color: #e2effe;"><span style="color: #1578da;">JyJ</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">36</span></td><td style="background-color: #ac768b;"><span style="color: #000000;">47.22</span></td>
        </tr><tr>
        <td style="background-color: #d2dfee;"><span style="color: #000000;">9</span></td><td style="background-color: #d2dfee;"><span style="color: #1578da;">BarrackS</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">14</span></td><td style="background-color: #d47265;"><span style="color: #000000;">35.71</span></td>
        </tr><tr>
        <td style="background-color: #e2effe;"><span style="color: #000000;">10</span></td><td style="background-color: #e2effe;"><span style="color: #1578da;">Mong</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">19</span></td><td style="background-color: #e27058;"><span style="color: #000000;">31.58</span></td>
        </tr><tr>
        <td style="background-color: #d2dfee;"><span style="color: #000000;">11</span></td><td style="background-color: #d2dfee;"><span style="color: #1578da;">Mind</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">35</span></td><td style="background-color: #ec6f4e;"><span style="color: #000000;">28.57</span></td>
        </tr><tr>
        <td style="background-color: #e2effe;"><span style="color: #000000;">12</span></td><td style="background-color: #e2effe;"><span style="color: #1578da;">Sea</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">25</span></td><td style="background-color: #ee6f4c;"><span style="color: #000000;">28.0</span></td>
        </tr>  </tbody>
    </table>

<table border="1" class="dataframe table table-striped table-bordered">
      <thead>
      <tr>
        <th colspan="4" style="font-size: 24px; text-align: center;">TvP</th>
    </tr><tr style="text-align: right;"><th>Rank</th><th>Name</th><th>Games</th><th>Winrate</th></tr>
      </thead>
      <tbody>
      <tr>
        <td style="background-color: #d2dfee;"><span style="color: #000000;">1</span></td><td style="background-color: #d2dfee;"><span style="color: #1578da;">FlaSh</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">28</span></td><td style="background-color: #4382ee;"><span style="color: #000000;">82.14</span></td>
        </tr><tr>
        <td style="background-color: #e2effe;"><span style="color: #000000;">2</span></td><td style="background-color: #e2effe;"><span style="color: #1578da;">Mong</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">20</span></td><td style="background-color: #737dc0;"><span style="color: #000000;">65.0</span></td>
        </tr><tr>
        <td style="background-color: #d2dfee;"><span style="color: #000000;">3</span></td><td style="background-color: #d2dfee;"><span style="color: #1578da;">Sea</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">17</span></td><td style="background-color: #857bb0;"><span style="color: #000000;">58.82</span></td>
        </tr><tr>
        <td style="background-color: #e2effe;"><span style="color: #000000;">4</span></td><td style="background-color: #e2effe;"><span style="color: #1578da;">Light</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">69</span></td><td style="background-color: #877aae;"><span style="color: #000000;">57.97</span></td>
        </tr><tr>
        <td style="background-color: #d2dfee;"><span style="color: #000000;">5</span></td><td style="background-color: #d2dfee;"><span style="color: #1578da;">Rush</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">39</span></td><td style="background-color: #a17895;"><span style="color: #000000;">48.72</span></td>
        </tr><tr>
        <td style="background-color: #e2effe;"><span style="color: #000000;">6</span></td><td style="background-color: #e2effe;"><span style="color: #1578da;">Mind</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">37</span></td><td style="background-color: #a17895;"><span style="color: #000000;">48.65</span></td>
        </tr><tr>
        <td style="background-color: #d2dfee;"><span style="color: #000000;">7</span></td><td style="background-color: #d2dfee;"><span style="color: #1578da;">Sharp</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">69</span></td><td style="background-color: #a47792;"><span style="color: #000000;">47.83</span></td>
        </tr><tr>
        <td style="background-color: #e2effe;"><span style="color: #000000;">8</span></td><td style="background-color: #e2effe;"><span style="color: #1578da;">BarrackS</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">19</span></td><td style="background-color: #a57791;"><span style="color: #000000;">47.37</span></td>
        </tr><tr>
        <td style="background-color: #d2dfee;"><span style="color: #000000;">9</span></td><td style="background-color: #d2dfee;"><span style="color: #1578da;">Last</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">51</span></td><td style="background-color: #a67790;"><span style="color: #000000;">47.06</span></td>
        </tr><tr>
        <td style="background-color: #e2effe;"><span style="color: #000000;">10</span></td><td style="background-color: #e2effe;"><span style="color: #1578da;">JyJ</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">23</span></td><td style="background-color: #bc757b;"><span style="color: #000000;">39.13</span></td>
        </tr><tr>
        <td style="background-color: #d2dfee;"><span style="color: #000000;">11</span></td><td style="background-color: #d2dfee;"><span style="color: #1578da;">sSak</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">20</span></td><td style="background-color: #c87370;"><span style="color: #000000;">35.0</span></td>
        </tr><tr>
        <td style="background-color: #e2effe;"><span style="color: #000000;">12</span></td><td style="background-color: #e2effe;"><span style="color: #1578da;">RoyaL</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">27</span></td><td style="background-color: #cc736c;"><span style="color: #000000;">33.33</span></td>
        </tr><tr>
        <td style="background-color: #d2dfee;"><span style="color: #000000;">13</span></td><td style="background-color: #d2dfee;"><span style="color: #1578da;">Ample</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">14</span></td><td style="background-color: #ee6f4c;"><span style="color: #000000;">21.43</span></td>
        </tr>  </tbody>
    </table>

<table border="1" class="dataframe table table-striped table-bordered">
      <thead>
      <tr>
        <th colspan="4" style="font-size: 24px; text-align: center;">TvZ</th>
    </tr><tr style="text-align: right;"><th>Rank</th><th>Name</th><th>Games</th><th>Winrate</th></tr>
      </thead>
      <tbody>
      <tr>
        <td style="background-color: #d2dfee;"><span style="color: #000000;">1</span></td><td style="background-color: #d2dfee;"><span style="color: #1578da;">FlaSh</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">54</span></td><td style="background-color: #4382ee;"><span style="color: #000000;">70.37</span></td>
        </tr><tr>
        <td style="background-color: #e2effe;"><span style="color: #000000;">2</span></td><td style="background-color: #e2effe;"><span style="color: #1578da;">Last</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">41</span></td><td style="background-color: #4a81e7;"><span style="color: #000000;">68.29</span></td>
        </tr><tr>
        <td style="background-color: #d2dfee;"><span style="color: #000000;">3</span></td><td style="background-color: #d2dfee;"><span style="color: #1578da;">Mind</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">46</span></td><td style="background-color: #4d81e5;"><span style="color: #000000;">67.39</span></td>
        </tr><tr>
        <td style="background-color: #e2effe;"><span style="color: #000000;">4</span></td><td style="background-color: #e2effe;"><span style="color: #1578da;">RoyaL</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">37</span></td><td style="background-color: #677ecb;"><span style="color: #000000;">59.46</span></td>
        </tr><tr>
        <td style="background-color: #d2dfee;"><span style="color: #000000;">5</span></td><td style="background-color: #d2dfee;"><span style="color: #1578da;">Ample</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">17</span></td><td style="background-color: #6a7ec9;"><span style="color: #000000;">58.82</span></td>
        </tr><tr>
        <td style="background-color: #e2effe;"><span style="color: #000000;">6</span></td><td style="background-color: #e2effe;"><span style="color: #1578da;">JyJ</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">41</span></td><td style="background-color: #6b7ec9;"><span style="color: #000000;">58.54</span></td>
        </tr><tr>
        <td style="background-color: #d2dfee;"><span style="color: #000000;">7</span></td><td style="background-color: #d2dfee;"><span style="color: #1578da;">Sea</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">19</span></td><td style="background-color: #6d7dc6;"><span style="color: #000000;">57.89</span></td>
        </tr><tr>
        <td style="background-color: #e2effe;"><span style="color: #000000;">8</span></td><td style="background-color: #e2effe;"><span style="color: #1578da;">Leta</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">11</span></td><td style="background-color: #787cbc;"><span style="color: #000000;">54.55</span></td>
        </tr><tr>
        <td style="background-color: #d2dfee;"><span style="color: #000000;">9</span></td><td style="background-color: #d2dfee;"><span style="color: #1578da;">Light</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">84</span></td><td style="background-color: #7f7bb5;"><span style="color: #000000;">52.38</span></td>
        </tr><tr>
        <td style="background-color: #e2effe;"><span style="color: #000000;">10</span></td><td style="background-color: #e2effe;"><span style="color: #1578da;">Rush</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">69</span></td><td style="background-color: #9379a2;"><span style="color: #000000;">46.38</span></td>
        </tr><tr>
        <td style="background-color: #d2dfee;"><span style="color: #000000;">11</span></td><td style="background-color: #d2dfee;"><span style="color: #1578da;">Sharp</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">64</span></td><td style="background-color: #97799f;"><span style="color: #000000;">45.31</span></td>
        </tr><tr>
        <td style="background-color: #e2effe;"><span style="color: #000000;">12</span></td><td style="background-color: #e2effe;"><span style="color: #1578da;">BarrackS</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">18</span></td><td style="background-color: #ac768a;"><span style="color: #000000;">38.89</span></td>
        </tr><tr>
        <td style="background-color: #d2dfee;"><span style="color: #000000;">13</span></td><td style="background-color: #d2dfee;"><span style="color: #1578da;">sSak</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">12</span></td><td style="background-color: #db715e;"><span style="color: #000000;">25.0</span></td>
        </tr><tr>
        <td style="background-color: #e2effe;"><span style="color: #000000;">14</span></td><td style="background-color: #e2effe;"><span style="color: #1578da;">Mong</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">26</span></td><td style="background-color: #ee6f4c;"><span style="color: #000000;">19.23</span></td>
        </tr>  </tbody>
    </table>
</div>

<div class="table-container">

<table border="1" class="dataframe table table-striped table-bordered">
      <thead>
      <tr>
        <th colspan="4" style="font-size: 24px; text-align: center;">PvT</th>
    </tr><tr style="text-align: right;"><th>Rank</th><th>Name</th><th>Games</th><th>Winrate</th></tr>
      </thead>
      <tbody>
      <tr>
        <td style="background-color: #d2dfee;"><span style="color: #000000;">1</span></td><td style="background-color: #d2dfee;"><span style="color: #d3a514;">Snow</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">48</span></td><td style="background-color: #4382ee;"><span style="color: #000000;">66.67</span></td>
        </tr><tr>
        <td style="background-color: #e2effe;"><span style="color: #000000;">2</span></td><td style="background-color: #e2effe;"><span style="color: #d3a514;">Mini</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">71</span></td><td style="background-color: #5e7fd5;"><span style="color: #000000;">60.56</span></td>
        </tr><tr>
        <td style="background-color: #d2dfee;"><span style="color: #000000;">3</span></td><td style="background-color: #d2dfee;"><span style="color: #d3a514;">Jaehoon</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">12</span></td><td style="background-color: #677ecc;"><span style="color: #000000;">58.33</span></td>
        </tr><tr>
        <td style="background-color: #e2effe;"><span style="color: #000000;">4</span></td><td style="background-color: #e2effe;"><span style="color: #d3a514;">Horang2</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">19</span></td><td style="background-color: #697eca;"><span style="color: #000000;">57.89</span></td>
        </tr><tr>
        <td style="background-color: #d2dfee;"><span style="color: #000000;">5</span></td><td style="background-color: #d2dfee;"><span style="color: #d3a514;">Best</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">67</span></td><td style="background-color: #6e7dc5;"><span style="color: #000000;">56.72</span></td>
        </tr><tr>
        <td style="background-color: #e2effe;"><span style="color: #000000;">6</span></td><td style="background-color: #e2effe;"><span style="color: #d3a514;">Bisu</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">53</span></td><td style="background-color: #6f7dc5;"><span style="color: #000000;">56.6</span></td>
        </tr><tr>
        <td style="background-color: #d2dfee;"><span style="color: #000000;">7</span></td><td style="background-color: #d2dfee;"><span style="color: #d3a514;">Rain</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">69</span></td><td style="background-color: #827bb2;"><span style="color: #000000;">52.17</span></td>
        </tr><tr>
        <td style="background-color: #e2effe;"><span style="color: #000000;">8</span></td><td style="background-color: #e2effe;"><span style="color: #d3a514;">Shuttle</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">44</span></td><td style="background-color: #9579a0;"><span style="color: #000000;">47.73</span></td>
        </tr><tr>
        <td style="background-color: #d2dfee;"><span style="color: #000000;">9</span></td><td style="background-color: #d2dfee;"><span style="color: #d3a514;">Stork</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">32</span></td><td style="background-color: #99789d;"><span style="color: #000000;">46.88</span></td>
        </tr><tr>
        <td style="background-color: #e2effe;"><span style="color: #000000;">10</span></td><td style="background-color: #e2effe;"><span style="color: #d3a514;">GuemChi</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">14</span></td><td style="background-color: #aa778c;"><span style="color: #000000;">42.86</span></td>
        </tr><tr>
        <td style="background-color: #d2dfee;"><span style="color: #000000;">11</span></td><td style="background-color: #d2dfee;"><span style="color: #d3a514;">Movie</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">16</span></td><td style="background-color: #dd715c;"><span style="color: #000000;">31.25</span></td>
        </tr><tr>
        <td style="background-color: #e2effe;"><span style="color: #000000;">12</span></td><td style="background-color: #e2effe;"><span style="color: #d3a514;">free</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">11</span></td><td style="background-color: #ee6f4c;"><span style="color: #000000;">27.27</span></td>
        </tr>  </tbody>
    </table>

<table border="1" class="dataframe table table-striped table-bordered">
      <thead>
      <tr>
        <th colspan="4" style="font-size: 24px; text-align: center;">PvP</th>
    </tr><tr style="text-align: right;"><th>Rank</th><th>Name</th><th>Games</th><th>Winrate</th></tr>
      </thead>
      <tbody>
      <tr>
        <td style="background-color: #d2dfee;"><span style="color: #000000;">1</span></td><td style="background-color: #d2dfee;"><span style="color: #d3a514;">Rain</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">51</span></td><td style="background-color: #4382ee;"><span style="color: #000000;">84.31</span></td>
        </tr><tr>
        <td style="background-color: #e2effe;"><span style="color: #000000;">2</span></td><td style="background-color: #e2effe;"><span style="color: #d3a514;">Snow</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">48</span></td><td style="background-color: #8f7aa6;"><span style="color: #000000;">60.42</span></td>
        </tr><tr>
        <td style="background-color: #d2dfee;"><span style="color: #000000;">3</span></td><td style="background-color: #d2dfee;"><span style="color: #d3a514;">Bisu</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">18</span></td><td style="background-color: #b17686;"><span style="color: #000000;">50.0</span></td>
        </tr><tr>
        <td style="background-color: #e2effe;"><span style="color: #000000;">4</span></td><td style="background-color: #e2effe;"><span style="color: #d3a514;">Mini</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">34</span></td><td style="background-color: #ba757d;"><span style="color: #000000;">47.06</span></td>
        </tr><tr>
        <td style="background-color: #d2dfee;"><span style="color: #000000;">5</span></td><td style="background-color: #d2dfee;"><span style="color: #d3a514;">Shuttle</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">19</span></td><td style="background-color: #ca736e;"><span style="color: #000000;">42.11</span></td>
        </tr><tr>
        <td style="background-color: #e2effe;"><span style="color: #000000;">6</span></td><td style="background-color: #e2effe;"><span style="color: #d3a514;">Horang2</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">12</span></td><td style="background-color: #cb736d;"><span style="color: #000000;">41.67</span></td>
        </tr><tr>
        <td style="background-color: #d2dfee;"><span style="color: #000000;">7</span></td><td style="background-color: #d2dfee;"><span style="color: #d3a514;">Stork</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">48</span></td><td style="background-color: #d27267;"><span style="color: #000000;">39.58</span></td>
        </tr><tr>
        <td style="background-color: #e2effe;"><span style="color: #000000;">8</span></td><td style="background-color: #e2effe;"><span style="color: #d3a514;">Best</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">44</span></td><td style="background-color: #dc715d;"><span style="color: #000000;">36.36</span></td>
        </tr><tr>
        <td style="background-color: #d2dfee;"><span style="color: #000000;">9</span></td><td style="background-color: #d2dfee;"><span style="color: #d3a514;">Jaehoon</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">13</span></td><td style="background-color: #ee6f4c;"><span style="color: #000000;">30.77</span></td>
        </tr><tr>
        <td style="background-color: #e2effe;"><span style="color: #000000;">10</span></td><td style="background-color: #e2effe;"><span style="color: #d3a514;">Movie</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">13</span></td><td style="background-color: #ee6f4c;"><span style="color: #000000;">30.77</span></td>
        </tr>  </tbody>
    </table>

<table border="1" class="dataframe table table-striped table-bordered">
      <thead>
      <tr>
        <th colspan="4" style="font-size: 24px; text-align: center;">PvZ</th>
    </tr><tr style="text-align: right;"><th>Rank</th><th>Name</th><th>Games</th><th>Winrate</th></tr>
      </thead>
      <tbody>
      <tr>
        <td style="background-color: #d2dfee;"><span style="color: #000000;">1</span></td><td style="background-color: #d2dfee;"><span style="color: #d3a514;">Rain</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">62</span></td><td style="background-color: #4382ee;"><span style="color: #000000;">59.68</span></td>
        </tr><tr>
        <td style="background-color: #e2effe;"><span style="color: #000000;">2</span></td><td style="background-color: #e2effe;"><span style="color: #d3a514;">Best</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">64</span></td><td style="background-color: #4981e8;"><span style="color: #000000;">57.81</span></td>
        </tr><tr>
        <td style="background-color: #d2dfee;"><span style="color: #000000;">3</span></td><td style="background-color: #d2dfee;"><span style="color: #d3a514;">Mini</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">111</span></td><td style="background-color: #5380df;"><span style="color: #000000;">54.95</span></td>
        </tr><tr>
        <td style="background-color: #e2effe;"><span style="color: #000000;">4</span></td><td style="background-color: #e2effe;"><span style="color: #d3a514;">Bisu</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">58</span></td><td style="background-color: #5880da;"><span style="color: #000000;">53.45</span></td>
        </tr><tr>
        <td style="background-color: #d2dfee;"><span style="color: #000000;">5</span></td><td style="background-color: #d2dfee;"><span style="color: #d3a514;">Stork</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">19</span></td><td style="background-color: #5b7fd7;"><span style="color: #000000;">52.63</span></td>
        </tr><tr>
        <td style="background-color: #e2effe;"><span style="color: #000000;">6</span></td><td style="background-color: #e2effe;"><span style="color: #d3a514;">Shuttle</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">37</span></td><td style="background-color: #687ecb;"><span style="color: #000000;">48.65</span></td>
        </tr><tr>
        <td style="background-color: #d2dfee;"><span style="color: #000000;">7</span></td><td style="background-color: #d2dfee;"><span style="color: #d3a514;">Snow</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">91</span></td><td style="background-color: #7c7cb8;"><span style="color: #000000;">42.86</span></td>
        </tr><tr>
        <td style="background-color: #e2effe;"><span style="color: #000000;">8</span></td><td style="background-color: #e2effe;"><span style="color: #d3a514;">free</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">11</span></td><td style="background-color: #9279a3;"><span style="color: #000000;">36.36</span></td>
        </tr><tr>
        <td style="background-color: #d2dfee;"><span style="color: #000000;">9</span></td><td style="background-color: #d2dfee;"><span style="color: #d3a514;">Horang2</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">11</span></td><td style="background-color: #ee6f4c;"><span style="color: #000000;">9.09</span></td>
        </tr>  </tbody>
    </table>
</div>

<div class="table-container">

<table border="1" class="dataframe table table-striped table-bordered">
      <thead>
      <tr>
        <th colspan="4" style="font-size: 24px; text-align: center;">ZvT</th>
    </tr><tr style="text-align: right;"><th>Rank</th><th>Name</th><th>Games</th><th>Winrate</th></tr>
      </thead>
      <tbody>
      <tr>
        <td style="background-color: #d2dfee;"><span style="color: #000000;">1</span></td><td style="background-color: #d2dfee;"><span style="color: #d73529;">EffOrt</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">23</span></td><td style="background-color: #4382ee;"><span style="color: #000000;">69.57</span></td>
        </tr><tr>
        <td style="background-color: #e2effe;"><span style="color: #000000;">2</span></td><td style="background-color: #e2effe;"><span style="color: #d73529;">SoulKey</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">94</span></td><td style="background-color: #5e7fd4;"><span style="color: #000000;">62.77</span></td>
        </tr><tr>
        <td style="background-color: #d2dfee;"><span style="color: #000000;">3</span></td><td style="background-color: #d2dfee;"><span style="color: #d73529;">Queen</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">47</span></td><td style="background-color: #747dc0;"><span style="color: #000000;">57.45</span></td>
        </tr><tr>
        <td style="background-color: #e2effe;"><span style="color: #000000;">4</span></td><td style="background-color: #e2effe;"><span style="color: #d73529;">Action</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">44</span></td><td style="background-color: #897aac;"><span style="color: #000000;">52.27</span></td>
        </tr><tr>
        <td style="background-color: #d2dfee;"><span style="color: #000000;">5</span></td><td style="background-color: #d2dfee;"><span style="color: #d73529;">hero</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">85</span></td><td style="background-color: #9079a5;"><span style="color: #000000;">50.59</span></td>
        </tr><tr>
        <td style="background-color: #e2effe;"><span style="color: #000000;">6</span></td><td style="background-color: #e2effe;"><span style="color: #d73529;">Sacsri</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">18</span></td><td style="background-color: #9279a3;"><span style="color: #000000;">50.0</span></td>
        </tr><tr>
        <td style="background-color: #d2dfee;"><span style="color: #000000;">7</span></td><td style="background-color: #d2dfee;"><span style="color: #d73529;">Larva</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">24</span></td><td style="background-color: #a37793;"><span style="color: #000000;">45.83</span></td>
        </tr><tr>
        <td style="background-color: #e2effe;"><span style="color: #000000;">8</span></td><td style="background-color: #e2effe;"><span style="color: #d73529;">Jaedong</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">41</span></td><td style="background-color: #b57582;"><span style="color: #000000;">41.46</span></td>
        </tr><tr>
        <td style="background-color: #d2dfee;"><span style="color: #000000;">9</span></td><td style="background-color: #d2dfee;"><span style="color: #d73529;">Soma</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">36</span></td><td style="background-color: #bf7479;"><span style="color: #000000;">38.89</span></td>
        </tr><tr>
        <td style="background-color: #e2effe;"><span style="color: #000000;">10</span></td><td style="background-color: #e2effe;"><span style="color: #d73529;">Modesty</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">32</span></td><td style="background-color: #c57473;"><span style="color: #000000;">37.5</span></td>
        </tr><tr>
        <td style="background-color: #d2dfee;"><span style="color: #000000;">11</span></td><td style="background-color: #d2dfee;"><span style="color: #d73529;">Shine</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">38</span></td><td style="background-color: #c77371;"><span style="color: #000000;">36.84</span></td>
        </tr><tr>
        <td style="background-color: #e2effe;"><span style="color: #000000;">12</span></td><td style="background-color: #e2effe;"><span style="color: #d73529;">MIsO</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">22</span></td><td style="background-color: #c9736f;"><span style="color: #000000;">36.36</span></td>
        </tr><tr>
        <td style="background-color: #d2dfee;"><span style="color: #000000;">13</span></td><td style="background-color: #d2dfee;"><span style="color: #d73529;">Killer</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">11</span></td><td style="background-color: #ee6f4c;"><span style="color: #000000;">27.27</span></td>
        </tr>  </tbody>
    </table>

<table border="1" class="dataframe table table-striped table-bordered">
      <thead>
      <tr>
        <th colspan="4" style="font-size: 24px; text-align: center;">ZvP</th>
    </tr><tr style="text-align: right;"><th>Rank</th><th>Name</th><th>Games</th><th>Winrate</th></tr>
      </thead>
      <tbody>
      <tr>
        <td style="background-color: #d2dfee;"><span style="color: #000000;">1</span></td><td style="background-color: #d2dfee;"><span style="color: #d73529;">Soma</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">39</span></td><td style="background-color: #4382ee;"><span style="color: #000000;">71.79</span></td>
        </tr><tr>
        <td style="background-color: #e2effe;"><span style="color: #000000;">2</span></td><td style="background-color: #e2effe;"><span style="color: #d73529;">hero</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">47</span></td><td style="background-color: #5780db;"><span style="color: #000000;">65.96</span></td>
        </tr><tr>
        <td style="background-color: #d2dfee;"><span style="color: #000000;">3</span></td><td style="background-color: #d2dfee;"><span style="color: #d73529;">SoulKey</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">89</span></td><td style="background-color: #5a7fd9;"><span style="color: #000000;">65.17</span></td>
        </tr><tr>
        <td style="background-color: #e2effe;"><span style="color: #000000;">4</span></td><td style="background-color: #e2effe;"><span style="color: #d73529;">Jaedong</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">30</span></td><td style="background-color: #6b7ec8;"><span style="color: #000000;">60.0</span></td>
        </tr><tr>
        <td style="background-color: #d2dfee;"><span style="color: #000000;">5</span></td><td style="background-color: #d2dfee;"><span style="color: #d73529;">EffOrt</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">36</span></td><td style="background-color: #7a7cb9;"><span style="color: #000000;">55.56</span></td>
        </tr><tr>
        <td style="background-color: #e2effe;"><span style="color: #000000;">6</span></td><td style="background-color: #e2effe;"><span style="color: #d73529;">Larva</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">51</span></td><td style="background-color: #7d7cb7;"><span style="color: #000000;">54.9</span></td>
        </tr><tr>
        <td style="background-color: #d2dfee;"><span style="color: #000000;">7</span></td><td style="background-color: #d2dfee;"><span style="color: #d73529;">Shine</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">24</span></td><td style="background-color: #8d7aa7;"><span style="color: #000000;">50.0</span></td>
        </tr><tr>
        <td style="background-color: #e2effe;"><span style="color: #000000;">8</span></td><td style="background-color: #e2effe;"><span style="color: #d73529;">Queen</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">52</span></td><td style="background-color: #9479a1;"><span style="color: #000000;">48.08</span></td>
        </tr><tr>
        <td style="background-color: #d2dfee;"><span style="color: #000000;">9</span></td><td style="background-color: #d2dfee;"><span style="color: #d73529;">Action</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">50</span></td><td style="background-color: #a27794;"><span style="color: #000000;">44.0</span></td>
        </tr><tr>
        <td style="background-color: #e2effe;"><span style="color: #000000;">10</span></td><td style="background-color: #e2effe;"><span style="color: #d73529;">Killer</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">15</span></td><td style="background-color: #b07687;"><span style="color: #000000;">40.0</span></td>
        </tr><tr>
        <td style="background-color: #d2dfee;"><span style="color: #000000;">11</span></td><td style="background-color: #d2dfee;"><span style="color: #d73529;">Calm</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">10</span></td><td style="background-color: #b07687;"><span style="color: #000000;">40.0</span></td>
        </tr><tr>
        <td style="background-color: #e2effe;"><span style="color: #000000;">12</span></td><td style="background-color: #e2effe;"><span style="color: #d73529;">MIsO</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">15</span></td><td style="background-color: #dd715c;"><span style="color: #000000;">26.67</span></td>
        </tr><tr>
        <td style="background-color: #d2dfee;"><span style="color: #000000;">13</span></td><td style="background-color: #d2dfee;"><span style="color: #d73529;">Sacsri</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">23</span></td><td style="background-color: #ee6f4c;"><span style="color: #000000;">21.74</span></td>
        </tr>  </tbody>
    </table>

<table border="1" class="dataframe table table-striped table-bordered">
      <thead>
      <tr>
        <th colspan="4" style="font-size: 24px; text-align: center;">ZvZ</th>
    </tr><tr style="text-align: right;"><th>Rank</th><th>Name</th><th>Games</th><th>Winrate</th></tr>
      </thead>
      <tbody>
      <tr>
        <td style="background-color: #d2dfee;"><span style="color: #000000;">1</span></td><td style="background-color: #d2dfee;"><span style="color: #d73529;">Queen</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">44</span></td><td style="background-color: #4382ee;"><span style="color: #000000;">54.55</span></td>
        </tr><tr>
        <td style="background-color: #e2effe;"><span style="color: #000000;">2</span></td><td style="background-color: #e2effe;"><span style="color: #d73529;">SoulKey</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">61</span></td><td style="background-color: #4881e9;"><span style="color: #000000;">54.1</span></td>
        </tr><tr>
        <td style="background-color: #d2dfee;"><span style="color: #000000;">3</span></td><td style="background-color: #d2dfee;"><span style="color: #d73529;">Soma</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">26</span></td><td style="background-color: #4a81e7;"><span style="color: #000000;">53.85</span></td>
        </tr><tr>
        <td style="background-color: #e2effe;"><span style="color: #000000;">4</span></td><td style="background-color: #e2effe;"><span style="color: #d73529;">hero</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">54</span></td><td style="background-color: #4c81e5;"><span style="color: #000000;">53.7</span></td>
        </tr><tr>
        <td style="background-color: #d2dfee;"><span style="color: #000000;">5</span></td><td style="background-color: #d2dfee;"><span style="color: #d73529;">EffOrt</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">15</span></td><td style="background-color: #5081e2;"><span style="color: #000000;">53.33</span></td>
        </tr><tr>
        <td style="background-color: #e2effe;"><span style="color: #000000;">6</span></td><td style="background-color: #e2effe;"><span style="color: #d73529;">Larva</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">38</span></td><td style="background-color: #737dc0;"><span style="color: #000000;">50.0</span></td>
        </tr><tr>
        <td style="background-color: #d2dfee;"><span style="color: #000000;">7</span></td><td style="background-color: #d2dfee;"><span style="color: #d73529;">Action</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">29</span></td><td style="background-color: #867baf;"><span style="color: #000000;">48.28</span></td>
        </tr><tr>
        <td style="background-color: #e2effe;"><span style="color: #000000;">8</span></td><td style="background-color: #e2effe;"><span style="color: #d73529;">Shine</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">17</span></td><td style="background-color: #d17267;"><span style="color: #000000;">41.18</span></td>
        </tr><tr>
        <td style="background-color: #d2dfee;"><span style="color: #000000;">9</span></td><td style="background-color: #d2dfee;"><span style="color: #d73529;">Jaedong</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">26</span></td><td style="background-color: #ee6f4c;"><span style="color: #000000;">38.46</span></td>
        </tr>  </tbody>
    </table>
</div>
<span style="font-size: 12px;"><i>Note: Only players with at least 10 games in the matchup have been included</i></span>
<br/><br/>

A few things I found interesting in those rankings:

- While Light is often praised for his TvZ, it is statistically his worst matchup
- Mong has the most lopsided record, being #2 behind FlaSh in TvP but dead last in TvT and TvZ
- No one has a 55%+ winrate in ZvZ. It really seems to be the most random matchup
- Soulkey is not the best in any matchup but he's top 3 in all matchups
- FlaSh is #1 in every Terran matchup
- Rain is the absolute monarch of Aiur...

...which brings us to the next table: best and worst matchup scores across all matchups:

<div class="table-container">

<table border="1" class="dataframe table table-striped table-bordered">
    <thead>
    <tr>
    <th colspan="4" style="font-size: 24px; text-align: center;">All matchups</th>
</tr><tr style="text-align: right;"><th>Rank</th><th>Name</th><th>Matchup</th><th>Winrate</th></tr>
    </thead>
    <tbody>
    <tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">1</span></td><td style="background-color: #d2dfee;"><span style="color: #d3a514;">Rain</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">PvP</span></td><td style="background-color: #1150ee;"><span style="color: #000000;">84.31</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">2</span></td><td style="background-color: #e2effe;"><span style="color: #1578da;">FlaSh</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">TvP</span></td><td style="background-color: #3569ee;"><span style="color: #000000;">82.14</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">3</span></td><td style="background-color: #d2dfee;"><span style="color: #1578da;">FlaSh</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">TvT</span></td><td style="background-color: #7c9cee;"><span style="color: #000000;">77.78</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">4</span></td><td style="background-color: #e2effe;"><span style="color: #1578da;">Last</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">TvT</span></td><td style="background-color: #dcdfee;"><span style="color: #000000;">72.0</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">5</span></td><td style="background-color: #d2dfee;"><span style="color: #d73529;">Soma</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">ZvP</span></td><td style="background-color: #dfe1ee;"><span style="color: #000000;">71.79</span></td>
    </tr>  </tbody>
</table>

<table border="1" class="dataframe table table-striped table-bordered">
    <thead>
    <tr>
    <th colspan="4" style="font-size: 24px; text-align: center;">All matchups (worst)</th>
</tr><tr style="text-align: right;"><th>Rank</th><th>Name</th><th>Matchup</th><th>Winrate</th></tr>
    </thead>
    <tbody>
    <tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">1</span></td><td style="background-color: #d2dfee;"><span style="color: #1578da;">Mong</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">TvZ</span></td><td style="background-color: #ee3d1a;"><span style="color: #000000;">19.23</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">2</span></td><td style="background-color: #e2effe;"><span style="color: #d73529;">Sacsri</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">ZvP</span></td><td style="background-color: #ee694f;"><span style="color: #000000;">21.74</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">3</span></td><td style="background-color: #d2dfee;"><span style="color: #d73529;">MIsO</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">ZvP</span></td><td style="background-color: #eec0b7;"><span style="color: #000000;">26.67</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">4</span></td><td style="background-color: #e2effe;"><span style="color: #1578da;">Sea</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">TvT</span></td><td style="background-color: #eed7d3;"><span style="color: #000000;">28.0</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">5</span></td><td style="background-color: #d2dfee;"><span style="color: #1578da;">Mind</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">TvT</span></td><td style="background-color: #eee1df;"><span style="color: #000000;">28.57</span></td>
    </tr>  </tbody>
</table>

</div>
<span style="font-size: 12px;"><i>Note: Only players with at least 15 games in the database have been included</i></span>
<br/><br/>

FlaSh once again asserting dominance by occupying two spots on the top 5. His TvZ is also just outside the top 5 here. In addition to that, I'm surprised to see that Mind's TvT is so weak.
<br/><br/>
<h2 id="4">Elo rankings</h2>
Now, these winrates have all been historical, spanning the entire period from the 1st ASL in 2016 to the latest one in 2024. If we want to get a better idea of who are the strongest players right now, it might be interesting to look at how their Elo rating might look like. Calculating Elo with k = 30 and starting rating = 1600, we get the following ranking as of November 2nd, 2024:

<table border="1" class="dataframe table table-striped table-bordered">
    <thead>
    <tr>
    <th colspan="4" style="font-size: 24px; text-align: center;">ASL+KSL Elo rankings, Nov 2nd 2024</th>
</tr><tr style="text-align: right;"><th>Rank</th><th>Name</th><th>Games</th><th>Rating</th>    </tr>
    </thead>
    <tbody>
    <tr>
    <td><span style="color: #000000; background-color: #d2dfee;">1</span></td><td><span style="color: #d73529; background-color: #d2dfee;">SoulKey</span></td><td><span style="color: #000000; background-color: #d2dfee;">244</span></td><td><span style="color: #000000; background-color: #d2dfee;">1943</span></td>
    </tr><tr>
    <td><span style="color: #000000; background-color: #e2effe;">2</span></td><td><span style="color: #1578da; background-color: #e2effe;">FlaSh</span></td><td><span style="color: #000000; background-color: #e2effe;">118</span></td><td><span style="color: #000000; background-color: #e2effe;">1848</span></td>
    </tr><tr>
    <td><span style="color: #000000; background-color: #d2dfee;">3</span></td><td><span style="color: #1578da; background-color: #d2dfee;">Sharp</span></td><td><span style="color: #000000; background-color: #d2dfee;">190</span></td><td><span style="color: #000000; background-color: #d2dfee;">1790</span></td>
    </tr><tr>
    <td><span style="color: #000000; background-color: #e2effe;">4</span></td><td><span style="color: #d3a514; background-color: #e2effe;">Rain</span></td><td><span style="color: #000000; background-color: #e2effe;">182</span></td><td><span style="color: #000000; background-color: #e2effe;">1786</span></td>
    </tr><tr>
    <td><span style="color: #000000; background-color: #d2dfee;">5</span></td><td><span style="color: #d73529; background-color: #d2dfee;">hero</span></td><td><span style="color: #000000; background-color: #d2dfee;">186</span></td><td><span style="color: #000000; background-color: #d2dfee;">1744</span></td>
    </tr><tr>
    <td><span style="color: #000000; background-color: #e2effe;">6</span></td><td><span style="color: #d73529; background-color: #e2effe;">EffOrt</span></td><td><span style="color: #000000; background-color: #e2effe;">74</span></td><td><span style="color: #000000; background-color: #e2effe;">1742</span></td>
    </tr><tr>
    <td><span style="color: #000000; background-color: #d2dfee;">7</span></td><td><span style="color: #d3a514; background-color: #d2dfee;">Snow</span></td><td><span style="color: #000000; background-color: #d2dfee;">187</span></td><td><span style="color: #000000; background-color: #d2dfee;">1731</span></td>
    </tr><tr>
    <td><span style="color: #000000; background-color: #e2effe;">8</span></td><td><span style="color: #1578da; background-color: #e2effe;">Light</span></td><td><span style="color: #000000; background-color: #e2effe;">191</span></td><td><span style="color: #000000; background-color: #e2effe;">1725</span></td>
    </tr><tr>
    <td><span style="color: #000000; background-color: #d2dfee;">9</span></td><td><span style="color: #d3a514; background-color: #d2dfee;">Mini</span></td><td><span style="color: #000000; background-color: #d2dfee;">216</span></td><td><span style="color: #000000; background-color: #d2dfee;">1720</span></td>
    </tr><tr>
    <td><span style="color: #000000; background-color: #e2effe;">10</span></td><td><span style="color: #1578da; background-color: #e2effe;">Last</span></td><td><span style="color: #000000; background-color: #e2effe;">117</span></td><td><span style="color: #000000; background-color: #e2effe;">1716</span></td>
    </tr><tr>
    <td><span style="color: #000000; background-color: #d2dfee;">11</span></td><td><span style="color: #1578da; background-color: #d2dfee;">Rush</span></td><td><span style="color: #000000; background-color: #d2dfee;">157</span></td><td><span style="color: #000000; background-color: #d2dfee;">1709</span></td>
    </tr><tr>
    <td><span style="color: #000000; background-color: #e2effe;">12</span></td><td><span style="color: #d73529; background-color: #e2effe;">Larva</span></td><td><span style="color: #000000; background-color: #e2effe;">113</span></td><td><span style="color: #000000; background-color: #e2effe;">1702</span></td>
    </tr><tr>
    <td><span style="color: #000000; background-color: #d2dfee;">13</span></td><td><span style="color: #1578da; background-color: #d2dfee;">JyJ</span></td><td><span style="color: #000000; background-color: #d2dfee;">100</span></td><td><span style="color: #000000; background-color: #d2dfee;">1692</span></td>
    </tr><tr>
    <td><span style="color: #000000; background-color: #e2effe;">14</span></td><td><span style="color: #d3a514; background-color: #e2effe;">Best</span></td><td><span style="color: #000000; background-color: #e2effe;">175</span></td><td><span style="color: #000000; background-color: #e2effe;">1681</span></td>
    </tr><tr>
    <td><span style="color: #000000; background-color: #d2dfee;">15</span></td><td><span style="color: #d3a514; background-color: #d2dfee;">Bisu</span></td><td><span style="color: #000000; background-color: #d2dfee;">129</span></td><td><span style="color: #000000; background-color: #d2dfee;">1678</span></td>
    </tr><tr>
    <td><span style="color: #000000; background-color: #e2effe;">16</span></td><td><span style="color: #d73529; background-color: #e2effe;">Soma</span></td><td><span style="color: #000000; background-color: #e2effe;">101</span></td><td><span style="color: #000000; background-color: #e2effe;">1673</span></td>
    </tr><tr>
    <td><span style="color: #000000; background-color: #d2dfee;">17</span></td><td><span style="color: #1578da; background-color: #d2dfee;">Mind</span></td><td><span style="color: #000000; background-color: #d2dfee;">118</span></td><td><span style="color: #000000; background-color: #d2dfee;">1655</span></td>
    </tr><tr>
    <td><span style="color: #000000; background-color: #e2effe;">18</span></td><td><span style="color: #d73529; background-color: #e2effe;">Queen</span></td><td><span style="color: #000000; background-color: #e2effe;">143</span></td><td><span style="color: #000000; background-color: #e2effe;">1641</span></td>
    </tr><tr>
    <td><span style="color: #000000; background-color: #d2dfee;">19</span></td><td><span style="color: #1578da; background-color: #d2dfee;">RoyaL</span></td><td><span style="color: #000000; background-color: #d2dfee;">86</span></td><td><span style="color: #000000; background-color: #d2dfee;">1634</span></td>
    </tr><tr>
    <td><span style="color: #000000; background-color: #e2effe;">20</span></td><td><span style="color: #1578da; background-color: #e2effe;">BarrackS</span></td><td><span style="color: #000000; background-color: #e2effe;">51</span></td><td><span style="color: #000000; background-color: #e2effe;">1634</span></td>
    </tr><tr>
    <td><span style="color: #000000; background-color: #d2dfee;">21</span></td><td><span style="color: #d73529; background-color: #d2dfee;">Action</span></td><td><span style="color: #000000; background-color: #d2dfee;">123</span></td><td><span style="color: #000000; background-color: #d2dfee;">1614</span></td>
    </tr><tr>
    <td><span style="color: #000000; background-color: #e2effe;">22</span></td><td><span style="color: #1578da; background-color: #e2effe;">Leta</span></td><td><span style="color: #000000; background-color: #e2effe;">25</span></td><td><span style="color: #000000; background-color: #e2effe;">1609</span></td>
    </tr><tr>
    <td><span style="color: #000000; background-color: #d2dfee;">23</span></td><td><span style="color: #d73529; background-color: #d2dfee;">Calm</span></td><td><span style="color: #000000; background-color: #d2dfee;">24</span></td><td><span style="color: #000000; background-color: #d2dfee;">1603</span></td>
    </tr><tr>
    <td><span style="color: #000000; background-color: #e2effe;">24</span></td><td><span style="color: #1578da; background-color: #e2effe;">Ample</span></td><td><span style="color: #000000; background-color: #e2effe;">34</span></td><td><span style="color: #000000; background-color: #e2effe;">1586</span></td>
    </tr><tr>
    <td><span style="color: #000000; background-color: #d2dfee;">25</span></td><td><span style="color: #d3a514; background-color: #d2dfee;">Horang2</span></td><td><span style="color: #000000; background-color: #d2dfee;">42</span></td><td><span style="color: #000000; background-color: #d2dfee;">1586</span></td>
    </tr><tr>
    <td><span style="color: #000000; background-color: #e2effe;">26</span></td><td><span style="color: #d3a514; background-color: #e2effe;">Stork</span></td><td><span style="color: #000000; background-color: #e2effe;">99</span></td><td><span style="color: #000000; background-color: #e2effe;">1574</span></td>
    </tr><tr>
    <td><span style="color: #000000; background-color: #d2dfee;">27</span></td><td><span style="color: #d73529; background-color: #d2dfee;">Jaedong</span></td><td><span style="color: #000000; background-color: #d2dfee;">97</span></td><td><span style="color: #000000; background-color: #d2dfee;">1573</span></td>
    </tr><tr>
    <td><span style="color: #000000; background-color: #e2effe;">28</span></td><td><span style="color: #d3a514; background-color: #e2effe;">Jaehoon</span></td><td><span style="color: #000000; background-color: #e2effe;">32</span></td><td><span style="color: #000000; background-color: #e2effe;">1566</span></td>
    </tr><tr>
    <td><span style="color: #000000; background-color: #d2dfee;">29</span></td><td><span style="color: #d73529; background-color: #d2dfee;">Sacsri</span></td><td><span style="color: #000000; background-color: #d2dfee;">43</span></td><td><span style="color: #000000; background-color: #d2dfee;">1566</span></td>
    </tr><tr>
    <td><span style="color: #000000; background-color: #e2effe;">30</span></td><td><span style="color: #d3a514; background-color: #e2effe;">Shuttle</span></td><td><span style="color: #000000; background-color: #e2effe;">100</span></td><td><span style="color: #000000; background-color: #e2effe;">1565</span></td>
    </tr><tr>
    <td><span style="color: #000000; background-color: #d2dfee;">31</span></td><td><span style="color: #1578da; background-color: #d2dfee;">Sea</span></td><td><span style="color: #000000; background-color: #d2dfee;">61</span></td><td><span style="color: #000000; background-color: #d2dfee;">1560</span></td>
    </tr><tr>
    <td><span style="color: #000000; background-color: #e2effe;">32</span></td><td><span style="color: #1578da; background-color: #e2effe;">sSak</span></td><td><span style="color: #000000; background-color: #e2effe;">48</span></td><td><span style="color: #000000; background-color: #e2effe;">1538</span></td>
    </tr><tr>
    <td><span style="color: #000000; background-color: #d2dfee;">33</span></td><td><span style="color: #d3a514; background-color: #d2dfee;">free</span></td><td><span style="color: #000000; background-color: #d2dfee;">31</span></td><td><span style="color: #000000; background-color: #d2dfee;">1537</span></td>
    </tr><tr>
    <td><span style="color: #000000; background-color: #e2effe;">34</span></td><td><span style="color: #d73529; background-color: #e2effe;">Shine</span></td><td><span style="color: #000000; background-color: #e2effe;">79</span></td><td><span style="color: #000000; background-color: #e2effe;">1530</span></td>
    </tr><tr>
    <td><span style="color: #000000; background-color: #d2dfee;">35</span></td><td><span style="color: #d3a514; background-color: #d2dfee;">Movie</span></td><td><span style="color: #000000; background-color: #d2dfee;">38</span></td><td><span style="color: #000000; background-color: #d2dfee;">1523</span></td>
    </tr><tr>
    <td><span style="color: #000000; background-color: #e2effe;">36</span></td><td><span style="color: #d73529; background-color: #e2effe;">MIsO</span></td><td><span style="color: #000000; background-color: #e2effe;">47</span></td><td><span style="color: #000000; background-color: #e2effe;">1520</span></td>
    </tr><tr>
    <td><span style="color: #000000; background-color: #d2dfee;">37</span></td><td><span style="color: #d3a514; background-color: #d2dfee;">GuemChi</span></td><td><span style="color: #000000; background-color: #d2dfee;">31</span></td><td><span style="color: #000000; background-color: #d2dfee;">1519</span></td>
    </tr><tr>
    <td><span style="color: #000000; background-color: #e2effe;">38</span></td><td><span style="color: #d73529; background-color: #e2effe;">Killer</span></td><td><span style="color: #000000; background-color: #e2effe;">31</span></td><td><span style="color: #000000; background-color: #e2effe;">1519</span></td>
    </tr><tr>
    <td><span style="color: #000000; background-color: #d2dfee;">39</span></td><td><span style="color: #d73529; background-color: #d2dfee;">Modesty</span></td><td><span style="color: #000000; background-color: #d2dfee;">40</span></td><td><span style="color: #000000; background-color: #d2dfee;">1518</span></td>
    </tr><tr>
    <td><span style="color: #000000; background-color: #e2effe;">40</span></td><td><span style="color: #1578da; background-color: #e2effe;">Mong</span></td><td><span style="color: #000000; background-color: #e2effe;">65</span></td><td><span style="color: #000000; background-color: #e2effe;">1510</span></td>
    </tr>  </tbody>
</table>

SoulKey's recent streak has put him so far in the lead he's almost 100 points ahead of FlaSh at number 2. It will be interesting to hopefully see them battle it out in the next ASL. We should also note that FlaSh dropped some rating during his last recorded games when he was knocked out by Soma in ASL season 10 while playing Random. One can certainly speculate that he might have been closer to Soulkey if he had stuck to his main race.

<h4 id="5"></h4>
Having access to the exact date each game in the database was played, we are also able to draw a graph of how the top players' ratings have developed over the years:

<img src="images/5elotimeseries.png" alt="Elo time series" class="wide-image">

What this graph shows most clearly is just how dominant FlaSh was in 2017-18. 2018-19 brought a sea change with Rain, Last, SoulKey and Light rising to prominence. Later on, in 2021, we saw the rise to greatness of Larva, Mini and Rush. 
<br/>
<h2 id="13">Player winrates and game duration</h2>

Having access to the each game's duration, I drew up a script to search for players with high variance between winrates for different game duration intervals. Here's what I found:

<h3>If you're playing Snow or JyJ, finish them off quickly!</h3>

<img src="images/13Snowwinratebyduration.png" alt="Winrate by duration, Snow" class="wide-image">
<img src="images/13JyJwinratebyduration.png" alt="Winrate by duration, JyJ" class="wide-image">

Snow and JyJ both show a clear trend. If the game is short, they likely lose. The longer the game goes on, the more likely they are to end up winning.

<h3>If you're playing BarrackS, you have a window</h3>

<img src="images/13BarrackSwinratebyduration.png" alt="Winrate by duration, BarrackS" class="wide-image">

BarrackS very often loses after 15-17 minutes but if he makes it past that, he's actually likely to win. 

<h3>If you're playing Mini, try to survive until the late game</h3>

<img src="images/13Miniwinratebyduration.png" alt="Winrate by duration, Mini" class="wide-image">

Ever aggressive, Mini wins his games in the early and midgame.

<h3>If you're playing Shine, kill him in the midgame</h3>

<img src="images/13Shinewinratebyduration.png" alt="Winrate by duration, Shine" class="wide-image">

Shine is dangerous in the early and late game but vulnerable in the midgame.

<h3>Jaedong is weak for three minutes</h3>

<img src="images/13Jaedongwinratebyduration.png" alt="Winrate by duration, Jaedong" class="wide-image">

Jaedong's graph is the most anomalous. He has an extremely low winrate in games that end after 11 to 14 minutes but a very solid winrate in games that end after 8 to 11 and 14 to 17 minutes. In SSL 1, we saw him miss his lurker timing against Light and lose after 11 minutes, which was symptomatic of his TvZ as a whole accordin to Artosis.

<span style="font-size: 12px;"><i>Note: The intervals in the above graphs have been automatically generated to each represent an equal share (roughly 20%) of the player's games, and only players with a lot of games in the database have been included. The winrate in each duration interval for each player in the graphs above is thus calculated from somewhere between 15 and 30 games. This does mean there's a lot of uncertainty but likely most of the trends are not random.</i></span>
<br/><br/>

Lastly, before we move on to some general tournament stats, here's a ranking of the pro players from "fastest" to "slowest" based on their average game duration:

<h4 id="12"></h4>

<table border="1" class="dataframe table table-striped table-bordered">
    <thead>
    <tr>
    <th colspan="4" style="font-size: 24px; text-align: center;">Average game duration by player</th>
</tr><tr style="text-align: right;"><th>Rank</th><th>Name</th><th>Race</th><th>Avg. game duration</th>    </tr>
    </thead>
    <tbody>
    <tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">1</span></td><td style="background-color: #d2dfee;"><span style="color: #d73529;"><b>HyuN</b></span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">Zerg</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">9:50</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">2</span></td><td style="background-color: #e2effe;"><span style="color: #d73529;"><b>beast</b></span></td><td style="background-color: #e2effe;"><span style="color: #000000;">Zerg</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">9:54</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">3</span></td><td style="background-color: #d2dfee;"><span style="color: #d73529;"><b>Hyuk</b></span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">Zerg</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">11:09</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">4</span></td><td style="background-color: #e2effe;"><span style="color: #d73529;"><b>Calm</b></span></td><td style="background-color: #e2effe;"><span style="color: #000000;">Zerg</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">12:09</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">5</span></td><td style="background-color: #d2dfee;"><span style="color: #d73529;"><b>Soma</b></span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">Zerg</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">12:22</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">6</span></td><td style="background-color: #e2effe;"><span style="color: #d73529;"><b>Queen</b></span></td><td style="background-color: #e2effe;"><span style="color: #000000;">Zerg</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">12:40</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">7</span></td><td style="background-color: #d2dfee;"><span style="color: #d73529;"><b>MIsO</b></span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">Zerg</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">12:49</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">8</span></td><td style="background-color: #e2effe;"><span style="color: #d73529;"><b>Shine</b></span></td><td style="background-color: #e2effe;"><span style="color: #000000;">Zerg</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">12:55</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">9</span></td><td style="background-color: #d2dfee;"><span style="color: #d73529;"><b>Killer</b></span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">Zerg</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">12:55</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">10</span></td><td style="background-color: #e2effe;"><span style="color: #d73529;"><b>hero</b></span></td><td style="background-color: #e2effe;"><span style="color: #000000;">Zerg</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">12:59</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">11</span></td><td style="background-color: #d2dfee;"><span style="color: #1578da;"><b>BarrackS</b></span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">Terran</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">13:02</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">12</span></td><td style="background-color: #e2effe;"><span style="color: #d73529;"><b>Jaedong</b></span></td><td style="background-color: #e2effe;"><span style="color: #000000;">Zerg</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">13:10</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">13</span></td><td style="background-color: #d2dfee;"><span style="color: #d73529;"><b>SoulKey</b></span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">Zerg</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">13:10</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">14</span></td><td style="background-color: #e2effe;"><span style="color: #d73529;"><b>Sacsri</b></span></td><td style="background-color: #e2effe;"><span style="color: #000000;">Zerg</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">13:11</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">15</span></td><td style="background-color: #d2dfee;"><span style="color: #d3a514;"><b>Bisu</b></span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">Protoss</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">13:23</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">16</span></td><td style="background-color: #e2effe;"><span style="color: #d3a514;"><b>Mini</b></span></td><td style="background-color: #e2effe;"><span style="color: #000000;">Protoss</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">13:33</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">17</span></td><td style="background-color: #d2dfee;"><span style="color: #d73529;"><b>ggaemo</b></span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">Zerg</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">13:40</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">18</span></td><td style="background-color: #e2effe;"><span style="color: #d73529;"><b>Modesty</b></span></td><td style="background-color: #e2effe;"><span style="color: #000000;">Zerg</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">13:49</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">19</span></td><td style="background-color: #d2dfee;"><span style="color: #d3a514;"><b>Movie</b></span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">Protoss</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">13:56</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">20</span></td><td style="background-color: #e2effe;"><span style="color: #d73529;"><b>Larva</b></span></td><td style="background-color: #e2effe;"><span style="color: #000000;">Zerg</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">13:58</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">21</span></td><td style="background-color: #d2dfee;"><span style="color: #d73529;"><b>EffOrt</b></span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">Zerg</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">14:00</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">22</span></td><td style="background-color: #e2effe;"><span style="color: #d3a514;"><b>nOOb</b></span></td><td style="background-color: #e2effe;"><span style="color: #000000;">Protoss</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">14:08</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">23</span></td><td style="background-color: #d2dfee;"><span style="color: #1578da;"><b>RoyaL</b></span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">Terran</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">14:17</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">24</span></td><td style="background-color: #e2effe;"><span style="color: #d73529;"><b>Action</b></span></td><td style="background-color: #e2effe;"><span style="color: #000000;">Zerg</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">14:19</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">25</span></td><td style="background-color: #d2dfee;"><span style="color: #d3a514;"><b>Horang2</b></span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">Protoss</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">14:41</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">26</span></td><td style="background-color: #e2effe;"><span style="color: #d3a514;"><b>Jaehoon</b></span></td><td style="background-color: #e2effe;"><span style="color: #000000;">Protoss</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">14:46</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">27</span></td><td style="background-color: #d2dfee;"><span style="color: #d3a514;"><b>Rain</b></span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">Protoss</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">14:47</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">28</span></td><td style="background-color: #e2effe;"><span style="color: #1578da;"><b>FlaSh</b></span></td><td style="background-color: #e2effe;"><span style="color: #000000;">Terran</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">14:48</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">29</span></td><td style="background-color: #d2dfee;"><span style="color: #d3a514;"><b>Stork</b></span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">Protoss</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">14:59</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">30</span></td><td style="background-color: #e2effe;"><span style="color: #1578da;"><b>Ample</b></span></td><td style="background-color: #e2effe;"><span style="color: #000000;">Terran</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">15:08</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">31</span></td><td style="background-color: #d2dfee;"><span style="color: #d3a514;"><b>Best</b></span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">Protoss</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">15:12</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">32</span></td><td style="background-color: #e2effe;"><span style="color: #1578da;"><b>Rush</b></span></td><td style="background-color: #e2effe;"><span style="color: #000000;">Terran</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">15:21</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">33</span></td><td style="background-color: #d2dfee;"><span style="color: #1578da;"><b>Light</b></span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">Terran</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">15:22</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">34</span></td><td style="background-color: #e2effe;"><span style="color: #1578da;"><b>ForGG</b></span></td><td style="background-color: #e2effe;"><span style="color: #000000;">Terran</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">15:22</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">35</span></td><td style="background-color: #d2dfee;"><span style="color: #d3a514;"><b>Snow</b></span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">Protoss</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">15:29</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">36</span></td><td style="background-color: #e2effe;"><span style="color: #d3a514;"><b>GuemChi</b></span></td><td style="background-color: #e2effe;"><span style="color: #000000;">Protoss</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">15:30</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">37</span></td><td style="background-color: #d2dfee;"><span style="color: #1578da;"><b>Piano</b></span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">Terran</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">15:55</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">38</span></td><td style="background-color: #e2effe;"><span style="color: #d3a514;"><b>Shuttle</b></span></td><td style="background-color: #e2effe;"><span style="color: #000000;">Protoss</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">16:05</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">39</span></td><td style="background-color: #d2dfee;"><span style="color: #1578da;"><b>Leta</b></span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">Terran</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">16:05</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">40</span></td><td style="background-color: #e2effe;"><span style="color: #1578da;"><b>Last</b></span></td><td style="background-color: #e2effe;"><span style="color: #000000;">Terran</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">16:07</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">41</span></td><td style="background-color: #d2dfee;"><span style="color: #1578da;"><b>sSak</b></span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">Terran</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">16:26</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">42</span></td><td style="background-color: #e2effe;"><span style="color: #1578da;"><b>Mind</b></span></td><td style="background-color: #e2effe;"><span style="color: #000000;">Terran</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">16:36</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">43</span></td><td style="background-color: #d2dfee;"><span style="color: #1578da;"><b>Sea</b></span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">Terran</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">16:41</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">44</span></td><td style="background-color: #e2effe;"><span style="color: #1578da;"><b>JyJ</b></span></td><td style="background-color: #e2effe;"><span style="color: #000000;">Terran</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">16:45</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">45</span></td><td style="background-color: #d2dfee;"><span style="color: #d3a514;"><b>free</b></span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">Protoss</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">17:16</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">46</span></td><td style="background-color: #e2effe;"><span style="color: #1578da;"><b>Sharp</b></span></td><td style="background-color: #e2effe;"><span style="color: #000000;">Terran</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">17:28</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">47</span></td><td style="background-color: #d2dfee;"><span style="color: #1578da;"><b>Mong</b></span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">Terran</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">17:51</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">48</span></td><td style="background-color: #e2effe;"><span style="color: #1578da;"><b>Speed</b></span></td><td style="background-color: #e2effe;"><span style="color: #000000;">Terran</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">20:45</span></td>
    </tr>  </tbody>
</table>

<span style="font-size: 12px;"><i>Note: Only players with at least 10 games in the database have been included</i></span>

Some findings here:
- BarrackS is suspiciously up there with the Zergs. Infested?
- free is practically a Terran trapped in a Protoss' body
- FlaSh is notably the third fastest Terran, but this may in part be because a few of his matches were not actually played in Terran matchups. This will only have had a minor effect though.
- The slowest player is named Speed.
<br/><br/>

Finally, we can take a look at how quickly or slowly each player <i>wins</i> on average.

<table border="1" class="dataframe table table-striped table-bordered">
    <thead>
    <tr>
    <th colspan="4" style="font-size: 24px; text-align: center;">Average game duration by player (wins only)</th>
</tr><tr style="text-align: right;"><th>Rank</th><th>Name</th><th>Race</th><th>Avg. game duration</th>    </tr>
    </thead>
    <tbody>
    <tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">1</span></td><td style="background-color: #d2dfee;"><span style="color: #d73529;"><b>MIsO</b></span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">Zerg</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">10:54</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">2</span></td><td style="background-color: #e2effe;"><span style="color: #d73529;"><b>Soma</b></span></td><td style="background-color: #e2effe;"><span style="color: #000000;">Zerg</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">11:49</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">3</span></td><td style="background-color: #d2dfee;"><span style="color: #d73529;"><b>Queen</b></span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">Zerg</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">12:20</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">4</span></td><td style="background-color: #e2effe;"><span style="color: #d3a514;"><b>Mini</b></span></td><td style="background-color: #e2effe;"><span style="color: #000000;">Protoss</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">12:30</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">5</span></td><td style="background-color: #d2dfee;"><span style="color: #1578da;"><b>Ample</b></span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">Terran</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">12:51</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">6</span></td><td style="background-color: #e2effe;"><span style="color: #d73529;"><b>Modesty</b></span></td><td style="background-color: #e2effe;"><span style="color: #000000;">Zerg</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">12:57</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">7</span></td><td style="background-color: #d2dfee;"><span style="color: #d3a514;"><b>Bisu</b></span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">Protoss</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">13:00</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">8</span></td><td style="background-color: #e2effe;"><span style="color: #d73529;"><b>hero</b></span></td><td style="background-color: #e2effe;"><span style="color: #000000;">Zerg</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">13:00</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">9</span></td><td style="background-color: #d2dfee;"><span style="color: #d73529;"><b>Jaedong</b></span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">Zerg</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">13:08</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">10</span></td><td style="background-color: #e2effe;"><span style="color: #d73529;"><b>Shine</b></span></td><td style="background-color: #e2effe;"><span style="color: #000000;">Zerg</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">13:12</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">11</span></td><td style="background-color: #d2dfee;"><span style="color: #d73529;"><b>SoulKey</b></span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">Zerg</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">13:19</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">12</span></td><td style="background-color: #e2effe;"><span style="color: #d73529;"><b>Larva</b></span></td><td style="background-color: #e2effe;"><span style="color: #000000;">Zerg</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">13:28</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">13</span></td><td style="background-color: #d2dfee;"><span style="color: #d73529;"><b>Action</b></span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">Zerg</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">13:52</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">14</span></td><td style="background-color: #e2effe;"><span style="color: #d3a514;"><b>Rain</b></span></td><td style="background-color: #e2effe;"><span style="color: #000000;">Protoss</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">13:59</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">15</span></td><td style="background-color: #d2dfee;"><span style="color: #d73529;"><b>EffOrt</b></span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">Zerg</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">14:05</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">16</span></td><td style="background-color: #e2effe;"><span style="color: #d73529;"><b>Sacsri</b></span></td><td style="background-color: #e2effe;"><span style="color: #000000;">Zerg</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">14:09</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">17</span></td><td style="background-color: #d2dfee;"><span style="color: #1578da;"><b>FlaSh</b></span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">Terran</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">14:21</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">18</span></td><td style="background-color: #e2effe;"><span style="color: #d3a514;"><b>Movie</b></span></td><td style="background-color: #e2effe;"><span style="color: #000000;">Protoss</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">14:25</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">19</span></td><td style="background-color: #d2dfee;"><span style="color: #d3a514;"><b>GuemChi</b></span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">Protoss</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">14:30</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">20</span></td><td style="background-color: #e2effe;"><span style="color: #d3a514;"><b>Jaehoon</b></span></td><td style="background-color: #e2effe;"><span style="color: #000000;">Protoss</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">14:55</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">21</span></td><td style="background-color: #d2dfee;"><span style="color: #d3a514;"><b>free</b></span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">Protoss</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">14:57</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">22</span></td><td style="background-color: #e2effe;"><span style="color: #1578da;"><b>Rush</b></span></td><td style="background-color: #e2effe;"><span style="color: #000000;">Terran</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">15:05</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">23</span></td><td style="background-color: #d2dfee;"><span style="color: #d3a514;"><b>Best</b></span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">Protoss</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">15:23</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">24</span></td><td style="background-color: #e2effe;"><span style="color: #1578da;"><b>RoyaL</b></span></td><td style="background-color: #e2effe;"><span style="color: #000000;">Terran</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">15:50</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">25</span></td><td style="background-color: #d2dfee;"><span style="color: #d3a514;"><b>Stork</b></span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">Protoss</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">15:54</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">26</span></td><td style="background-color: #e2effe;"><span style="color: #1578da;"><b>Last</b></span></td><td style="background-color: #e2effe;"><span style="color: #000000;">Terran</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">16:11</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">27</span></td><td style="background-color: #d2dfee;"><span style="color: #1578da;"><b>BarrackS</b></span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">Terran</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">16:30</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">28</span></td><td style="background-color: #e2effe;"><span style="color: #d3a514;"><b>Shuttle</b></span></td><td style="background-color: #e2effe;"><span style="color: #000000;">Protoss</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">16:48</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">29</span></td><td style="background-color: #d2dfee;"><span style="color: #1578da;"><b>Light</b></span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">Terran</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">16:52</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">30</span></td><td style="background-color: #e2effe;"><span style="color: #1578da;"><b>Mind</b></span></td><td style="background-color: #e2effe;"><span style="color: #000000;">Terran</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">16:55</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">31</span></td><td style="background-color: #d2dfee;"><span style="color: #d3a514;"><b>Snow</b></span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">Protoss</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">16:58</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">32</span></td><td style="background-color: #e2effe;"><span style="color: #1578da;"><b>sSak</b></span></td><td style="background-color: #e2effe;"><span style="color: #000000;">Terran</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">17:22</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">33</span></td><td style="background-color: #d2dfee;"><span style="color: #d3a514;"><b>Horang2</b></span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">Protoss</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">17:26</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">34</span></td><td style="background-color: #e2effe;"><span style="color: #1578da;"><b>Leta</b></span></td><td style="background-color: #e2effe;"><span style="color: #000000;">Terran</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">17:34</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">35</span></td><td style="background-color: #d2dfee;"><span style="color: #1578da;"><b>Sea</b></span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">Terran</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">17:37</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">36</span></td><td style="background-color: #e2effe;"><span style="color: #1578da;"><b>Sharp</b></span></td><td style="background-color: #e2effe;"><span style="color: #000000;">Terran</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">18:14</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">37</span></td><td style="background-color: #d2dfee;"><span style="color: #1578da;"><b>Mong</b></span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">Terran</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">18:49</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">38</span></td><td style="background-color: #e2effe;"><span style="color: #1578da;"><b>JyJ</b></span></td><td style="background-color: #e2effe;"><span style="color: #000000;">Terran</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">18:52</span></td>
    </tr>  </tbody>
</table>

This shows JyJ as the most "patient" player, with his average victory having the longest duration. At the top, we find notoriously aggressive MIsO (a.k.a. Where), while Mini and his zealot pressure leads the non-Zerg pack.

<h1 id="TournamentStats">4. Tournament Stats</h1>

In this section, we'll look at some overall stats. First we'll look at the longest and shortest games, game duration by matchup, and game duration by spawn locations. Then we'll take a look at how Bo5 and Bo7 series normally play out, and then finally the advantage of being seeded and the probability of winning a group decider match.
<br/>
<h2 id="9">Longest and shortest games in ASL/KSL history</h2>

Just for curiosity's sake, these were the longest games ever played in ASL or KSL:

<table border="1" class="dataframe table table-striped table-bordered">
    <thead>
    <tr>
    <th colspan="9" style="font-size: 24px; text-align: center;">Longest games</th>
</tr><tr style="text-align: right;"><th>Rank</th><th>Matchup</th><th>Winner</th><th>Loser</th><th>Map</th><th>Date</th><th>Tournament</th><th>Season</th><th>Duration</th>    </tr>
    </thead>
    <tbody>
    <tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">1</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">TvT</span></td><td style="background-color: #d2dfee;"><span style="color: #1578da;"><b>Last</b></span></td><td style="background-color: #d2dfee;"><span style="color: #1578da;"><b>Sharp</b></span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">Sylphid</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">2019-7-21</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">ASL</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">8</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;"><b>48 minutes</b></span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">2</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">TvT</span></td><td style="background-color: #e2effe;"><span style="color: #1578da;"><b>Mind</b></span></td><td style="background-color: #e2effe;"><span style="color: #1578da;"><b>Rush</b></span></td><td style="background-color: #e2effe;"><span style="color: #000000;">Fighting Spirit</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">2017-9-12</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">ASL</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">4</span></td><td style="background-color: #e2effe;"><span style="color: #000000;"><b>47 minutes</b></span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">3</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">PvZ</span></td><td style="background-color: #d2dfee;"><span style="color: #d73529;"><b>SoulKey</b></span></td><td style="background-color: #d2dfee;"><span style="color: #d3a514;"><b>Snow</b></span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">Blitz Y</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">2024-4-16</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">ASL</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">17</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;"><b>44 minutes</b></span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">4</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">TvT</span></td><td style="background-color: #e2effe;"><span style="color: #1578da;"><b>Sea</b></span></td><td style="background-color: #e2effe;"><span style="color: #1578da;"><b>FlaSh</b></span></td><td style="background-color: #e2effe;"><span style="color: #000000;">Benzene</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">2017-1-22</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">ASL</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">2</span></td><td style="background-color: #e2effe;"><span style="color: #000000;"><b>41 minutes</b></span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">5</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">PvZ</span></td><td style="background-color: #d2dfee;"><span style="color: #d3a514;"><b>Best</b></span></td><td style="background-color: #d2dfee;"><span style="color: #d73529;"><b>Action</b></span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">Nemesis</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">2023-4-3</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">ASL</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">15</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;"><b>41 minutes</b></span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">6</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">TvP</span></td><td style="background-color: #e2effe;"><span style="color: #1578da;"><b>Light</b></span></td><td style="background-color: #e2effe;"><span style="color: #d3a514;"><b>Rain</b></span></td><td style="background-color: #e2effe;"><span style="color: #000000;">Fighting Spirit</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">2018-10-18</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">KSL</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">2</span></td><td style="background-color: #e2effe;"><span style="color: #000000;"><b>40 minutes</b></span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">7</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">PvZ</span></td><td style="background-color: #d2dfee;"><span style="color: #d3a514;"><b>Shuttle</b></span></td><td style="background-color: #d2dfee;"><span style="color: #d73529;"><b>EffOrt</b></span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">Transistor</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">2018-4-15</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">ASL</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">5</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;"><b>39 minutes</b></span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">8</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">PvZ</span></td><td style="background-color: #e2effe;"><span style="color: #d73529;"><b>hero</b></span></td><td style="background-color: #e2effe;"><span style="color: #d3a514;"><b>Mini</b></span></td><td style="background-color: #e2effe;"><span style="color: #000000;">Third World</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">2018-5-13</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">ASL</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">5</span></td><td style="background-color: #e2effe;"><span style="color: #000000;"><b>39 minutes</b></span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">9</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">TvZ</span></td><td style="background-color: #d2dfee;"><span style="color: #d73529;"><b>SoulKey</b></span></td><td style="background-color: #d2dfee;"><span style="color: #1578da;"><b>Mong</b></span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">Vermeer</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">2022-2-17</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">ASL</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">13</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;"><b>39 minutes</b></span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">10</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">TvP</span></td><td style="background-color: #e2effe;"><span style="color: #d3a514;"><b>Best</b></span></td><td style="background-color: #e2effe;"><span style="color: #1578da;"><b>Light</b></span></td><td style="background-color: #e2effe;"><span style="color: #000000;">Seventy-six</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">2023-3-28</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">ASL</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">15</span></td><td style="background-color: #e2effe;"><span style="color: #000000;"><b>39 minutes</b></span></td>
    </tr>  </tbody>
</table>

...and these were the shortest:

<table border="1" class="dataframe table table-striped table-bordered">
    <thead>
    <tr>
    <th colspan="9" style="font-size: 24px; text-align: center;">Shortest games</th>
</tr><tr style="text-align: right;"><th>Rank</th><th>Matchup</th><th>Winner</th><th>Loser</th><th>Map</th><th>Date</th><th>Tournament</th><th>Season</th><th>Duration</th>    </tr>
    </thead>
    <tbody>
    <tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">1</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">TvZ</span></td><td style="background-color: #d2dfee;"><span style="color: #d73529;"><b>SoulKey</b></span></td><td style="background-color: #d2dfee;"><span style="color: #1578da;"><b>FlaSh</b></span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">Camelot</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">2017-5-28</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">ASL</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">3</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;"><b>2 minutes</b></span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">2</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">TvZ</span></td><td style="background-color: #e2effe;"><span style="color: #d73529;"><b>SoulKey</b></span></td><td style="background-color: #e2effe;"><span style="color: #1578da;"><b>Sharp</b></span></td><td style="background-color: #e2effe;"><span style="color: #000000;">Gladiator</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">2018-8-24</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">KSL</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">1</span></td><td style="background-color: #e2effe;"><span style="color: #000000;"><b>2 minutes</b></span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">3</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">TvZ</span></td><td style="background-color: #d2dfee;"><span style="color: #1578da;"><b>Mind</b></span></td><td style="background-color: #d2dfee;"><span style="color: #d73529;"><b>SoulKey</b></span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">Heartbreak Ridge</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">2018-11-9</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">KSL</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">2</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;"><b>2 minutes</b></span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">4</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">TvZ</span></td><td style="background-color: #e2effe;"><span style="color: #d73529;"><b>Shine</b></span></td><td style="background-color: #e2effe;"><span style="color: #1578da;"><b>BarrackS</b></span></td><td style="background-color: #e2effe;"><span style="color: #000000;">Nemesis</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">2022-8-30</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">ASL</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">14</span></td><td style="background-color: #e2effe;"><span style="color: #000000;"><b>2 minutes</b></span></td>
    </tr>  </tbody>
</table>

<span style="font-size: 12px;"><i>Note: Since game duration is only registered by whole minutes completed, games with the same duration in minutes cannot be ranked among each other. There are 29 games in the database that ended between 3:00 and 4:00 but only the four shown above ended between 2:00 and 3:00.</i></span>
<br/><br/>

SoulKey is known as a macrozerg but that apparently doesn't stop him from having been involved in 3 of the 4 shortest ever games in ASL and KSL.

Unsurprisingly, the two longest ever games were all TvTs. These are the average game durations by matchup:

<h4 id="A9"></h4>

<table border="1" class="dataframe table table-striped table-bordered">
    <thead>
    <tr>
    <th colspan="3" style="font-size: 24px; text-align: center;">Average duration of each matchup</th>
</tr><tr style="text-align: right;"><th>Rank</th><th>Matchup</th><th>Average duration</th>    </tr>
    </thead>
    <tbody>
    <tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">1</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">TvT</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">17m58s</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">2</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">TvP</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">16m54s</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">3</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">PvZ</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">14m34s</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">4</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">TvZ</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">14m20s</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">5</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">PvP</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">12m25s</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">6</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">ZvZ</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">9m16s</span></td>
    </tr>  </tbody>
</table>

And these have been the longest games in each matchup respectively:

<h4 id="10"></h4>

<table border="1" class="dataframe table table-striped table-bordered">
    <thead>
    <tr>
    <th colspan="8" style="font-size: 24px; text-align: center;">Longest game of each matchup</th>
</tr><tr style="text-align: right;"><th>Matchup</th><th>Winner</th><th>Loser</th><th>Map</th><th>Date</th><th>Tournament</th><th>Season</th><th>Duration</th>    </tr>
    </thead>
    <tbody>
    <tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">TvT</span></td><td style="background-color: #d2dfee;"><span style="color: #1578da;"><b>Last</b></span></td><td style="background-color: #d2dfee;"><span style="color: #1578da;"><b>Sharp</b></span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">Sylphid</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">2019-7-21</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">ASL</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">8</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;"><b>48 minutes</b></span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">PvZ</span></td><td style="background-color: #e2effe;"><span style="color: #d73529;"><b>SoulKey</b></span></td><td style="background-color: #e2effe;"><span style="color: #d3a514;"><b>Snow</b></span></td><td style="background-color: #e2effe;"><span style="color: #000000;">Blitz Y</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">2024-4-16</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">ASL</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">17</span></td><td style="background-color: #e2effe;"><span style="color: #000000;"><b>44 minutes</b></span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">TvP</span></td><td style="background-color: #d2dfee;"><span style="color: #1578da;"><b>Light</b></span></td><td style="background-color: #d2dfee;"><span style="color: #d3a514;"><b>Rain</b></span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">Fighting Spirit</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">2018-10-18</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">KSL</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">2</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;"><b>40 minutes</b></span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">TvZ</span></td><td style="background-color: #e2effe;"><span style="color: #d73529;"><b>SoulKey</b></span></td><td style="background-color: #e2effe;"><span style="color: #1578da;"><b>Mong</b></span></td><td style="background-color: #e2effe;"><span style="color: #000000;">Vermeer</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">2022-2-17</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">ASL</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">13</span></td><td style="background-color: #e2effe;"><span style="color: #000000;"><b>39 minutes</b></span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">PvP</span></td><td style="background-color: #d2dfee;"><span style="color: #d3a514;"><b>Snow</b></span></td><td style="background-color: #d2dfee;"><span style="color: #d3a514;"><b>free</b></span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">Optimizer</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">2020-10-11</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">ASL</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">10</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;"><b>31 minutes</b></span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">ZvZ</span></td><td style="background-color: #e2effe;"><span style="color: #d73529;"><b>Action</b></span></td><td style="background-color: #e2effe;"><span style="color: #d73529;"><b>EffOrt</b></span></td><td style="background-color: #e2effe;"><span style="color: #000000;">Apocalypse</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">2023-8-21</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">ASL</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">16</span></td><td style="background-color: #e2effe;"><span style="color: #000000;"><b>23 minutes</b></span></td>
    </tr>  </tbody>
</table>

<h2 id="14">Effect of cross spawns on game duration</h2>

It's well known that cross spawns makes games longer, but this effect is drastically stronger in some matchups than others. Here's how cross spawns affects game duration:

<table border="1" class="dataframe table table-striped table-bordered">
    <thead>
    <tr>
    <th colspan="4" style="font-size: 24px; text-align: center;">Matchup duration by spawns</th>
</tr><tr style="text-align: right;"><th>Matchup</th><th>Adjacent spawns</th><th>Cross spawns</th><th>Difference</th>    </tr>
    </thead>
    <tbody>
    <tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">PvZ</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">13m32s</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">16m4s</span></td><td style="background-color: #1150ee;"><span style="color: #000000;">19.46</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">ZvZ</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">9m20s</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">10m15s</span></td><td style="background-color: #819fee;"><span style="color: #000000;">10.25</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">PvP</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">11m56s</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">13m5s</span></td><td style="background-color: #83a0ee;"><span style="color: #000000;">10.04</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">Overall</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">14m17s</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">15m26s</span></td><td style="background-color: #99afee;"><span style="color: #000000;">8.26</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">TvP</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">16m9s</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">17m15s</span></td><td style="background-color: #a7baee;"><span style="color: #000000;">7.08</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">TvT</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">16m47s</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">17m46s</span></td><td style="background-color: #b4c3ee;"><span style="color: #000000;">5.99</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">TvZ</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">14m31s</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">14m51s</span></td><td style="background-color: #dfe1ee;"><span style="color: #000000;">2.45</span></td>
    </tr>  </tbody>
</table>

Cross spawns has by far the strongest effect on the duration of PvZs, whereas it has little effect on TvT and TvZ. Again, I'll leave it to the experts to interpret this difference but I'm curious about the answer.
<br/><br/>

<h2>Series stats</h2>
<h3 id="A3">The first game myth</h3>

In almost every single pre-series interview ever, one or both players states that they "just need to win the first map" and then they'll probably take the whole series. It's really remarkable how ubiquitous this belief is. (And by the way, why are those pre-series interviews always so boring?! Is it something about Korean culture? Whenever they're on, I keep thinking of all the stupid nonsense I'd be saying if I had the floor instead.) Anyway, that was actually what prompted me to start gathering all this data in the first place. This incessantly repeated claim just sounded spurious to me, so I wanted to check it. So I did, and I found that

- The winner of game 1 ended up winning the Best-of-5 <span style="font-size: 18px"><b>73.1%</b></span> of the time.

That might look like a lot at first glance but we have to remember that obviously winning any one game in a best of 5 is going to drastically increase your chances of winning the whole series. To find out if the first game is really so important, what we can do is compare this figure to the same figure for games 2 and 3. Plugging those into the same query, we find that

- The winner of game 2 ended up winning the Best-of-5 <span style="font-size: 18px"><b>71.1%</b></span> of the time, whereas
- The winner of game 3 ended up winning the Best-of-5 <span style="font-size: 18px"><b>73.6%</b></span> of the time.

So winning game 1 is statistically less important than winning game 3, but really each game is almost exactly equally important. This is based on 201 Best-of-5s in the database. Running the same calculations for Best-of-7s actually indicates that game 2 is more important than any other game but that's based on only 45 recorded Best-of-7s and therefore tells us almost nothing.

In ASL Season 17, Soulkey became the first player to win an ASL finals series after losing the first game. This only goes to show that such streaks are bound to be broken sooner or later. Still, it was statistically remarkable while it lasted.

In conclusion:

<img src="images/busted.png" alt="Busted!">
<br/>

<h3 id="A4">Map selection advantage</h3>

Players and casters often place some emphasis on the advantage of map selection. I wanted to test this assumption also and in doing so, I found something surprising:

<h4><i>Being the one who selects the map is just as important in mirror matchups as in non-mirror matchups</i></h4>

Generally speaking;

- the player who chose the map went on to win the game in <span style="font-size: 18px"><b>54.3%</b></span> of cases, 
- whereas for mirror matchups only, the map chooser won <span style="font-size: 18px"><b>53.1%</b></span> of the time

This is surprising because the advantage of choosing a map is often chalked up to being about whether this map is generally good for your race in the given matchup or not.

The relatively low overall winrate for the map chooser seems partially to be due to the limited average range of choices. Once we get to the last few maps of the series, there might only be two or three maps left to choose from, which might not be much of an advantage. As such, we can see that when counting only the first map choice:

- the player who chose the first map won that game in <span style="font-size: 18px"><b>58.8%</b></span> of cases.

<br/>
<h3>Reverse sweeps</h3>

The last series stat I've registered is the probability of reverse sweeps. In 201 Best-of-5s, we have seen seven reverse sweeps. The probability of making a reverse sweep in a Best-of-5 (i.e. the probability that if you're down 0-2, you go on to win the series) stands at <span style="font-size: 18px"><b>6.8%</b></span>.

In 45 Best-of-7s across ASL and KSL, there has never been a reverse sweep.

<br/>
<h3 id="A7">Seeds</h3>

Having dealt with the first game myth, let's try to take on another pre-game-interview cliché: "My goal is to make it to the Round of 4 and get seeded for the next season". Further investigation shows that this cliché has somewhat more merit. Comparing the average season results of seeded players and non-seeded players, we get the following:

- Average result of seeded player: **8.3**
- Average result of non-seeded player: **14.8**

This means that the average result for a seeded player was roughly getting eliminated in the Round of 8, whereas the average result of a non-seeded player was roughly getting eliminated in the Round of 16. This is a really considerable advantage, and it should be noted I am comparing the **same set of players**, meaning the average result for non-seeded players listed here is the average result for *players who have been seeded in at least one season, in seasons where they were not seeded*. So the figures can't be explained by arguing that players who earn a seed are obviously just better than those who don't. More likely the explanation is that the ASL's Round of 24 with its Best-of-1 format is a real slaughterhouse that even the best players struggle to make it out of alive.

To further galvanize this point, becoming a seeded player greatly increases your chance of becoming a seeded player again in the next season:

- Probability of gaining seed as already seeded player: <span style="font-size: 18px"><b>39.7%</b></span>
- Probability of gaining seed as non-seeded player: <span style="font-size: 18px"><b>17.3%</b></span>
<br/>
<h3 id="A8">Decider matches: Winners' loser vs losers' winner</h3>

That leaves just one more thing I wanted to check. Something has always bothered me about the double elimination format employed in starleague group stages. It seems unfair when there's a rematch in the decider match and the winner of the first match gets eliminated. Those players came out 1-1 on the night and although the advancing player did win the intervening match, that may only have been because he was facing easier opposition in the losers' match than the eliminated player was facing in the winners' match.

In any case, I found that across 176 decider matches,

- Winners' loser advanced <span style="font-size: 18px"><b>53.8%</b></span> of the time, while
- Losers' winner advanced <span style="font-size: 18px"><b>46.2%</b></span> of the time



<br/><br/>
<h1>5. <span style="font-size: 24px;">(You must construct)</span> Additional notes</h1>
Please get in touch if you have found any errors in these charts, if you feel there's something important I forgot to mention, or if you have any requests for insights you'd like me to pull from the database. Anything pertaining to game duration, map details, tournament results, series outcomes or temporal developments should be possible to draw from there. The database also includes some columns that I have not touched upon here, such as birth year of the players, year of publication for maps, ASL tiers, and Ro. 24 and Ro. 16 group affiliations. I have also categorized maps as island or standard but since so few games have been played on island maps, I can't really make any inferences about that. What I don't have is any information about build orders. That would be the next level. But it would be challenging to categorize the build orders in useful ways and very time-consuming to gather the data.

I would like to stress that I am not a statistician. I'm just a layperson with a basic understanding, doing my best. I haven't bothered to calculate p-values for all the charts, and my uncertainty assessments are just estimates. I apologize if you're a professional statistician and reading any of this has caused you to facepalm.

Feel free to copy these charts and tables but please link here if you publish them.

Thanks to Liquipedia for providing most of the data and to everyone who's keeping Starcraft alive during its very first century as the greatest game ever!

How to get in touch:

Reddit: <a href="https://reddit.com/u/jacobvso">u/jacobvso</a>  
TL.net: <a href="https://tl.net/forum/profile.php?user=JackyVSO">JackyVSO</a>

If you're interested in a detailed explanation of how I did this, that is available [here](https://github.com/JackyVSO/Starcraft/blob/main/readme.md).

<br/><br/>
<br/><br/>


