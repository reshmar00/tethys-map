import os
import json
from django.http import JsonResponse
from tethys_sdk.layouts import MapLayout
from tethys_sdk.routing import controller
from .app import App


@controller(name="home", app_workspace=True)
class MapLayoutTutorialMap(MapLayout):
    app = App
    base_template = f'{App.package}/base.html'
    map_title = 'Map Layout Tutorial'
    map_subtitle = 'NOAA-OWP NextGen Model Outputs'


# ---- New GeoJSON endpoint ----
@controller(name="geojson")
def serve_geojson(request):
    """
    Serve the GeoJSON for the frontend map.
    """
    GEOJSON_PATH = os.path.join(
        os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
        'resource_data-files', 'GeoJSON', 'counties.geojson'
    )

    with open(GEOJSON_PATH, 'r') as f:
        data = json.load(f)
    return JsonResponse(data)