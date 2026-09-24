import { useEffect, useRef, useState } from "react";
import {
  CircleMarker,
  MapContainer,
  Popup,
  TileLayer,
  useMap,
} from "react-leaflet";

import "leaflet/dist/leaflet.css";


/* =========================================================
   MAP FITTER
   ========================================================= */

function MapFitter({ zones }) {
  const map = useMap();

  useEffect(() => {
    if (!zones || zones.length === 0) return;

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

    if (coordinates.length === 0) return;

    map.fitBounds(coordinates, {
      padding: [45, 45],
      maxZoom: 10,
    });
  }, [zones, map]);

  return null;
}


/* =========================================================
   SMALL UI ICONS
   ========================================================= */

function Icon({ type }) {
  const icons = {
    mission: (
      <svg viewBox="0 0 24 24" aria-hidden="true">
        <circle cx="12" cy="12" r="8" />
        <circle cx="12" cy="12" r="3" />
        <path d="M12 2v3M12 19v3M2 12h3M19 12h3" />
      </svg>
    ),

    location: (
      <svg viewBox="0 0 24 24" aria-hidden="true">
        <path d="M20 10c0 5-8 11-8 11S4 15 4 10a8 8 0 1 1 16 0Z" />
        <circle cx="12" cy="10" r="2.5" />
      </svg>
    ),

    clock: (
      <svg viewBox="0 0 24 24" aria-hidden="true">
        <circle cx="12" cy="12" r="8.5" />
        <path d="M12 7v5l3 2" />
      </svg>
    ),

    wave: (
      <svg viewBox="0 0 24 24" aria-hidden="true">
        <path d="M3 9c3-4 6 4 9 0s6 4 9 0" />
        <path d="M3 14c3-4 6 4 9 0s6 4 9 0" />
        <path d="M3 19c3-4 6 4 9 0s6 4 9 0" />
      </svg>
    ),

    shield: (
      <svg viewBox="0 0 24 24" aria-hidden="true">
        <path d="M12 3 19 6v5c0 5-3 8-7 10-4-2-7-5-7-10V6l7-3Z" />
        <path d="m9 12 2 2 4-5" />
      </svg>
    ),

    data: (
      <svg viewBox="0 0 24 24" aria-hidden="true">
        <rect x="4" y="4" width="16" height="16" rx="2" />
        <path d="M8 15v-3M12 15V8M16 15v-5" />
      </svg>
    ),

    send: (
      <svg viewBox="0 0 24 24" aria-hidden="true">
        <path d="m4 5 16 7-16 7 3-7-3-7Z" />
        <path d="M7 12h13" />
      </svg>
    ),

    search: (
      <svg viewBox="0 0 24 24" aria-hidden="true">
        <circle cx="10.5" cy="10.5" r="6" />
        <path d="m15 15 5 5" />
      </svg>
    ),

    info: (
      <svg viewBox="0 0 24 24" aria-hidden="true">
        <circle cx="12" cy="12" r="9" />
        <path d="M12 10v6M12 7h.01" />
      </svg>
    ),

    check: (
      <svg viewBox="0 0 24 24" aria-hidden="true">
        <circle cx="12" cy="12" r="9" />
        <path d="m8 12 3 3 5-6" />
      </svg>
    ),
  };

  return (
    <span className="icon">
      {icons[type] || icons.info}
    </span>
  );
}


/* =========================================================
   AGENT STATUS
   ========================================================= */

function AgentStrip({ active }) {
  const agents = [
    ["PFZ", "Potential Fishing Zone"],
    ["OCEAN", "Ocean Conditions"],
    ["WX", "Weather Intelligence"],
    ["GIS", "Spatial Reasoning"],
  ];

  return (
    <div className="agent-strip">

      {agents.map(([shortName, label]) => (
        <div
          className={`agent-item ${active ? "active" : ""}`}
          key={shortName}
        >
          <span className="agent-pulse" />
          <div>
            <strong>{shortName}</strong>
            <span>{label}</span>
          </div>
        </div>
      ))}

    </div>
  );
}


