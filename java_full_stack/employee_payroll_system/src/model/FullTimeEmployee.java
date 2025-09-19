package model;

public class FullTimeEmployee extends Employee {
    private double monthlySalary;

    public FullTimeEmployee(int id, String name, double monthlySalary) {
        super(id, name);
        this.monthlySalary = monthlySalary;
    }

    @Override
    public void calculateSalary() {
        double dailyRate = monthlySalary / 30;
        salary = monthlySalary - (getLeavesTaken() * dailyRate);
    }

    public double getMonthlySalary() { return monthlySalary; }
}
