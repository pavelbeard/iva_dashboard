from fastapi import FastAPI, Request

app = FastAPI()


@app.post("/api/disk")
async def info(request: Request):
    print(await request.json())
    return {'good': 'work', 'disk': 'info'}


@app.post("/api/ram")
async def info(request: Request):
    print(await request.json())
    return {'good': 'work', 'ram': 'info'}


@app.post("/api/cpu")
async def info(request: Request):
    print(await request.json())
    return {'good': 'work', 'cpu': 'info'}


@app.get("/api/settings")
async def settings():
    return {"interval": "10"}
