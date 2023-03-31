from fastapi import FastAPI
from create_job import crete_job
app = FastAPI()


@app.get("/job")
def create_job():
    crete_job()
    return {'MESSAGE': 'Job Submitted'}
