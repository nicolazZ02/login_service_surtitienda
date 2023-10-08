from fastapi import Request
from fastapi.responses import JSONResponse
from app.common import UtilsHelper, settings
from uuid import uuid4

async def correlation_id_middleware(request: Request, call_next):
    correlation_id = UtilsHelper.create_correlation_id()
    request.state.correlation_id = correlation_id
    response = await call_next(request)
    response.headers[settings.CORRELATION_ID_HEADER] = correlation_id
    return response