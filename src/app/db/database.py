from pymongo import MongoClient

DB_CLIENT= MongoClient("mongodb+srv://filessend109:mongodb@cluster0.bf4zl3m.mongodb.net")
NAME_OF_DB= "fastapi-db"
DB= DB_CLIENT[NAME_OF_DB]



