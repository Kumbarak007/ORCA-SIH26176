function Recommendation({ recommendation }) {
  if (!recommendation) {
    return null;
  }

  const isFeasible =
    recommendation.status === "FEASIBLE";

  return (
    <div className="recommendation-card">

      {/* Header */}
      <div className="recommendation-header">

        <div>
          <div className="section-label">
            ORCA MISSION DECISION
          </div>

          <h2>
            Recommended Fishing Zone
          </h2>
        </div>

        <div
          className="status-badge"
          style={{
            background: isFeasible
              ? "#dcfce7"
              : "#fee2e2",
            color: isFeasible
              ? "#166534"
              : "#b91c1c",
          }}
        >
          {recommendation.status || "UNKNOWN"}
        </div>

      </div>

      {/* Recommended Zone */}
      <div
        className="recommended-zone"
        style={{
          background: isFeasible
            ? "#f0fdf4"
            : "#fef2f2",
          borderColor: isFeasible
            ? "#bbf7d0"
            : "#fecaca",
        }}
      >

        <div>

          <div
            className="zone-label"
            style={{
              color: isFeasible
                ? "#166534"
                : "#b91c1c",
            }}
          >
            RECOMMENDED ZONE
          </div>

          <div
            className="zone-value"
            style={{
              color: isFeasible
                ? "#15803d"
                : "#dc2626",
            }}
          >
            {recommendation.zone_id || "NONE"}
          </div>

        </div>

      </div>

      {/* Decision Metrics */}
      <div className="decision-metrics">

        <div className="metric-card">

          <div className="metric-icon">
            🎯
          </div>

          <div>

            <div className="metric-label">
              Decision Score
            </div>

            <div className="metric-value">

              <span>
                {recommendation.score ?? "—"}
              </span>

              <span className="metric-unit">
                {" "}
                / 100
              </span>

            </div>

          </div>

        </div>


        <div className="metric-card">

          <div className="metric-icon">
            🎣
          </div>

          <div>

            <div className="metric-label">
              Decision Type
            </div>

            <div className="metric-value">
              Mission-Aware
            </div>

          </div>

        </div>


        <div className="metric-card">

          <div className="metric-icon">
            🛡️
          </div>

          <div>

            <div className="metric-label">
              Safety Check
            </div>

            <div
              className="metric-value"
              style={{
                color: isFeasible
                  ? "#15803d"
                  : "#dc2626",
              }}
            >
              {isFeasible
                ? "Passed"
                : "Not Passed"}
            </div>

          </div>

        </div>

      </div>

      {/* Decision Rationale */}
      <div className="decision-reason">

        <h3>
          Why ORCA selected this zone
        </h3>

        <p>
          {recommendation.rationale ||
            "ORCA evaluated the available marine zones using fishing potential, ocean conditions, weather safety and spatial constraints."}
        </p>

      </div>

      {/* Decision Factors */}
      <div className="decision-factors">

        <div className="factor">
          <span>🎣</span>
          <span>Fishing Potential</span>
        </div>

        <div className="factor">
          <span>🌊</span>
          <span>Ocean Conditions</span>
        </div>

        <div className="factor">
          <span>🌤️</span>
          <span>Weather Safety</span>
        </div>

        <div className="factor">
          <span>📍</span>
          <span>Spatial Constraints</span>
        </div>

      </div>

    </div>
  );
}

export default Recommendation;