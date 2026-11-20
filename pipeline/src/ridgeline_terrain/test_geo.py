import math

import pytest

from ridgeline_terrain.geo import arcsec_cell_size_m


def test_cells_are_square_at_equator():
    dx, dy = arcsec_cell_size_m(1 / 3, 0.0)
    assert dx == pytest.approx(dy)


def test_cells_are_narrow_at_snoqualmie_pass():
    dx, dy = arcsec_cell_size_m(1 / 3, 47.4)
    assert dy == pytest.approx(10.31, rel=1e-3)
    assert dx / dy == pytest.approx(math.cos(math.radians(47.4)))  # ~0.68


def test_rasterio_loads():
    import rasterio

    assert rasterio.__gdal_version__