escreva "Calculadora do terminal - Facilitation"

variavel bool codigo_ja_rodou = Falso #(pode ser Verdadeiro ou True ou 1 e Falso ou False ou 0)

entrada texto nome "Qual é seu nome? "

repita 3 vezes{
    escreva "Facilitation é legal"
}
escreva "Digite o primeiro número: "
entrada quebrada numero1

escreva "Digite o segundo número: "
entrada quebrada numero2

escreva  "Escolha a operação: +, -, *, /"
entrada operacao

se operacao for "+"{
    resultado = numero1 + numero2}
senão operacao for "-"{
    resultado = numero1 - numero2}
senão operacao for "*"{
    resultado = numero1 * numero2}
senão operacao for "/"{
    se numero2 for == 0
        escreva "Erro: divisão por zero!"
        pare
    resultado = numero1 / numero2}

senão{
    escreva "Operação inválida."
    pare}
escreva "O resultado é: " + resultado
codigo_ja_rodou = Verdadeiro