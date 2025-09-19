import model.*;
import service.EmployeeManager;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        EmployeeManager manager = new EmployeeManager();
        Scanner sc = new Scanner(System.in);

        while (true) {
            System.out.println("\n--- Employee Payroll System ---");
            System.out.println("1. Add Full-time Employee");
            System.out.println("2. Add Part-time Employee");
            System.out.println("3. List Employees");
            System.out.println("4. Update Employee");
            System.out.println("5. Take Leave");
            System.out.println("6. Generate Payslip");
            System.out.println("7. Delete Employee");
            System.out.println("8. Exit");
            System.out.print("Choose option: ");

            int choice = sc.nextInt();
            sc.nextLine();

            switch (choice) {
                case 1 -> {
                    System.out.print("Enter ID: ");
                    int id = sc.nextInt(); sc.nextLine();
                    System.out.print("Enter Name: ");
                    String name = sc.nextLine();
                    System.out.print("Enter Monthly Salary: ");
                    double monthlySalary = sc.nextDouble();
                    Employee fte = new FullTimeEmployee(id, name, monthlySalary);
                    manager.addEmployee(fte);
                }
                case 2 -> {
                    System.out.print("Enter ID: ");
                    int id = sc.nextInt(); sc.nextLine();
                    System.out.print("Enter Name: ");
                    String name = sc.nextLine();
                    System.out.print("Enter Hourly Rate: ");
                    double rate = sc.nextDouble();
                    System.out.print("Enter Hours Worked: ");
                    int hours = sc.nextInt();
                    Employee pte = new PartTimeEmployee(id, name, rate, hours);
                    manager.addEmployee(pte);
                }
                case 3 -> manager.listEmployees();
                case 4 -> {
                    System.out.print("Enter ID: ");
                    int id = sc.nextInt(); sc.nextLine();
                    System.out.print("Enter New Name: ");
                    String newName = sc.nextLine();
                    System.out.print("Enter New Salary: ");
                    double newSalary = sc.nextDouble();
                    manager.updateEmployee(id, newName, newSalary);
                }
                case 5 -> {
                    System.out.print("Enter ID: ");
                    int id = sc.nextInt();
                    System.out.print("Enter Leave Days: ");
                    int days = sc.nextInt();
                    manager.takeLeave(id, days);
                }
                case 6 -> {
                    System.out.print("Enter ID: ");
                    int id = sc.nextInt();
                    manager.generatePayslip(id);
                }
                case 7 -> {
                    System.out.print("Enter ID: ");
                    int id = sc.nextInt();
                    manager.deleteEmployee(id);
                }
                case 8 -> {
                    System.out.println("Exiting...");
                    return;
                }
                default -> System.out.println("Invalid choice!");
            }
        }
    }
}
