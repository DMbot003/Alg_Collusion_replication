import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

# Set working directory
current_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_path)

# Load data
NashPrice = 1.47293
CoopPrice = 1.92498
numPeriods = 15

# Read data with whitespace delimiter
try:
    data = pd.read_csv("A_irToBR.txt", sep="\s+", header=0)
    print("Data loaded successfully. Shape:", data.shape)
    print("Data columns:", data.columns[:5])
    print("Data index:", data.index[:5])
except FileNotFoundError:
    print("Error: 'A_irToBR.txt' not found in current directory.")
    raise
except Exception as e:
    print(f"Error loading data: {e}")
    raise

# Transpose the dataframe
data = data.T
print("Transposed data shape:", data.shape)
print("Transposed data index:", data.index[:5])

# Check if 'AggrPricePre' exists in the index
if 'AggrPricePre' not in data.index:
    print("Error: 'AggrPricePre' not found in data index.")
    raise KeyError("'AggrPricePre' not found")

# Create dataframe for plotting
p = pd.DataFrame({'time': range(numPeriods + 1)})
print("Initial p DataFrame:\n", p.head())

# Get indices for AggrDevPriceShockPer (excluding standard errors)
ll = [i for i in data.index if 'AggrDevPriceShockPer' in i and 'seAggrDevPriceShockPer' not in i]
ll = ll[:numPeriods]
print(f"AggrDevPriceShockPer indices (first {numPeriods}):", ll)

# Populate AvgPGDevAg
try:
    aggr_price_pre = data.loc['AggrPricePre', data.columns[0]]
    print("AggrPricePre value:", aggr_price_pre)
    p['AvgPGDevAg'] = [aggr_price_pre] + list(data.loc[ll, data.columns[0]])
    print("AvgPGDevAg:\n", p['AvgPGDevAg'].head())
except KeyError as e:
    print(f"KeyError: {e}")
    raise

# Get indices for AggrNonDevPriceShockPer (excluding standard errors)
ll = [i for i in data.index if 'AggrNonDevPriceShockPer' in i and 'seAggrNonDevPriceShockPer' not in i]
ll = ll[:numPeriods]
print(f"AggrNonDevPriceShockPer indices (first {numPeriods}):", ll)

# Populate AvgPGNonDevAg
try:
    p['AvgPGNonDevAg'] = [aggr_price_pre] + list(data.loc[ll, data.columns[0]])
    print("AvgPGNonDevAg:\n", p['AvgPGNonDevAg'].head())
except KeyError as e:
    print(f"KeyError: {e}")
    raise

# Create the plot
plt.figure(figsize=(6, 4))

# Plot Deviating Agent (Red line, red square markers)
plt.plot(p['time'], p['AvgPGDevAg'], 
         color='red', 
         marker='s',  # Square marker
         markersize=5,  # Adjust marker size
         linewidth=2, 
         label='Deviating agent')

# Plot Non-Deviating Agent (Blue line, green triangle markers)
plt.plot(p['time'], p['AvgPGNonDevAg'], 
         color='blue', 
         marker='^',  # Triangle marker (pointing up)
         markersize=5,  # Adjust marker size
         markeredgecolor='green',  # Green marker edge
         markerfacecolor='green',  # Green marker fill
         linestyle='-',  # Solid line (changed from dashed)
         linewidth=2, 
         label='Nondeviating agent')

# Add reference lines
# Nash Price (Dashed, dark gray)
plt.axhline(y=NashPrice, color='darkgray', linestyle='--', linewidth=1, label='Nash price')
# Monopoly Price (Dash-dot, red)
plt.axhline(y=CoopPrice, color='red', linestyle='-.', linewidth=1, label='Monopoly price')
# Long-run Price (Solid, green)
plt.axhline(y=aggr_price_pre, color='green', linestyle='-', linewidth=1, label='Long-run price')

# Customize axes
plt.xlabel('Time')
plt.ylabel('Price')
plt.xticks([0, 1, 5, 10, 15])
plt.ylim(min(min(p['AvgPGDevAg']), min(p['AvgPGNonDevAg']), NashPrice),
         max(max(p['AvgPGDevAg']), max(p['AvgPGNonDevAg']), CoopPrice))

# Add legend (position adjusted to match the image)
plt.legend(loc=(0.65, 0.35), frameon=True, fontsize=8)

# Add title below the plot
plt.figtext(0.5, -0.05, 'FIGURE 4', ha='center', fontsize=10)

# Adjust layout
plt.tight_layout()

# Save to PDF
plt.savefig('figure_4_py.pdf', format='pdf', bbox_inches='tight')
plt.close()

print("Plot saved successfully as 'figure_4.pdf'")