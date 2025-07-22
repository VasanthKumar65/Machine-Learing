#A3
import statistics
import matplotlib.pyplot as plt

# --- Hardcoded sample from IRCTC Stock Data ---
data = [
    {"date": "Jun 29, 2021", "month": "Jun", "day": "Tue", "price": 2081.85, "chg": 0.20},
    {"date": "Jun 28, 2021", "month": "Jun", "day": "Mon", "price": 2077.75, "chg": 0.43},
    {"date": "Jun 25, 2021", "month": "Jun", "day": "Fri", "price": 2068.85, "chg": -0.20},
    {"date": "Jun 24, 2021", "month": "Jun", "day": "Thu", "price": 2072.95, "chg": -0.26},
    {"date": "Jun 23, 2021", "month": "Jun", "day": "Wed", "price": 2078.25, "chg": -0.23},
    {"date": "Jun 22, 2021", "month": "Jun", "day": "Tue", "price": 2083.00, "chg": 0.30},
    {"date": "Jun 21, 2021", "month": "Jun", "day": "Mon", "price": 2076.85, "chg": 3.24},
    {"date": "Jun 18, 2021", "month": "Jun", "day": "Fri", "price": 2011.70, "chg": -1.89},
    {"date": "Jun 17, 2021", "month": "Jun", "day": "Thu", "price": 2050.40, "chg": -1.89},
    {"date": "Jun 16, 2021", "month": "Jun", "day": "Wed", "price": 2089.95, "chg": -0.38},
    {"date": "Apr 30, 2021", "month": "Apr", "day": "Fri", "price": 1785.35, "chg": -0.21},
    {"date": "Apr 29, 2021", "month": "Apr", "day": "Thu", "price": 1793.50, "chg": 0.25},
    {"date": "Apr 28, 2021", "month": "Apr", "day": "Wed", "price": 1775.40, "chg": -0.46},
    {"date": "Apr 27, 2021", "month": "Apr", "day": "Tue", "price": 1758.80, "chg": 0.32},
    {"date": "Apr 26, 2021", "month": "Apr", "day": "Mon", "price": 1741.30, "chg": -0.51},
    {"date": "May 03, 2021", "month": "May", "day": "Mon", "price": 1805.75, "chg": 1.08},
    {"date": "May 04, 2021", "month": "May", "day": "Tue", "price": 1821.20, "chg": 0.86}

]
prices = [entry["price"] for entry in data]
chg_percents = [entry["chg"] for entry in data]
days = [entry["day"] for entry in data]

# 1. Mean and Variance of Price
mean_price = statistics.mean(prices)
variance_price = statistics.variance(prices)

print(f"Mean Price               : ₹{mean_price:.2f}")
print(f"Variance of Price        : {variance_price:.2f}")

# 2. Mean Price on Wednesdays
wed_prices = [entry["price"] for entry in data if entry["day"] == "Wed"]
mean_wed = statistics.mean(wed_prices)
print(f"\nMean Price on Wednesdays : ₹{mean_wed:.2f}")
print("Observation              :", "Higher" if mean_wed > mean_price else "Lower or Similar")

# 3. Mean Price in April
apr_prices = [entry["price"] for entry in data if entry["month"] == "Apr"]
if apr_prices:
    mean_apr = statistics.mean(apr_prices)
    print(f"\nMean Price in April      : ₹{mean_apr:.2f}")
    print("Observation              :", "Higher" if mean_apr > mean_price else "Lower or Similar")
else:
    print("\nMean Price in April      : No April data available.")

# 4. Probability of Loss (chg < 0)
loss_days = [chg for chg in chg_percents if chg < 0]
prob_loss = len(loss_days) / len(data)
print(f"\nProbability of Loss       : {prob_loss:.2%}")

# 5. Profit on Wednesday
wed_chg = [entry["chg"] for entry in data if entry["day"] == "Wed"]
wed_profit_days = [chg for chg in wed_chg if chg > 0]
prob_profit_wed = len(wed_profit_days) / len(wed_chg)
print(f"Profit on Wednesday       : {prob_profit_wed:.2%}")

# 6. Conditional P(Profit | Wednesday)
# Same as above in this case
print(f"Conditional P(Profit|Wed) : {prob_profit_wed:.2%}")

#7. Scatter Plot: Chg% vs Day of Week
plt.figure(figsize=(8, 5))
plt.scatter(days, chg_percents, color='blue', alpha=0.7)
plt.title("Chg% vs Day of the Week")
plt.xlabel("Day")
plt.ylabel("Chg%")
plt.grid(True)
plt.tight_layout()
plt.show()