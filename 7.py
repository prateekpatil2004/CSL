import numpy as np
import pandas as pd 
from scipy import stats


exam = np.array([85, 87, 88, 90, 93, 85, 84])
groupa = np.array([82, 86, 85, 87, 92, 80, 81])
groupb = np.array([85, 89, 88, 90, 93, 85, 84])  
before = np.array([82, 84, 85, 90, 79, 87, 83])
after = np.array([85, 87, 89, 81, 83, 88, 92])

# One-sample t-test
def onetest(data, pmean):
    t_stat, p_value = stats.ttest_1samp(data, pmean)
    return t_stat, p_value


def twotest(group1, group2):
    t_stat, p_value = stats.ttest_ind(group1, group2)
    return t_stat, p_value

# Paired sample t-test
def pair_test(before, after):
    t_stat, p_value = stats.ttest_rel(before, after)
    return t_stat, p_value

# Function to analyze the result of the t-test
def analyze(t_stat, p_value, alpha=0.05):
    print(f"T-statistic: {t_stat}")
    print(f"P-value: {p_value}")
    if p_value < alpha:
        print("Result: The null hypothesis is rejected (statistically significant difference).")
    else:
        print("Result: The null hypothesis cannot be rejected (no statistically significant difference).")

# One-sample t-test
print("One-sample t-test")
t_stat, p_value = onetest(exam, 85)
analyze(t_stat, p_value)
print()

# Two-sample t-test
print("Two-sample t-test")
t_stat, p_value = twotest(groupa, groupb)
analyze(t_stat, p_value)
print()

# Paired-sample t-test
print("Paired-sample t-test")
t_stat, p_value = pair_test(before, after)
analyze(t_stat, p_value)
print()
