function Explanation({ explanation }) {
  if (!explanation) {
    return null;
  }

  return (
    <div className="card">

      <h2>ORCA Decision Explanation</h2>

      <div
        className="explanation-content"
        style={{ whiteSpace: "pre-line" }}
      >
        {explanation}
      </div>

    </div>
  );
}

export default Explanation;