/* =========================================================
   MISSION UNDERSTANDING
   ========================================================= */

function MissionUnderstanding({ mission }) {
  if (!mission) return null;

  const priorityMap = {
    fishing_potential: "Fishing Potential",
    safety: "Safety",
    distance: "Travel Distance",
    balanced: "Balanced",
  };

  const constraints = mission.constraints || {};
  const preferences = mission.preferences || {};

  const details = [
    [
      "Objective",
      mission.objective || "Not specified",
      "mission",
    ],
    [
      "Location",
      mission.location || "Not specified",
      "location",
    ],
    [
      "Departure",
      mission.departure_time || "Not specified",
      "clock",
    ],
    [
      "Duration",
      mission.fishing_duration_hours !== null &&
      mission.fishing_duration_hours !== undefined
        ? `${mission.fishing_duration_hours} hours`
        : "Not specified",
      "clock",
    ],
    [
      "Return Deadline",
      mission.return_deadline || "Not specified",
      "clock",
    ],
    [
      "Primary Priority",
      priorityMap[preferences.primary_preference] ||
        "Balanced",
      "mission",
    ],
  ];

  return (
    <section className="panel mission-panel">

      <div className="panel-heading">
        <div>
          <span className="eyebrow">
            MISSION INTERPRETATION
          </span>

          <h2>Mission Understanding</h2>
        </div>

        <span className="verified-badge">
          <Icon type="check" />
          Parsed
        </span>
      </div>

      <div className="mission-grid">

        {details.map(([label, value, icon]) => (
          <div className="mission-detail" key={label}>

            <div className="detail-icon">
              <Icon type={icon} />
            </div>

            <div>
              <span className="detail-label">
                {label}
              </span>

              <strong>{value}</strong>
            </div>

          </div>
        ))}

      </div>

      <div className="constraint-area">

        <span className="detail-label">
          ACTIVE CONSTRAINTS
        </span>

        <div className="constraint-list">

          {constraints.avoid_high_wind && (
            <span className="constraint">
              <span className="constraint-dot" />
              Avoid high wind
            </span>
          )}

          {constraints.avoid_unsafe_sea && (
            <span className="constraint">
              <span className="constraint-dot" />
              Avoid unsafe sea
            </span>
          )}

          {constraints.avoid_restricted_areas && (
            <span className="constraint">
              <span className="constraint-dot" />
              Avoid restricted areas
            </span>
          )}

          {constraints.max_wave_height !== null &&
            constraints.max_wave_height !== undefined && (
              <span className="constraint">
                <span className="constraint-dot" />
                Maximum wave {constraints.max_wave_height} m
              </span>
            )}

        </div>

      </div>

    </section>
  );
}


/* =========================================================
   RECOMMENDATION
   ========================================================= */

function Recommendation({ recommendation }) {
  if (!recommendation) return null;

  const feasible =
    recommendation.status === "FEASIBLE";

  return (
    <section
      className={`recommendation-panel ${
        feasible ? "feasible" : "not-feasible"
      }`}
    >

      <div className="recommendation-top">

        <div>
          <span className="eyebrow">
            MARINEX DECISION ENGINE
          </span>

          <h2>Mission Recommendation</h2>

          <p>
            Selected after evaluating marine,
            weather and spatial evidence.
          </p>
        </div>

        <div className="decision-status">
          <span className="status-dot" />
          {recommendation.status}
        </div>

      </div>

      <div className="recommendation-main">

        <div className="selected-zone">

          <span className="zone-caption">
            RECOMMENDED ZONE
          </span>

          <div className="zone-name">
            {recommendation.zone_id || "NONE"}
          </div>

          <div className="zone-subtitle">
            Mission-compatible operating area
          </div>

        </div>

        <div className="score-block">

          <span className="zone-caption">
            DECISION SCORE
          </span>

          <div className="score">
            {recommendation.score ?? "—"}
            <small>/100</small>
          </div>

        </div>

      </div>

      <div className="decision-rationale">

        <div className="rationale-icon">
          <Icon type="info" />
        </div>

        <div>
          <span className="detail-label">
            DECISION RATIONALE
          </span>

          <p>
            {recommendation.rationale ||
              "ORCA evaluated the available marine zones using fishing potential, ocean conditions, weather safety and spatial constraints."}
          </p>
        </div>

      </div>

      <div className="decision-factors">

        <div>
          <span className="factor-code">PFZ</span>
          <span>Fishing Potential</span>
        </div>

        <div>
          <span className="factor-code">OCN</span>
          <span>Ocean Conditions</span>
        </div>

        <div>
          <span className="factor-code">WX</span>
          <span>Weather Safety</span>
        </div>

        <div>
          <span className="factor-code">GIS</span>
          <span>Spatial Constraints</span>
        </div>

      </div>

    </section>
  );
}


