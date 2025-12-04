from tethys_sdk.base import TethysAppBase
from tethys_sdk.base import url_map_maker


class App(TethysAppBase):
    """
    Tethys app class for Hello World.
    """
    name = 'Hello World'
    description = ''
    package = 'hello_world'  # WARNING: Do not change this value
    index = 'home'
    icon = f'{package}/images/icon.gif'
    root_url = 'hello-world'
    color = '#d35400'
    tags = ''
    enable_feedback = False
    feedback_emails = []

# ---- Adding new URL map for the endpoint ----

def url_maps(self):
    UrlMap = url_map_maker(self.root_url)
    url_maps = (
        UrlMap(
            name='home',
            url='hello-world',
            controller='hello_world.controllers.MapLayoutTutorialMap'
        ),
        UrlMap(
            name='geojson',
            url='hello-world/geojson',
            controller='hello_world.controllers.serve_geojson'
        ),
        UrlMap(
            name='map',
            url='hello-world/map',
            controller='hello_world.controllers.map_page'
        ),
    )
    return url_maps