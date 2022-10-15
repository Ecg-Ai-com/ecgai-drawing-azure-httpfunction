import json

import azure.functions as func
import fastapi
import nest_asyncio
from ecgai_drawing.create_ecg_plot import CreateEcgPlot
from ecgai_drawing.enums.artifact import Artifact
from ecgai_drawing.enums.color_style import ColorStyle
from ecgai_drawing.models.ecg_leads import Leads

from create_ecg_image import create_ecg_plot_response
from create_ecg_image.create_ecg_plot_request import CreateEcgPlotRequest

# pydevd_pycharm.settrace("localhost", port=12345, stdoutToServer=True, stderrToServer=True)
from create_ecg_image.mapper import to_create_ecg_plot_response

# import sys
#
# sys.path.append("path/to/pydevd-pycharm.egg")
# import pydevd_pycharm
#
# pydevd_pycharm.settrace('localhost', port=12345, stdoutToServer=True, stderrToServer=True)

app = fastapi.FastAPI()

nest_asyncio.apply()


@app.get("/create_ecg_image")
async def create_ecg_image(request: CreateEcgPlotRequest) -> create_ecg_plot_response:
    try:
        leads = Leads.create(record_name=request.record_name, sample_rate=request.sample_rate, leads=request.ecg_leads)
        plot = CreateEcgPlot(
            transaction_id=request.transaction_id,
            record_name=request.record_name,
            sample_rate=request.sample_rate,
            ecg_leads=leads,
            color_style=ColorStyle(request.color_style),
            show_grid=request.show_grid,
            artifact=Artifact(request.artifact),
            file_name=request.file_name,
        )
        image = plot.handle()
        response = to_create_ecg_plot_response(image)
        return func.HttpResponse(json.dumps(response.to_json()))
    except Exception as e:
        print(e)


@app.get("/sample")
async def index():
    return {
        "info": "Try /hello/Shivani for parameterized route.",
    }


@app.get("/hello/{name}")
async def get_name(name: str):
    return {
        "name": name,
    }


async def main(req: func.HttpRequest, context: func.Context) -> func.HttpResponse:
    """Each request is redirected to the ASGI handler."""
    return func.AsgiMiddleware(app).handle(req, context)
