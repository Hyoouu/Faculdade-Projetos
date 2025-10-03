// Arrow Functions


// Exemplo básico de uma arrow function que soma dois números
let somar = (a, b) => {
    return a + b;
};

// Chamada da arrow function somar
console.log("Resultado da soma usando arrow function: " + somar(10, 5));

// Exemplo de arrow function com um único parâmetro (não precisa de parênteses)
let dobrar = n => n * 2;

// Chamando a função dobrar e exibindo o resultado
console.log("Resultado de dobrar usando arrow function: " + dobrar(7));


// Exemplo de uma arrow function usada como callback

let numeros = [1, 2, 3, 4, 5];


// Usando arrow function com o método map para dobrar os valores do array
let numerosDobrados = numeros.map( n => n*2 );

// Exibindo o array resultante no console
console.log("Números dobrados usando função arrow com map: " + numerosDobrados);

// Arrow function com corpo de função mais complexo
let saudacao = (nome, idade) => {
    let mensagem = `olá, meu nome é ${nome} e eu tenho ${idade} anos.`;
    return mensagem;
};

// Chamando a função e exibindo o resultado no console
console.log(saudacao("Gustavo", 39));
