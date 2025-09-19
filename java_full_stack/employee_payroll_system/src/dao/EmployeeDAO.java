package dao;

import db.DBConnection;
import model.*;

import java.sql.*;
import java.util.ArrayList;

public class EmployeeDAO {

    // Add employee
    public void addEmployee(Employee emp) {
        String sql = "INSERT INTO employees (id, name, type, salary, leavesTaken, hourlyRate, hoursWorked, monthlySalary) VALUES (?, ?, ?, ?, ?, ?, ?, ?)";
        try (Connection conn = DBConnection.getConnection();
             PreparedStatement stmt = conn.prepareStatement(sql)) {

            stmt.setInt(1, emp.getId());
            stmt.setString(2, emp.getName());

            if (emp instanceof FullTimeEmployee) {
                FullTimeEmployee fte = (FullTimeEmployee) emp;
                stmt.setString(3, "FullTime");
                stmt.setDouble(4, emp.getSalary());
                stmt.setInt(5, emp.getLeavesTaken());
                stmt.setNull(6, Types.DOUBLE);
                stmt.setNull(7, Types.INTEGER);
                stmt.setDouble(8, fte.getMonthlySalary());
            } else if (emp instanceof PartTimeEmployee) {
                PartTimeEmployee pte = (PartTimeEmployee) emp;
                stmt.setString(3, "PartTime");
                stmt.setDouble(4, emp.getSalary());
                stmt.setInt(5, emp.getLeavesTaken());
                stmt.setDouble(6, pte.getHourlyRate());
                stmt.setInt(7, pte.getHoursWorked());
                stmt.setNull(8, Types.DOUBLE);
            }

            stmt.executeUpdate();
            System.out.println(" Employee added to DB!");

        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    // Fetch all employees
    public ArrayList<Employee> getAllEmployees() {
        ArrayList<Employee> employees = new ArrayList<>();
        String sql = "SELECT * FROM employees";

        try (Connection conn = DBConnection.getConnection();
             Statement stmt = conn.createStatement();
             ResultSet rs = stmt.executeQuery(sql)) {

            while (rs.next()) {
                int id = rs.getInt("id");
                String name = rs.getString("name");
                String type = rs.getString("type");
                double salary = rs.getDouble("salary");
                int leaves = rs.getInt("leavesTaken");

                if ("FullTime".equalsIgnoreCase(type)) {
                    double monthlySalary = rs.getDouble("monthlySalary");
                    FullTimeEmployee fte = new FullTimeEmployee(id, name, monthlySalary);
                    fte.setSalary(salary);
                    for (int i = 0; i < leaves; i++) fte.takeLeave(1);
                    employees.add(fte);
                } else {
                    double hourlyRate = rs.getDouble("hourlyRate");
                    int hoursWorked = rs.getInt("hoursWorked");
                    PartTimeEmployee pte = new PartTimeEmployee(id, name, hourlyRate, hoursWorked);
                    pte.setSalary(salary);
                    for (int i = 0; i < leaves; i++) pte.takeLeave(1);
                    employees.add(pte);
                }
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return employees;
    }

    // Get employee by ID
    public Employee getEmployeeById(int id) {
        String sql = "SELECT * FROM employees WHERE id = ?";
        try (Connection conn = DBConnection.getConnection();
             PreparedStatement stmt = conn.prepareStatement(sql)) {

            stmt.setInt(1, id);
            ResultSet rs = stmt.executeQuery();

            if (rs.next()) {
                String name = rs.getString("name");
                String type = rs.getString("type");
                double salary = rs.getDouble("salary");
                int leaves = rs.getInt("leavesTaken");

                if ("FullTime".equalsIgnoreCase(type)) {
                    double monthlySalary = rs.getDouble("monthlySalary");
                    FullTimeEmployee fte = new FullTimeEmployee(id, name, monthlySalary);
                    fte.setSalary(salary);
                    for (int i = 0; i < leaves; i++) fte.takeLeave(1);
                    return fte;
                } else {
                    double hourlyRate = rs.getDouble("hourlyRate");
                    int hoursWorked = rs.getInt("hoursWorked");
                    PartTimeEmployee pte = new PartTimeEmployee(id, name, hourlyRate, hoursWorked);
                    pte.setSalary(salary);
                    for (int i = 0; i < leaves; i++) pte.takeLeave(1);
                    return pte;
                }
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return null;
    }

    // Update leaves
    public void updateLeaves(int id, int leavesTaken) {
        String sql = "UPDATE employees SET leavesTaken = ? WHERE id = ?";
        try (Connection conn = DBConnection.getConnection();
             PreparedStatement stmt = conn.prepareStatement(sql)) {

            stmt.setInt(1, leavesTaken);
            stmt.setInt(2, id);
            stmt.executeUpdate();

        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    // Update salary
    public void updateSalary(int id, double salary) {
        String sql = "UPDATE employees SET salary = ? WHERE id = ?";
        try (Connection conn = DBConnection.getConnection();
             PreparedStatement stmt = conn.prepareStatement(sql)) {

            stmt.setDouble(1, salary);
            stmt.setInt(2, id);
            stmt.executeUpdate();

        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    // Update employee name/salary manually
    public void updateEmployee(int id, String newName, Double newSalary) {
        String sql = "UPDATE employees SET name = ?, salary = ? WHERE id = ?";
        try (Connection conn = DBConnection.getConnection();
             PreparedStatement stmt = conn.prepareStatement(sql)) {

            stmt.setString(1, newName);
            stmt.setDouble(2, newSalary);
            stmt.setInt(3, id);
            stmt.executeUpdate();

        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    // Delete employee
    public void deleteEmployee(int id) {
        String sql = "DELETE FROM employees WHERE id = ?";
        try (Connection conn = DBConnection.getConnection();
             PreparedStatement stmt = conn.prepareStatement(sql)) {

            stmt.setInt(1, id);
            stmt.executeUpdate();

        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
}
