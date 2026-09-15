import {
  MapContainer,
  TileLayer,
  CircleMarker,
  Popup,
  useMap,
} from "react-leaflet";

import "leaflet/dist/leaflet.css";

function MapLegend() {
  return (
    <div className="orca-map-legend">

      <strong>ORCA Zone Status</strong>

      <br />

      <span style={{ color: "#16a34a" }}>
        ●
      </span>{" "}
      Recommended

      <br />

      <span style={{ color: "#dc2626" }}>
        ●
      </span>{" "}
      Rejected

      <br />

      <span style={{ color: "#2563eb" }}>
        ●
      </span>{" "}
      Candidate

    </div>
  );
}


/*
 * Automatically adjusts the map view when
 * ORCA receives new zone data.
 */
function FitMapToZones({ zones }) {
  const map = useMap();

  if (!zones || zones.length === 0) {
    return null;
  }

  const coordinates = zones
    .filter(
      (zone) =>
        zone.location &&
        zone.location.latitude !== undefined &&
        zone.location.longitude !== undefined
    )
    .map((zone) => [
      zone.location.latitude,
      zone.location.longitude,
    ]);

  if (coordinates.length === 0) {
    return null;
  }

  const bounds = coordinates;

  map.fitBounds(bounds, {
    padding: [40, 40],
    maxZoom: 10,
  });

  return null;
}


function MarineMap({ data }) {

  const zones = data?.fused_data || [];

  const recommendation =
    data?.recommendation || null;

  const rejectedPlans =
    recommendation?.rejected_plans || [];


  return (
    <div className="card">

      <h2>
        Marine Map
      </h2>

      <div className="marine-map-wrapper">

        <MapContainer
          center={[15.20, 73.96]}
          zoom={9}
          scrollWheelZoom={true}
          className="marine-map"
        >

          {/* OpenStreetMap */}
          <TileLayer
            attribution='&copy; OpenStreetMap contributors'
            url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
          />


          {/* Automatically fit map to ORCA zones */}
          <FitMapToZones zones={zones} />


          {/* ORCA Zone Markers */}
          {zones.map((zone) => {

            const isRecommended =
              zone.zone_id ===
              recommendation?.zone_id;


            const isRejected =
              rejectedPlans.some(
                (plan) =>
                  plan.zone_id ===
                  zone.zone_id
              );


            let markerColor;
            let statusText;


            if (isRecommended) {

              markerColor = "#16a34a";
              statusText = "RECOMMENDED";

            } else if (isRejected) {

              markerColor = "#dc2626";
              statusText = "REJECTED";

            } else {

              markerColor = "#2563eb";
              statusText = "CANDIDATE";

            }


            return (
              <CircleMarker
                key={zone.zone_id}
                center={[
                  zone.location.latitude,
                  zone.location.longitude,
                ]}
                radius={10}
                pathOptions={{
                  color: markerColor,
                  fillColor: markerColor,
                  fillOpacity: 0.8,
                  weight: 3,
                }}
              >

                <Popup>

                  <div className="map-popup">

                    <strong>
                      {zone.zone_id}
                    </strong>

                    <br />

                    <strong>
                      Status:
                    </strong>{" "}
                    {statusText}

                    <br />
                    <br />

                    <strong>
                      Fishing suitability:
                    </strong>{" "}
                    {zone.pfz?.suitability ?? "—"}

                    <br />

                    <strong>
                      Chlorophyll-a:
                    </strong>{" "}
                    {zone.ocean?.chlorophyll_a ?? "—"}
                    {" "}
                    mg/m³

                    <br />

                    <strong>
                      SST:
                    </strong>{" "}
                    {zone.ocean?.sst ?? "—"}
                    {" "}
                    °C

                    <br />

                    <strong>
                      Wave height:
                    </strong>{" "}
                    {zone.ocean?.wave_height ?? "—"}
                    {" "}
                    m

                    <br />

                    <strong>
                      Wind speed:
                    </strong>{" "}
                    {zone.weather?.wind_speed ?? "—"}
                    {" "}
                    km/h

                    <br />

                    <strong>
                      Weather risk:
                    </strong>{" "}
                    {zone.weather?.risk ?? "—"}

                    <br />

                    <strong>
                      Distance:
                    </strong>{" "}
                    {zone.gis?.distance_km ?? "—"}
                    {" "}
                    km

                  </div>

                </Popup>

              </CircleMarker>
            );
          })}


          {/* Legend */}
          <div className="leaflet-bottom leaflet-right">

            <div className="leaflet-control">
              <MapLegend />
            </div>

          </div>

        </MapContainer>

      </div>

    </div>
  );
}

export default MarineMap;