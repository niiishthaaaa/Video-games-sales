
# 🎮 Video Game Sales Analysis & Visualization

This project explores and visualizes video game sales data using Python. It includes detailed cleaning, visualizations, and statistical testing to understand trends across genres, consoles, critic scores, and more.

---

## 📁 Dataset

The dataset includes various attributes such as:

- `name`: Title of the game  
- `genre`: Game genre (e.g., Action, Sports, RPG)  
- `console`: Console/platform released on (e.g., PS4, Xbox)  
- `release_date`: Date of release  
- `total_sales`: Total global sales  
- `critic_score`: Aggregate critic review score  
- `user_score`: (if available) User review score  

The original CSV file can be found here:  
`vg sales.csv`

---

## 📊 Key Features

### ✅ Data Cleaning
- Parsed and cleaned release dates
- Filled missing values
- Removed incomplete rows for meaningful analysis

### 📈 Visualizations

1. **Total Sales by Genre** – Horizontal bar chart  
2. **Top Consoles by Game Count**  
3. **Boxplot of Sales for Top Consoles**  
4. **Critic Score vs Total Sales** – Scatter plot  
5. **Release Year vs Sales Trend** – Line plot  
6. **Correlation Heatmap**  
7. **Critic Score Distribution by Genre** – Violin (optional)  
8. **Game Release Count by Year** – Count plot  
9. **Histogram of Total Sales**  
10. **Pie Chart of Top Console Sales**  
11. **Line Plot: Average Critic Score per Year**  
12. **Line Plot: Game Count per Year**  
13. **Line Plot: Total Sales by Genre over Time**  
14. **Heatmap: Avg Critic Score by Genre and Console**

---

## 📊 Statistical Analysis

- **T-Test**: Compare total sales between `Action` and `Sports` games  
- **Z-Test**: Same comparison using Z-test  
- **Chi-Square Test**: Relationship between `Genre` and `Console`


## 📌 Project Purpose

This project was built for academic and personal learning purposes, aiming to:

- Practice data analysis and visualization techniques
- Explore patterns in game sales and review scores
- Apply real-world statistical tests on meaningful data

---

## 📬 License

This project is open-source under the MIT License. Feel free to fork and modify.
