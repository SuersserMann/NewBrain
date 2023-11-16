import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import csv

##Exercise 1
##reading CSV data into dictionary
data = {"population": [], "density": [], "hours": []}
with open("corr.csv", 'r') as infile:
    csvreader = csv.reader(infile, delimiter=',')
    for row in csvreader:
        data["population"].append(float(row[0]))
        data["density"].append(float(row[1]))
        data["hours"].append(float(row[2]))

print(stats.pearsonr(data["population"], data["density"]))
# this is high because it's total number of hours, so more people = more hours worked!
# usually we would work with hours per capita = the average number of hours each person works.
print(stats.pearsonr(data["population"], data["hours"]))
print(stats.pearsonr(data["hours"], data["density"]))

##Exercise 2
# Your computer will crash

##Exercise 3
X = [29.8, 30.1, 30.5,
     30.6, 31.3, 31.7, 32.6,
     33.1, 32.7, 32.8]
Y = [327, 456, 509,
     497, 596, 573, 661,
     741, 809, 717]

r = stats.pearsonr(X, Y)[0]
plt.scatter(X, Y, label="r = {:.3f}".format(r))
plt.legend()
# plt.show()
plt.close()

##Exercise 4
# These are time series data over fairly short periods (approximately 10 years, so approximately
# 10 data points) and a huge number of data sets are checked. It is not unlikely to find
# 10 or so data points following roughly the same trend if you check thousands of pairs!

##Exercise 5
data = {"popdensity": [], "elderlydensity": []}
with open("old.csv", 'r') as infile:
    csvreader = csv.reader(infile, delimiter=',')
    for row in csvreader:
        data["popdensity"].append(float(row[0]))
        data["elderlydensity"].append(float(row[1]))

r = stats.pearsonr(data["popdensity"], data["elderlydensity"])[0]
plt.scatter(data["popdensity"], data["elderlydensity"], label="r = {:.3f}".format(r))
plt.legend()
plt.xlabel("Population Density")
plt.ylabel("Elderly Population Density")
plt.savefig("CensusPopOld.png")
plt.close()
# The correlation is high, but the plot doesn't look linear!

# Exercise 6
sr = stats.spearmanr(data["popdensity"], data["elderlydensity"])
print(sr)
# the spearman correlation measures monotone relationships and is very high

# Exercise 7
for i, (k, v) in enumerate(data.items()):
    plt.boxplot(np.log(v), vert=False, labels=["{}".format(k)], positions=[i])
plt.xlabel(r"log($\rho$)")
plt.tight_layout()
plt.savefig("box.png")
plt.close()

##Exercise 8
r = stats.pearsonr(np.log(data["popdensity"]), np.log(data["elderlydensity"]))[0]
plt.scatter(data["popdensity"], data["elderlydensity"], label="r = {:.3f}".format(r))
plt.legend()
plt.xlabel("Population Density")
plt.ylabel("Elderly Population Density")
plt.yscale('log')
plt.xscale('log')
plt.savefig("LogCensusPopOld.png")
plt.close()
# Now the plot is much more linear!

##Exercise 9
# y = A x**b
# log(y) = log( A x**b )
# log(y) = log(A) + log(x**b)
# log(y) = log(A) = b log(x)

##Exercise 10
r = stats.pearsonr(np.log(data["popdensity"]), np.log(data["elderlydensity"]))[0]
plt.scatter(data["popdensity"], data["elderlydensity"], label="r = {:.3f}".format(r))
xv = np.linspace(min(data["popdensity"]), max(data["popdensity"]), 100)
plt.plot(xv, xv ** 0.87 * np.exp(-1.528), color='r', lw=2, ls="--", label=r"$y \propto x^{0.87}$")
plt.legend()
plt.xlabel("Population Density")
plt.ylabel("Elderly Population Density")
plt.yscale('log')
plt.xscale('log')
plt.savefig("LogCensusPopOldFit.png")
plt.close()

##Exercise 11
# y -> 2**0.87 y
# higher population density corresponds to lower density of elderly

##Exercise 12
##I'm going to write out math in python notation!
##This is not valid python code, though you could make it so if you wanted to
# m, c are constants
# x is a numpy array
"""
#definition of variables related to x
N = len(x) == len(y)
xbar = sum(x)/N
sigmax = sum( (x - xbar)**2 )/(N-1)

#definition of y
y = m*x + c

#average of y
ybar = sum(m*x + c)/N = m*xbar + c

#standard deviation of y
sigmay = sum( (y - ybar)**2 ) / (N-1)
== sum( (m*x + c - m*xbar - c)**2 ) / (N-1)
== m*sum( (x-xbar)**2 ) / (N-1)
== m*sigmax

#definition of correlation coefficient
r = (1/(N-1))*sum(   (x - xbar)*(y - ybar)/(sigmax*sigmay)  )
#substitute
r = (1/(N-1))*sum(   (x - xbar)*( m*x + c - m*xbar - c)/(sigmax*sigmay)  )
== (1/(N-1))*sum(  m(x - xbar)**2/(sigmax*m*sigmax)    )
== (1/(N-1))*sum(  (x - xbar)**2 )/(sigmax**2)    
##using the definition of sigmax
== (sigmax**2)/(sigmax**2)
== 1
"""
##If y is a linear function of x, they it is perfectly correlated with x
##We will discuss linear functions in a later lecture