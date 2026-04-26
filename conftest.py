import sys
from pathlib import Path
import pytest
import time
import threading
import uvicorn
from src.api import app

sys.path.insert(0, str(Path(__file__).parent))

@pytest.fixture(scope="session")
def server():
    thread = threading.Thread(
        target=uvicorn.run,
        args= (app,),
        kwargs={"port": 8000},
        daemon= True,
    )
    thread.start()
    time.sleep(1)