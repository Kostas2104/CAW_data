import os

# Railway automatically injects DATABASE_URL
DATABASE_URL = os.getenv("postgresql://postgres:HHbFxDnoMzxQNDQWUHnaqoNvDnvnpUze@postgres.railway.internal:5432/railway")

# API Keys
API_KEY_CRONOSCAN = "3TSECYS4FZFNCWEUK5HCFTP9W5WMSX5NUY"
API_KEY_CMC = "a8fd7838-7f35-4f17-8e5a-c8af39ef18ba"

# Contract Address for CAW
CAW_CONTRACT_ADDRESS = "0xcCcCcCcCdbEC186DC426F8B5628AF94737dF0E60"

# Wallet Addresses for CAW
CAW_ADDRESSES = [
    "0x25aA97464F38a1506a16160bbc03cfC6DD863da3",
    "0x069E536d2429172e402A8c0DDCE822FC60a3677f",
    "0x8995909DC0960FC9c75B6031D683124a4016825b",
    "0x000000000000000000000000000000000000dead",
]

# Database URL (set this in Railway environment variables)
DATABASE_URL = "your_postgresql_database_url"
