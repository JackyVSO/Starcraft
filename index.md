---
layout: default
title: Stats from the remastered era of pro Starcraft 1
---

# Stats from the remastered era of pro Starcraft 1
#### by Jacob Stubbe Østergaard / JackyVSO  

## Introduction
The following is a set of insights gleaned from data on offline Starcraft 1 tournament games at the pro level between 2016 and 2023. The dataset comprises all 16 seasons of ASL and all 4 seasons of KSL for a total of <span style="font-size: 18px;">**1,906 games**</span>. This is enough to make lots of statistically significant inferences but also few enough that more fine-grained insights that build on a small subset of the games come with a lot of uncertainty. It should also be noted that, since the dataset consists exclusively of top level games, the insights in this article apply only to Starcraft played at the very highest skill level. Different dynamics may be at play at other levels.

Game data includes players, outcome, date, duration, spawn locations, map details, map selection and tournament context. I have personally compiled this data in a SQL database, which I have then queried for the insights. Most of the data has been collected from Liquipedia, while game duration and spawn location has been collected from AfreecaTV VODs.

Making these stats available is my attempt to give something back to the community. I hope you find them interesting. Please comment if you have further questions that may be answered from this dataset, and I'll get back to you.

## Table of contents
This article is divided into four main parts: Matchups, Maps, Players and Tournament Stats. For the casuals, I recommend using this menu to find the stats you're interested in. For the nerds, I recommend diving right in and reading the article from end to end.

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
- [Tileset frequency](#A6)



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
<img src="images/A5matchupfrequency.png", alt="Distribution of matchups">

We can see that mirror matchups are quite rare, which is only logical. The comparative scarcity of TvPs can be explained by a slight overrepresentation of Zergs in ASL and KSL in general (see the figures for total games played by each race in the table below) but that leaves no obvious explanation for why there have then been more TvTs than ZvZs. Maybe Zergs try to avoid each other in group selections. Maybe ZvZ series are generally more one-sided and therefore shorter than TvTs series. I don't know. Now let's move on to matchup winrates, about which this study shows that

<span style="font-size: 24px;"><i>Artosis is technically correct - the best kind of correct</i></span>
<h4 id="A2"></h4>

This table shows the overall winrate for each race across both its non-mirror matchups:

<style>
  .table {
    width: 80%;
    border-collapse: collapse;
    margin: 20px auto;
    font-family: 'IBM Plex Mono', sans-serif;
  }
  .table th, .table td {
    padding: 8px 12px;
    text-align: center;
  }
  .table th {
    background-color: #a2afbe;
    color: #000000;
  }
  .table-striped tbody tr:nth-child(odd) {
    background-color: #d2dfee;
  }
  .table-striped tr:nth-child(even) {
    background-color: #e2effe;
}
  .table-bordered {
    border: 1px solid #ccc;
  }
</style>
<table border="1" class="dataframe table table-striped table-bordered">
    <thead>
    <tr>
    <th colspan="3" style="font-size: 24px; text-align: center;">Overall race winrates</th>
</tr><tr style="text-align: right;"><th>Race</th><th>Total games</th><th>Overall winrate</th>    </tr>
    </thead>
    <tbody>
    <tr>
    <td style="background-color: #d2dfee;"><span style="color: #1578da;">Terran</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">1091</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">50.33</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #d3a514;">Protoss</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">1057</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">50.67</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #d73529;">Zerg</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">1162</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">49.09</span></td>
    </tr>  </tbody>
</table>

 It seems to show that Protoss is the best race by a margin of 0.3 percentage points over Terran. It also seems to show that Terran is the 2nd best race. But since Artosis often points out that Terran only appears to be doing well because Flash is so good, I decided to check what the winrates would be without Flash. To make a fair comparison, I also removed the statistically best player for each of the other races (Rain for Protoss and Effort for Zerg), and this is what the updated figures look like:

<table border="1" class="dataframe table table-striped table-bordered">
    <thead>
    <tr>
    <th colspan="3" style="font-size: 24px; text-align: center;">Overall race winrates</th>
</tr><tr style="text-align: right;"><th>Race</th><th>Total games</th><th>Overall winrate</th>    </tr>
    </thead>
    <tbody>
    <tr>
    <td style="background-color: #d2dfee;"><span style="color: #1578da;">Terran</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">973</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">47.97</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #d3a514;">Protoss</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">892</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">49.94</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #d73529;">Zerg</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">1088</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">48.29</span></td>
    </tr>  </tbody>
</table>

So Terran does seem to be the worst race without Flash, but only 0.3 percentage points below Zerg.  

(While this was a fun exercise, I should really emphasize that it means very little. The Protoss winrate advantage of 50.67 vs 50.33 over Terran amounts to an advantage of no more than four games, which makes it statistically insignificant by any reasonable standards. There is really only one thing that these numbers show very clearly, and that is that Starcraft is a remarkably balanced game - at least when played on carefully designed maps)  

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

These graphs tell quite a different story than the overall winrates. The power distributions have actually fluctuated greatly as the races have struggled for the upper hand in the metagame. The pictures becomes still more nuanced when we take game duration and spawn locations into consideration.  
First, let's look at how game duration correlates to matchup winrates. 

<span style="font-size: 12px;">*Note:because of the limited data available (only 400-500 tournament games played in each non-mirror matchup since 2016), I have created these graphs using 10 automatically clustered intervals, which means the intervals are of different length but each represent roughly the same amount of games (20-50 games per interval). Using any more intervals than this, let alone setting a point for every single minute, would leave some intervals with way too few data points, which would make the graphs noisy/random. The presented graphs represent a compromise between that and a very coarse version with only a few intervals but more certainty. Their minor details do not represent reality but their major trends are accurate.*</span>

<h3 id="11">Zerg rules the early game but struggles in the midgame. The late game is balanced.</h3>

<img src="./images/11TvPwinratesbyduration.png" alt="TvP winrate by game duration" class="wide-image">
<img src="./images/11TvZwinratesbyduration.png" alt="TvZ winrate by game duration" class="wide-image">
<img src="./images/11PvZwinratesbyduration.png" alt="PvZ winrate by game duration" class="wide-image">

We can see that if the game ends quickly, that bodes well for Zerg. In TvZ, there is a clear trend of early victories being Zerg, midgame victories being Terran, and the late game being very even. Long games are quite evenly split in all three matchups. PvZ has a similar trend but with semi-long games being once again Zerg-favored.

Moving on to spawn locations, we come to one of the most unambiguous findings of this study:

<h3 id="A10">Cross spawns is VERY BAD for Terran</h3>
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

If that table began to reveal how circumstance-dependent the power dynamics between the races are, these charts should drive the point home. They show how matchup winrates are affect by whether it's a 2-player, 3-player or 4-player map:

<h4 id="7"></h4>
<img src="images/7TvPspawns.png" alt="TvP winrates by number of spawn locations" class="wide-image">
<img src="images/7TvZspawns.png" alt="TvZ winrates by number of spawn locations" class="wide-image">
<img src="images/7PvZspawns.png" alt="PvZ winrates by number of spawn locations" class="wide-image">

The most notable thing here is just how lopsided TvP on 2-player maps is. Out of 116 games in the database, Terran has won 38 and Protoss has won 78. If TvP was never played on 2-player maps, it would be a Terran-favored matchup. Terran also fares better with more spawning locations against Zerg, although this is far less pronounced. This is consistent with another finding in the data, which was that *the bigger the map (by size in tiles), the better for Terran*. I have not included that figure here because it shows the same as the above but less markedly.
PvZ, on the other hand, seems hardly to be affected by the number of spawning locations on the map at all. I'll leave it to more accomplished players to explain this difference.

<h1 class="h1" id="Maps"> 2. Maps</h1>

Now let's keep our focus on the maps for a bit before we move on to stats about players. No less than 68 different maps have been used in ASL and KSL: 19 2-player maps (553 games), 14 3-player maps (391 games), and 35 4-player maps (962 games).

<h4 id="A6"></h4>
<img src="images/A6Tilesets.png" alt="Distribution of map tilesets">

(For some reason, we almost never see maps on Ash World tileset. Why?)

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
    <td style="background-color: #d2dfee;"><span style="color: #000000;">1</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">Sylphid</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">141</span></td><td style="background-color: #eee1df;"><span style="color: #000000;">47.1</span></td><td style="background-color: #eec8c1;"><span style="color: #000000;">47.1</span></td><td style="background-color: #ee9b8b;"><span style="color: #000000;">58.8</span></td><td style="background-color: #2261ff;"><span style="color: #000000;">94.4</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">2</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">Eddy</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">55</span></td><td style="background-color: #eed9d6;"><span style="color: #000000;">54.5</span></td><td style="background-color: #ee9685;"><span style="color: #000000;">58.8</span></td><td style="background-color: #eec7bf;"><span style="color: #000000;">46.7</span></td><td style="background-color: #2761fa;"><span style="color: #000000;">94.0</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">3</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">Butter</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">41</span></td><td style="background-color: #eed4d0;"><span style="color: #000000;">44.4</span></td><td style="background-color: #ee765f;"><span style="color: #000000;">37.5</span></td><td style="background-color: #eee1df;"><span style="color: #000000;">50.0</span></td><td style="background-color: #3d5fe5;"><span style="color: #000000;">92.1</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">4</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">Polypoid</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">77</span></td><td style="background-color: #eedfdd;"><span style="color: #000000;">53.3</span></td><td style="background-color: #ee6348;"><span style="color: #000000;">64.7</span></td><td style="background-color: #eebdb4;"><span style="color: #000000;">54.5</span></td><td style="background-color: #4b5dd7;"><span style="color: #000000;">90.9</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">5</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">Eclipse</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">94</span></td><td style="background-color: #eeaca0;"><span style="color: #000000;">36.0</span></td><td style="background-color: #eecdc6;"><span style="color: #000000;">52.4</span></td><td style="background-color: #eeac9f;"><span style="color: #000000;">43.3</span></td><td style="background-color: #4b5dd7;"><span style="color: #000000;">90.9</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">6</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">Vermeer</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">46</span></td><td style="background-color: #eeb3a8;"><span style="color: #000000;">62.5</span></td><td style="background-color: #ee674c;"><span style="color: #000000;">64.3</span></td><td style="background-color: #eee1df;"><span style="color: #000000;">50.0</span></td><td style="background-color: #625cc2;"><span style="color: #000000;">89.0</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">7</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">Circuit Breaker</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">149</span></td><td style="background-color: #eea99c;"><span style="color: #000000;">64.7</span></td><td style="background-color: #ee9a8a;"><span style="color: #000000;">58.3</span></td><td style="background-color: #ee7d67;"><span style="color: #000000;">62.5</span></td><td style="background-color: #6f5ab5;"><span style="color: #000000;">87.9</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">8</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">Fighting Spirit</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">105</span></td><td style="background-color: #eebfb7;"><span style="color: #000000;">40.0</span></td><td style="background-color: #ee846f;"><span style="color: #000000;">60.9</span></td><td style="background-color: #ee664c;"><span style="color: #000000;">34.6</span></td><td style="background-color: #715ab3;"><span style="color: #000000;">87.7</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">9</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">Benzene</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">48</span></td><td style="background-color: #eecdc7;"><span style="color: #000000;">42.9</span></td><td style="background-color: #ee3d1a;"><span style="color: #000000;">30.8</span></td><td style="background-color: #ee9f90;"><span style="color: #000000;">58.3</span></td><td style="background-color: #775aad;"><span style="color: #000000;">87.2</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">10</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">Heartbreak Ridge</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">48</span></td><td style="background-color: #ee907e;"><span style="color: #000000;">30.0</span></td><td style="background-color: #ee9e8e;"><span style="color: #000000;">57.9</span></td><td style="background-color: #eeb4a9;"><span style="color: #000000;">55.6</span></td><td style="background-color: #775aad;"><span style="color: #000000;">87.2</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">11</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">Transistor</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">41</span></td><td style="background-color: #eea090;"><span style="color: #000000;">66.7</span></td><td style="background-color: #ee765f;"><span style="color: #000000;">37.5</span></td><td style="background-color: #ee5c3f;"><span style="color: #000000;">33.3</span></td><td style="background-color: #965790;"><span style="color: #000000;">84.6</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">12</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">Overwatch</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">54</span></td><td style="background-color: #eeb3a8;"><span style="color: #000000;">37.5</span></td><td style="background-color: #ee3d1a;"><span style="color: #000000;">69.2</span></td><td style="background-color: #ee3d1a;"><span style="color: #000000;">70.6</span></td><td style="background-color: #b25575;"><span style="color: #000000;">82.2</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">13</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">Gladiator</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">47</span></td><td style="background-color: #ee3d1a;"><span style="color: #000000;">12.5</span></td><td style="background-color: #eee1df;"><span style="color: #000000;">50.0</span></td><td style="background-color: #ee4827;"><span style="color: #000000;">69.2</span></td><td style="background-color: #ff4e2b;"><span style="color: #000000;">75.7</span></td>
    </tr>  </tbody>
</table>

*The winrates displayed are for the first race mentioned in the matchup (e.g. Sylphid has a 47.1% winrate for T in TvP, 47.1% for T in TvZ and 58.8% for P in PvZ)*

So Sylphid appears to be the most balanced map yet made, closely followed by (In The Way of An) Eddy, whereas Gladiator is the least balanced - even though it's somehow perfectly balanced in TvZ. Looking at the scores for Vermeer, Polypoid and Circuit Breaker, we can see that what is sometimes termed "standard maps" are actually clearly Terran-favored, whereas more unusual maps might be less comfortable for Terran.

<h1 id="Players">3. Players</h1>
In this section, we'll abandon the bird's eye view and instead zoom in on how the individual Starcraft 1 pros have been faring against each other. A total of 76 players have qualified for ASL and/or KSL. Here they're listed according to how many tournament games they've played:

<h4 id="1"></h4>
<table border="1" class="dataframe table table-striped table-bordered">
    <thead>
    <tr>
    <th colspan="3" style="font-size: 24px; text-align: center;">Total games played (ASL+KSL)</th>
</tr><tr style="text-align: right;"><th>Rank</th><th>Player</th><th>Games</th>    </tr>
    </thead>
    <tbody>
    <tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">1</span></td><td style="background-color: #d2dfee;"><span style="color: #d73529;">SoulKey</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">205</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">2</span></td><td style="background-color: #e2effe;"><span style="color: #d3a514;">Mini</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">200</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">3</span></td><td style="background-color: #d2dfee;"><span style="color: #1578da;">Light</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">170</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">4</span></td><td style="background-color: #e2effe;"><span style="color: #d3a514;">Rain</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">165</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">5</span></td><td style="background-color: #d2dfee;"><span style="color: #d3a514;">Best</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">163</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">6</span></td><td style="background-color: #e2effe;"><span style="color: #1578da;">Sharp</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">157</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">7</span></td><td style="background-color: #d2dfee;"><span style="color: #d3a514;">Snow</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">157</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">8</span></td><td style="background-color: #e2effe;"><span style="color: #d73529;">hero</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">151</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">9</span></td><td style="background-color: #d2dfee;"><span style="color: #d73529;">Queen</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">140</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">10</span></td><td style="background-color: #e2effe;"><span style="color: #1578da;">Rush</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">135</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">11</span></td><td style="background-color: #d2dfee;"><span style="color: #1578da;">FlaSh</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">118</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">12</span></td><td style="background-color: #e2effe;"><span style="color: #1578da;">Last</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">117</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">13</span></td><td style="background-color: #d2dfee;"><span style="color: #d73529;">Action</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">115</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">14</span></td><td style="background-color: #e2effe;"><span style="color: #d73529;">Larva</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">113</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">15</span></td><td style="background-color: #d2dfee;"><span style="color: #d3a514;">Bisu</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">111</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">16</span></td><td style="background-color: #e2effe;"><span style="color: #1578da;">Mind</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">108</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">17</span></td><td style="background-color: #d2dfee;"><span style="color: #d73529;">Soma</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">101</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">18</span></td><td style="background-color: #e2effe;"><span style="color: #d3a514;">Shuttle</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">91</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">19</span></td><td style="background-color: #d2dfee;"><span style="color: #d3a514;">Stork</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">91</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">20</span></td><td style="background-color: #e2effe;"><span style="color: #d73529;">Jaedong</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">88</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">21</span></td><td style="background-color: #d2dfee;"><span style="color: #1578da;">JyJ</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">84</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">22</span></td><td style="background-color: #e2effe;"><span style="color: #d73529;">EffOrt</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">74</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">23</span></td><td style="background-color: #d2dfee;"><span style="color: #d73529;">Shine</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">73</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">24</span></td><td style="background-color: #e2effe;"><span style="color: #1578da;">RoyaL</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">71</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">25</span></td><td style="background-color: #d2dfee;"><span style="color: #1578da;">Mong</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">58</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">26</span></td><td style="background-color: #e2effe;"><span style="color: #1578da;">Sea</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">53</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">27</span></td><td style="background-color: #d2dfee;"><span style="color: #d73529;">MIsO</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">47</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">28</span></td><td style="background-color: #e2effe;"><span style="color: #1578da;">sSak</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">42</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">29</span></td><td style="background-color: #d2dfee;"><span style="color: #d3a514;">Horang2</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">42</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">30</span></td><td style="background-color: #e2effe;"><span style="color: #d73529;">Sacsri</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">40</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">31</span></td><td style="background-color: #d2dfee;"><span style="color: #d73529;">Modesty</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">40</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">32</span></td><td style="background-color: #e2effe;"><span style="color: #d3a514;">Movie</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">38</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">33</span></td><td style="background-color: #d2dfee;"><span style="color: #1578da;">Ample</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">34</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">34</span></td><td style="background-color: #e2effe;"><span style="color: #1578da;">BarrackS</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">34</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">35</span></td><td style="background-color: #d2dfee;"><span style="color: #d3a514;">Jaehoon</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">32</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">36</span></td><td style="background-color: #e2effe;"><span style="color: #d3a514;">GuemChi</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">31</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">37</span></td><td style="background-color: #d2dfee;"><span style="color: #d3a514;">free</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">29</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">38</span></td><td style="background-color: #e2effe;"><span style="color: #d73529;">Killer</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">29</span></td>
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
    <td style="background-color: #e2effe;"><span style="color: #000000;">44</span></td><td style="background-color: #e2effe;"><span style="color: #d73529;">Hyuk</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">15</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">45</span></td><td style="background-color: #d2dfee;"><span style="color: #d73529;">beast</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">14</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">46</span></td><td style="background-color: #e2effe;"><span style="color: #d73529;">HyuN</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">12</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">47</span></td><td style="background-color: #d2dfee;"><span style="color: #d3a514;">nOOb</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">11</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">48</span></td><td style="background-color: #e2effe;"><span style="color: #d73529;">815</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">9</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">49</span></td><td style="background-color: #d2dfee;"><span style="color: #d3a514;">Brain</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">8</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">50</span></td><td style="background-color: #e2effe;"><span style="color: #d3a514;">Ss1nz</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">8</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">51</span></td><td style="background-color: #d2dfee;"><span style="color: #d73529;">ZeLoT</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">7</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">52</span></td><td style="background-color: #e2effe;"><span style="color: #d3a514;">Ruin</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">7</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">53</span></td><td style="background-color: #d2dfee;"><span style="color: #1578da;">HiyA</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">6</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">54</span></td><td style="background-color: #e2effe;"><span style="color: #d3a514;">Pusan</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">5</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">55</span></td><td style="background-color: #d2dfee;"><span style="color: #d3a514;">Sky</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">5</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">56</span></td><td style="background-color: #e2effe;"><span style="color: #d3a514;">Tyson</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">5</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">57</span></td><td style="background-color: #d2dfee;"><span style="color: #d3a514;">YSC</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">5</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">58</span></td><td style="background-color: #e2effe;"><span style="color: #1578da;">BishOp</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">5</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">59</span></td><td style="background-color: #d2dfee;"><span style="color: #d3a514;">Lazy</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">4</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">60</span></td><td style="background-color: #e2effe;"><span style="color: #1578da;">firebathero</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">4</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">61</span></td><td style="background-color: #d2dfee;"><span style="color: #1578da;">ByuL</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">4</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">62</span></td><td style="background-color: #e2effe;"><span style="color: #1578da;">Iris</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">3</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">63</span></td><td style="background-color: #d2dfee;"><span style="color: #1578da;">NaDa</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">3</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">64</span></td><td style="background-color: #e2effe;"><span style="color: #d73529;">Yoon</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">3</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">65</span></td><td style="background-color: #d2dfee;"><span style="color: #d3a514;">Hint</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">2</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">66</span></td><td style="background-color: #e2effe;"><span style="color: #d3a514;">Maru</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">2</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">67</span></td><td style="background-color: #d2dfee;"><span style="color: #d73529;">Force(Name)</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">2</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">68</span></td><td style="background-color: #e2effe;"><span style="color: #d73529;">Terror</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">2</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">69</span></td><td style="background-color: #d2dfee;"><span style="color: #d73529;">PURPOSE</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">2</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">70</span></td><td style="background-color: #e2effe;"><span style="color: #1578da;">Tinkle</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">2</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">71</span></td><td style="background-color: #d2dfee;"><span style="color: #1578da;">soso</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">2</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">72</span></td><td style="background-color: #e2effe;"><span style="color: #1578da;">Scan</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">2</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">73</span></td><td style="background-color: #d2dfee;"><span style="color: #1578da;">Speed</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">2</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">74</span></td><td style="background-color: #e2effe;"><span style="color: #d73529;">JJabNewDa</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">2</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">75</span></td><td style="background-color: #d2dfee;"><span style="color: #d73529;">ivOry</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">2</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">76</span></td><td style="background-color: #e2effe;"><span style="color: #d73529;">Yerim2</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">0</span></td>
    </tr>  </tbody>
</table>

Notably, the two finalists of this last ASL are also the two players with the most total games played in ASL and KSL.  
Now let's take a look at the top players in each matchup:

<table border="1" class="dataframe table table-striped table-bordered small-table">
  <thead>
  <tr>
    <th colspan="4" style="font-size: 24px; text-align: center;">TvT</th>
</tr><tr style="text-align: right;"><th>Rank</th><th>Name</th><th>Games</th><th>Winrate</th>    </tr>
  </thead>
  <tbody>
  <tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">1</span></td><td style="background-color: #d2dfee;"><span style="color: #1578da;">FlaSh</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">27</span></td><td style="background-color: #4382ee;"><span style="color: #000000;">77.78</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">2</span></td><td style="background-color: #e2effe;"><span style="color: #1578da;">Last</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">25</span></td><td style="background-color: #5680dc;"><span style="color: #000000;">72.0</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">3</span></td><td style="background-color: #d2dfee;"><span style="color: #1578da;">Light</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">33</span></td><td style="background-color: #877aae;"><span style="color: #000000;">57.58</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">4</span></td><td style="background-color: #e2effe;"><span style="color: #1578da;">RoyaL</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">16</span></td><td style="background-color: #8b7aaa;"><span style="color: #000000;">56.25</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">5</span></td><td style="background-color: #d2dfee;"><span style="color: #1578da;">Sharp</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">52</span></td><td style="background-color: #9379a2;"><span style="color: #000000;">53.85</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">6</span></td><td style="background-color: #e2effe;"><span style="color: #1578da;">Rush</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">45</span></td><td style="background-color: #9579a1;"><span style="color: #000000;">53.33</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">7</span></td><td style="background-color: #d2dfee;"><span style="color: #1578da;">sSak</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">14</span></td><td style="background-color: #a07896;"><span style="color: #000000;">50.0</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">8</span></td><td style="background-color: #e2effe;"><span style="color: #1578da;">JyJ</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">26</span></td><td style="background-color: #ba757e;"><span style="color: #000000;">42.31</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">9</span></td><td style="background-color: #d2dfee;"><span style="color: #1578da;">BarrackS</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">14</span></td><td style="background-color: #d07269;"><span style="color: #000000;">35.71</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">10</span></td><td style="background-color: #e2effe;"><span style="color: #1578da;">Mind</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">31</span></td><td style="background-color: #db715e;"><span style="color: #000000;">32.26</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">11</span></td><td style="background-color: #d2dfee;"><span style="color: #1578da;">Sea</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">22</span></td><td style="background-color: #dd715c;"><span style="color: #000000;">31.82</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">12</span></td><td style="background-color: #e2effe;"><span style="color: #1578da;">Mong</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">15</span></td><td style="background-color: #ee6f4c;"><span style="color: #000000;">26.67</span></td>
    </tr>  </tbody>
</table>

<table border="1" class="dataframe table table-striped table-bordered small-table">
  <thead>
  <tr>
    <th colspan="4" style="font-size: 24px; text-align: center;">TvP</th>
</tr><tr style="text-align: right;"><th>Rank</th><th>Name</th><th>Games</th><th>Winrate</th>    </tr>
  </thead>
  <tbody>
  <tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">1</span></td><td style="background-color: #d2dfee;"><span style="color: #1578da;">FlaSh</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">28</span></td><td style="background-color: #4382ee;"><span style="color: #000000;">82.14</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">2</span></td><td style="background-color: #e2effe;"><span style="color: #1578da;">Mong</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">20</span></td><td style="background-color: #737dc0;"><span style="color: #000000;">65.0</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">3</span></td><td style="background-color: #d2dfee;"><span style="color: #1578da;">Sea</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">16</span></td><td style="background-color: #7a7cba;"><span style="color: #000000;">62.5</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">4</span></td><td style="background-color: #e2effe;"><span style="color: #1578da;">Light</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">61</span></td><td style="background-color: #847bb0;"><span style="color: #000000;">59.02</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">5</span></td><td style="background-color: #d2dfee;"><span style="color: #1578da;">Rush</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">28</span></td><td style="background-color: #9e7898;"><span style="color: #000000;">50.0</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">6</span></td><td style="background-color: #e2effe;"><span style="color: #1578da;">Mind</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">34</span></td><td style="background-color: #a67790;"><span style="color: #000000;">47.06</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">7</span></td><td style="background-color: #d2dfee;"><span style="color: #1578da;">Last</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">51</span></td><td style="background-color: #a67790;"><span style="color: #000000;">47.06</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">8</span></td><td style="background-color: #e2effe;"><span style="color: #1578da;">Sharp</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">56</span></td><td style="background-color: #b27685;"><span style="color: #000000;">42.86</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">9</span></td><td style="background-color: #d2dfee;"><span style="color: #1578da;">JyJ</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">17</span></td><td style="background-color: #b67581;"><span style="color: #000000;">41.18</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">10</span></td><td style="background-color: #e2effe;"><span style="color: #1578da;">sSak</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">18</span></td><td style="background-color: #bd747b;"><span style="color: #000000;">38.89</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">11</span></td><td style="background-color: #d2dfee;"><span style="color: #1578da;">RoyaL</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">23</span></td><td style="background-color: #d57264;"><span style="color: #000000;">30.43</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">12</span></td><td style="background-color: #e2effe;"><span style="color: #1578da;">Ample</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">14</span></td><td style="background-color: #ee6f4c;"><span style="color: #000000;">21.43</span></td>
    </tr>  </tbody>
</table>

<table border="1" class="dataframe table table-striped table-bordered small-table">
  <thead>
  <tr>
    <th colspan="4" style="font-size: 24px; text-align: center;">TvZ</th>
</tr><tr style="text-align: right;"><th>Rank</th><th>Name</th><th>Games</th><th>Winrate</th>    </tr>
  </thead>
  <tbody>
  <tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">1</span></td><td style="background-color: #d2dfee;"><span style="color: #1578da;">FlaSh</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">54</span></td><td style="background-color: #4382ee;"><span style="color: #000000;">70.37</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">2</span></td><td style="background-color: #e2effe;"><span style="color: #1578da;">Last</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">41</span></td><td style="background-color: #4a81e8;"><span style="color: #000000;">68.29</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">3</span></td><td style="background-color: #d2dfee;"><span style="color: #1578da;">Mind</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">43</span></td><td style="background-color: #5480de;"><span style="color: #000000;">65.12</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">4</span></td><td style="background-color: #e2effe;"><span style="color: #1578da;">RoyaL</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">32</span></td><td style="background-color: #5c7fd6;"><span style="color: #000000;">62.5</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">5</span></td><td style="background-color: #d2dfee;"><span style="color: #1578da;">Ample</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">17</span></td><td style="background-color: #687ecb;"><span style="color: #000000;">58.82</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">6</span></td><td style="background-color: #e2effe;"><span style="color: #1578da;">JyJ</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">41</span></td><td style="background-color: #697eca;"><span style="color: #000000;">58.54</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">7</span></td><td style="background-color: #d2dfee;"><span style="color: #1578da;">Leta</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">11</span></td><td style="background-color: #767cbe;"><span style="color: #000000;">54.55</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">8</span></td><td style="background-color: #e2effe;"><span style="color: #1578da;">Sea</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">15</span></td><td style="background-color: #7a7cba;"><span style="color: #000000;">53.33</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">9</span></td><td style="background-color: #d2dfee;"><span style="color: #1578da;">Light</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">76</span></td><td style="background-color: #7c7cb8;"><span style="color: #000000;">52.63</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">10</span></td><td style="background-color: #e2effe;"><span style="color: #1578da;">Rush</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">62</span></td><td style="background-color: #8a7aab;"><span style="color: #000000;">48.39</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">11</span></td><td style="background-color: #d2dfee;"><span style="color: #1578da;">Sharp</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">48</span></td><td style="background-color: #8b7aa9;"><span style="color: #000000;">47.92</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">12</span></td><td style="background-color: #e2effe;"><span style="color: #1578da;">BarrackS</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">13</span></td><td style="background-color: #c37475;"><span style="color: #000000;">30.77</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #000000;">13</span></td><td style="background-color: #d2dfee;"><span style="color: #1578da;">sSak</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">10</span></td><td style="background-color: #c57473;"><span style="color: #000000;">30.0</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #000000;">14</span></td><td style="background-color: #e2effe;"><span style="color: #1578da;">Mong</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">23</span></td><td style="background-color: #ee6f4c;"><span style="color: #000000;">17.39</span></td>
    </tr>  </tbody>
</table>

dsfds