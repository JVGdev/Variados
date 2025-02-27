javali()(

path="./"
package="javali"
actDir=${PWD##*/} #Pegando dir atual
# actDir=${actDir:-/} #Corrigindo para caso de root

criarClass(){
	# $1 = nome; $2 = path

	if ["$actDir" == "com"]; then
		echo " "
	fi

	echo "public class $1{
	/*
		Entre paramêtros e argumentos aqui, meu nobre.
	*/
	public static void main(String[] args){
		// Comece escrevendo aqui.
}
}
	
" >> $2/$1.java
}
	
# Garantir que só possa ser usado de dentro da 'com' ou de um pacote
criarPClass(){
	#$1 = nomeClasse; $2=nomePacote; 
		
	echo "
package ${2/"/"/"."};

public class $1{
	
	public static void main(String[] args){
		// Comece escrevendo aqui.
	}
} " >> $2/$1.java
}



cat << "EOF"	
	      _,-""""-..__
         |`,-'_. `  ` ``  `--'""".
         ;  ,'  | ``  ` `  ` ```  `.
       ,-'   ..-' ` ` `` `  `` `  ` |==.
     ,'    ^    `  `    `` `  ` `.  ;   \
    `}_,-^-   _ .  ` \ `  ` __ `   ;    #
       `"---"' `-`. ` \---""`.`.  `;
                  \\` ;       ; `. `,
                   ||`;      / / | |
                   //_;`    ,_;' ,_;

    --------------------------------------
EOF


while test $# -gt 0; do
	case $1 in
		-h|--help)
			echo " "
			echo "$package - (Padrão) Cria uma classe Java."
      			echo " "
      			echo "$package [Opção] [Argumentos]"
      			echo " "
			echo "Opção:"
			echo "-h, --help	Mostra essa mensagem ;)"
			echo "-f, --folder	Cria um diretório Java para alocar a classe."
			echo "-c, --class	Cria uma classe Java."
      			echo " "
			return
		;;
		-c|--class)
			shift
		
			criarClass $1 ${path}

			echo "-> Classe '$1' criada com sucesso em '${path}' :)"
			echo "____________________"

			shift
		;;
		-f|--folder)
			shift

			mkdir ./$1
			mkdir ./$1/src
			path="./$1/src"
			
			
			echo "-> Diretório Java '$1' foi criado com sucesso ;]"
			echo "...................."
			
			shift
		
		;;
		-p|--package)
			shift 
			
			if [ "$actDir" == "src" ] && [ ! -d "./com/" ]; then
				mkdir com/
			fi

			mkdir com/$1
			criarPClass $2 com/$1
			
			shift
		;;

		*)
			break;

	esac
done		#Fim das flags


echo " "


shift "$(($OPTIND -1))"	
)