/* =========================================================
   EVIDENCE
   ========================================================= */

function EvidenceSection({ evidence }) {
  if (!evidence || evidence.length === 0) {
    return null;
  }

  return (
    <section className="panel">

      <div className="panel-heading">
        <div>
          <span className="eyebrow">
            EVIDENCE FUSION
          </span>

          <h2>Decision Evidence</h2>
        </div>

        <span className="evidence-count">
          {evidence.length} data points
        </span>
      </div>

      <div className="evidence-grid">

        {evidence.map((item, index) => (

          <div
            className="evidence-card"
            key={`${item.source}-${item.variable}-${index}`}
          >

            <div className="evidence-header">

              <span className="source-tag">
                {item.source}
              </span>

              <span className="confidence">
                {item.confidence}
              </span>

            </div>

            <span className="evidence-variable">
              {item.variable}
            </span>

            <strong className="evidence-value">
              {item.value}
              {item.unit ? ` ${item.unit}` : ""}
            </strong>

            <div className="evidence-line">
              <span />
            </div>

            <span className="evidence-meta">
              Source confidence
            </span>

          </div>

        ))}

      </div>

    </section>
  );
}


/* =========================================================
   CANDIDATE PLANS
   ========================================================= */

function CandidatePlans({ plans, recommendation }) {
  if (!plans || plans.length === 0) {
    return null;
  }

  return (
    <section className="panel">

      <div className="panel-heading">
        <div>
          <span className="eyebrow">
            PLAN SEARCH
          </span>

          <h2>Candidate Plan Comparison</h2>
        </div>

        <span className="evidence-count">
          {plans.length} zones evaluated
        </span>
      </div>

      <div className="table-wrapper">

        <table className="plans-table">

          <thead>
            <tr>
              <th>ZONE</th>
              <th>SCORE</th>
              <th>FEASIBILITY</th>
              <th>DECISION</th>
            </tr>
          </thead>

          <tbody>

            {plans.map((plan) => {

              const recommended =
                plan.zone_id === recommendation?.zone_id;

              return (
                <tr key={plan.zone_id}>

                  <td>
                    <span className="table-zone">
                      {plan.zone_id}
                    </span>
                  </td>

                  <td>
                    <span className="table-score">
                      {plan.feasible
                        ? plan.score
                        : "—"}
                    </span>
                  </td>

                  <td>
                    <span
                      className={
                        plan.feasible
                          ? "feasible-text"
                          : "rejected-text"
                      }
                    >
                      {plan.feasible
                        ? "Feasible"
                        : "Rejected"}
                    </span>
                  </td>

                  <td>

                    {recommended ? (
                      <span className="table-badge recommended">
                        Recommended
                      </span>
                    ) : plan.feasible ? (
                      <span className="table-badge candidate">
                        Candidate
                      </span>
                    ) : (
                      <span className="table-badge rejected">
                        Rejected
                      </span>
                    )}

                  </td>

                </tr>
              );
            })}

          </tbody>

        </table>

      </div>

    </section>
  );
}


/* =========================================================
   REJECTED ALTERNATIVES
   ========================================================= */

