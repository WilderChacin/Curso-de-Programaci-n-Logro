//PARTE 1//

// console.log("PARTE 1: Salida Tecnica");

// // 1
// function invertirNumero(n) {
//     let original = n;
//     let invertido = 0;
//     while (n > 0) {
//         let ultimoDigito = n % 10; 
//         invertido = (invertido * 10) + ultimoDigito; 
//         n = Math.floor(n / 10); 
//     }
//     console.log(`Invertir: Entrada ${original} -> Salida ${invertido}`);
// }

// //2
// function binarioADecimal(nBinario) {
//     let original = nBinario;
//     let decimal = 0;
//     let multiplicador = 1; 

//     while (nBinario > 0) {
//         let digito = nBinario % 10; 
//         decimal = decimal + (digito * multiplicador);
//         multiplicador = multiplicador * 2; 
//         nBinario = Math.floor(nBinario / 10);
//     }
//     console.log(`Binario: ${original} es ${decimal} en decimal`);
// }

// //3
// function raizCuadradaEntera(n) {
//     if (n < 0) return NaN;
//     if (n === 0) return 0;
    
//     let i = 1;
    
//     while (i * i <= n) {
//         i++;
//     }
//     console.log(`Raíz entera de ${n} es: ${i - 1}`);
// }

// // 4
// function factoresPrimos(n) {
//     let original = n;
//     let divisor = 2;
   
//     let resultado = ""; 

//     while (n > 1) {
//         if (n % divisor === 0) {
//             resultado += divisor + " "; 
//             n = n / divisor;
//         } else {
//             divisor++;
//         }
//     }
//     console.log(`Factores primos de ${original}: ${resultado}`);
// }

// // 5
// function sonAmigos(a, b) {
    
    
//     let sumaA = 0;
//     for (let i = 1; i <= a / 2; i++) {
//         if (a % i === 0) sumaA += i;
//     }

//     let sumaB = 0;
//     for (let j = 1; j <= b / 2; j++) {
//         if (b % j === 0) sumaB += j;
//     }

//     let sonAmigos = (sumaA === b && sumaB === a);
//     console.log(`¿Son amigos ${a} y ${b}? -> ${sonAmigos ? "SÍ" : "NO"}`);
// }


// invertirNumero(12345);      
// binarioADecimal(1011);      
// raizCuadradaEntera(20);     
// factoresPrimos(12);         
// sonAmigos(220, 284);        


//PARTE 2//

// console.log("\n Parte 2: Patrones y Bucles");

// // 1
// function diamanteHueco(n) {
//     console.log(`--- Diamante (n=${n}) ---`);
//     if (n % 2 === 0) n++; // Aseguramos que sea impar
//     let centro = Math.floor(n / 2);

//     for (let fila = 0; fila < n; fila++) {
//         let distanciaDelCentro = fila <= centro ? fila : (n - 1) - fila;
        
//         let posIzq = centro - distanciaDelCentro;
//         let posDer = centro + distanciaDelCentro;

//         let linea = "";
//         for (let col = 0; col < n; col++) {
//             if (col === posIzq || col === posDer) {
//                 linea += "*";
//             } else {
//                 linea += " ";
//             }
//         }
//         console.log(linea);
//     }
// }

// // 2
// function relojArena(n) {
//     console.log(`--- Reloj de Arena (n=${n}) ---`);
    
//     if (n % 2 === 0) n++; 
    
//     let centro = Math.floor(n / 2);

//     for (let i = 0; i < n; i++) {
//         let linea = "";
        
//         let espacios = i <= centro ? i : (n - 1) - i;
        
//         let cantidadNumeros = n - (2 * espacios);

//         // 1
//         for (let s = 0; s < espacios; s++) {
//             linea += " ";
//         }

//         // 2
//         for (let num = 0; num < cantidadNumeros; num++) {
            
//             linea += (num % 10); 
//         }

//         console.log(linea);
//     }
// }


// diamanteHueco(7);
// relojArena(7);




//PARTE 3//

console.log("\n=== PARTE 3: Estado y Algoritmos ===");

// 1
function diaDelAnio(dia, mes, anio) {
    
    let esBisiesto = (anio % 4 === 0 && anio % 100 !== 0) || (anio % 400 === 0);
    let totalDias = dia;

    for (let m = 1; m < mes; m++) {
        switch (m) {
            case 1: 
            case 3: 
            case 5:
            case 7: 
            case 8: 
            case 10: 
            case 12: 
                totalDias += 31;
                break;
            case 4: 
            case 6: 
            case 9: 
            case 11: 
                totalDias += 30;
                break;
            case 2: 
                totalDias += esBisiesto ? 29 : 28;
                break;
        }
    }
    console.log(`Fecha ${dia}/${mes}/${anio} -> Día número: ${totalDias}`);
}

// 2
function validarTarjeta(numero) {
    let suma = 0;
    let tempNumero = numero;
    let posicion = 1; 

    while (tempNumero > 0) {
        let digito = tempNumero % 10; 
        
        if (posicion % 2 === 0) {
            digito = digito * 2;
            if (digito > 9) {
                digito = digito - 9;
            }
        }
        
        suma += digito;
        tempNumero = Math.floor(tempNumero / 10); 
        posicion++;
    }

    let esValida = (suma % 10 === 0);
    console.log(`Tarjeta ${numero}: ${esValida ? "VÁLIDA" : "INVÁLIDA"} (Suma: ${suma})`);
}

// 3
function cajeroAutomatico(monto) {
    console.log(`--- Retirando $${monto} ---`);
    let restante = monto;
    

    
    let b100 = Math.floor(restante / 100);
    if (b100 > 0) {
        console.log(`Billetes de 100: ${b100}`);
        restante = restante % 100;
    }

    
    let b50 = Math.floor(restante / 50);
    if (b50 > 0) {
        console.log(`Billetes de 50: ${b50}`);
        restante = restante % 50;
    }

    
    let b20 = Math.floor(restante / 20);
    if (b20 > 0) {
        console.log(`Billetes de 20: ${b20}`);
        restante = restante % 20;
    }

    
    let b10 = Math.floor(restante / 10);
    if (b10 > 0) {
        console.log(`Billetes de 10: ${b10}`);
        restante = restante % 10;
    }

    
    let b5 = Math.floor(restante / 5);
    if (b5 > 0) {
        console.log(`Billetes de 5: ${b5}`);
        restante = restante % 5;
    }

    
    let b1 = restante; 
    if (b1 > 0) {
        console.log(`Monedas de 1: ${b1}`);
    }
}


diaDelAnio(1, 3, 2023);     
diaDelAnio(1, 3, 2024);     


validarTarjeta(12345674); 
cajeroAutomatico(387);      
























