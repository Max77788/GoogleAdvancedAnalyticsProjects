#!/usr/bin/env python
# coding: utf-8

# # **Course 3 Automatidata project**
# **Course 3 - Go Beyond the Numbers: Translate Data into Insights**

# You are the newest data professional in a fictional data analytics firm: Automatidata. The team is still early into the project, having only just completed an initial plan of action and some early Python coding work. 
# 
# Luana Rodriquez, the senior data analyst at Automatidata, is pleased with the work you have already completed and requests your assistance with some EDA and data visualization work for the New York City Taxi and Limousine Commission project (New York City TLC) to get a general understanding of what taxi ridership looks like. The management team is asking for a Python notebook showing data structuring and cleaning, as well as any matplotlib/seaborn visualizations plotted to help understand the data. At the very least, include a box plot of the ride durations and some time series plots, like a breakdown by quarter or month. 
# 
# Additionally, the management team has recently asked all EDA to include Tableau visualizations. For this taxi data, create a Tableau dashboard showing a New York City map of taxi/limo trips by month. Make sure it is easy to understand to someone who isn’t data savvy, and remember that the assistant director at the New York City TLC is a person with visual impairments.

# # Course 3 End-of-course project: Exploratory data analysis
# 
# In this activity, you will examine data provided and prepare it for analysis.  
# <br/>   
# 
# **The purpose** of this project is to conduct exploratory data analysis on a provided data set.
#   
# **The goal** is to clean data set and create a visualization.
# <br/>  
# *This activity has 4 parts:*
# 
# **Part 1:** Imports, links, and loading
# 
# **Part 2:** Data Exploration
# *   Data cleaning
# 
# 
# **Part 3:** Building visualizations
# 
# **Part 4:** Evaluate and share results
# 
# <br/> 
# Follow the instructions and answer the questions below to complete the activity. Then, you will complete an Executive Summary using the questions listed on the PACE Strategy Document.
# 
# Be sure to complete this activity before moving on. The next course item will provide you with a completed exemplar to compare to your own work. 
# 
# 

# Recall that you have a helpful tool at your disposal! Refer to the [PACE strategy document ](https://docs.google.com/document/d/1iSHdbfQR6w8RClJNWai8oJXn9tQmYoTKn6QohuaK4-s/template/preview?resourcekey=0-ZIHnbxL1dd2u9A47iEVXvg) to help apply your learnings, apply new problem-solving skills, and guide your approach to this project.
# 
# 

# # **Visualize a story in Tableau and Python**

# In this activity, you will design a professional data visualization that tells a story, and will help someone make a data-driven decision for their business needs. Please note that this activity is optional, and will not affect your completion of the course.
# 
# Completing this activity will help you practice planning out and plotting a data visualization based on a specific business need. The structure of this activity is designed to emulate the proposals you will likely be assigned in your career as a data professional. Completing this activity will help prepare you for those career moments. 
# 
# 
# Follow the instructions and answer the question below to complete the activity. Then, you will complete an executive summary using the questions listed on the PACE Strategy Document.
# 
# Be sure to complete this activity before moving on. The next course item will provide you with a completed exemplar to compare to your own work. 
# 

# # **PACE stages** 
# 
# 
# <img src="images/Pace.png" width="100" height="100" align=left>
# 
#    *        [Plan](#scrollTo=psz51YkZVwtN&line=3&uniqifier=1)
#    *        [Analyze](#scrollTo=mA7Mz_SnI8km&line=4&uniqifier=1)
#    *        [Construct](#scrollTo=Lca9c8XON8lc&line=2&uniqifier=1)
#    *        [Execute](#scrollTo=401PgchTPr4E&line=2&uniqifier=1)

# <img src="images/Plan.png" width="100" height="100" align=left>
# 
# 
# ## PACE: Plan 
# 
# In this stage, consider the following questions where applicable to complete your code response:
# 1. Identify any outliers: 
# 
# 
# *   What methods are best for identifying outliers?
# *   How do you make the decision to keep or exclude outliers from any future models?
# 
# 

# ==> ENTER YOUR RESPONSE HERE

# ### Task 1. Imports, links, and loading
# Go to Tableau Public
# The following link will help you complete this activity. Keep Tableau Public open as you proceed to the next steps. 
# 
# Link to supporting materials: 
# Tableau Public: https://public.tableau.com/s/ 
# 
# For EDA of the data, import the data and packages that would be most helpful, such as pandas, numpy and matplotlib. 
# 
# As shown in this cell, the dataset has been automatically loaded in for you. You do not need to download the .csv file, or provide more code, in order to access the dataset and proceed with this lab. Please continue with this activity by completing the following instructions.
# 

# In[1]:


#==> ENTER YOUR CODE HERE
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns


# In[2]:


# RUN THIS CELL TO IMPORT YOUR DATA.
df = pd.read_csv('2017_Yellow_Taxi_Trip_Data.csv')


