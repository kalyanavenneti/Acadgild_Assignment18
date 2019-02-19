
# coding: utf-8

# In[1]:


# importing the libraries
import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import math


# In[3]:


# Question 1: Is gender independent of education level? A random sample of 395 people were surveyed and each person was asked to 
# report the highest education level they obtained. The data that resulted from the survey is summarized in the following table:

# High School Bachelors Masters Ph.d. Total Female 60 54 46 41 201 Male 40 44 53 57 194 Total 100 98 99 98 395

# Question: Are gender and education level dependent at 5% level of significance? In other words, given the data collected above, 
# is there a relationship between the gender of an individual and the level of education that they have obtained?

# Creating DataFrame from the data in the question
lst_qual = ['High School','Bachelors','Masters','PHD']     
lst_f = [60,54,46,41]                                         
lst_m = [40,44,53,57]                                      
df=pd.DataFrame({'Qualification':lst_qual,'Count_F': lst_f ,'Count_M': lst_m})
df


# In[5]:


# Adding  columns for Mean, Standard Deviation, Z Score and P Values for Female(F) and Male (M) in DataFrame

df['Mean_F']=df['Count_F'].mean()
df['Mean_M']=df['Count_M'].mean()

df['Std_Dev_F']=df['Count_F'].std()
df['Std_Dev_M']=df['Count_M'].std()

df['Z_F']=stats.zscore(df['Count_F'])
df['Z_M']=stats.zscore(df['Count_M'])

df['p_F']=[stats.norm.cdf(pval) for pval in stats.zscore(df['Count_F'])]
df['p_M']=[stats.norm.cdf(pval) for pval in stats.zscore(df['Count_M'])]
df


# In[34]:


print('From the above observations using the above dataframe pvalue of Male and Female is more than 5% (significance level), there is a relationship between the gender of an individual and the level of education that they have obtained.\n')
print('Female populations are High in number when compared to Male in qualification at Highschool & Bachelors degree levels\n')
print('Male populations are High in number when compared to Female in qualification at Masters & Phd degree levels\n')


# In[23]:


# Question 2: Using the following data, perform a oneway analysis of variance using α=.05. Write up the results in APA format. 
#[Group1: 51, 45, 33, 45, 67] 
#[Group2: 23, 43, 23, 43, 45]
#[Group3: 56, 76, 74, 87, 56] 
 
# Creating DataFrame from the data in the question
lst_grp1 = [51, 45, 33, 45, 67]   # Group1
lst_grp2 = [23, 43, 23, 43, 45]   # Group2
lst_grp3 = [56, 76, 74, 87, 56]   # Group3

df=pd.DataFrame({'Grp1':lst_grp1,'Grp2': lst_grp2 ,'Grp3': lst_grp3})
df


# In[24]:


p_Val=stats.f_oneway(df['Grp1'],df['Grp2'],df['Grp3']).pvalue
F_Val=stats.f_oneway(df['Grp1'],df['Grp2'],df['Grp3']).statistic

α = 0.05   # Significance level

print('Null Hypothesis: \t Group1=Group2=Group3')

print('\nHypothesis testing with 5% significance')

print('\n p Value is greater than α , so Null Hypothesis(Group1=Group2=Group3) can be Accepted. ')

print('\n the results in APA format is as below:')

print('\t Significance level:\t', round(α,4))
print('\t F Value:\t\t', round(F_Val,4))
print('\t p Value:\t\t', round(p_Val,4), ' <', round(α,4) , '(Significance level)' )
print('\t So, Accept Null Hypothesis: \t Group1=Group2=Group3' )


# In[26]:


# Question 3: Calculate F Test for given 10, 20, 30, 40, 50 and 5,10,15, 20, 25. For 10, 20, 30, 40, 50:

# Creating DataFrame from the data in the question
lst_grp1 = [10,20,30,40,50]
lst_grp2 = [5,10,15, 20, 25]

df=pd.DataFrame({'Grp1':lst_grp1,'Grp2': lst_grp2})
df


# In[30]:


# Adding  columns in the Dataframe for Mean, Standard Deviation and Variance

df['Mean_Grp1']=df['Grp1'].mean()
df['Mean_Grp2']=df['Grp2'].mean()

df['Std_Dev_Grp1']=df['Grp1'].std()
df['Std_Dev_Grp2']=df['Grp2'].std()

df['Var_Grp1']=df['Grp1'].var()
df['Var_Grp2']=df['Grp2'].var()
df


# In[32]:


# Calculate the P Values
# Hypothesis Test
print('Null Hypothesis Group1 = Group2') 

α =0.05  # significance level, confidence level 95%
print('\nSignificance level:\t', round(α,4))

# F test
# F-Test Formula:\t (Varience of Group 1)/(Varience of Group 2)
F_Val=df['Grp1'].var()/df['Grp2'].var()
print('F Test Results:\t\t',F_Val)

p_Val = stats.f.cdf(F_Val, len(df['Grp1'])-1,len(df['Grp1'])-1)

print('p Values :\t\t',p_Val)

print('\nHere:\t p Value:\t', round(p_Val,4), ' >', round(α,4) , '(Significance level)' )
print('\t Therefore will be rejecting  Null Hypothesis')

