from fastapi import FastAPI

app=FastAPI()

@app.get("/ping")
def get_success():
    return {'message':'Success!'}