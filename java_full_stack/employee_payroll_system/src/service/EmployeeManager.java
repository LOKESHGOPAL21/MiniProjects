package service;

import dao.EmployeeDAO;
import model.Employee;

public class EmployeeManager {
    private EmployeeDAO dao = new EmployeeDAO();

    public void addEmployee(Employee emp) {
        emp.calculateSalary();
        dao.addEmployee(emp);
    }

    public void listEmployees() {
        var employees = dao.getAllEmployees();
        if (employees.isEmpty()) {
            System.out.println("No employees in DB.");
            return;
        }
        for (Employee e : employees) {
            e.displayDetails();
        }
    }

    public void updateEmployee(int id, String newName, Double newSalary) {
        dao.updateEmployee(id, newName, newSalary);
    }

    public void takeLeave(int id, int days) {
        Employee emp = dao.getEmployeeById(id);
        if (emp != null) {
            emp.takeLeave(days);
            emp.calculateSalary();
            dao.updateLeaves(id, emp.getLeavesTaken());
            dao.updateSalary(id, emp.getSalary());
            System.out.println(" Leave applied for " + emp.getName() +
                    ", total leaves = " + emp.getLeavesTaken() +
                    ", new salary = " + emp.getSalary());
        } else {
            System.out.println("Employee not found.");
        }
    }

    public void generatePayslip(int id) {
        Employee e = dao.getEmployeeById(id);
        if (e != null) {
            e.generatePayslip();
        } else {
            System.out.println("Employee not found.");
        }
    }

    public void deleteEmployee(int id) {
        dao.deleteEmployee(id);
    }
}
