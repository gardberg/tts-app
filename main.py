import uvicorn

if __name__ == '__main__':
    uvicorn.run("server.api:app", reload=True)
