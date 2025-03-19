from flask import Flask, jsonify
import psycopg2
from psycopg2.extras import DictCursor
from config import DATABASE_URL

app = Flask(__name__)

def connect_db():
    return psycopg2.connect(DATABASE_URL, cursor_factory=DictCursor)

@app.route("/data", methods=["GET"])
def get_data():
    """Fetch latest CAW data from the database"""
    conn = connect_db()
    cur = conn.cursor()

    cur.execute("SELECT * FROM crypto_data ORDER BY timestamp DESC LIMIT 10")  # Last 10 entries
    data = cur.fetchall()
    
    cur.close()
    conn.close()

    return jsonify([dict(row) for row in data])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