# <img src="images/Analyze.png" width="100" height="100" align=left>
# 
# ## PACE: Analyze 
# 
# Consider the questions in your PACE Strategy Document to reflect on the Analyze stage.

# ### Task 2a. Data exploration and cleaning
# 
# Decide which columns are applicable
# 
# The first step is to assess your data. Check the Data Source page on Tableau Public to get a sense of the size, shape and makeup of the data set. Then answer these questions to yourself: 
# 
# Given our scenario, which data columns are most applicable? 
# Which data columns can I eliminate, knowing they won’t solve our problem scenario? 
# 
# Consider functions that help you understand and structure the data. 
# 
# *    head()
# *    describe()
# *    info()
# *    groupby()
# *    sortby()
# 
# What do you do about missing data (if any)? 
# 
# Are there data outliers? What are they and how might you handle them? 
# 
# 
# 

# ==> ENTER YOUR RESPONSE HERE
# I investigate the nature of missing values. Then I ask the responsible for it person to provide missing data or tell me how must it be interpreted otherwise. Then using some data validation's available methods, such as inserting mean or mode(if categorical variable) of the column, are utilized to deal with null values.
# 
# Regarding outliers, if the data's spread is wide then I would assure the dataset's values' integrity by addressing its owner. In other case, I would remove the outliers in order not to skew and introduce bias into the consequent analysis or machine learning model. 

# Start by discovering, using head and size. 

# In[3]:


#==> ENTER YOUR CODE HERE
df.head()


# In[4]:


#==> ENTER YOUR CODE HERE
df.shape


# In[5]:


df.size


# Use describe... 

# In[6]:


#==> ENTER YOUR CODE HERE
df.describe(include='all')


# And info. 

# In[7]:


#==> ENTER YOUR CODE HERE
df.info()


# In[8]:


# Giving Trip's ID column a proper name
df.rename(columns = {"Unnamed: 0":"Trip_ID"}, inplace = True)


# Perform a check for outliers on relevant columns sucah as trip distance and trip duration. Remember, one of the best ways to look for outliers is a box plot visualization. 
# 
# **Note:** Remember to convert your date columns to datetime in order to derive total trip duration.  

# In[9]:


#==> ENTER YOUR CODE HERE

# Convert to datetime data type
df["tpep_pickup_datetime"] = pd.to_datetime(df["tpep_pickup_datetime"])
df["tpep_dropoff_datetime"] = pd.to_datetime(df["tpep_dropoff_datetime"])


# In[10]:


# Calculating each trip's duration
df["trip_duration_mins"] = (df["tpep_dropoff_datetime"] - df["tpep_pickup_datetime"]).astype('timedelta64[m]')


# In[11]:


# Function for boxplot creation and displaying the fraction of outliers
# in the whole population
def box_plot_plus_ouliers_frac(data, col, fig_width=8, fig_height=12):
    """Requires Pandas, Numpy, Seaborn and Matplotlib being preinstalled
    Returns box plot of indicated pandas Series and percentage of outliers
    in the column"""
    twenty_fifth_percentile = data[col].quantile(0.25)

    seventy_fifth_percentile = data[col].quantile(0.75)

    iqr = seventy_fifth_percentile - twenty_fifth_percentile

    lower_threshold = twenty_fifth_percentile - (1.5*iqr)

    upper_threshold = seventy_fifth_percentile + (1.5*iqr)

    condition_for_outliers = (data[col] > upper_threshold) | (data[col] < lower_threshold) 

    outliers = data[condition_for_outliers]
    
    # Box plot for values
    fig = sns.boxplot(data=data, y=col)

    # Change figure's size
    sns.set(rc={'figure.figsize':(fig_width, fig_height)})
    plt.show()
    
    outliers_frac = (len(outliers)/len(df))*100
    print("The fraction of outliers in the {} column of the provided dataset is {:.2f}%)".format(col, outliers_frac))
    
    return outliers 


# In[12]:


#df.to_csv(r'CleanedForTableauData.csv')


# ### Task 2b. Assess whether dimensions and measures are correct

# 
# 
# In Tableau, staying on the data source page, double check the data types for the applicable columns you selected on the previous step. Pay particular attention to the dimensions and measures to assure they are correct. 
# 

# Review the instructions at [this link](https://docs.google.com/document/d/1pcfUlttD2Y_a9A4VrKPzikZWCAfFLsBAhuKuomjcUjA/template/preview) to create the required Tableau visualization. 

# ### Task 2c. Select visualization type(s)

# Select data visualization types that will help you understand and explain the data.
# 
# Now that you know which data columns you’ll use, it is time to decide which data visualization makes the most sense for EDA of the TLC dataset. What type of data visualization(s) would be most helpful? 
# 
# * Line graph
# * Bar chart
# * Box plot
# * Histogram
# * Heat map
# * Scatter plot
# * A geographic map
# 

# ==> ENTER YOUR RESPONSE HERE
# Line graphs are going to be the most useful as they are the most suitable to show the trends over time. Also, scatterplot sounds about right to show the correlation between two continuous variables 

