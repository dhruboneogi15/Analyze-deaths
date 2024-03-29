import pandas as pd
import seaborn as sns
import numpy as np
import plotly.express as px

washington_post_data = pd.read_csv("police-data.csv")

print(washington_post_data.shape)
washington_post_data.head()

print(washington_post_data.isna().values.any())
washington_post_data.duplicated().values.any()

data = washington_post_data

print(data.shape)
data.head()

#converting date column to datetime index
data["date"] = pd.DatetimeIndex(data["date"]).year
data.rename(columns = {'date':'year'}, inplace = True)

data.info()

#q1:death rate on years by race
race_death_rate = data.groupby(["year","race"],as_index=False).agg({"name":pd.Series.count})
race_death_rate.rename({"name":"deaths_count"},axis=1,inplace=True)
race_death_rate.head()

r_bar = px.bar(race_death_rate,
               x="year",
               y="deaths_count",
               color="race",
               title="deaths people over the years by race")
r_bar.update_layout(xaxis_title="year",
                    yaxis_title="deaths count")
r_bar.show()

#q2:death rate on years by gender
gender_death_rate = data.groupby(["year","gender"],as_index=False).agg({"name":pd.Series.count})
gender_death_rate.rename({"name":"deaths_count"},axis=1,inplace=True)
gender_death_rate.head()

g_bar = px.bar(gender_death_rate,
               x="year",
               y="deaths_count",
               color="gender",
               title="deaths people over the years by gender",
               barmode="group")
g_bar.update_layout(xaxis_title="year",
                    yaxis_title="deaths count")
g_bar.show()

#q3:death rate on years by age
age_death_rate = data.groupby(["year","age"],as_index=False).agg({"name":pd.Series.count})
age_death_rate.rename({"name":"deaths_count"},axis=1,inplace=True)
age_death_rate.head()

a_bar = px.bar(age_death_rate,
               x="year",
               y="deaths_count",
               color="age",
               title="deaths people over the years by age")
a_bar.update_layout(xaxis_title="year",
                    yaxis_title="deaths count")
a_bar.show()

#q4:death rate on years by city and state
state_city_deaths = data.groupby(["state","city"],as_index=False).agg({"name":pd.Series.count})
state_city_deaths.rename({"name":"deaths_count"},axis=1,inplace=True)
state_city_deaths.head()

a_sun = px.sunburst(state_city_deaths,
               names="city",
               parents="state",
               values="deaths_count",
               title="deaths people over the years by city and state")
a_sun.show()

#q5:how many people who killed was armed?
is_armed = data.value_counts("armed")
is_armed.head()

a_pie = px.pie(names=is_armed.index,
               values=is_armed.values,
               title="was people who killed armed?")
a_pie.show()

#q6:how many people who killed had signs_of_mental_illness?
is_mentally_ill = data.value_counts("signs_of_mental_illness")
is_mentally_ill.head()

i_pie = px.pie(names=is_mentally_ill.index,
               values=is_mentally_ill.values,
               color=is_mentally_ill.values,
               title="was people who killed had signs_of_mental_illness?")
i_pie.show()

#q7:how many people who killed had body_camera?
has_body_camera = data.value_counts("body_camera")
has_body_camera.head()

c_pie = px.pie(names=has_body_camera.index,
               values=has_body_camera.values,
               color=has_body_camera.values,
               title="was people who killed had has_body_camera?"
               ,hole=.3)
c_pie.show()

#q8:which police_departments_killed most of the people in the us :top 20?
police_departments_killed = data.groupby("police_departments_involved",as_index=False).agg({"name":pd.Series.count})
police_departments_killed.rename({"name":"deaths_count"},axis=1,inplace=True)
police_departments_killed.sort_values("deaths_count",ascending=False,inplace=True)

top_20_police_departments_killers = police_departments_killed[:20]
top_20_police_departments_killers.head()

d_bar = px.bar(top_20_police_departments_killers,
               x="police_departments_involved",
               y="deaths_count",
               color="deaths_count",
               title="deaths people over the years by responsive police department top 20")
d_bar.update_layout(xaxis_title="year",
                    yaxis_title="deaths count")
d_bar.show()