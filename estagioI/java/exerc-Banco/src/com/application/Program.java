
package com.application;

import java.util.Scanner;
import java.util.Locale;
import com.entities.Conta;


public class Program{
	
	public static void main(String[] args){
		
		Scanner sc = new Scanner(System.in);
		
		System.out.println("Enter account number: ");
		int number = sc.nextInt();
		sc.nextLine();

		System.out.println("Enter account holder: ");
		String holder = sc.nextLine();

		System.out.println("\nIs there an initial deposit(y/n)?");
		char op = sc.next().charAt(0);
		double money = 0;
		if(op == 'y'){
			System.out.println("\nEnter initial deposit value: ");
			money = sc.nextDouble();
		}

		Conta acc = new Conta(number, holder, money);

		System.out.println("\nAccount data: ");
		System.out.println(acc);

		System.out.println("\nEnter a deposit value: ");
		acc.deposit(sc.nextDouble());
		
		System.out.println("\nUpdated account data: ");
		System.out.println(acc);
	
		System.out.println("\nEnter a withdraw value: ");
		acc.withdraw(sc.nextDouble());
		
		System.out.println("\nUpdated account data:");
		System.out.println(acc);
		


		sc.close();
		

	}
} 
