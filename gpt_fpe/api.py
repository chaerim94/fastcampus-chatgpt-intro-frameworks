import os
from typing import Dict

from chains import (
    default_chain,
    read_prompt_template
)
from database import query_db
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel

load_dotenv()


app = FastAPI()


class UserRequest(BaseModel):
    user_message: str


CUR_DIR = os.path.dirname(os.path.abspath(__file__))


@app.post("/qna")
def gernerate_answer(req: UserRequest) -> Dict[str, str]:
    context = req.dict()
    context["input"] = context["user_message"]

    answer = default_chain.run(context["user_message"])

    return {"answer": answer}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
