import numpy as np
import matplotlib.pyplot as plt

# data to plot
n_groups = 3

cross_score = (0.545, 0.6, 0.542)
test_score = (0.484, 0.447, 0.484)

# create plot
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.35
opacity = 0.8

rects1 = plt.bar(index, cross_score, bar_width,
alpha=opacity,
color='b',
label='Cross Validatioin Score')

rects2 = plt.bar(index + bar_width, test_score, bar_width,
alpha=opacity,
color='g',
label='Test Score')

plt.xlabel('Classifiers')
plt.ylabel('Scores')
plt.title('Points Score')
plt.xticks(index + bar_width, ('SVM', 'KNN', 'NN'))


plt.tight_layout()
plt.legend(loc=(1.04,0))
plt.show()
