
package com.entities;
import java.util.List;
import java.util.Calendar;
import com.entities.enums.*;
import java.util.ArrayList;

public class Worker{
	private String name;
	private WorkerLevel level;
	private double baseSalary;
	private List<HourContract> contracts = new ArrayList<>();
	private Department department;

	public Worker(){
	}

	public Worker(String name, WorkerLevel level, double baseSalary){
		this.name = name;
		this.level = level;
		this.baseSalary = baseSalary;
	}		
		
	/* - - - - - - */
	public void setName(String name){
		this.name = name;
	}
	public String getName(){
		return name;
	}
	
	public void setLevel(WorkerLevel level){
		this.level = level;
	}
	public WorkerLevel getLevel(){
		return level;
	}

	public void setBaseSalary(double baseSalary){
		this.baseSalary = baseSalary;
	}
	public double getBaseSalary(){
		return baseSalary;
	}
	
	public void setDepartment(Department department){
		this.department = department;
	}
	public Department getDepartment(){
		return department;
	}
	/* - - - - - */

	public List<HourContract> getContracts(){
		return contracts;
	}

	public void addContract(HourContract contract){
		this.contracts.add(contract);
	}

	public Boolean removeContract(HourContract contract){
		return contracts.remove(contract);
	}

	public double income(int year, int month){
		double sum = baseSalary;
		Calendar cal = Calendar.getInstance();
		for(HourContract c: contracts){
			cal.setTime(c.getDate());
			int c_year = cal.get(Calendar.YEAR);
			int c_month = 1 + cal.get(Calendar.MONTH);
			if(c_year == year && c_month == month){
				sum += c.totalValue();
			}
		}
		return sum;
	}

} 
