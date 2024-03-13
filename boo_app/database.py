import asyncio

import motor.motor_asyncio

from boo_app.config import DB_HOST, DB_PORT, DB_NAME

MONGO_DETAILS = f"mongodb://{DB_HOST}:{DB_PORT}"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)
client.get_io_loop = asyncio.get_running_loop

database = client[DB_NAME]

profile_collection = database.get_collection("profiles")
account_collection = database.get_collection("accounts")
comment_collection = database.get_collection("comments")
like_collection = database.get_collection("likes")
vote_collection = database.get_collection("votes")
vote_option_collection = database.get_collection("vote_options")
vote_option_category_collection = database.get_collection("vote_option_categories")
