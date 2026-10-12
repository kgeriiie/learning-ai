from fastapi import FastAPI
from pyarrow.lib import duration
from pydantic import BaseModel, Field
from document_mcp.process_document import async_answer_it, answer_it
import logging
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Question(BaseModel):
    question: str = Field(min_length=1, max_length=100)

class AnswerResult(BaseModel):
    question: str = Field(min_length=1, max_length=100)
    answer: str = Field(min_length=1)
    success: bool = Field(default=False)
    attempts: int = Field(default=0)

app = FastAPI()

@app.get("/hello")
def hello():
    return {"message": "szia uram kőő kóla?"}

@app.post("/ask", response_model=AnswerResult)
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

    return AnswerResult(question=payload.question, answer=result.answer, success=result.success, attempts=result.attempts)

@app.post("/ask-async", response_model=AnswerResult)
async def ask(payload: Question):
    logger.info(f"process question: {payload.question}")
    start_time = time.time()
    result = await async_answer_it(payload.question)

    result_success_str = "unsuccessfully"
    if result.success:
        result_success_str = "successfully"

    end_time = time.time()

    logger.info(
        f"question was answered: {result_success_str}. (attempts: {result.attempts}) ({(end_time - start_time):.2f} seconds)")

    return AnswerResult(question=payload.question, answer=result.answer, success=result.success, attempts=result.attempts)