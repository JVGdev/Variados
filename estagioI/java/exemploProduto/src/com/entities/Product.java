
package com.entities;

public class Product {
	
	public String nome;
	public double price;
	public int qnt;

	public double TotalValueInStock(){
		return price * qnt;
	}
	
	public void AddProducts(int n){	
		qnt += n; 
	}

	public void RemoveProducts(int n){
		qnt -= n;
	}

	public String toString(){
		double total = TotalValueInStock();
		return "Produto: " + nome + "; Preço: " + String.format("%2f", price) + "; Unidades: " + qnt + "; Preço total: " + String.format("%2f", total) + ".";
	}
} 

