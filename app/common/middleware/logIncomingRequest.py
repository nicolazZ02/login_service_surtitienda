import time
from typing import Callable, List
from fastapi import Request, Response
from fastapi.routing import APIRoute
from ..logs.logging import Logger
logger = Logger.get_logger(__name__)

# Middleware para generar registro de log
class LogRoutes(APIRoute):
    def get_route_handler(self) -> Callable:
        original_route_handler = super().get_route_handler()
        
        def get_request_handler(request: Request):
            # get controller from request
            routes: List[APIRoute] = request.app.routes
            for route in routes:
                if route.path_regex.match(request.url.path) and request.method in route.methods:
                    return route.endpoint.__name__ if hasattr(route.endpoint, '__name__') else 'fastapi_core'

        async def log_route_handler(request: Request) -> Response:
            func_name = get_request_handler(request)
            request.state.func_name = func_name
            route_name = request.url.path

            request_body = await request.body()
            
            logger.info('{} - {} - start - correlationId {} - Request: {}'.format(route_name, func_name, request.state.correlation_id, request_body.decode()))
            start_time = time.time()
            
            response: Response = await original_route_handler(request)

            process_time = (time.time() - start_time) * 1000
            formatted_process_time = '{0:.2f}'.format(process_time)
            
            response_body = response.body
            
            logger.info('{} - {} - end in time (ms): {} - correlationId {} - Response: {}'.format(route_name, func_name, formatted_process_time, request.state.correlation_id, response_body.decode()))
            
            return response

        return log_route_handler