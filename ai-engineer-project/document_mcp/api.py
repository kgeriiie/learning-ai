from fastapi import FastAPI
from pyarrow.lib import duration
from pydantic import BaseModel
from document_mcp.process_document import answer_it
import logging
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Question(BaseModel):
    question: str

app = FastAPI()

@app.get("/hello")
def hello():
    return {"message": "szia"}

@app.post("/ask")
def ask(payload: Question):
    logger.info(f"process question: {payload.question}")
    start_time = time.time()
    result = answer_it(payload.question)

    result_success_str = "unsuccessfully"
    if result.success:
        result_success_str = "successfully"

    end_time = time.time()

    logger.info(
        f"question was answered: {result_success_str}. (attempts: {result.attempts}) ({(end_time - start_time):.2f} seconds)")

    return {"question": payload.question, "answer": result.answer}