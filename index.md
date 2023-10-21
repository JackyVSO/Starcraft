---
layout: default
title: Stats from the remastered era of pro Starcraft 1
---

# Markdown Heading
#### by Jacob Stubbe Østergaard / JackyVSO 

## Introduction
The following is a set of insights gleaned from data on offline Starcraft 1 tournament games at the pro level between 2016 and 2023. The dataset comprises all 16 seasons of ASL and all 4 seasons of KSL for a total of <span style="font-size: 20px;">**1,906 games**</span>. This is enough to make lots of statistically significant inferences but also few enough that more fine-grained insights that build on a small subset of the games come with a lot of uncertainty. It should also be noted that, since the dataset consists exclusively of top level games, the insights in this article apply only to Starcraft played at the very highest skill level. Different dynamics may be at play at other levels.

Game data includes players, outcome, date, duration, spawn locations, map details, map selection and tournament context. I have personally compiled this data in a SQL database, which I have then queried for the insights. Most of the data has been collected from Liquipedia, while game duration and spawn location has been collected from AfreecaTV VODs.

Making these stats available is my attempt to give something back to the community. I hope you find them interesting. Please comment if you have further questions that may be answered from this dataset, and I'll get back to you.

## Table of contents
This article is divided into four main parts: Matchups, Maps, Players and Tournament Stats. For the casuals, I recommend using this menu to find the stats you're interested in. For the nerds, I recommend diving right in and reading the article from end to end.

### 1. [Matchups](#Matchups)
- [Overall winrate for each race](#A2)
- [Frequency of each matchup](#A5)
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

<h1 class="h1" id="#Matchups"> 1. Matchups</h1>
<span style="font-size: 24px;"><i>Artosis is technically correct - the best kind of correct</i></span>
<h4 id="#A2">.</h4>

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
    <tr style="text-align: right;"><table border="1" class="dataframe table table-striped table-bordered">
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

This table shows the overall winrate for each race across both of its non-mirror matchups. It seems to show that Protoss is the best race by a margin of 0.3 percentage points over Terran. It also seems to show that Terran is the 2nd best race. But since Artosis often points out that Terran only appears to be doing well because Flash is so good, I decided to check what the winrates would be without Flash. To make a fair comparison, I also removed the statistically best player for each of the other races (Rain for Protoss and Effort for Zerg), and this is what the updated figures look like:

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
    <td style="background-color: #d2dfee;"><span style="color: #1578da;">Terran</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">973</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">47.97</span></td>
    </tr><tr>
    <td style="background-color: #e2effe;"><span style="color: #d3a514;">Protoss</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">892</span></td><td style="background-color: #e2effe;"><span style="color: #000000;">49.94</span></td>
    </tr><tr>
    <td style="background-color: #d2dfee;"><span style="color: #d73529;">Zerg</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">1088</span></td><td style="background-color: #d2dfee;"><span style="color: #000000;">48.29</span></td>
    </tr>  </tbody>
</table>

So Terran does seem to be the worst race without Flash, but only 0.3 percentage points below Zerg.  

(While this was a fun exercise, I should really emphasize that it means very little. The Protoss winrate advantage of 50.67 vs 50.33 over Terran amounts to an advantage of no more than four games, which makes it statistically insignificant by any reasonable standards.)  

Now let's look at the winrates of the individual non-mirror matchups. The numbers confirm the well-known pattern of T > Z > P > T but suggests that Zerg's advantage over Protoss is slightly smaller than Terran's advantage over Zerg and Protoss' advantage over Terran:  

<h4 id="#A11">.</h4>

![TvP overall winrate](images\A11TvPoverallwinrate.png "TVP overall winrate")  
![TvZ overall winrate](images\A11TvZoverallwinrate.png "TVZ overall winrate")  
![PvZ overall winrates](images\A11PvZoverallwinrate.png "PVZ overall winrate")  

While these figures are very unsurprising, it becomes a lot more interesting when you go into some more detail. For starters, let's take a look at the development of the matchup winrates year on year:

<h4 id="#6">.</h4>

![TvP winrate YoY](images\6TvPwinrates.png "TvP winrate 2016-2023")  
![TvZ winrate YoY](images\6TvZwinrates.png "TvP winrate 2016-2023")  
![PvZ winrate YoY](images\6PvZwinrates.png "TvP winrate 2016-2023")  

These graphs tell quite a different story than the overall winrates. The power distributions have actually fluctuated greatly as the races have struggled for the upper hand in the metagame. The pictures becomes still more nuanced when we take game duration and spawn locations into consideration.