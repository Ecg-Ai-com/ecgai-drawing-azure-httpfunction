# noinspection DuplicatedCode
import pathlib
import uuid

import pytest as pytest
from ecgai_drawing.enums.artifact import Artifact
from ecgai_drawing.enums.color_style import ColorStyle
from matplotlib.testing.compare import compare_images

from create_ecg_image import CreateEcgPlotRequest, create_ecg_image
from tests.test_factory import (
    BASE_IMAGE_NAME,
    COLOR_WITH_GRID_NAME,
    COLOR_WITHOUT_GRID_NAME,
    GREY_SCALE_WITH_GRID_NAME,
    GREY_SCALE_WITHOUT_GRID_NAME,
    MASK_NAME,
    get_image_path,
    load_base_image,
    save_base_image_to_test_directory,
    save_byte_image_to_test_directory,
    setup_test_record_data,
    single_valid_record_path_name,
)


@pytest.mark.parametrize("record_path_name", single_valid_record_path_name)
@pytest.mark.asyncio
async def test_create_draw_ecg_plot_with_color_no_grid_compare_against_base_image(record_path_name, tmp_path):
    # Arrange
    ecg_leads = setup_test_record_data(path_name=record_path_name)

    image = load_base_image(COLOR_WITHOUT_GRID_NAME)
    save_base_image_to_test_directory(image=image, path=tmp_path)
    base_image_file_name = get_image_path(name=BASE_IMAGE_NAME, path=tmp_path)

    transaction_id = uuid.uuid4().hex

    # request = EcgPlotRequest.create(
    #     transaction_id=transaction_id,
    #     record_name="ECG 12 lead",
    #     sample_rate=ecg_leads.sample_rate,
    #     ecg_leads=ecg_leads,
    #     color_style=ColorStyle.COLOR,
    #     show_grid=False,
    #     artifact=Artifact.ARTIFACT_UNSPECIFIED,
    #     file_name="00001",
    # )
    request = CreateEcgPlotRequest.create(
        transaction_id=transaction_id,
        record_name="ECG 12 lead",
        sample_rate=ecg_leads.sample_rate,
        ecg_leads=ecg_leads.leads,
        color_style=ColorStyle.COLOR,
        show_grid=False,
        artifact=Artifact.ARTIFACT_UNSPECIFIED,
        file_name="00001",
    )
    # Act
    draw_response = await create_ecg_image(request)

    # Assert
    file_name = image_name(draw_response)
    save_byte_image_to_test_directory(byte_image=draw_response.image, image_name=file_name, path=tmp_path)

    image_file_name = get_image_path(name=file_name, path=tmp_path)
    compare_images(expected=str(base_image_file_name), actual=str(image_file_name), tol=0)
    count = count_files(tmp_path)

    assert count == 2


@pytest.mark.parametrize("record_path_name", single_valid_record_path_name)
@pytest.mark.asyncio
async def test_create_draw_ecg_plot_with_color_with_grid_compare_against_base_image(record_path_name, tmp_path):
    # Arrange
    ecg_leads = setup_test_record_data(path_name=record_path_name)

    image = load_base_image(COLOR_WITH_GRID_NAME)
    save_base_image_to_test_directory(image=image, path=tmp_path)
    base_image_file_name = get_image_path(name=BASE_IMAGE_NAME, path=tmp_path)

    transaction_id = uuid.uuid4().hex

    # request = EcgPlotRequest.create(
    #     transaction_id=transaction_id,
    #     record_name="ECG 12 lead",
    #     sample_rate=ecg_leads.sample_rate,
    #     ecg_leads=ecg_leads,
    #     color_style=ColorStyle.COLOR,
    #     show_grid=True,
    #     artifact=Artifact.ARTIFACT_UNSPECIFIED,
    #     file_name="00001",
    # )
    request = CreateEcgPlotRequest.create(
        transaction_id=transaction_id,
        record_name="ECG 12 lead",
        sample_rate=ecg_leads.sample_rate,
        ecg_leads=ecg_leads.leads,
        color_style=ColorStyle.COLOR,
        show_grid=True,
        artifact=Artifact.ARTIFACT_UNSPECIFIED,
        file_name="00001",
    )
    # Act
    draw_response = await create_ecg_image(request)

    # Assert
    file_name = image_name(draw_response)
    save_byte_image_to_test_directory(byte_image=draw_response.image, image_name=file_name, path=tmp_path)

    image_file_name = get_image_path(name=file_name, path=tmp_path)
    compare_images(expected=str(base_image_file_name), actual=str(image_file_name), tol=0)
    count = count_files(tmp_path)

    assert count == 2


