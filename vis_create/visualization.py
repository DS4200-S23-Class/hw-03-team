import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib.colors import ListedColormap

# set size of font + make graph look nice
sns.set(font_scale=1)

# read file into dataframe
college_df = pd.read_csv('vis_create/top_colleges_2022.csv')

# calculate number of students receiving financial aid
college_df['receivingAid'] = college_df['undergradPop'] * college_df['percentOfStudentsFinAid'] / 100
college_df['aidPerStudent'] = college_df['totalGrantAid'] / college_df['receivingAid']

# isolate necessary columns
individual_aid = college_df['aidPerStudent'].to_numpy()
median_salary = college_df['medianBaseSalary'].to_numpy()
rank = college_df['rank'].to_numpy()

# plot data w/ sequential colormap
plt.figure(figsize=(15, 8))
plt.scatter(individual_aid, median_salary, c=rank, cmap='autumn')

# add data/labels and a color bar
plt.xlabel('Avg Amount of Financial Aid per Undergrad Student')
plt.ylabel('Median Base Salary for Faculty')
plt.title('Top 500 Universities: Student Financial Aid vs. Base Salary & Ranking')

# add colorbar for rankings
colorbar = plt.colorbar(label='School Ranking', orientation='horizontal')
colorbar.ax.invert_yaxis()

plt.show()