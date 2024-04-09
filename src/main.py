# ================= core modules ================
from fastapi import FastAPI

# ================= middleware =============
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.middleware.cors import CORSMiddleware

# =============== Main routes ================
from app.main import AppRouter

# ============= app instance ================
app = FastAPI(root_path="/api")

# ============ apply middlewares ===============
# host restriction for security purpose
app.add_middleware(TrustedHostMiddleware, allowed_hosts=["*"])
# compress the response size and improve the performence
app.add_middleware(GZipMiddleware, minimum_size=1000)
app.add_middleware(
    CORSMiddleware, 
    allow_origins=["*"], 
    allow_headers=["*"], 
    allow_methods=[
        "GET",
        "POST",
        "PUT",
        "DELETE",
        "PATCH",
        "OPTIONS"
    ]
)

# ================ event call
# @app.on_event("startup")
# async def startup():
#     print("event started >>>>>>>>>>>>>")

# ============= all routes ===============================
app.include_router(AppRouter)

# @app.on_event("shutdown")
# async def shoudown():
#     print("shoutdown >>>>>>>>>>>")

if __name__ == '__main__':
    import uvicorn
    
    # bootstraping the main.py file initially
    uvicorn.run("main:app", host="0.0.0.0", port=4422, reload=True)