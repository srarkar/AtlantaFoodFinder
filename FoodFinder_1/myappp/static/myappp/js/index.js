async function init() {
  await customElements.whenDefined('gmp-map');

  const map = document.querySelector('gmp-map');
  const marker = document.querySelector('gmp-advanced-marker');
  const placePicker = document.querySelector('gmpx-place-picker');
  const infowindow = new google.maps.InfoWindow();

  map.innerMap.setOptions({
    mapTypeControl: false
  });

  placePicker.addEventListener('gmpx-placechange', async () => {
    const place = placePicker.value;

    if (!place.location) {
      window.alert("No details available for input: '" + place.name + "'");
      infowindow.close();
      marker.position = null;
      return;
    }

    // Fetch details from the Places API
    const service = new google.maps.places.PlacesService(map.innerMap);
    service.getDetails({ placeId: place.placeId }, (details, status) => {
      if (status === google.maps.places.PlacesServiceStatus.OK) {
        marker.position = place.location;

        infowindow.setContent(
          `<strong>${details.name}</strong><br>
           <span>${details.formatted_address}</span><br>
           <span>${details.rating ? 'Rating: ' + details.rating : 'No rating available'}</span><br>
           <span>${details.formatted_phone_number ? details.formatted_phone_number : 'No phone number available'}</span><br>
           <span>${details.website ? `<a href="${details.website}" target="_blank">Website</a>` : 'No website available'}</span>
        `);
        infowindow.open(map.innerMap, marker);
      } else {
        window.alert("Failed to retrieve details: " + status);
      }
    });

    if (place.viewport) {
      map.innerMap.fitBounds(place.viewport);
    } else {
      map.center = place.location;
      map.zoom = 17;
    }
  });
}

document.addEventListener('DOMContentLoaded', init);
