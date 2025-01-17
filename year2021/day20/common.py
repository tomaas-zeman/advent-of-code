import numpy as np
from aocutils import Numpy


def enhance(data: list[str], iterations: int):
    enhancer = data[0]
    image = np.pad(
        Numpy.from_input_as_str(data[2:]), pad_width=iterations * 2, constant_values="."
    )

    for _ in range(iterations):
        clone = np.copy(image)

        for row in range(1, image.shape[0] - 1):
            for col in range(1, image.shape[1] - 1):
                index = int(
                    "".join(
                        "0" if e == "." else "1"
                        for e in image[row - 1 : row + 2, col - 1 : col + 2].flatten()
                    ),
                    2,
                )

                clone[row, col] = enhancer[index]

        image = clone

    return np.count_nonzero(
        image[
            iterations : image.shape[0] - iterations,
            iterations : image.shape[1] - iterations,
        ]
        == "#"
    )
