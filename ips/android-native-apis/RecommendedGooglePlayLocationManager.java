/*
 * 2. Google Play Services Location API (Recommended)
Use the Fused Location Provider for high-level location access with better battery optimization.

Retrieve the last known location using getLastLocation() or request periodic updates with requestLocationUpdates().


Requires Google Play Services and permissions (ACCESS_FINE_LOCATION)


Example:
 */


 FusedLocationProviderClient fusedLocationClient = LocationServices.getFusedLocationProviderClient(this);
 fusedLocationClient.getLastLocation()
     .addOnSuccessListener(location -> {
         if (location != null) {
             double latitude = location.getLatitude();
             double longitude = location.getLongitude();
         }
     });
 