import React, { useState, useEffect } from "react";
import ExpenseList from "./components/ExpenseList";
import ExpenseForm from "./components/ExpenseForm";
import ExpenseFilter from "./components/ExpenseFilter";
import ExpenseSummary from "./components/ExpenseSummary";

function App() {
  const [expenses, setExpenses] = useState(() => {
    const saved = localStorage.getItem("expenses");
    return saved ? JSON.parse(saved) : [];
  });

  const [filterType, setFilterType] = useState("Day"); 
  const [editingExpense, setEditingExpense] = useState(null);

  useEffect(() => {
    localStorage.setItem("expenses", JSON.stringify(expenses));
  }, [expenses]);

  const addExpenseHandler = (expense) => {
    if (editingExpense) {
      setExpenses((prev) =>
        prev.map((exp) => (exp.id === editingExpense.id ? expense : exp))
      );
      setEditingExpense(null);
    } else {
      setExpenses((prev) => [expense, ...prev]);
    }
  };

  const deleteExpenseHandler = (id) => {
    setExpenses((prev) => prev.filter((exp) => exp.id !== id));
  };

  const editExpenseHandler = (expense) => {
    setEditingExpense(expense);
  };

  // Grouping function
  const groupExpenses = () => {
    const grouped = {};

    expenses.forEach((exp) => {
      const dateObj = new Date(exp.date);

      let key;
      if (filterType === "Day") {
        key = dateObj.toDateString(); // e.g. "Mon Sep 15 2025"
      } else {
        key = `${dateObj.toLocaleString("default", { month: "long" })} ${dateObj.getFullYear()}`; // e.g. "September 2025"
      }

      if (!grouped[key]) {
        grouped[key] = { total: 0, items: [] };
      }
      grouped[key].total += exp.amount;
      grouped[key].items.push(exp);
    });

    return grouped;
  };

  const groupedExpenses = groupExpenses();

  return (
    <div style={{ padding: "20px", maxWidth: "600px", margin: "auto" }}>
      <h1 style={{ textAlign: "center" }}>Expense Tracker</h1>
      <ExpenseForm
        onAddExpense={addExpenseHandler}
        editingExpense={editingExpense}
      />
      <ExpenseFilter selected={filterType} onChangeFilter={setFilterType} />
      <ExpenseSummary grouped={groupedExpenses} />
      <ExpenseList
        grouped={groupedExpenses}
        onDelete={deleteExpenseHandler}
        onEdit={editExpenseHandler}
      />
    </div>
  );
}

export default App;
