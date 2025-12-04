document.addEventListener('DOMContentLoaded', function () {
    var map = L.map('map').setView([39.5, -111.5], 6);

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '© OpenStreetMap contributors'
    }).addTo(map);

    // Fetch the GeoJSON from Tethys endpoint
    fetch('/tethysapp/hello_world/geojson')
        .then(response => response.json())
        .then(data => {
            L.geoJSON(data, {
                style: { color: '#2c3e50', weight: 1, fillColor: '#3498db', fillOpacity: 0.5 },
                onEachFeature: function (feature, layer) {
                    if (feature.properties && feature.properties.COUNTY) {
                        layer.bindPopup('County: ' + feature.properties.COUNTY);
                    }
                }
            }).addTo(map);
        });
});