function RejectedAlternatives({ plans }) {
  if (!plans || plans.length === 0) {
    return null;
  }

  return (
    <section className="panel">

      <div className="panel-heading">
        <div>
          <span className="eyebrow">
            CONSTRAINT ANALYSIS
          </span>

          <h2>Rejected Alternatives</h2>
        </div>
      </div>

      <div className="rejected-list">

        {plans.map((plan) => (

          <div
            className="rejected-card"
            key={plan.zone_id}
          >

            <div className="rejected-zone">
              <span className="rejected-marker" />
              <strong>{plan.zone_id}</strong>
            </div>

            <div className="reasons">

              {plan.rejection_reasons?.map(
                (reason, index) => (
                  <span key={index}>
                    {reason}
                  </span>
                )
              )}

            </div>

          </div>

        ))}

      </div>

    </section>
  );
}


/* =========================================================
   EXPLANATION
   ========================================================= */

function Explanation({ explanation }) {
  if (!explanation) return null;

  return (
    <section className="panel explanation-panel">

      <div className="panel-heading">
        <div>
          <span className="eyebrow">
            DECISION TRACE
          </span>

          <h2>Why MARINEX Recommends This Plan</h2>
        </div>
      </div>

      <div className="explanation-box">
        <div className="explanation-line" />

        <p>{explanation}</p>
      </div>

    </section>
  );
}


/* =========================================================
   MARINE MAP
   ========================================================= */

function MarineMap({ data }) {
  const zones = data?.fused_data || [];
  const recommendation = data?.recommendation;
  const rejectedPlans =
    recommendation?.rejected_plans || [];

  return (
    <section className="panel map-panel">

      <div className="panel-heading">

        <div>
          <span className="eyebrow">
            SPATIAL INTELLIGENCE
          </span>

          <h2>Marine Operating Map</h2>
        </div>

        <div className="map-status">
          <span className="status-dot" />
          Live analysis layer
        </div>

      </div>

      <div className="map-shell">

        <MapContainer
          center={[15.2, 73.96]}
          zoom={9}
          scrollWheelZoom={true}
          className="marine-map"
        >

          <TileLayer
            attribution="&copy; OpenStreetMap contributors"
            url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
          />

          <MapFitter zones={zones} />

          {zones.map((zone) => {

            const recommended =
              zone.zone_id ===
              recommendation?.zone_id;

            const rejected =
              rejectedPlans.some(
                (plan) =>
                  plan.zone_id === zone.zone_id
              );

            const color = recommended
              ? "#21d4c5"
              : rejected
              ? "#ff5d73"
              : "#4ca8ff";

            const status = recommended
              ? "RECOMMENDED"
              : rejected
              ? "REJECTED"
              : "CANDIDATE";

            return (
              <CircleMarker
                key={zone.zone_id}
                center={[
                  zone.location.latitude,
                  zone.location.longitude,
                ]}
                radius={recommended ? 12 : 9}
                pathOptions={{
                  color,
                  fillColor: color,
                  fillOpacity: 0.75,
                  weight: 2,
                }}
              >

                <Popup>

                  <div className="map-popup">

                    <strong>
                      {zone.zone_id}
                    </strong>

                    <span className="popup-status">
                      {status}
                    </span>

                    <div>
                      Fishing suitability:{" "}
                      {zone.pfz?.suitability ?? "—"}
                    </div>

                    <div>
                      Chlorophyll-a:{" "}
                      {zone.ocean?.chlorophyll_a ?? "—"}
                      {" mg/m³"}
                    </div>

                    <div>
                      SST:{" "}
                      {zone.ocean?.sst ?? "—"}
                      {" °C"}
                    </div>

                    <div>
                      Wave height:{" "}
                      {zone.ocean?.wave_height ?? "—"}
                      {" m"}
                    </div>

                    <div>
                      Wind speed:{" "}
                      {zone.weather?.wind_speed ?? "—"}
                      {" km/h"}
                    </div>

                    <div>
                      Weather risk:{" "}
                      {zone.weather?.risk ?? "—"}
                    </div>

                    <div>
                      Distance:{" "}
                      {zone.gis?.distance_km ?? "—"}
                      {" km"}
                    </div>

                  </div>

                </Popup>

              </CircleMarker>
            );
          })}

        </MapContainer>

        <div className="map-legend">

          <div>
            <span className="legend-dot recommended-dot" />
            Recommended
          </div>

          <div>
            <span className="legend-dot candidate-dot" />
            Candidate
          </div>

          <div>
            <span className="legend-dot rejected-dot" />
            Rejected
          </div>

        </div>

      </div>

    </section>
  );
}


