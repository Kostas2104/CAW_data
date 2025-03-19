import psycopg2
from config import DATABASE_URL

def connect_db():
    return psycopg2.connect(DATABASE_URL, sslmode="require")

def save_data(market_data, caw_volume_usd_gateio):
    """Save CAW data to the database"""
    conn = connect_db()
    cur = conn.cursor()

    cur.execute("""
    INSERT INTO crypto_data (market_cap_caw, price_caw, price_cro, volume_24h_caw, caw_volume_gateio)
    VALUES (%s, %s, %s, %s, %s)
    """, (market_data["market_cap_caw"], market_data["price_caw"], market_data["price_cro"], 
          market_data["volume_24h_caw"], caw_volume_usd_gateio))

    conn.commit()
    cur.close()
    conn.close()
