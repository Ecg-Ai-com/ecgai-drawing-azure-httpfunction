import base64

from ecgai_drawing.ecg_plot_image import EcgPlotImage

from create_ecg_image.create_ecg_plot_response import CreateEcgPlotResponse


def to_create_ecg_plot_response(ecg_plot_image: EcgPlotImage) -> CreateEcgPlotResponse:
    return CreateEcgPlotResponse.create(
        transaction_id=ecg_plot_image.transaction_id,
        record_name=ecg_plot_image.record_name,
        file_name=ecg_plot_image.file_name,
        file_extension=ecg_plot_image.file_extension,
        image=base64.b64encode(ecg_plot_image.image).decode("ASCII"),
    )