/* =========================================================
   CHAT
   ========================================================= */

function ChatPanel({
  history,
  input,
  setInput,
  onSubmit,
  loading,
}) {
  const chatRef = useRef(null);

  useEffect(() => {
    if (chatRef.current) {
      chatRef.current.scrollTop =
        chatRef.current.scrollHeight;
    }
  }, [history, loading]);

  const submit = () => {
    if (!input.trim() || loading) return;
    onSubmit(input.trim());
  };

  return (
    <section className="mission-command panel">

      <div className="command-header">

        <div>

          <span className="eyebrow">
            MISSION COMMAND
          </span>

          <h2>
            Describe your marine mission
          </h2>

          <p>
            MARINEX interprets your objective and coordinates
            PFZ, ocean, weather and GIS intelligence.
          </p>

        </div>

        <div className="orca-core">

          <div className="core-ring">
            ORCA
          </div>

          <span>INTELLIGENCE ONLINE</span>

        </div>

      </div>

      <AgentStrip active={loading || history.length > 0} />

      <div
        className="conversation"
        ref={chatRef}
      >

        {history.length === 0 && (
          <div className="welcome-message">

            <div className="message-avatar">
              O
            </div>

            <div>

              <span className="message-author">
                ORCA
              </span>

              <p>
                Mission system ready. Describe your
                fishing or marine operation in natural
                language.
              </p>

            </div>

          </div>
        )}

        {history.map((message, index) => (

          <div
            key={index}
            className={`message ${
              message.role === "user"
                ? "user-message"
                : "orca-message"
            }`}
          >

            <div className="message-avatar">
              {message.role === "user"
                ? "YOU"
                : "O"}
            </div>

            <div className="message-content">

              <span className="message-author">
                {message.role === "user"
                  ? "MISSION INPUT"
                  : "ORCA"}
              </span>

              <p>{message.content}</p>

            </div>

          </div>

        ))}

        {loading && (
          <div className="message orca-message">

            <div className="message-avatar">
              O
            </div>

            <div className="message-content">

              <span className="message-author">
                ORCA
              </span>

              <div className="thinking">
                <span />
                <span />
                <span />
                Processing marine evidence
              </div>

            </div>

          </div>
        )}

      </div>

      <div className="input-container">

        <textarea
          value={input}
          onChange={(event) =>
            setInput(event.target.value)
          }
          onKeyDown={(event) => {

            if (
              event.key === "Enter" &&
              !event.shiftKey
            ) {
              event.preventDefault();
              submit();
            }

          }}
          placeholder="Example: Find a safe fishing zone near Goa tomorrow morning for 5 hours..."
          disabled={loading}
        />

        <button
          className="send-button"
          onClick={submit}
          disabled={loading || !input.trim()}
        >
          <Icon type="send" />

          <span>
            {loading
              ? "Analyzing"
              : "Analyze Mission"}
          </span>
        </button>

      </div>

      <div className="input-hint">
        Enter to analyze · Shift + Enter for new line
      </div>

    </section>
  );
}


/* =========================================================
   MAIN APPLICATION
   ========================================================= */

