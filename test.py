from utils import Point
from geo_fence_detector import GeoFenceDetectorPolygon as gdp

vertices = [Point(0,0), Point(2,0), Point(2,2), Point(0,2)]
observer = Point(1.5, 1.5)
detector = gdp(vertices, observer)
print(detector.isInsideGeoFence())
print(detector.isInsideGeoFenceWithObserver(Point(4,4)))