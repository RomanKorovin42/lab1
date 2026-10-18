"""Заготовки задач на NumPy."""

import numpy as np
from grader_contracts.numpy_tasks import (
    BinarizeInput, ChessInput, EllipseInput, MatrixInput, MatrixStatistics,
    MatrixVectorBatchInput, OneHotInput, RandomMatrixInput, RectangleInput,
    TimeSeriesInput, TimeSeriesStatistics,
)


def sum_prod(data: MatrixVectorBatchInput) -> np.ndarray:
    matrices, vectors = data.matrices, data.vectors
    sum = np.matmul(matrices, vectors).sum(axis=0)

    return sum

data = MatrixVectorBatchInput(
    matrices = np.array([
        [[1, 2],
        [3, 4]],

        [[0, 1],
        [1, 0]],
    ]),  # форма (2, 2, 2)

    vectors = np.array([
        [[1],
        [2]],

        [[3],
        [4]],
    ])  # форма (2, 2, 1)
)

sum_prod(data)


def binarize(data: BinarizeInput) -> np.ndarray:
    matrix, threshold = data.matrix, data.threshold

    return (matrix > threshold).astype(int)


def unique_rows(data: MatrixInput) -> list[list[float]]:
    matrix = data.matrix
    rows = []

    for row in matrix:
        uniqueNums = []
        for num in row:
            if num not in uniqueNums:
                uniqueNums.append(float(num))
        rows.append(uniqueNums)

    return rows

data1 = MatrixInput(
    matrix=np.array([
        [1, 1, 2],
        [5, 4, 1],
    ])
)

unique_rows(data1)




def unique_columns(data: MatrixInput) -> list[list[float]]:
    matrix = data.matrix
    columns = []
    x = 0

    while x < len(matrix[0]):
        uniqueNums = []
        for i in matrix:
            if i[x] not in uniqueNums:
                uniqueNums.append(float(i[x]))
        columns.append(uniqueNums)
        x += 1
    
    return columns

unique_columns(data1)

def matrix_statistics(data: RandomMatrixInput) -> MatrixStatistics:
    rows, columns, mean, std, seed = data.rows, data.columns, data.mean, data.std, data.seed

    range = np.random.default_rng(seed)
    matrix = range.normal(loc=mean, scale=std, size=(rows, columns))

    rowMeans = np.mean(matrix, axis=1)
    columnMeans = np.mean(matrix, axis=0)
    rowVariances = np.var(matrix, axis=1)
    columnVariances = np.var(matrix, axis=0)

    return MatrixStatistics(
        matrix=matrix,
        row_means=rowMeans,
        column_means=columnMeans,
        row_variances=rowVariances,
        column_variances=columnVariances,
    )


def chess(data: ChessInput) -> np.ndarray:
    rows, columns, first, second = data.rows, data.columns, data.first, data.second

    i, j = np.indices((rows, columns))
    mask = (i + j) % 2 == 0
    print(np.where(mask, first, second))
    return np.where(mask, first, second)


def draw_rectangle(data: RectangleInput) -> np.ndarray:
    width, height = data.width, data.height
    image_height, image_width = data.image_height, data.image_width
    shape_color, background_color = data.shape_color, data.background_color
    raise NotImplementedError  # TODO


def draw_ellipse(data: EllipseInput) -> np.ndarray:
    semi_axis_x, semi_axis_y = data.semi_axis_x, data.semi_axis_y
    image_height, image_width = data.image_height, data.image_width
    shape_color, background_color = data.shape_color, data.background_color
    raise NotImplementedError  # TODO


def analyze_time_series(data: TimeSeriesInput) -> TimeSeriesStatistics:
    values, window = data.values, data.window
    raise NotImplementedError  # TODO


def one_hot(data: OneHotInput) -> np.ndarray:
    labels, class_count = np.asarray(data.labels, dtype=int), data.class_count

    if class_count is None:
        class_count = int(labels.max()) + 1 if labels.size else 0

    result = np.zeros((labels.size, class_count), dtype=int)
    result[np.arange(labels.size), labels] = 1
    print(result)
    return result
