from fastapi import FastAPI

from core.config import settings
from api import router as api_router


app = FastAPI()
app.include_router(
    api_router,
    prefix=settings.api.prefix
)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app="main:app", reload=True)
