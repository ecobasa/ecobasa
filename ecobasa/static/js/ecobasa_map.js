EcobasaMap = {
	map: null,
	//mapUrl: "http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
	mapUrl: "http://otile1.mqcdn.com/tiles/1.0.0/osm/{z}/{x}/{y}.png",
	attrib: 'Map data © <a href="http://openstreetmap.org">OpenStreetMap</a> contributors',
	minZoom: 1,
	maxZoom: 15,
	defaultZoom: 5,

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
		EcobasaMap.map.addLayer(layer);
		var berlin = new L.LatLng(52.52, 13.39);
		EcobasaMap.map.setView(berlin, EcobasaMap.defaultZoom);
	},
}
