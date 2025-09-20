// Declaração de uma variável chamada resultado e atribuição de uma função anônima a ela

let somarParâmetros = function(parametro1, parametro2) {
    console.log("Parâmetro 1 é: " + parametro1);
    console.log("Parâmetro 2 é: " + parametro2);
    
    let resultado = parametro1 + parametro2;

    console.log("Resultado da soma: " + resultado);
    return resultado;
};

// Chamada de função anônima armazenada na variável somarParâmetros
let resultado =  somarParâmetros(10, 5);
console.log("Resultado da chamada de função somarParametros: " + resultado);

// Definindo uma função que aceita outra função como argumento
function executarFuncao(funcao, valor1, valor2) {
    console.log("\nExecutando a função passada como argumento...");
    return funcao(valor1, valor2);
}

// Passando a função anônima como argumento para a função executarFuncao
let resultadoExecucao = executarFuncao(somarParâmetros, 20, 30);
console.log("Resultado da execução da função passada como argumento: " + resultadoExecucao);

// Definind e chamando uma função anônima imediatamente
let resultadoImediato = (function(a, b){
console.log("\nFunção de chamada imediata: ");
return a*b;
})(4, 6);
console.log("Resultado da função de chamada imediata: " + resultadoImediato);


