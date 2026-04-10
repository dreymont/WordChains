from fastapi import FastAPI, HTTPException
from src.main import find_chain, load_dictionary
app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/wordchains/{start}/{end}")
def get_chain(start: str, end: str):
    if len(start) != len(end):
        raise HTTPException(status_code=400, detail="Words must be the same length")

    dictionary = load_dictionary('src/ScrabbleWords.txt', len(start))

    if start not in dictionary:
        raise HTTPException(status_code=404, detail=f"Word '{start}' not found in dictionary")

    if end not in dictionary:
        raise HTTPException(status_code=404, detail=f"Word '{end}' not found in dictionary")

    result = find_chain(start, end, dictionary)

    return {"chain": result}