# <img src="images/Construct.png" width="100" height="100" align=left>
# 
# ## PACE: Construct 
# 
# Consider the questions in your PACE Strategy Document to reflect on the Construct stage.

# ### Task 3. Building visualizations
# 
# You’ve assessed your data, and decided on which data variables are most applicable. It’s time to plot your visualization(s)!
# 

# #### Boxplots

# In[17]:


# Boxplot for trip duration column
outliers_duration = box_plot_plus_ouliers_frac(df, "trip_duration_mins")


# In[14]:


# Boxplot trip distance column
outliers_distance = box_plot_plus_ouliers_frac(df, "trip_distance")


# #### Scatter plot

# #### *Remove those trips with costs associated, but with a trip distance = to "0."*

# ![DistanceVsPriceViz.png](attachment:DistanceVsPriceViz.png)

# In[15]:


# Heatmap for correlations*
correllation_price = df.corr()
sns.heatmap(data=correllation_price["total_amount"].to_frame(), annot=True, cmap='Paired')


# *_'Paired' color map was chosen in order to make the visualiztion accessible for color-blinded individuals_

# ### Lineplot of prices over time and by each month

# In[18]:


df['Month_Year'] = pd.PeriodIndex(df['tpep_pickup_datetime'], freq="M")

df['Month_Year_time'] = df['Month_Year'].dt.to_timestamp()

df_by_time = df.sort_values('Month_Year')

df_by_time_s = df.groupby('Month_Year', as_index=False)['total_amount'].mean()


# In[116]:


g = sns.lineplot(x="Month_Year_time", y="total_amount", data=df_by_time)
#g.xaxis_date(df['Month_Year_time'].unique())
#g.xaxis_date()
g.set_ylim(0, 20)
g.set_xlabel("Month")
g.set_ylabel("Price($)")
sns.set(rc={'figure.figsize':(16,12)})
plt.title("Taxi Trips Price Trend Over 2017", fontsize=20)
plt.show()


# ---------------------------------------------

# In[117]:


# Barplot of the same statistics
g = sns.barplot(x="Month_Year", y="total_amount", data=df_by_time_s)
#g.xaxis_date(df['Month_Year'])
#g.xaxis_date()
#g.set(title = "Taxi Trips Prices in Each Month of 2017")
g.set_xlabel("Month")
g.set_ylabel("Price($)")
plt.title("Taxi Trips Mean Price in Each Month of 2017", fontsize=20)
#sns.set(font_scale=1)
sns.set(rc={'figure.figsize':(16,12)})
plt.show()


# You can do a scatterplot in Tableau Public as well, which can be easier to manipulate and present. If you'd like step by step instructions, you can review the following link: 

# [Tableau visualization guidelines](https://docs.google.com/document/d/1pcfUlttD2Y_a9A4VrKPzikZWCAfFLsBAhuKuomjcUjA/template/preview)

# <img src="images/Execute.png" width="100" height="100" align=left>
# 
# ## PACE: Execute 
# 
# Consider the questions in your PACE Strategy Document to reflect on the Execute stage.

# ### Task 4a. Results and evaluation
# 
# Having built visualizations in Tableau and in Python, what have you learned about the dataset? What other questions have your visualizations uncovered that you should pursue? 
# 
# ***Pro tip:*** Put yourself in your client's perspective, what would they want to know? 
# 
# Use the following code fields to pursue any additional EDA based on the visualizations you've laready plotted. Also use the space to make sure your visualizations are clean, easily understandable, and accessible. 
# 
# ***Ask yourself:*** Did you consider color, contrast, emphasis, and labeling?
# 
# 

# ==> ENTER YOUR RESPONSE HERE
# 
# I have learned how to approach analysis in logical organized manner, so it is controlled and steered correctly
# 
# My other questions are what are other attributes which could add extra insights in forming of trip's price 
# 
# My client would likely want to know the actionable steps he must undertake in order to increase profitability of his business. For example, how to reduce unnecessary charges, so people use TLC's services more frequently.
# 

# ### Task 4b. Conclusion
# *Make it professional and presentable*
# 
# You have visualized the data you need to share with the director now. Remember, the goal of a data visualization is for an audience member to glean the information on the chart in mere seconds.
# 
# *Questions to ask yourself for reflection:*
# Why is it important to conduct Exploratory Data Analysis? Why would we need to create a visual map of the NYC Taxi rides? Why would this be useful?
# 

# ==> ENTER YOUR RESPONSE HERE
# 
# EDA is important because it allows to get a wide perspective on data, reveal its issues and, more importantly, features to inspect in order to get closer to the reaching project's initial goal.
# 
# 
# Visualizations helped me understand the spread of trip duration and distance values, correlation between these variables and the overall affect of attributes on total price
# 
# 

# You’ve now completed a professional data visualization according to a business need. Well done! Be sure to save your work as a reference for later work in Tableau. 
