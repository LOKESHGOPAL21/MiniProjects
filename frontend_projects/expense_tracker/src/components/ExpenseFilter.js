import React from "react";

function ExpenseFilter({ selected, onChangeFilter }) {
  return (
    <div
      style={{
        margin: "20px 0",
        display: "flex",
        justifyContent: "space-between",
        alignItems: "center",
      }}
    >
      <label>Group expenses by: </label>
      <select
        value={selected}
        onChange={(e) => onChangeFilter(e.target.value)}
        style={{ padding: "5px" }}
      >
        <option value="Day">Day</option>
        <option value="Month">Month</option>
      </select>
    </div>
  );
}

export default ExpenseFilter;
