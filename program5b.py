import numpy as np

array_1d = np.array([1, 2, 3, 4, 5])
print("1D Array:", array_1d)

array_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("2D Array:\n", array_2d)

print("Array shape:", array_2d.shape)
print("Sum of all elements:", np.sum(array_2d))
print("Mean of the array:", np.mean(array_2d))
print("Transposed Array:\n", np.transpose(array_2d))

print("First row of 2D array:", array_2d[0])
print("Element at row 1, column 2:", array_2d[1, 2])
print("Slicing:\n", array_2d[:, 1:])
import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)
print("DataFrame:\n", df)

print("DataFrame shape:", df.shape)
print("Summary Statistics:\n", df.describe())
print("DataFrame Info:")
print(df.info())

df['Salary'] = [50000, 60000, 70000]
print("Updated DataFrame:\n", df)

print("Selecting 'Age' column:\n", df['Age'])
print("Selecting first row:\n", df.iloc[0])
print("Filtering by Age > 28:\n", df[df['Age'] > 28])
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.figure(figsize=(10, 5))
plt.plot(x, y, label='sin(x)', color='blue')
plt.title('Line Plot of sin(x)')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.grid(True)
plt.savefig('lineplot.png')
plt.close()
print("Line plot saved as lineplot.png")

categories = ['A', 'B', 'C']
values = [10, 20, 15]
plt.figure(figsize=(8, 5))
plt.bar(categories, values, color=['red', 'green', 'blue'])
plt.title('Bar Plot Example')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.savefig('barplot.png')
plt.close()
print("Bar plot saved as barplot.png")

x = np.random.rand(50)
y = np.random.rand(50)
plt.figure(figsize=(8, 5))
plt.scatter(x, y, color='purple')
plt.title('Scatter Plot Example')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.savefig('scatterplot.png')
plt.close()
print("Scatter plot saved as scatterplot.png")

data = np.random.randn(1000)
plt.figure(figsize=(8, 5))
plt.hist(data, bins=30, color='orange', edgecolor='black')
plt.title('Histogram Example')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.savefig('histogram.png')
plt.close()
print("Histogram saved as histogram.png")