
package com.application;
import java.text.ParseException;
import java.util.Scanner;
import java.util.Date;
import java.util.Locale;
import java.util.Vector;
import java.text.SimpleDateFormat;
import com.entities.*;
import com.entities.enums.WorkerLevel;

public class Program{
	
	public static void main(String[] args) throws ParseException {

		Locale.setDefault(Locale.US);		
		Scanner sc = new Scanner(System.in);
		SimpleDateFormat sdf = new SimpleDateFormat("dd/MM/yyyy");
		
		System.out.print("Enter department's name: ");
		Department department = new Department(sc.nextLine());
		
		Worker worker = new Worker();
		worker.setDepartment(department);

		System.out.printf("Enter worker data:\n");
		System.out.printf("Name: ");
		worker.setName(sc.nextLine());
		System.out.printf("Level: ");
		worker.setLevel(WorkerLevel.valueOf(sc.nextLine()));
		System.out.printf("Base Salary: ");
		worker.setBaseSalary(sc.nextDouble());

		System.out.printf("How many contracts to this worker? ");
		int n = sc.nextInt();
		for(int i = 0; i < n; i++){
			
			System.out.printf("Enter contract #%d data:\n", i+1);
			System.out.printf("Date (DD/MM/YY): ");
			Date contractDate = sdf.parse(sc.next());

			System.out.printf("Value Per Hour: ");
			double valuePerHour = sc.nextDouble();

			System.out.printf("Duration (Hours): ");
			int hours = sc.nextInt();

			HourContract contract = new HourContract(contractDate, valuePerHour, hours);
			worker.addContract(contract);
		}

		System.out.printf("\nEnter month and year to calculate income (MM/YYYY): ");
		String monthYear = sc.next();
		int month = Integer.parseInt(monthYear.substring(0, 2));
		int year = Integer.parseInt(monthYear.substring(3));

		System.out.println("Name: " + worker.getName());
		System.out.println("Department: " + worker.getDepartment().getName());

		System.out.println("Income for " + monthYear + ": " + String.format("%2f", worker.income(year, month)));

		sc.close();

	}
} 
