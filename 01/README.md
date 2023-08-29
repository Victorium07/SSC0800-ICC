### Descrição

Neste exercício, verificaremos a conversão de tipos de dados e, também, como buscar comandos de bibliotecas prontas de Python.

Você deve ler uma entrada, que será um valor inteiro.

Em seguida, o inteiro deve ser formatado para um hexadecimal. Verificar a seção "integer representation types" da documentação: https://docs.python.org/3/library/string.html#format-specification-mini-language Sugestão: usar a função "format"

Lembre-se que a função de formatação especificada aceita o tipo inteiro!

Parabéns. Você tem um número hexadecimal. Agora, para converter cada byte dele em um caractere, precisamos transformá-lo em uma cadeia de bytes. Por sorte, Python tem a função "fromhex", do tipo padrão "bytes". A documentação abaixo ensina como utilizá-la https://docs.python.org/3/library/stdtypes.html#bytes.fromhex

Agora, com sua cadeia de bytes, resta transformá-la em uma cadeia de caracteres. Para isso, temos mais uma biblioteca pronta! Com a função decode, da biblioteca codecs, podemos fazer o que desejamos. Verifique a documentação para utilizar esta função: https://docs.python.org/3/library/codecs.html#codecs.Codec.decode

Dois detalhes importantes: 1 - Usaremos a codificação UTF-8, para padronizar nossas saídas. Como usá-las? É só ver a documentação da biblioteca de codecs: https://docs.python.org/3/library/codecs.html#standard-encodings

2 - Quando a função decode encontra valores que não consegue traduzir, por padrão, ela dá erro. Não queremos isso. Portanto, vamos usar o modo de erros como 'replace'. Como fazer isso? Documentação, claro ;) https://docs.python.org/3/library/codecs.html#error-handlers   

Considere o número 1097167471, cujo valor em hexadecimal é 4165726f. Cada byte dele será dado por um grupo de dois caracteres, portanto, aqui teremos os bytes, em hex, dados por 41, 65, 72 e 6f, cujos valores decimais são 65, 101, 114 e 111.

Se observarmos em uma tabela ASCII, notamos que cada valor decimal desses corresponde a um caractere, respectivamente 'A', 'e', 'r' e 'o'. Portanto, temos a cadeia de bytes b'Aero', que, com a codificação UTF-8, origina a string 'Aero'.

Logo, para a entrada 1097167471, espera-se a saída Aero.