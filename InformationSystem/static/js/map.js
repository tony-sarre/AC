var map1 = L.map('map1').setView([14.497401, -14.452362], 8);
  var map2 = L.map('map2').setView([14.497401, -14.452362], 8);

  // Event listener on map1
  map1.on('click', function(e) {
    $.ajax({
      url: '/map_view/',
      type: 'POST',
      data: {
        'lat': e.latlng.lat,
        'lng': e.latlng.lng,
      },
      success: function(data) {
        // Update map2 with returned data
        for (var i = 0; i < data.length; i++) {
          var marker = L.marker([data[i].lat, data[i].lng]).addTo(map2);
        }
      }
    });
  });



  //GPS
function getLocation() {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(showPosition);
  } else {
    alert("Geolocation is not supported by this browser.");
  }
}

function showPosition(position) {
  var location_field = document.getElementById('id_location');
  location_field.value = position.coords.latitude + ',' + position.coords.longitude;
}
