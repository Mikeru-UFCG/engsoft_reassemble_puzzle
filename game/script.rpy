# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define j = Character("Java")

image java neutro = "images/java_sprites/java_neutro.png"
image java encarando = "images/java_sprites/java_stare.png"
image java rindo = "images/java_sprites/java_rindo.png"
image java zangado = "images/java_sprites/java_zangado.png"
image java falando = "images/java_sprites/java_speaks.png"
image java bocejando = "images/java_sprites/java_bocejando.png"
image sala_de_aula = "images/background/sala_de_aula_anime.jpg"

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene sala_de_aula

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show java bocejando

    # These display lines of dialogue.

    j "Ahhhhhhhh... que sono ... (bocejo)"

    show java falando

    j "Opa, você já está aqui?"

    show java neutro

    j "Prazer em conhecê-lo, novato, meu nome é Java, linguagem de programação orientada a objetos."

    show java encarando

    j "Os outros me pediram para te aplicar um pequeno teste, está preparado?"

    show java neutro

    j "Então, vamos começar."

    show java falando

    j "Primeira questão ... "

    show java neutro

    j "Como você escreveria o bubble sort?"

    show java falando

    j "Os parâmetros são: um array de objetos comparáveis do tipo T, e 2 inteiros: ..."

    show java neutro

    j "Um índice esquerdo e um índice direito."

    j "O retorno deve ser vazio."

    show java encarando

    j "E você deve escrever o algoritmo em Java."

    show java rindo

    j "Preparado? Vamos lá, isso é muito fácil!"

    $setup_bs_puzzle()

    call screen bubble_sort_puzzle

    label bubble_sort_complete:

        show java encarando

        j "Muito bom, parece compilável."

        show java falando

        j "Mas ainda falta 2 questões, vamos para a próxima..."

        j "Com os parâmetros e os retornos ditos anteriormente, ..."

        show java neutro

        j "Escreva o algoritmo do insertion sort."
        
        $setup_is_puzzle()

        call screen insertion_sort_puzzle

    label insertion_sort_complete:

        show java neutro

        j "Ótimo, muito bom. Estou testando e não encontro erros."

        show java bocejando

        j "(Ahhhh, quem eu estou tentando enganar, esse código está horrível.)"

        j "(Um return dentro de uma loop for? Fala sério...)"

        j "(Miguel provavelmente reparou aqui só depois de escrever o código dessa demo.)"

        j "(Ahhh, pelo amor de Deus...)"

        j "(Tudo bem, Java, só segue o roteiro, não estrague a experiência do novato.)"

        show java falando

        j "Mas não solte sua caneta, eu ainda tenho mais uma questão para você..."

        show java neutro

        j "Escreva o algoritmo do selection sort."

        show java rindo

        j "Os parametros e o retorno são os mesmos, você vai tirar de letra!"

        $setup_ss_puzzle()

        call screen selection_sort_puzzle

    label selection_sort_complete:
        
        show java bocejando

        j "Hmm........ "

        show java zangado

        j "O que?! Quem?! Onde?! Quando?!"

        show java falando
        
        j "Ah, é você, terminou de escrever?"

        show java neutro

        j "Hmm, muito bom, tambêm passa nos testes."

        show java rindo

        j "Parabéns novato, você realmente tem tudo que precisa para ser um programador."

        show java falando

        j "Está aprovado."

        show java neutro

        j "Agora se você me der licença, irei na cantina reabastecer meu café."

        show java bocejando

        j "Se não tomar uma xícara a cada 5 minutos, eu apago ..."

        show java rindo

        j "Até mais, nos vemos nas aulas!"

    return