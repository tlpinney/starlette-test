import logfire
from starlette.applications import Starlette
from starlette.responses import PlainTextResponse
from starlette.requests import Request
from starlette.routing import Route

logfire.configure()


async def home(request: Request) -> PlainTextResponse:
    return PlainTextResponse("Hello, world!")


app = Starlette(routes=[Route("/", home)])
logfire.instrument_starlette(app)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app)
