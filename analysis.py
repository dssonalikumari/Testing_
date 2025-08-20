# analysis.py
import matplotlib.pyplot as plt

# Quarterly data
quarters = ["Q1", "Q2", "Q3", "Q4"]
ratios = [2.79, 3.64, 8.68, 6.28]
industry_target = 8
average = sum(ratios) / len(ratios)

print(f"Average Inventory Turnover Ratio (2024): {average:.2f}")
print(f"Industry Benchmark Target: {industry_target}")

# Plot
plt.figure(figsize=(8, 5))
plt.plot(quarters, ratios, marker="o", label="Company Performance", linewidth=2)
plt.axhline(y=industry_target, color="r", linestyle="--", label="Industry Target (8)")
plt.title("Inventory Turnover Ratio - 2024 Quarterly Trend")
plt.xlabel("Quarter")
plt.ylabel("Inventory Turnover Ratio")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("turnover_trend.png", dpi=300)
plt.show()
