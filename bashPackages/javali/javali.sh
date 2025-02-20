javali()(
	criarClass(){
	# $1 = nome; $2 = path

		echo "public class $1{
	/*
		Entre paramêtros e argumentos aqui, meu nobre.
	*/
	public static void main(String[] args){
		// Comece escrevendo aqui.
	}
}
" 			>> $2/$1.java
	}

path="./"
package="javali"

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

--------------------"
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
      			echo " "
			return
		;;
		-c|--class)
			shift
		
			main="$1"
			echo "Nome da classe definida como ${main};"

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
		*)
			break;

	esac
done		#Fim das flags


criarClass $1 ${path}

echo "-> Classe '$1' criada com sucesso em '${path}' :)"
echo "____________________"
echo " "


shift "$(($OPTIND -1))"	
)

