from get_gateio_caw_volume_in_usd import get_gateio_caw_volume_in_usd
from get_prices import get_cmc_data
from database import create_tables, save_data

# Create database tables if they don't exist
create_tables()

# Fetch data
caw_volume_usd_gateio = get_gateio_caw_volume_in_usd()
market_data = get_cmc_data()

# Save to database
if market_data:
    save_data(market_data, caw_volume_usd_gateio)
    print("Data saved to database successfully!")
