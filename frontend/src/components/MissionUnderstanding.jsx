function MissionUnderstanding({ mission }) {
  if (!mission) {
    return null;
  }

  const priorityMap = {
    fishing_potential: "Fishing Potential",
    safety: "Safety",
    distance: "Travel Distance",
    balanced: "Balanced",
  };

  const constraints = mission.constraints || {};
  const preferences = mission.preferences || {};

  return (
    <div className="card mission-summary-card">

      <div className="mission-summary-header">

        <div>
          <div className="section-label">
            ORCA MISSION UNDERSTANDING
          </div>

          <h2>
            Interpreted Mission
          </h2>
        </div>

        <div className="understanding-badge">
          ✓ UNDERSTOOD
        </div>

      </div>

      <div className="mission-summary-grid">

        {/* Objective */}
        <div className="mission-detail">
          <div className="detail-icon">🎯</div>

          <div>
            <div className="detail-label">
              Objective
            </div>

            <div className="detail-value">
              {mission.objective || "Not specified"}
            </div>
          </div>
        </div>

        {/* Location */}
        <div className="mission-detail">
          <div className="detail-icon">📍</div>

          <div>
            <div className="detail-label">
              Location
            </div>

            <div className="detail-value">
              {mission.location || "Not specified"}
            </div>
          </div>
        </div>

        {/* Departure */}
        <div className="mission-detail">
          <div className="detail-icon">🕐</div>

          <div>
            <div className="detail-label">
              Departure
            </div>

            <div className="detail-value">
              {mission.departure_time || "Not specified"}
            </div>
          </div>
        </div>

        {/* Fishing Duration */}
        <div className="mission-detail">
          <div className="detail-icon">⏱️</div>

          <div>
            <div className="detail-label">
              Fishing Duration
            </div>

            <div className="detail-value">
              {mission.fishing_duration_hours !== null &&
              mission.fishing_duration_hours !== undefined
                ? `${mission.fishing_duration_hours} hours`
                : "Not specified"}
            </div>
          </div>
        </div>

        {/* Return Deadline */}
        <div className="mission-detail">
          <div className="detail-icon">🏁</div>

          <div>
            <div className="detail-label">
              Return Deadline
            </div>

            <div className="detail-value">
              {mission.return_deadline || "Not specified"}
            </div>
          </div>
        </div>

        {/* Priority */}
        <div className="mission-detail">
          <div className="detail-icon">⭐</div>

          <div>
            <div className="detail-label">
              Primary Priority
            </div>

            <div className="detail-value">
              {priorityMap[preferences.primary_preference] ||
                "Balanced"}
            </div>
          </div>
        </div>

      </div>

      {/* Constraints */}
      <div className="mission-constraints">

        <div className="constraints-title">
          Active Safety &amp; Spatial Constraints
        </div>

        <div className="constraint-list">

          {constraints.avoid_high_wind && (
            <span className="constraint-badge">
              ✓ Avoid High Wind
            </span>
          )}

          {constraints.avoid_unsafe_sea && (
            <span className="constraint-badge">
              ✓ Avoid Unsafe Sea
            </span>
          )}

          {constraints.avoid_restricted_areas && (
            <span className="constraint-badge">
              ✓ Avoid Restricted Areas
            </span>
          )}

          {constraints.max_wave_height !== null &&
            constraints.max_wave_height !== undefined && (
              <span className="constraint-badge">
                ✓ Max Wave Height:{" "}
                {constraints.max_wave_height} m
              </span>
            )}

        </div>

      </div>

    </div>
  );
}

export default MissionUnderstanding;