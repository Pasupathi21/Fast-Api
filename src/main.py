from fastapi import FastAPI
# from routers.main import router
from app.main import router 

app = FastAPI(root_path="/api")


app.include_router(router)

if __name__ == '__main__':
    app.run(app, host="0.0.0.0", port=4444)