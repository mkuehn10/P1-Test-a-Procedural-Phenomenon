
# coding: utf-8

# # Statistics: The Science of Decisions Project Instructions
# 
# ## Background Information
# 
# In a Stroop task, participants are presented with a list of words, with each word displayed in a color of ink. The participant’s task is to say out loud the color of the ink in which the word is printed. The task has two conditions: a congruent words condition, and an incongruent words condition. In the congruent words condition, the words being displayed are color words whose names match the colors in which they are printed: for example RED, BLUE. In the incongruent words condition, the words displayed are color words whose names do not match the colors in which they are printed: for example PURPLE, ORANGE. In each case, we measure the time it takes to name the ink colors in equally-sized lists. Each participant will go through and record a time from each condition.

# ### Questions for Investigation
# #### 1. What is our independent variable?  What is our dependent variable?
# The independent variable is whether or not one is exposed to the congruent words condition or the incongruent words condition.  The dependent variable is the time it takes to name the ink colors in equally-sized lists.

# #### 2. What is an appropriate set of hypotheses for this task? What kind of statistical test do you expect to perform? Justify your choices.
# Let $ \mu_{C} $ = the population mean time it takes to name the ink colors under the congruent words condition.   
# Let $ μ_I $ = the population mean time it takes to name the ink colors under the incongruent words condition.
# 
# $ H_{0}:  \mu_C = \mu_I $    
# $ H_A: \mu_C \ne \mu_I $   
# 
# The null hypothesis is that there is no difference between the two conditions.  The alternative hypothesis is that there is a difference between the two conditions.  The test is to see if there is a difference.  I selected a two-tailed test because there is no assumption of whether or not it will take less time or more time.
# 
# The statistical test that will be performed is a paired sample t-test.  This test will be used to compare the differences between the performance of participants on the congruent and incongruent conditions.  In order to do this, the differences will be calculated and treated as a sample.
# 
# A t-test is applicable because the sample size of 24 is smaller than 30.  The actual population standard deviations for the mean times for each of the populations are unknown which rules out the use of any type of z-test.  Based on the analysis of the histograms and summary statistics in question 3, it is a fair assumption that both populations are approximately normally distributed based on the shapes of the histograms and the fact that the sample means and medians are very close.
# 
# 

# As a general note, be sure to keep a record of any resources that you use or refer to in the creation of your project. You will need to report your sources as part of the project submission.
# Now it’s your chance to try out the Stroop task for yourself. Go to this [link](https://www.google.com/url?q=https://faculty.washington.edu/chudler/java/ready.html&sa=D&ust=1455910929447000&usg=AFQjCNETT8fHY1_z3LQybK7dHsqRZZtlNA), which has a Java-based applet for performing the Stroop task. Record the times that you received on the task (you do not need to submit your times to the site.) Now, download [this dataset](https://www.google.com/url?q=https://drive.google.com/file/d/0B9Yf01UaIbUgQXpYb2NhZ29yX1U/view?usp%3Dsharing&sa=D&ust=1455910929448000&usg=AFQjCNGABagMd0cZJewduz7uu3xHyVkW4A) which contains results from a number of participants in the task. Each row of the dataset contains the performance for one participant, with the first number their results on the congruent task and the second number their performance on the incongruent task.
# 

# #### 3. Report some descriptive statistics regarding this dataset. Include at least one measure of central tendency and at least one measure of variability.

# In[70]:

import pandas as pd

dataFrame = pd.read_csv('stroopdata.csv')

print dataFrame
print

def descriptive_statistics(column):
    print column + " Summary Statistics"
    print "Mean:",dataFrame[column].mean()
    print "Median:",dataFrame[column].median()
    print "Variance:",dataFrame[column].var()
    print "Standard Deviation:",dataFrame[column].std()

descriptive_statistics('Congruent')
print
descriptive_statistics('Incongruent')


# #### 4. Provide one or two visualizations that show the distribution of the sample data. Write one or two sentences noting what you observe about the plot or plots.

# In[61]:

import matplotlib.pyplot as plt
get_ipython().magic(u'matplotlib inline')
plt.style.use('ggplot')
#dataFrame['Congruent'].plot(kind = 'hist', bins=6)
plt.hist(dataFrame['Congruent'], bins = [6,9,12,15,18,21,24])
plt.title("Histogram of Congruent")
plt.xlabel("Time in seconds")
plt.ylabel("Frequency")
plt.axis([6, 24, 0, 10])
plt.show()

plt.hist(dataFrame['Incongruent'], bins = [15,18,21,24,27,30,33,36])
plt.title("Histogram of Incongruent")
plt.xlabel("Time in seconds")
plt.ylabel("Frequency")
plt.axis([15, 36, 0, 8])
plt.show()


# **Congruent**: The shape of the congruent histogram is approximately normal or mound-shaped.  The center appears to be somewhere between 12 and 15.  The range of the histogram goes from 6 to 24.
# 
# **Incongruent**: The shape of the incongruent histogram is skewed somewhat to the right due to the data points within the 33-36 range.  These observations may or may not be outliers (further analysis would be needed to determine this).  The center appears to be somewhere in the range of 18 to 24.  The range of the histogram goes from 15 to 36.

# #### 5. Now, perform the statistical test and report your results. What is your confidence level and your critical statistic value? Do you reject the null hypothesis or fail to reject it? Come to a conclusion in terms of the experiment task. Did the results match up with your expectations?

# In[69]:

import scipy.stats

print "Lower t-critical value:",scipy.stats.t.ppf(0.025, 23)
print "Upper t-critical value:",scipy.stats.t.ppf(0.975, 23)
print
print "t-statistic:",scipy.stats.ttest_rel(dataFrame['Congruent'],dataFrame['Incongruent']).statistic
print "two-tailed p-value",scipy.stats.ttest_rel(dataFrame['Congruent'],dataFrame['Incongruent']).pvalue


# Using the scipy.stats.t.ppf function to find the t-critical value for a 95% confidence level yields t-critcal values of -2.0687 and 2.0687.  The scipy.stats.ttest_rel function shows the results of running the statistical test.  The t-statistics of -8.0207 is well below the t-critical value of -2.0687 which means that it falls within the rejection region.  With a p-value so small of 0.00000004103, we reject the null hypothesis that the mean of the congruent condition times and the mean of the incongruent condition times are equal.  There is strong evidence to support that there is a difference between the two means.  I expected there to be a significant difference since it took me so much longer to identify the colors during the incongruent condition.

# #### 6. Optional: What do you think is responsible for the effects observed? Can you think of an alternative or similar task that would result in a similar effect? Some research about the problem will be helpful for thinking about these two questions!
# I believe that the incongruent task takes so much longer because the brain needs to process and reconcile two conflicting pieces of information.  In the congruent task, the color matches the word, so there is no conflict between the two signals that the brain is processing.  In the incongruent task, there is a conflict between the two signals, so one of the verbal perception needs to be suppressed in order to identify the correct color.
# 
# An interesting variation of this task could present words representing feelings (e.g. happiness, sadness, fear, etc.) along with a visual picture of someone exhibiting this characteristic.  People would be asked to interpret what they believe the facial expression to be.  The incongruent condition of this task could pair a happy facial expression with the word sad.  People would still need to identify what they think the facial expression is.
# 

# In[ ]:



