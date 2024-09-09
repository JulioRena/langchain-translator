from main import chain
from fastapi import FastAPI
from langserve import add_routes


app = FastAPI(title="IA Translator", description="Translate any text you want")

add_routes(app, chain, path="/translater")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
    


