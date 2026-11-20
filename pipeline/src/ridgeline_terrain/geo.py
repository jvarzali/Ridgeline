import math

METERS_PER_DEGREE_LAT = 111_320.0  # spherical approximation


def arcsec_cell_size_m(arcsec: float, lat_deg: float) -> tuple[float, float]:
    """Approximate ground size (east-west, north-south) in meters of a cell
    that spans `arcsec` arc-seconds in each direction at latitude `lat_deg`."""
    deg = arcsec / 3600.0
    dy = deg * METERS_PER_DEGREE_LAT
    dx = dy * math.cos(math.radians(lat_deg))
    return dx, dy