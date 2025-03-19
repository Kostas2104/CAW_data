from datetime import datetime
from get_gateio_caw_volume_in_usd import get_gateio_caw_volume_in_usd
from get_prices import get_cmc_data
from database import save_data

# Get the current timestamp
record_date = datetime.now()

# Fetch data
caw_volume_usd_gateio = get_gateio_caw_volume_in_usd()
market_data = get_cmc_data()

# Save to database with timestamp
if market_data:
    save_data(record_date, market_data, caw_volume_usd_gateio)
    print(f"Data saved to database successfully at {record_date}!")
