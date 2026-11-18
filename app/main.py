import os
import socket
from fastapi import FastAPI

app = FastAPI()

@app.get("/")

def home():
  return{
         "message":os.getenv("APP_MESSAGE", "Hello from kubernetes"),
         "pod": socket.gethostname()
      }

@app.get("/health")
def health():
    return {"status": "ok"}