@pytest.mark.parametrize("record_path_name", single_valid_record_path_name)
@pytest.mark.asyncio
async def test_create_draw_ecg_plot_with_grey_scale_with_grid_compare_against_base_image(record_path_name, tmp_path):
    # Arrange
    ecg_leads = setup_test_record_data(path_name=record_path_name)

    image = load_base_image(GREY_SCALE_WITH_GRID_NAME)
    save_base_image_to_test_directory(image=image, path=tmp_path)
    base_image_file_name = get_image_path(name=BASE_IMAGE_NAME, path=tmp_path)

    transaction_id = uuid.uuid4().hex

    request = CreateEcgPlotRequest.create(
        transaction_id=transaction_id,
        record_name="ECG 12 lead",
        sample_rate=ecg_leads.sample_rate,
        ecg_leads=ecg_leads.leads,
        color_style=ColorStyle.GREY_SCALE,
        show_grid=True,
        artifact=Artifact.ARTIFACT_UNSPECIFIED,
        file_name="00001",
    )
    # Act
    draw_response = await create_ecg_image(request)

    # Assert
    file_name = image_name(draw_response)
    save_byte_image_to_test_directory(byte_image=draw_response.image, image_name=file_name, path=tmp_path)

    image_file_name = get_image_path(name=file_name, path=tmp_path)
    compare_images(expected=str(base_image_file_name), actual=str(image_file_name), tol=0)
    count = count_files(tmp_path)

    assert count == 2


@pytest.mark.parametrize("record_path_name", single_valid_record_path_name)
@pytest.mark.asyncio
async def test_create_draw_ecg_plot_with_grey_scale_without_grid_compare_against_base_image(record_path_name, tmp_path):
    # Arrange
    ecg_leads = setup_test_record_data(path_name=record_path_name)

    image = load_base_image(GREY_SCALE_WITHOUT_GRID_NAME)
    save_base_image_to_test_directory(image=image, path=tmp_path)
    base_image_file_name = get_image_path(name=BASE_IMAGE_NAME, path=tmp_path)

    transaction_id = uuid.uuid4().hex

    request = CreateEcgPlotRequest.create(
        transaction_id=transaction_id,
        record_name="ECG 12 lead",
        sample_rate=ecg_leads.sample_rate,
        ecg_leads=ecg_leads.leads,
        color_style=ColorStyle.GREY_SCALE,
        show_grid=False,
        artifact=Artifact.ARTIFACT_UNSPECIFIED,
        file_name="00001",
    )
    # Act
    draw_response = await create_ecg_image(request)

    # Assert
    file_name = image_name(draw_response)
    save_byte_image_to_test_directory(byte_image=draw_response.image, image_name=file_name, path=tmp_path)

    image_file_name = get_image_path(name=file_name, path=tmp_path)
    compare_images(expected=str(base_image_file_name), actual=str(image_file_name), tol=0)
    count = count_files(tmp_path)

    assert count == 2


@pytest.mark.parametrize("record_path_name", single_valid_record_path_name)
@pytest.mark.asyncio
async def test_create_draw_ecg_plot_with_mask_compare_against_base_image(record_path_name, tmp_path):
    # Arrange
    ecg_leads = setup_test_record_data(path_name=record_path_name)

    image = load_base_image(MASK_NAME)
    save_base_image_to_test_directory(image=image, path=tmp_path)
    base_image_file_name = get_image_path(name=BASE_IMAGE_NAME, path=tmp_path)

    transaction_id = uuid.uuid4().hex

    request = CreateEcgPlotRequest.create(
        transaction_id=transaction_id,
        record_name="ECG 12 lead",
        sample_rate=ecg_leads.sample_rate,
        ecg_leads=ecg_leads.leads,
        color_style=ColorStyle.MASK,
        show_grid=False,
        artifact=Artifact.ARTIFACT_UNSPECIFIED,
        file_name="00001",
    )
    # Act
    draw_response = await create_ecg_image(request)

    # Assert
    file_name = image_name(draw_response)
    save_byte_image_to_test_directory(byte_image=draw_response.image, image_name=file_name, path=tmp_path)

    image_file_name = get_image_path(name=file_name, path=tmp_path)
    compare_images(expected=str(base_image_file_name), actual=str(image_file_name), tol=0)
    count = count_files(tmp_path)

    assert count == 2


def image_name(draw_response) -> str:
    name = draw_response.file_name + draw_response.file_extension
    return name


def count_files(path: pathlib.Path, name: str = "*.*"):
    return len(list(pathlib.Path(path).glob(name)))
