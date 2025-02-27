
package com.entities;

public class Conta{

	private int accNum;
	private String nome;
	private double money;

	public Conta(int accNum, String nome, double money){
		this.accNum = accNum;
		this.nome = nome;
		this.money = money;
	}

	public String getName(){
		return nome;
	}

	public void setName(String name){
		this.nome = name;
	}

	public double getMoney(){
		return money;
	}

	public void deposit(double money){
		this.money += money;
	}
	
	public void withdraw(double money){
		this.money -= money + 5;
	}

	public String toString(){
		return "Account " + accNum + ", Holder: " + nome + ", Balance: $ " + money; 
	}	
}
