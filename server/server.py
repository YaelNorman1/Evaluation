from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.responses import FileResponse 
import uvicorn


app = FastAPI()
app.mount("/client/static", StaticFiles(directory="client/static"), name="static")


@app.get("/")
def root():
    # async def read_index():
    return FileResponse('client/static/index.html')

if __name__ == "__main__":
    uvicorn.run("server:app", host="0.0.0.0", port=8050, reload=True)