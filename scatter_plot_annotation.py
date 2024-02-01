import matplotlib.pyplot as plt
import numpy as np

# Load the data from the tables
# You can use pandas or any other method to read the data
# For simplicity, I will use some dummy data here
products = ["Milk", "Bread", "Butter", "Jam", "Eggs", "Flour", "Cheese", "Champagne", "Whipped Cream", "Berries"]
support = np.array([0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0.05, 0.02])
lift = np.array([1.0, 1.2, 1.5, 1.8, 2.0, 2.5, 3.0, 4.0, 5.0, 6.0])

# Create the scatter plot
plt.scatter(support, lift)

# Label the points with the product names
for i, product in enumerate(products):
    plt.annotate(product, (support[i], lift[i]))

# Add the axis labels and title
plt.xlabel("Support")
plt.ylabel("Lift")
plt.title("Support vs Lift for Different Products")