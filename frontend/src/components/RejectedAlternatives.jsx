function RejectedAlternatives({ rejectedPlans }) {
  if (!rejectedPlans || rejectedPlans.length === 0) {
    return null;
  }

  return (
    <div className="card">

      <h2>Rejected Alternatives</h2>

      <div>
        {rejectedPlans.map((plan) => (
          <div
            key={plan.zone_id}
            className="rejected-item"
          >

            <div className="rejected-zone">
              {plan.zone_id}
            </div>

            <div className="rejection-reasons">
              {plan.rejection_reasons?.map(
                (reason, index) => (
                  <div
                    key={index}
                    className="rejection-reason"
                  >
                    • {reason}
                  </div>
                )
              )}
            </div>

          </div>
        ))}
      </div>

    </div>
  );
}

export default RejectedAlternatives;