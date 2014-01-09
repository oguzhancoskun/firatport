function supports_html5_storage() {
  try {
    return 'localStorage' in window && window['localStorage'] !== null;
  } catch (e) {
    return false;
  }
}
      
      var map;
      var mapMarkers = new Array();
      var icon1 = L.icon({
	    iconUrl: 'dist/png/m1.png',
	    iconSize: [32, 32]
	  });
	  var icon2 = L.icon({
	    iconUrl: 'dist/png/m2.png',
	    iconSize: [32, 32]
	  });
	  var icon3 = L.icon({
	    iconUrl: 'dist/png/m3.png',
	    iconSize: [32, 32]
	  });
	  var icon4 = L.icon({
	    iconUrl: 'dist/png/m4.png',
	    iconSize: [32,32]
	  });
	  var iconServer = L.icon({
	    iconUrl: 'dist/png/server.png',
	    iconSize: [64,64]
	  });

      function init() {
        navigator.geolocation.getCurrentPosition(function(position) {
            map = L.map('map').setView([38.6773, 39.1918], 15);
            L.marker([38.67708, 39.20192],{icon: icon1}).addTo(map).bindPopup("bilgi işlem");//bilgi işlemm
            L.marker([38.68227, 39.17466],{icon: icon2}).addTo(map).bindPopup("teknokent");//teknokent
            L.marker([38.68157, 39.19616],{icon: icon3}).addTo(map).bindPopup("yazılım");//teknoloji
            L.marker([38.67326, 39.18919],{icon: icon4}).addTo(map).bindPopup("bilmuh");//bilgisayar
            L.marker([38.67393, 39.18850],{icon: icon4}).addTo(map).bindPopup("kütüphane");//kütüphane
            //[position.coords.latitude, position.coords.longitude ], <zoom_parameter>
            L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: 'FiratPort, Sefa & Oguzhan', maxZoom: 18 }).addTo(map);
            noLoc = false;
        }
        , function(err) {
            if (err.code == 2) {//Position unavailable
                alert("Yetkisiz Alan, Kod:2");
            } else {
            alert(err.code);
            alert(err.message);
            }
        }/*, {timeout: 0, enableHighAccuracy: false, maximumAge: 75000}
        */
        );
      }