
/**
 * 1. Android Location API
Use the LocationManager class to access system location services.

Implement the LocationListener interface to receive location updates.

Example:
 */
LocationManager locationManager = (LocationManager) getSystemService(Context.LOCATION_SERVICE);
locationManager.requestLocationUpdates(
    LocationManager.GPS_PROVIDER,
    1000, // Minimum time interval in milliseconds
    1,    // Minimum distance in meters
    new LocationListener() {
        @Override
        public void onLocationChanged(Location location) {
            double latitude = location.getLatitude();
            double longitude = location.getLongitude();
        }
    });
