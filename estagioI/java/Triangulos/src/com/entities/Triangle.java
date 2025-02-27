
package com.entities;

public class Triangle{
	
	public double a;
	public double b;
	public double c;
	public double area;

	public void calculaArea(){
		double p = (a + b + c) / 2;
		area = Math.sqrt(p * (p - a) * (p - b) * (p - c));	
	}
} 
