EcobasaMap = {
	map: null,
	mapUrl: "http://otile1.mqcdn.com/tiles/1.0.0/sat/{z}/{x}/{y}.png",
	attrib: 'Map data © <a href="http://openstreetmap.org">OpenStreetMap</a> contributors',
	minZoom: 8,
	maxZoom: 13,
	defaultZoom: 5,
	tms: true,

	addMarker: function(lat, lon, community) {
		var marker = L.marker([lat, lon]).addTo(EcobasaMap.map);
		marker.bindPopup(community)
	},

	init: function(mapSelector) {
		EcobasaMap.map = L.map(mapSelector);
		var layer = new L.TileLayer(EcobasaMap.mapUrl, {
			minZoom: EcobasaMap.minZoom,
			maxZoom: EcobasaMap.maxZoom,
			attribution: EcobasaMap.attrib
		});

		var layer1 = new L.StamenTileLayer("watercolor", {
		});
		var layer2 = new L.StamenTileLayer("toner-lite", {
			opacity: 0.1,
		});
		EcobasaMap.map.addLayer(layer);
		EcobasaMap.map.addLayer(layer1);
		EcobasaMap.map.addLayer(layer2);
		layer1.setOpacity(0.6);
		layer2.setOpacity(0.3);
		var center = new L.LatLng(49.20, 16.00);
		EcobasaMap.map.setView(center, EcobasaMap.defaultZoom);
	},
}
