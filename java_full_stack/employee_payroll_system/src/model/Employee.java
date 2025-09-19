package model;

public abstract class Employee {
    private int id;
    private String name;
    protected double salary;
    private int leavesTaken = 0;

    public Employee(int id, String name) {
        this.id = id;
        this.name = name;
    }

    public int getId() { return id; }
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
    public void setSalary(double salary) { this.salary = salary; }
    public double getSalary() { return salary; }
    public int getLeavesTaken() { return leavesTaken; }

    public void takeLeave(int days) {
        leavesTaken += days;
    }

    public void generatePayslip() {
        System.out.println("\n--- Payslip ---");
        System.out.println("Employee ID: " + id);
        System.out.println("Name: " + name);
        System.out.println("Leaves Taken: " + leavesTaken);
        System.out.println("Net Salary: " + salary);
        System.out.println("----------------\n");
    }

    public abstract void calculateSalary();

    public void displayDetails() {
        System.out.println("ID: " + id + ", Name: " + name + ", Salary: " + salary);
    }
}
