# Define a dictionary with assets and their corresponding values
# Change asset value to USD value of each asset to calculate percentages of each asset in portfolio
assets = {
    'BTC': 1,
    'ETH': 1,
    'QNT': 1,
    'XRP': 1,
    'XLM': 1,
    'HBAR': 1
}

# Calculate the total sum
total = sum(assets.values())

# Calculate and print the proportion of each asset
for asset, value in assets.items():
    percentage = (value / total) * 100
    print(f'{asset}: {percentage:.2f}%')
