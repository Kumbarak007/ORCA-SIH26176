function EvidenceSection({ evidence }) {
  if (!evidence || evidence.length === 0) {
    return null;
  }

  return (
    <div className="card">

      <h2>Decision Evidence</h2>

      <div id="evidenceList">
        {evidence.map((item, index) => {

          const unit = item.unit
            ? ` ${item.unit}`
            : "";

          return (
            <div
              className="evidence-item"
              key={`${item.source}-${item.variable}-${index}`}
            >

              <div className="evidence-source">
                {item.source}
              </div>

              <div className="evidence-variable">
                {item.variable}
              </div>

              <div className="evidence-value">
                {item.value}
                {unit}
              </div>

              <div className="evidence-confidence">
                Confidence: {item.confidence}
              </div>

            </div>
          );
        })}
      </div>

    </div>
  );
}

export default EvidenceSection;