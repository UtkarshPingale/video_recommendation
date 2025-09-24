from fastapi import FastAPI, HTTPException
from app.fetcher import download_all_posts, list_downloaded_files, read_saved_file

app = FastAPI(title="Video Recommendation Data Downloader")

@app.get("/")
def root():
    return {"message": "FastAPI Video Data Downloader is running"}

@app.post("/data/download")
def download_data():
    try:
        files = download_all_posts()
        return {"message": "Data downloaded successfully", "files": files}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/data/files")
def get_files():
    files = list_downloaded_files()
    return {"files": files}

@app.get("/data/files/{filename}")
def read_file(filename: str):
    data = read_saved_file(filename)
    if "error" in data:
        raise HTTPException(status_code=404, detail=data["error"])
    return data
