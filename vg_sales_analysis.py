
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
import statsmodels.api as sm

# Load dataset
df = pd.read_csv(r"C:\Users\nisht\Downloads\vg sales.csv")
print(df.head())
# Clean the data
df_clean = df.dropna(subset=["total_sales", "critic_score", "genre", "console"]).copy()
df_clean["release_date"] = pd.to_datetime(df_clean["release_date"], errors='coerce', dayfirst=True)
df_clean["release_year"] = df_clean["release_date"].dt.year
print(df_clean.head())
print(df_clean.info())

#filling missing values with N/A
df_filled = df.fillna('N/A')
print(df_filled.head())

#Basic Visualizations
# 1. Total Sales by Genre
genre_sales = df_clean.groupby("genre")["total_sales"].sum().reset_index().sort_values(by="total_sales", ascending=False)
sns.barplot(data=genre_sales, x="total_sales", y="genre", color="skyblue")
plt.title("Total Sales by Genre")
plt.tight_layout()
plt.show()

# 2. Top 10 Consoles by Game Count
console_counts = df_clean["console"].value_counts().reset_index()
console_counts.columns = ["console", "count"]
console_counts = console_counts.head(10)

sns.barplot(data=console_counts, x="count", y="console", color="salmon")
plt.title("Top 10 Consoles by Game Count")
plt.tight_layout()
plt.show()

# 3. Sales Distribution of Top Consoles
top5_consoles = console_counts["console"].head(5)
sns.boxplot(data=df_clean[df_clean["console"].isin(top5_consoles)], x="console", y="total_sales")
plt.title("Sales Distribution of Top 5 Consoles")
plt.tight_layout()
plt.show()

# Scatter Plots 
# 4. Critic Score vs Total Sales
sns.scatterplot(data=df_clean, x="critic_score", y="total_sales", alpha=0.6)
plt.title("Critic Score vs Total Sales")
plt.tight_layout()
plt.show()

# 5. Release Year vs Total Sales
sns.scatterplot(data=df_clean, x="release_year", y="total_sales", alpha=0.5)
plt.title("Release Year vs Total Sales")
plt.tight_layout()
plt.show()

# 6. Critic Score vs User Score (if exists)
if "user_score" in df_clean.columns:
    df_clean = df_clean.dropna(subset=["user_score"])
    sns.scatterplot(data=df_clean, x="critic_score", y="user_score", alpha=0.6)
    plt.title("Critic Score vs User Score")
    plt.tight_layout()
    plt.show()

#New Visualizations

# 7. Correlation Heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(df_clean[["total_sales", "critic_score"]].corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()

# 8. Line Plot: Yearly Sales Trend
yearly_sales = df_clean.groupby("release_year")["total_sales"].sum().reset_index()
sns.lineplot(data=yearly_sales, x="release_year", y="total_sales", marker="o")
plt.title("Total Sales by Year")
plt.tight_layout()
plt.show()

# 9. Histogram: Distribution of Total Sales
sns.histplot(df_clean["total_sales"], bins=30, kde=True)
plt.title("Distribution of Total Sales")
plt.tight_layout()
plt.show()

# 10. Pie Chart: Top 5 Consoles by Sales Share
console_sales = df_clean[df_clean["console"].isin(top5_consoles)].groupby("console")["total_sales"].sum()
console_sales.plot.pie(autopct="%1.1f%%", startangle=140)
plt.title("Market Share of Top 5 Consoles")
plt.ylabel("")
plt.tight_layout()
plt.show()

# 12. Countplot: Number of Games Released per Year
plt.figure(figsize=(12, 6))
sns.countplot(data=df_clean, x="release_year", order=sorted(df_clean["release_year"].dropna().unique()))
plt.title("Number of Games Released per Year")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Barplot: Average Critic Score by Genre 
avg_critic = df_clean.groupby("genre")["critic_score"].mean().reset_index().sort_values(by="critic_score", ascending=False)
plt.figure(figsize=(12, 6))
sns.barplot(data=avg_critic, x="critic_score", y="genre", hue="genre", palette="viridis", legend=False)
plt.title("Average Critic Score by Genre")
plt.tight_layout()
plt.show()

# Statistical Tests

# T-test: Action vs Sports
action_sales = df_clean[df_clean["genre"] == "Action"]["total_sales"]
sports_sales = df_clean[df_clean["genre"] == "Sports"]["total_sales"]
t_stat, p_val = stats.ttest_ind(action_sales, sports_sales, equal_var=False, nan_policy='omit')
print(f"\nT-test (Action vs Sports): t-stat = {t_stat:.4f}, p-value = {p_val:.4f}")

# Chi-squared test: Genre vs Console
genre_console_crosstab = pd.crosstab(df_clean["genre"], df_clean["console"])
chi2, p, dof, expected = stats.chi2_contingency(genre_console_crosstab)
print(f"\nChi-squared test (Genre vs Console): chi2 = {chi2:.2f}, p = {p:.4f}")

# Z-test
from statsmodels.stats.weightstats import ztest
action_sales = df_clean[df_clean["genre"] == "Action"]["total_sales"]
sports_sales = df_clean[df_clean["genre"] == "Sports"]["total_sales"]

# Perform Z-test
z_stat, p_val = ztest(action_sales, sports_sales, value=0, alternative='two-sided')

print(f"\nZ-test (Action vs Sports): z-stat = {z_stat:.4f}, p-value = {p_val:.4f}")
