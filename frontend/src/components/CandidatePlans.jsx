function CandidatePlans({ plans, recommendation }) {
  if (!plans || plans.length === 0) {
    return null;
  }

  return (
    <div className="card">

      <h2>Candidate Plan Comparison</h2>

      <p className="plans-description">
        ORCA evaluates multiple feasible and infeasible zones
        before selecting the final mission recommendation.
      </p>

      <div className="plans-table-container">

        <table className="plans-table">

          <thead>
            <tr>
              <th>Zone</th>
              <th>Score</th>
              <th>Feasibility</th>
              <th>Decision</th>
            </tr>
          </thead>

          <tbody>

            {plans.map((plan) => {

              const isRecommended =
                plan.zone_id === recommendation?.zone_id;

              if (!plan.feasible) {
                return (
                  <tr key={plan.zone_id}>

                    <td>
                      <span className="plan-zone">
                        {plan.zone_id}
                      </span>
                    </td>

                    <td>
                      <span className="plan-score">
                        —
                      </span>
                    </td>

                    <td>
                      <span className="plan-rejected">
                        Rejected
                      </span>
                    </td>

                    <td>
                      <span className="plan-rejected-badge">
                        REJECTED
                      </span>
                    </td>

                  </tr>
                );
              }

              return (
                <tr key={plan.zone_id}>

                  <td>
                    <span className="plan-zone">
                      {plan.zone_id}
                    </span>
                  </td>

                  <td>
                    <span className="plan-score">
                      {plan.score}
                    </span>
                  </td>

                  <td>
                    <span className="plan-feasible">
                      Feasible
                    </span>
                  </td>

                  <td>
                    {isRecommended ? (
                      <span className="plan-recommended">
                        RECOMMENDED
                      </span>
                    ) : (
                      <span className="plan-candidate">
                        CANDIDATE
                      </span>
                    )}
                  </td>

                </tr>
              );
            })}

          </tbody>

        </table>

      </div>

    </div>
  );
}

export default CandidatePlans;