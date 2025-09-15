import React, { useState, useEffect } from "react";

function ExpenseForm({ onAddExpense, editingExpense }) {
  const [title, setTitle] = useState("");
  const [amount, setAmount] = useState("");
  const [date, setDate] = useState("");

  
  useEffect(() => {
    if (editingExpense) {
      setTitle(editingExpense.title);
      setAmount(editingExpense.amount);
      setDate(editingExpense.date);
    }
  }, [editingExpense]);

  const submitHandler = (e) => {
    e.preventDefault();
    if (!title || !amount || !date) return;

    const newExpense = {
      id: editingExpense ? editingExpense.id : Date.now(),
      title,
      amount: +amount,
      date,
    };

    onAddExpense(newExpense);

    setTitle("");
    setAmount("");
    setDate("");
  };

  return (
    <form
      onSubmit={submitHandler}
      style={{
        marginBottom: "20px",
        padding: "15px",
        border: "1px solid #ccc",
        borderRadius: "8px",
      }}
    >
      <h3>{editingExpense ? "Edit Expense" : "Add New Expense"}</h3>
      <div style={{ display: "flex", gap: "10px", marginBottom: "10px" }}>
        <input
          type="text"
          placeholder="Title"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          style={{ flex: 1, padding: "8px" }}
        />
        <input
          type="number"
          placeholder="Amount"
          value={amount}
          onChange={(e) => setAmount(e.target.value)}
          style={{ flex: 1, padding: "8px" }}
        />
        <input
          type="date"
          value={date}
          onChange={(e) => setDate(e.target.value)}
          style={{ flex: 1, padding: "8px" }}
        />
      </div>
      <button type="submit" style={{ padding: "8px 16px", cursor: "pointer" }}>
        {editingExpense ? "Update Expense" : "Add Expense"}
      </button>
    </form>
  );
}

export default ExpenseForm;
