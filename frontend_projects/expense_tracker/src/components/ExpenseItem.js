import React from "react";

function ExpenseItem({ title, amount, date, onDelete, onEdit }) {
  return (
    <div
      style={{
        margin: "8px 0",
        padding: "10px",
        border: "1px solid #ccc",
        borderRadius: "8px",
        display: "flex",
        justifyContent: "space-between",
        alignItems: "center",
      }}
    >
      <div>
        <h4>{title}</h4>
        <small>{new Date(date).toDateString()}</small>
      </div>
      <div style={{ display: "flex", alignItems: "center", gap: "10px" }}>
        <div style={{ fontWeight: "bold", fontSize: "18px" }}>₹{amount}</div>
        <button
          onClick={onEdit}
          style={{ padding: "5px 10px", cursor: "pointer" }}
        >
          Edit
        </button>
        <button
          onClick={onDelete}
          style={{
            padding: "5px 10px",
            cursor: "pointer",
            backgroundColor: "red",
            color: "white",
            border: "none",
          }}
        >
          Delete
        </button>
      </div>
    </div>
  );
}

export default ExpenseItem;
