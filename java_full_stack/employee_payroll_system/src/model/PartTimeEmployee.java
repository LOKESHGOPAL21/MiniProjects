package model;

public class PartTimeEmployee extends Employee {
    private double hourlyRate;
    private int hoursWorked;

    public PartTimeEmployee(int id, String name, double hourlyRate, int hoursWorked) {
        super(id, name);
        this.hourlyRate = hourlyRate;
        this.hoursWorked = hoursWorked;
    }

    @Override
    public void calculateSalary() {
        salary = hourlyRate * hoursWorked;
    }

    public double getHourlyRate() { return hourlyRate; }
    public int getHoursWorked() { return hoursWorked; }
}
