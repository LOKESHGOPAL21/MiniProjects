import React from "react";
import ExpenseItem from "./ExpenseItem";

function ExpenseList({ grouped, onDelete, onEdit }) {
  const groups = Object.keys(grouped);

  if (groups.length === 0) {
    return <p style={{ textAlign: "center" }}>No expenses found.</p>;
  }

  return (
    <div>
      {groups.map((group) => (
        <div
          key={group}
          style={{
            marginBottom: "20px",
            border: "1px solid #ddd",
            borderRadius: "8px",
            padding: "10px",
          }}
        >
          <h3 style={{ marginBottom: "10px" }}>
            {group} — Total: ₹{grouped[group].total}
          </h3>
          {grouped[group].items.map((expense) => (
            <ExpenseItem
              key={expense.id}
              title={expense.title}
              amount={expense.amount}
              date={expense.date}
              onDelete={() => onDelete(expense.id)}
              onEdit={() => onEdit(expense)}
            />
          ))}
        </div>
      ))}
    </div>
  );
}

export default ExpenseList;
