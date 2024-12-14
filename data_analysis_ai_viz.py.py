# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error


# Set visualization style
sns.set_style("whitegrid")


# Create a sample data for analysis
data = {
    "Square Footage": [1200, 1500, 1800, 2000, 2200, 2500, 2700, 3000, 3200, 3500],
    "Price": [200000, 240000, 300000, 320000, 350000, 400000, 420000, 460000, 480000, 500000],
    "Bedrooms": [2, 3, 3, 4, 4, 5, 5, 4, 5, 6],
    "Age": [10, 5, 20, 15, 8, 2, 5, 10, 3, 1],
}

# Convert the dictionary to a pandas DataFrame
df = pd.DataFrame(data)

# Display the first few rows of the DataFrame
print("Dataset Overview:\n", df)

# ================================================================
# Data Analysis
# ================================================================

# Descriptive statistics
print("\nDescriptive Statistics:\n", df.describe())

# Check for correlations
correlation_matrix = df.corr()
print("\nCorrelation Matrix:\n", correlation_matrix)

# Visualize the correlation matrix
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

# ================================================================
# Data Visualization
# ================================================================

# Scatter Plot - Relationship between Square Footage & Price
plt.figure(figsize=(8, 6))
sns.scatterplot(x="Square Footage", y="Price", data=df, s=100)
plt.title("Square Footage vs Price")
plt.xlabel("Square Footage")
plt.ylabel("Price")
plt.show()

# Pair Plot for feature relationships
sns.pairplot(df, hue="Bedrooms", palette="husl")
plt.show()

# Regression plot (Seaborn's regression plotting)
plt.figure(figsize=(8, 6))
sns.regplot(x="Square Footage", y="Price", data=df)
plt.title("Regression: Square Footage vs Price")
plt.xlabel("Square Footage")
plt.ylabel("Price")
plt.show()

# ================================================================
# Machine Learning with Linear Regression
# ================================================================

# Prepare data for ML
X = df[["Square Footage", "Bedrooms", "Age"]]  # Features
y = df["Price"]  # Target variable

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model's performance
mse = mean_squared_error(y_test, y_pred)
print("\nMean Squared Error on Test Data:", mse)

# Visualize actual vs predicted
plt.figure(figsize=(8, 6))
sns.scatterplot(x=y_test, y=y_pred)
plt.xlabel("Actual Prices")
plt.ylabel("Predicted Prices")
plt.title("Actual vs Predicted Prices")
plt.show()

# Coefficients of the model
print("\nModel Coefficients:", model.coef_)
print("Model Intercept:", model.intercept_)
