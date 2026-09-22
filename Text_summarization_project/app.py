from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from transformers import T5ForConditionalGeneration, T5Tokenizer
import torch
import re

app = FastAPI(
    title="Text Summarizer App",
    description="Summarize text using HuggingFace T5 Model",
    version="1.0"
)
