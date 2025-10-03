// calculadora.js

// Função que simula uma calculadora básica
function calculadora(n1, n2) {

// Operações aritméticas basicas
    let adicao = n1 + n2;
    let subtracao = n1 - n2;
    let multiplicacao = n1 * n2;
    let divisao = n1 / n2;
    let modulo = n1 % n2;
    let exponencial = n1 ** n2;

// Incremento e Decremento

// Vamos incrementar n1
    let incrementar = n1;
    incrementar++;

// Vamos decrementar n2
    let decrementar = n2;
    decrementar--;

// Exibindo os resultados no console
    console.log(`adiçao: ${n1} + ${n2} = ${adicao}`);
    console.log(`subtração: ${n1} - ${n2} = ${subtracao}`);
    console.log(`multiplicação: ${n1} * ${n2} = ${multiplicacao}`);
    console.log(`divisão: ${n1} / ${n2} = ${divisao}`);
    console.log(`modulo: ${n1} % ${n2} = ${modulo}`);
    console.log(`exponencial: ${n1} ** ${n2} = ${exponencial}`);
    console.log(`incrementar: ${n1}++ = ${incrementar}`);
    console.log(`decrementar: ${n2}-- = ${decrementar}`);
}

// Executando a função calculadora sem parâmetros
//calculadora();
// NaN = Not a Number

// Executando a função calculadora com parâmetros
calculadora(10, 5);