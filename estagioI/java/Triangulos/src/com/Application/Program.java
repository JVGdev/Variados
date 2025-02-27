
package com.Application;

import java.util.Locale;
import java.util.Scanner;
import com.entities.Triangle;

public class Program{
	/*
		Entre paramêtros e argumentos aqui, meu nobre.
	*/
	public static void main(String[] args){
		
		Locale.setDefault(Locale.US);
		Triangle x, y;
		x = new Triangle();
		y = new Triangle();
		
		Scanner sc = new Scanner(System.in);
		x.a = sc.nextDouble();
		x.b = sc.nextDouble();
		x.c = sc.nextDouble();
		y.a = sc.nextDouble();
		y.b = sc.nextDouble();
		y.c = sc.nextDouble();
		sc.close();

		x.calculaArea();
		y.calculaArea();

		System.out.printf("Triangle 'x' area: %4f%n", x.area);
		System.out.printf("Triangle 'y' area: %4f%n", y.area);
	
		if (x.area > y.area){System.out.println("Larger Area: X");} else {System.out.println("Larger Area: Y");}
	}
} 
