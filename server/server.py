from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.responses import FileResponse 
import uvicorn
from routes import ingredient_route


app = FastAPI()
app.include_router(ingredient_route.router)

app.mount("/client/static", StaticFiles(directory="client/static"), name="static")


@app.get("/")
def root():
    return FileResponse('client/static/index.html')

@app.get("/sanity")
def initilaize():
    return "OK"

if __name__ == "__main__":
    uvicorn.run("server:app", host="0.0.0.0", port=8000, reload=True)