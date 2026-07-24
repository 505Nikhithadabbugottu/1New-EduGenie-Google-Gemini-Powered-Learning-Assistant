from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import google.generativeai as genai

# Replace with your Gemini API Key
genai.configure(api_key="AQ.Ab8RN6JE-CfvNbKE_prcVUtf6qWXSYHAwFE1dNva6aTzYtQY0w")

app = FastAPI()

templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )


@app.get("/ask")
async def ask(question: str):

    model = genai.GenerativeModel("gemini-2.0-flash")

    response = model.generate_content(question)

    return {
        "question": question,
        "answer": response.text
    }