function App() {

  const [conversationHistory, setConversationHistory] =
    useState([]);

  const [input, setInput] = useState("");

  const [data, setData] = useState(null);

  const [loading, setLoading] = useState(false);

  const [status, setStatus] =
    useState("SYSTEM READY");


  const analyzeMission = async (mission) => {

    if (!mission.trim()) return;

    const userMessage = {
      role: "user",
      content: mission.trim(),
    };

    const updatedHistory = [
      ...conversationHistory,
      userMessage,
    ];

    setConversationHistory(updatedHistory);
    setInput("");
    setLoading(true);
    setStatus("ANALYZING MARINE EVIDENCE");


    try {

      const response = await fetch(
        "/api/analyze",
        {
          method: "POST",

          headers: {
            "Content-Type":
              "application/json",
          },

          body: JSON.stringify({
            mission: mission.trim(),
            conversation_history:
              updatedHistory,
          }),
        }
      );


      const result =
        await response.json();


      if (!response.ok) {
        throw new Error(
          result.error ||
          "Mission analysis failed."
        );
      }


      setData(result);


      setConversationHistory(
        (previous) => [
          ...previous,
          {
            role: "assistant",
            content:
              result.ai_explanation,
          },
        ]
      );


      setStatus("ANALYSIS COMPLETE");

    } catch (error) {

      console.error(error);

      setStatus("ANALYSIS ERROR");

      setConversationHistory(
        (previous) => [
          ...previous,
          {
            role: "assistant",
            content:
              `Unable to complete the analysis: ${error.message}`,
          },
        ]
      );

    } finally {

      setLoading(false);

    }
  };


  return (
    <div className="orca-app">

      {/* Ocean background */}
      <div className="ocean-grid" />
      <div className="ocean-glow glow-one" />
      <div className="ocean-glow glow-two" />

      {/* =================================================
          HEADER
          ================================================= */}

      <header className="topbar">

        <div className="brand">

          <div className="brand-mark">
            <div className="brand-orbit" />
            <span>O</span>
          </div>

          <div>
            <div className="brand-name">
              MARINEX
            </div>

            <div className="brand-subtitle">
              Marine Intelligence Platform
            </div>
          </div>

        </div>


        <div className="system-status">

          <span className="status-dot" />

          <div>
            <strong>
              {status}
            </strong>

            <span>
              Evidence-grounded decision support
            </span>
          </div>

        </div>

      </header>


      {/* =================================================
          HERO
          ================================================= */}

      <section className="hero">

        <div className="hero-content">

          <span className="eyebrow">
            MARINE ECOSYSTEM REASONING
          </span>

          <h1>
            From ocean data
            <br />
            to <span>mission intelligence.</span>
          </h1>

          <p>
            MARINEX coordinates marine evidence, spatial
            constraints and safety conditions to support
            mission-aware decisions.
          </p>

        </div>

        <div className="hero-wave">

          <svg
            viewBox="0 0 800 180"
            preserveAspectRatio="none"
          >
            <path
              d="M0 100 C100 30 180 150 280 90 S460 50 560 100 S700 150 800 70"
              fill="none"
            />

            <path
              d="M0 125 C100 65 180 175 280 115 S460 75 560 125 S700 175 800 95"
              fill="none"
            />
          </svg>

        </div>

      </section>


      {/* =================================================
          MAIN
          ================================================= */}

      <main className="dashboard">

        <ChatPanel
          history={conversationHistory}
          input={input}
          setInput={setInput}
          onSubmit={analyzeMission}
          loading={loading}
        />


        {data && (
          <>

            <MissionUnderstanding
              mission={data.mission}
            />


            <Recommendation
              recommendation={
                data.recommendation
              }
            />


            <EvidenceSection
              evidence={
                data.recommendation?.evidence
              }
            />


            <CandidatePlans
              plans={data.plans}
              recommendation={
                data.recommendation
              }
            />


            {data.recommendation
              ?.rejected_plans
              ?.length > 0 && (

              <RejectedAlternatives
                plans={
                  data.recommendation
                    .rejected_plans
                }
              />

            )}


            <Explanation
              explanation={
                data.ai_explanation
              }
            />


            <MarineMap data={data} />

          </>
        )}

      </main>


      {/* =================================================
          FOOTER
          ================================================= */}

      <footer className="footer">

        <div>
          ORCA · Marine Intelligence
        </div>

        <div>
          PFZ · OCEAN · WEATHER · GIS
        </div>

      </footer>

    </div>
  );
}

export default App;