from urllib.parse import quote

from typing import Any, Mapping, Optional

from fastapi.responses import Response
from starlette.background import BackgroundTask
from app.schemas import ContentDisposition


def _content_disposition(content_disposition_type: ContentDisposition, filename: str):
    content_disposition_filename = quote(filename)

    if content_disposition_filename != filename:
        content_disposition = "{}; filename*=utf-8''{}".format(
            content_disposition_type.value, content_disposition_filename
        )
    else:
        content_disposition = '{}; filename="{}"'.format(
            content_disposition_type.value, filename
        )
    
    return content_disposition


class PDFResponse(Response):
    def __init__(
        self,
        content: Any = None,
        filename: Optional[str] = "document.pdf",
        content_disposition_type: ContentDisposition = ContentDisposition.attachment,
        status_code: int = 200,
        headers: Mapping[str, str] | None = None,
        background: BackgroundTask | None = None
    ) -> None:
        if not filename.endswith(".pdf"):
            filename += ".pdf"

        super().__init__(content, status_code, headers, media_type="application/pdf", background=background)
        self.headers.setdefault("Content-Diposition", _content_disposition(content_disposition_type, filename))


class HTMLResponse(Response):
    def __init__(self, content: Any = None, status_code: int = 200, headers: Mapping[str, str] | None = None, media_type: str | None = None, background: BackgroundTask | None = None) -> None:
        super().__init__(content, status_code, headers, "text/html", background)
