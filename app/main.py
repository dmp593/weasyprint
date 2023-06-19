from pathlib import Path

from fastapi import FastAPI
from fastapi.requests import Request
from fastapi.responses import FileResponse

from weasyprint import HTML


from app.responses import PDFResponse
from app.schemas import ContentDisposition


app = FastAPI()


@app.get("/health", summary="Health Check Endpoint")
def health():
    return {"healthy": True}


@app.post("/pdf", summary="Generates a PDF from a text/html body")
async def pdf(
    request: Request,
    filename: str = "document.pdf",
    encoding: str = "utf-8",
    disposition: ContentDisposition = ContentDisposition.inline
) -> PDFResponse:
    data = await request.body()

    html = data.decode(encoding)
    pdf = HTML(string=html).write_pdf()

    return PDFResponse(pdf, filename=filename, content_disposition_type=disposition)


@app.get("/", summary="Home: Real-time PDF rendering")
def home():
    return FileResponse(Path("./app/templates/home.html"))
