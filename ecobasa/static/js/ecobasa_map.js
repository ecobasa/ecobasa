EcobasaMap = {
	map: null,
	mapUrl: "https://stamen-tiles.a.ssl.fastly.net/tiles/1.0.0/sat/{z}/{x}/{y}.png",
	attrib: 'Map data © <a href="http://openstreetmap.org">OpenStreetMap</a> contributors',
	minZoom: 8,
	maxZoom: 13,
	defaultZoom: 3,
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
		var url = "https://stamen-tiles.a.ssl.fastly.net/"
		var layer1 = new L.TileLayer("https://stamen-tiles-{s}.a.ssl.fastly.net/watercolor/{z}/{x}/{y}.png", {
		});
		var layer2 = new L.TileLayer("https://stamen-tiles-{s}.a.ssl.fastly.net/toner-lite/{z}/{x}/{y}.png", {
			opacity: 0.1,
		});
		EcobasaMap.map.addLayer(layer);
		EcobasaMap.map.addLayer(layer1);
		EcobasaMap.map.addLayer(layer2);
		layer1.setOpacity(0.6);
		layer2.setOpacity(0.3);
		googleSat = L.tileLayer('http://{s}.google.com/vt/lyrs=s&x={x}&y={y}&z={z}',{
	    maxZoom: 20,
	    subdomains:['mt0','mt1','mt2','mt3']
		});
		googleStreets = L.tileLayer('http://{s}.google.com/vt/lyrs=m&x={x}&y={y}&z={z}',{
	    maxZoom: 20,
	    subdomains:['mt0','mt1','mt2','mt3']
		});
		googleHybrid = L.tileLayer('http://{s}.google.com/vt/lyrs=s,h&x={x}&y={y}&z={z}',{
	    maxZoom: 20,
	    subdomains:['mt0','mt1','mt2','mt3']
		});
		var center = new L.LatLng(49.20, 16.00);
		EcobasaMap.map.setView(center, EcobasaMap.defaultZoom);
		var baseLayers = {
	    "Satellite": googleSat,
	    "Streets": googleStreets,
	    "Hybrid": googleHybrid,
	    "ecobasa map": layer2
	  };
	  var overlays = {

	  };
	  L.control.layers(baseLayers, overlays).addTo(EcobasaMap.map);
	},
}

StartMap = {
	map: null,
	mapUrl: "https://stamen-tiles.a.ssl.fastly.net/tiles/1.0.0/sat/{z}/{x}/{y}.png",
	attrib: 'Map data © <a href="http://openstreetmap.org">OpenStreetMap</a> contributors',
	minZoom: 8,
	maxZoom: 13,
	defaultZoom: 3,
	tms: true,
	scrollWheelZoom: false,

	addMarker: function(lat, lon, community) {
		var marker = L.marker([lat, lon]).addTo(StartMap.map);
		marker.bindPopup(community)
	},

	init: function(mapSelector) {
		StartMap.map = L.map(mapSelector);
		var layer = new L.TileLayer(StartMap.mapUrl, {
			minZoom: StartMap.minZoom,
			maxZoom: StartMap.maxZoom,
			attribution: StartMap.attrib
		});
		var url = "https://stamen-tiles.a.ssl.fastly.net/"
		var layer1 = new L.TileLayer("https://stamen-tiles-{s}.a.ssl.fastly.net/watercolor/{z}/{x}/{y}.png", {
		});
		var layer2 = new L.TileLayer("https://stamen-tiles-{s}.a.ssl.fastly.net/toner-lite/{z}/{x}/{y}.png", {
			opacity: 0.1,
		});
		StartMap.map.addLayer(layer);
		StartMap.map.addLayer(layer1);
		StartMap.map.addLayer(layer2);
		var basalayers = L.layerGroup([layer2]);
		layer1.setOpacity(0.6);
		layer2.setOpacity(0.3);
		var center = new L.LatLng(49.20, 16.00);
		StartMap.map.setView(center, StartMap.defaultZoom);
		StartMap.map.scrollWheelZoom.disable();
		StartMap.map.on('focus', function() { StartMap.map.scrollWheelZoom.enable(); });
    StartMap.map.on('click', function() {
      if (StartMap.map.scrollWheelZoom.enabled()) {
        StartMap.map.scrollWheelZoom.disable();
        }
        else {
        StartMap.map.scrollWheelZoom.enable();
        }
      });
	},
}
