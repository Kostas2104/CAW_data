import psycopg2
from psycopg2.extras import DictCursor
from config import DATABASE_URL

def connect_db():
    return psycopg2.connect(DATABASE_URL, cursor_factory=DictCursor)

def create_tables():
    """Create database table for CAW data"""
    conn = connect_db()
    cur = conn.cursor()
    
    cur.execute("""
    CREATE TABLE IF NOT EXISTS crypto_data (
        id SERIAL PRIMARY KEY,
        timestamp TIMESTAMP DEFAULT NOW(),
        market_cap_caw NUMERIC,
        price_caw NUMERIC,
        price_cro NUMERIC,
        volume_24h_caw NUMERIC,
        caw_volume_gateio NUMERIC
    )
    """)
    
    conn.commit()
    cur.close()
    conn.close()

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
