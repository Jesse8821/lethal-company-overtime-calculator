scrap_sold = float(input("\nquotafulfilled: "))  # Gebruik float voor decimale getallen

profitquota = float(input("\nprofitquota: "))

daysuntildeadline = int(input("\ndays until deadline: "))  # Gebruik int voor gehele getallen

# Berekeningen uitvoeren
overtime = (scrap_sold - profitquota) / 5 + 15 * daysuntildeadline

# Print het resultaat
print("\novertime: ", overtime)
