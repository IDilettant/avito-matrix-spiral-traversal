"""Main tests."""
import pook
import pytest
from mattrav.exceptions import FormatMatrixExceptions, GetMatrixException
from mattrav.matrix_traversal import get_matrix

GRAPHIC_MATRIX_4_SIZE = """+-----+-----+-----+-----+
|  10 |  20 |  30 |  40 |
+-----+-----+-----+-----+
|  50 |  60 |  70 |  80 |
+-----+-----+-----+-----+
|  90 | 100 | 110 | 120 |
+-----+-----+-----+-----+
| 130 | 140 | 150 | 160 |
+-----+-----+-----+-----+
"""
GRAPHIC_MATRIX_3_SIZE = """+-----+-----+-----+
|  10 |  20 |  30 |
+-----+-----+-----+
|  40 |  50 |  60 |
+-----+-----+-----+
|  70 |  80 |  90 |
+-----+-----+-----+
"""
GRAPHIC_MATRIX_WRONG = """|-----|-----|-----|
|  10 |  20 |  30 |
|-----|-----|-----|
"""
TRAVERSAL_4_SIZE = [
    10, 50, 90, 130,
    140, 150, 160, 120,
    80, 40, 30, 20,
    60, 100, 110, 70,
]
TRAVERSAL_3_SIZE = [
    10, 40, 70,
    80, 90, 60,
    30, 20, 50,
]
SOURCE_URL = 'https://raw.githubusercontent.com/avito-tech/python-trainee-assignment/main/matrix.txt'


@pytest.mark.asyncio
@pytest.mark.parametrize(
    'matrix, traversal',
    [
        (GRAPHIC_MATRIX_4_SIZE, TRAVERSAL_4_SIZE),
        (GRAPHIC_MATRIX_3_SIZE, TRAVERSAL_3_SIZE),
    ],
)
async def test_get_matrix(matrix, traversal):
    with pook.use(network=True):
        pook.get(
            SOURCE_URL,
            reply=200,
            response_json=matrix,
        )
        assert await get_matrix(SOURCE_URL) == traversal

        pook.get(
            SOURCE_URL,
            reply=200,
            response_json=matrix,
        )
        assert await get_matrix(SOURCE_URL) == traversal


@pytest.mark.asyncio
@pytest.mark.parametrize(
    'status_code, exception',
    [
        (200, FormatMatrixExceptions),
        (204, FormatMatrixExceptions),
        (400, GetMatrixException),
        (500, GetMatrixException),
    ],
)
async def test_get_matrix_format_exc(status_code, exception):
    with pook.use(network=True):
        pook.get(
            SOURCE_URL,
            reply=status_code,
            response_json=GRAPHIC_MATRIX_WRONG,
        )
        with pytest.raises(exception):
            await get_matrix(SOURCE_URL, raise_on_error=True)

        pook.get(
            SOURCE_URL,
            reply=status_code,
        )
        with pytest.raises(exception):
            await get_matrix(SOURCE_URL, raise_on_error=True)

        pook.get(
            SOURCE_URL,
            reply=status_code,
        )
        with pytest.raises(exception):
            await get_matrix(SOURCE_URL, raise_on_error=True)

        pook.get(
            SOURCE_URL,
            reply=status_code,
        )
        with pytest.raises(exception):
            await get_matrix(SOURCE_URL, raise_on_error=True)
