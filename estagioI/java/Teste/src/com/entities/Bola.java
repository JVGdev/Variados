
package com.entities;

public class Bola{
	
	private int radius;
	private int mass;
	private int value;
	private String nome;
	private boolean eRedondo;
	//

	// -+-+-+-+-+-+- //
	public int getRadius(){
		return radius;
	}
	public void setRadius(int radius){
		this.radius = radius;
	}

	public int getMass(){
		return mass;
	}
	public void setMass(int mass){
		this.mass = mass;
	}

	public int getValue(){
		return value;
	}
	public void setValue(int value){
		this.value = value;
	}

	public String getNome(){
		return nome;
	}
	public void setNome(String nome){
		this.nome = nome;
	}

	public boolean getERedondo(){
		return eRedondo;
	}
	public void setERedondo(boolean eRedondo){
		this.eRedondo = eRedondo;
	}
	// -+-+-+-+-+-+- //

} 
