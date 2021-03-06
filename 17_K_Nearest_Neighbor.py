import pandas as pd
df = pd.read_csv('/Users/Admin/Documents/Python/machine_learning/people_wealth.csv')
df.head()

# Checked Data Balancing
df['Group'].value_counts()

import matplotlib.pyplot as plt
Xx = df['Income']
Xy = df['Age']
y = df['Group']
plt.scatter(Xx, Xy, c=y)
plt.show()

# Normalization
from sklearn.preprocessing import StandardScaler
x = df[['Income','Age']]
scaling = StandardScaler()
x = scaling.fit_transform(x)

# Create KNN model
from sklearn.neighbors import KNeighborsClassifier
model = KNeighborsClassifier(n_neighbors = 3)
model = model.fit(x, y)

from mlxtend.plotting import plot_decision_regions
plot_decision_regions(x,y.values,clf=model)
plt.show()

model.predict(scaling.transform([ [220000, 65 ] ]))
