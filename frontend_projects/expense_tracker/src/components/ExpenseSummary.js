import React from "react";

function ExpenseSummary({ grouped }) {
  const grandTotal = Object.values(grouped).reduce(
    (sum, group) => sum + group.total,
    0
  );

  return (
    <div
      style={{
        marginBottom: "20px",
        padding: "10px",
        backgroundColor: "#f5f5f5",
        borderRadius: "8px",
        textAlign: "center",
      }}
    >
      <h3>Total Expenses: ₹{grandTotal}</h3>
    </div>
  );
}

export default ExpenseSummary;
