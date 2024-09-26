EcobasaMap = {
	map: null,
	mapUrl: "https://tiles.stadiamaps.com/tiles/stamen_watercolor/{z}/{x}/{y}.jpg",
	attrib: '&copy; <a href="https://stadiamaps.com/" target="_blank">Stadia Maps</a>' +
    '&copy; <a href="https://www.stamen.com/" target="_blank">Stamen Design</a>' +
    '&copy; <a href="https://openmaptiles.org/" target="_blank">OpenMapTiles</a>' +
    '&copy; <a href="https://www.openstreetmap.org/copyright/" target="_blank">OpenStreetMap</a>',
	minZoom: 8,
	maxZoom: 13,
	defaultZoom: 3,
	tms: true,

	addMarker: function(lat, lon, community) {
    var ecobasaIcon = L.Icon.extend({
      options: {
        iconwUrl: '/static/leaflet/images/marker-shadow.png',
        iconAnchor: [12, 41],
        popupAnchor: [0, -41]
      }
    });
    var ecobasaIcon = new ecobasaIcon({iconUrl: '/static/leaflet/images/marker-icon.png'});
		var marker = L.marker([lat, lon], {icon:ecobasaIcon}).addTo(EcobasaMap.map);
		marker.bindPopup(community)
	},

	init: function(mapSelector) {
		EcobasaMap.map = L.map(mapSelector);
		var layer = new L.TileLayer(EcobasaMap.mapUrl, {
			minZoom: EcobasaMap.minZoom,
			maxZoom: EcobasaMap.maxZoom,
			attribution: EcobasaMap.attrib
		});
		var url = "https://tiles.stadiamaps.com/"
		var layer1 = new L.TileLayer("https://tiles.stadiamaps.com/tiles/stamen_watercolor/{z}/{x}/{y}.jpg", {
		});
		var layer2 = new L.TileLayer("https://tiles.stadiamaps.com/tiles/stamen_toner_lite/{z}/{x}/{y}{r}.png", {
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

PioneerMap = {
	map: null,
	mapUrl: "https://tiles.stadiamaps.com/tiles/stamen_watercolor/{z}/{x}/{y}.jpg",
	attrib: '&copy; <a href="https://stadiamaps.com/" target="_blank">Stadia Maps</a>' +
    '&copy; <a href="https://www.stamen.com/" target="_blank">Stamen Design</a>' +
    '&copy; <a href="https://openmaptiles.org/" target="_blank">OpenMapTiles</a>' +
    '&copy; <a href="https://www.openstreetmap.org/copyright/" target="_blank">OpenStreetMap</a>',
  minZoom: 8,
	maxZoom: 13,
	defaultZoom: 3,
	tms: true,

	addMarker: function(lat, lon, pioneer) {
		var ecobasaIcon = L.Icon.extend({
	    options: {
	      shadowUrl: '/static/leaflet/images/marker-shadow.png',
	      iconAnchor:   [12, 41],
	      popupAnchor:  [0, -41]
		  }
		});
		var userIcon = new ecobasaIcon({iconUrl: '/static/leaflet/images/user-icon.png'});
		var marker = L.marker([lat, lon], {icon:userIcon}).addTo(PioneerMap.map);
		marker.bindPopup(pioneer)
	},

	init: function(mapSelector) {
		PioneerMap.map = L.map(mapSelector);
		var layer = new L.TileLayer(PioneerMap.mapUrl, {
			minZoom: PioneerMap.minZoom,
			maxZoom: PioneerMap.maxZoom,
			attribution: PioneerMap.attrib
		});
		var url = "https://stamen-tiles.a.ssl.fastly.net/"
		var layer1 = new L.TileLayer("https://tiles.stadiamaps.com/tiles/stamen_watercolor/{z}/{x}/{y}.jpg", {
		});
		var layer2 = new L.TileLayer("https://tiles.stadiamaps.com/tiles/stamen_toner_lite/{z}/{x}/{y}{r}.png", {
			opacity: 0.1,
		});
		PioneerMap.map.addLayer(layer);
		PioneerMap.map.addLayer(layer1);
		PioneerMap.map.addLayer(layer2);
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
		PioneerMap.map.setView(center, PioneerMap.defaultZoom);
		var baseLayers = {
	    "Satellite": googleSat,
	    "Streets": googleStreets,
	    "Hybrid": googleHybrid,
	    "ecobasa map": layer2
	  };
	  var overlays = {

	  };
	  L.control.layers(baseLayers, overlays).addTo(PioneerMap.map);
	},
}

StartMap = {
	map: null,
	mapUrl: "https://tiles.stadiamaps.com/tiles/stamen_watercolor/{z}/{x}/{y}.jpg",
	attrib: '&copy; <a href="https://stadiamaps.com/" target="_blank">Stadia Maps</a>' +
    '&copy; <a href="https://www.stamen.com/" target="_blank">Stamen Design</a>' +
    '&copy; <a href="https://openmaptiles.org/" target="_blank">OpenMapTiles</a>' +
    '&copy; <a href="https://www.openstreetmap.org/copyright/" target="_blank">OpenStreetMap</a>',
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
		var url = "https://tiles.stadiamaps.com/"
		var layer1 = new L.TileLayer("https://tiles.stadiamaps.com/tiles/stamen_watercolor/{z}/{x}/{y}.jpg", {
		});
		var layer2 = new L.TileLayer("https://tiles.stadiamaps.com/tiles/stamen_toner_lite/{z}/{x}/{y}{r}.png", {
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
