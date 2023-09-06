from configs import AppConfig

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()


@app.post(AppConfig.API_URL_PREFIX)
async def api():
    return JSONResponse({'hello': 'api'})
