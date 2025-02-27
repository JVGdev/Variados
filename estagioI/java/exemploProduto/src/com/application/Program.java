
package com.application;
import java.util.Scanner;
import java.util.Locale;

import com.entities.Product;


public class Program{
	public static void main(String[] args){
		
		Product prod = new Product();
		
		System.out.println("-+- Enter product data -+-");

		Scanner sc = new Scanner(System.in);
		
		System.out.print("Name: ");
		prod.nome = sc.nextLine();
		
		System.out.print("Price: ");
		prod.price = sc.nextDouble();
		
		System.out.print("Quantity in stock: ");
		prod.qnt = sc.nextInt();
		

		System.out.println(prod);
		System.out.println("Enter the number of products to be added to stock: ");
		prod.AddProducts(sc.nextInt());
		
		System.out.println("Enter the number of products to be added to stock: ");
		prod.RemoveProducts(sc.nextInt());
		
		sc.close();
		System.out.println(prod);
		
	}
} 
