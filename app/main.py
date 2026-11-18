import os
import socket
from fastapi import FastAPI

app = FastAPi()

@app.get("/")

def home():
  return{
         "message":os.getenv("APP_MESSAGE", "Hello from kubernetes"),
         "pod": socker.gethotsname()
      }
@app.get("/health")
  def health():
     return{"status":"ok"}
