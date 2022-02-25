# -*- coding: utf-8 -*-
"""RaceChart.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1K3qs_QAw4Yr8no7ppsuhweDIBKro8e4R
"""

pip install bar_chart_race

import pandas as pd

import bar_chart_race as bcr

df = pd.read_csv("https://raw.githubusercontent.com/dexplo/bar_chart_race/master/data/urban_pop.csv")

df.head()

df = df.set_index('year')

bcr.bar_chart_race(df = df, title = "Population Growth")

bcr.bar_chart_race(df = df, title = "Population Growth",n_bars=10, orientation='h', fixed_order= True, cmap = 'prism')

bcr.bar_chart_race(df = df, title = "Population Growth",n_bars=10, orientation='h', fixed_order= True, cmap = 'prism',sort='asc')

bcr.bar_chart_race(df = df, title = "Population Growth",n_bars=10, orientation='h', fixed_order= True)

bcr.bar_chart_race(df = df, title = "Population Growth",n_bars=10, orientation='v', fixed_order= True, cmap = 'prism', filename='sha-datavis-hm1-PopulationGrowth.mp4')

df2 = pd.read_csv("https://raw.githubusercontent.com/dexplo/bar_chart_race/master/data/covid19_tutorial.csv")

df2 = df2.set_index('date')

df2

bcr.bar_chart_race(df = df2, title = "COVID-19 Deaths by Country",n_bars=11, orientation='h', fixed_order= True, cmap = 'prism')