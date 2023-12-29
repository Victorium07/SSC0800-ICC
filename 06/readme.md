[Bônus - POO] Rinha de Pokémon - Vale 1.0 extra na média

Descrição
Você, um jovem treinador em busca de tornar-se um mestre Pokémon, que, por um acaso, também é um bom programador, teve uma ideia para acelerar a sua jornada: criar um simulador de batalhas Pokémon! bulba Por sorte, parte do código para esta jornada já foi feita pelo prof. ~~Carvalho~~ Leonardo, e está disponibilizado junto deste exercício.

Sua missão será modificar o código, que já contém os dados do Charmander e Squirtle, dos tipos fogo e água, respectivamente, para adicionar também dados do Bulbassauro (do tipo grama), e o Pikachu (elétrico). Além disso, você vai precisar ler o nome do Pokémon que irá batalhar antes de chamar a função read_pokemon_data() , e alterar a função main() para criar adequadamente um objeto da classe do Pokémon desejado.

Sugestão: criar uma função que cria os Pokémon, e chamá-la em um laço de repetição para os 2 Pokémon. Adicionar cada retorno da função a uma lista de objetos de Pokémon, e aí passar cada um dos 2 para a função de combate.

Para adicionar o Pikachu, é preciso adicionar o tipo 'ELECTRIC' na classe de Enumeração já presente no código:
class Types(IntEnum):
    FIRE = 0
    WATER = 1
    GRASS = 2
    NORMAL = 3

Lembre-se de escrever exatamente 'ELECTRIC' para o novo dado enumerado, ou as saídas estarão erradas. Não importa o número atribuído.

O tipo grama tem vantagem sobre água (ou seja, dobra o dano), mas é pouco efetivo contra fogo e grama (ou seja, reduz o dano pela metade).

Já o tipo elétrico tem vantagem sobre água, é neutro contra fogo, e é pouco efetivo contra grama e elétrico.

Os ataques de grama, fogo, e água são neutros contra Pokémon do tipo elétrico.

Além disso, tanto para o Bulbassauro quanto para o Pikachu será preciso extender (herdar) da classe Pokémon e modificar os dados de nome, tipo, e a função de receber dano (take_damage()).

Os Pokémon novos
Caso você não conheça, este é o Bulbassauro, que deverá ser adicionado com o nome Bulbasaur, e é do tipo grama (representado no enum pelo tipo GRASS):

Já este é o Pikachu, que deverá ser adicionado com o nome Pikachu, e é do tipo elétrico (representado no enum pelo tipo ELECTRIC):

Detalhes de implementação
A função main atual contém esta implementação:

level, hp, attack, defense = read_pokemon_data()
charmander = Charmander(level, hp, attack, defense)
level, hp, attack, defense = read_pokemon_data()
squirtle = Squirtle(level, hp, attack, defense)
start_battle(charmander, squirtle)
Nela, não existe verificação alguma sobre qual a espécie (classe) de Pokémon que queremos criar. Um dos desafios deste exercício é alterar a função read_pokemon_data() para receber, antes dos atributos, o nome do Pokémon. Então, deve-se fazer uma verificação condicional, a partir do nome lido, para definir de qual classe será o objeto Pokémon criado. Para verificar qual Pokémon será instanciado, use o método estático get_name() já presente no código.

Lembre-se que tanto o Pikachu quanto o Bulbassauro serão criados a partir de novas classes, ambas que herdam da classe mãe Pokemon. Assim, através da propriedade de polimorfismo, não importa qual a classe do Pokémon passado para a função start_battle(), a batalha ocorrerá normalmente.

Atente-se apenas a atribuir corretamente os valores adequados dos atributos (protegidos) de classe _name e _main_type de cada uma destas novas classes, e alterar a função take_damage() para considerar as novas fraquezas e vantagens de tipo.

Lembre-se: a vida é um inteiro. Logo, se o dano for reduzido pela metade, arredonde para um inteiro!

Entrada e Saída
A entrada consistirá de dois Pokémon. Cada Pokémon terá primeiro o seu nome fornecido, em uma linha e, na linha seguinte, todos os seus outros dados, separados por espaço. Assim, pode-se continuar utilizando a função de leitura de entrada já presente no código fornecido. Deve-se, apenas, adicionar a leitura de uma linha anterior aos dados, que conterá seu nome. Todos os nomes de Pokémon serão dados com a primeira letra maiúscula, assim como sua definição nas classes. Exemplo de uma entrada, em que um Bulbassauro e um Pikachu batalharão entre si:

Bulbasaur
1 10 5 3
Pikachu
2 12 6 4
Após a entrada ser lida e os Pokémon serem instanciados corretamente através de suas respectivas classes, 1 único turno de combate ocorrerá, com a função start_battle() sendo chamada.

A saída do código será a mesma já contida nas classes existentes. O polimorfismo e a herança farão a "mágica" de imprimir tudo sem necessitar alterações. Logo, a saída para o caso anterior seria:

Bulbasaur attacks with a 5 power GRASS move!
Pikachu took 1 damage!
Pikachu now has 11 hp left.
Pikachu attacks with a 6 power ELECTRIC move!
Bulbasaur took 1 damage!
Bulbasaur now has 9 hp left.