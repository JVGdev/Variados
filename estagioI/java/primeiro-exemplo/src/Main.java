import java.util.Locale; 	// Importando o mano Locale
import java.util.Scanner;	// Importando Scanner

public class Main {
	public static void main(String[] args) {
		int i = 32;
		double d = 10.35787;
		
		Locale.setDefault(new Locale("pt", "BR")); // Localizar o programa, outputs essas coisas. (Precisa imporatar o Locale)
		// Só afeta as linhas depois de ser chamado.

		System.out.println("O famoso Hello World meus manos!" + " AHAHAAHAHAHAHAHAAHAHAH " + i);

		System.out.println("Imprimindo a desgraça de doubles, meus manos.");	
		System.out.println("Normal: " + d);
		System.out.printf("Duas Casas: %.2f%n", d);  // %n == \n
		System.out.printf("Quatro casas: %.4f\n", d); // já arredonda :thumbsup:

		System.out.printf("Uma váriavel está no meio %d dessa frase. Ache o impostor.\n", i);

		//Captando dados meus manos
		
		System.out.print("Iniciando modo de captação de dados... \nDigite um número (Digite com vírgula, pois locale está pt-BR): ");
		
		Scanner sc = new Scanner(System.in);	// Iniciando Scanner

		double digit;
		digit = sc.nextDouble(); // Cacete, ele entende o double dependendo do Locale, se tivesse BR, a vírgula valeria como ponto (BOM SABER)

		System.out.println("Você digitou: " + digit);

		sc.close();	// Fechando o Scanner

	}

}
