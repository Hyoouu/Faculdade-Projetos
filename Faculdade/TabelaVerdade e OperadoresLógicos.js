// Exemplos de operadors lógicos e tabela verdade em JavaScript

// Operador E(&&) lógico
const a = true;
const b = false;

const resultadoE1 =  a && b; // false
const resultadoE2 = a && true; // true

console.log(`true && false = ${resultadoE1}`); // saída: false
console.log(`true && true = ${resultadoE2}`); // saída: true

// Operador OU (||) lógico
const resultadoOU1 = a || b; // true
const resultadoOU2 = a || false; //

console.log(`true || false = ${resultadoOU1}`); // saída: true
console.log(`true || false = ${resultadoOU2}`); // saída: true


// Operador NÃO (!) lógico
const resultadoNao1 = !a; // false
const resultadoNao2 = !b; // true

console.log(`!true = ${resultadoNao1}`); // saída: false
console.log(`!false = ${resultadoNao2}`); // saída: true

// Combinações de operadores lógicos
const resultandoCombinado1 = (a || b) && !b;
const resultandoCombinado2 = !(a && b) || a;

console.log(`(true || false) && !false = ${resultandoCombinado1}`); // saída: true
console.log(`(true && false) || true = ${resultandoCombinado2}`); // saída: true

