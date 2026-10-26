import matplotlib.pylab as plt
import numpy as np
# Sample data
x = np.linspace(0, 10, 10)
y = np.sin(x)
y2 = np.cos(x)
values = [5, 7, 3, 4, 6]
# Line Plot
plt.figure(figsize=(10, 6))
plt.subplot(2, 3, 1)
plt.plot(x, y, label="sin(x)", marker="o")
plt.plot(x, y2, label="cos(x)", marker="s")
plt.title("Line Plot")
plt.legend()
# Bar Chart
plt.subplot(2, 3, 2)
plt.bar(range(len(values)), values, color="skyblue")
plt.title("Bar Chart")
# Pie Chart
plt.subplot(2, 3, 3)
sizes = [20, 30, 25, 15, 10]
labels = ["A", "B", "C", "D", "E"]
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
plt.title("Pie Chart")
# Histogram
plt.subplot(2, 3, 4)
data = np.random.randn(1000) # 1000 random numbers
plt.hist(data, bins=20, color="lightgreen", edgecolor="black")
plt.title("Histogram")
# Scatter Plot
plt.subplot(2, 3, 5)
x_scatter = np.random.rand(50)
y_scatter = np.random.rand(50)
plt.scatter(x_scatter, y_scatter, color="red", marker="x")
plt.title("Scatter Plot")
plt.tight_layout()
plt.show()