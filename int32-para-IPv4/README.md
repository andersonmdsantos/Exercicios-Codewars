## Descrição
Pegue o seguinte endereço IPv4: 128.32.10.1

Este endereço tem 4 octetos onde cada octeto é um único byte (ou 8 bits).

1o octeto 128 tem a representação binária: 10000000

2o octeto 32 tem a representação binária: 00100000

3o octeto 10 tem a representação binária: 00001010

4o octeto 1 tem a representação binária: 00000001

Então 128.32.10.1 == 10000000.00100000.00001010.00000001

Como o endereço IP acima tem 32 bits, podemos representá-lo como o número de 32 bits não assinado: 2149583361

Complete a função que pega um número de 32 bits não assinado e retorna uma representação de string de seu endereço IPv4.

## Exemplos (entrada --> saída):
```
2149583361 ==> "128.32.10.1"
32         ==> "0.0.0.32"
0          ==> "0.0.0.0"
```