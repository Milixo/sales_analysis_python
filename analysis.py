import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Učitavanje CSV datoteke
df = pd.read_csv('sales_data.csv')

# Prikaz prvih nekoliko redaka podataka
print(df.head())

# Osnovne informacije o datasetu
print(df.info())

# Rješavanje nedostajućih vrijednosti
df = df.dropna()  

# Pretvaranje kolone 'Date' u datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Pretvaranje cijena iz stringa u float
df['Price'] = df['Price'].str.replace('$', '').astype(float)

# Prikaz osnovnih statistika
print(df.describe())

# Ekstrakcija mjeseca iz datuma
df['Month'] = df['Date'].dt.to_period('M')  # Dodaje kolonu s mjesecom

# Grupiranje prodaje po mjesecu
monthly_sales = df.groupby('Month')['Sales'].sum().reset_index()

# Provjera sadržaja i tipova podataka u monthly_sales
print(monthly_sales.head())
print(monthly_sales.dtypes)

# Provjera nenumeričkih vrijednosti u koloni 'Sales'
print("Nenumeričke vrijednosti u 'Sales':")
print(monthly_sales[~monthly_sales['Sales'].apply(lambda x: isinstance(x, (int, float)))])

# Ako je potrebno, konverzija kolone 'Month' u string format
monthly_sales['Month'] = monthly_sales['Month'].astype(str)

# Ako je potrebno, konverzija kolone 'Sales' u numerički format
monthly_sales['Sales'] = pd.to_numeric(monthly_sales['Sales'], errors='coerce')

# Ponovno prikazivanje informacija nakon čišćenja
print(monthly_sales.head())
print(monthly_sales.dtypes)

# Vizualizacija distribucije cijena
plt.figure(figsize=(10, 6))
sns.histplot(df['Price'], kde=True, bins=20)
plt.title('Distribution of Prices')
plt.xlabel('Price')
plt.ylabel('Frequency')
plt.show()

# Vizualizacija prodaje po mjesecu
plt.figure(figsize=(10, 6))
sns.lineplot(x='Month', y='Sales', data=monthly_sales, marker='o')
plt.title('Average Sales by Month')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.show()
