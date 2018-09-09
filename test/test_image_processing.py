"""
针对图片下载做测试，方便开发及hotfix

* https://pillow.readthedocs.io/en/latest/reference/Image.html
* https://docs.pytest.org/en/latest/contents.html
"""

import pytest

import himawaripy.__main__ as him


def test_basic():
    # 针对下载下来的图像片段进行合并处理
    him.thread_main()


def test_test():
    from PIL import Image

    MARGIN = 166

    png = Image.open('../dev/himawari.png')
    height = int(png.height + MARGIN * 2)
    width = int(height * 1.6)

    png_new = Image \
        .new('RGB', (width, height), 0)

    png_new.paste(png, (int(width / 2 - png.width / 2), MARGIN))
    png_new.show()
