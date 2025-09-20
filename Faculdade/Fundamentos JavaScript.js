// Exemplo de uso de var, let e const em JS

const externo = "Olá, eu sou uma constante global!";

// Declaração de variável usando var

function exemploVar() {
    if(true) {
        var mensagem = "Olá, sou uma var!";
    }
    console.log(mensagem);
}

// Chamando a função exemploVar
exemploVar();

// Exemplo de erro e correção

var mensagem1 = "Olá, sou uma var! Escopo externo!";
console.log(mensagem1);

//Declaração de uma variável usando let

function exemploLet() {
    if(true) {
        let mensagem = "Oi, eu sou uma Let!";
        console.log(mensagem)
    }
    //console.log(mensagem)
}

// Chamando a função exemploLet
exemploLet();

// Exemplo de erro e correção
let mensagem = "Oi, eu sou um Let Externo!";
console.log(mensagem);
// o erro se dá por conta que na linha 19 também há uma variável com o mesmo nome desta let, sendo assim, a solução é mudar o nome de uma das duas

// Declaração de uma constante usando const
function exemploConstante() {
    const mensagem = "Oi, eu sou uma Constante!";
    console.log(mensagem);
}

// Chamando a função exemploConstante
exemploConstante();

// Exemplo externo de const
console.log(externo);

// Exemplo externo tentar alterar a constante global
externo = "Nova Mensagem!";
// O erro ocorre porque estamos tentando alterar o valor de uma constante, o que não é permitido em JavaScript.
