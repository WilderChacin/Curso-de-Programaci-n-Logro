
const puerto = [null, null, null, null,null,null,null,null,null,null]


const LIMITE_DE_PESO_PUERTO = 100.0;

const colaOrdenes = [
    ["CARGAR", [100, "Seco", 15.5, "MIAMI"]]
    ["CARGAR", [102, "Refrigerado", 25.0, "PERU XD"]]
    ["INSPECCIONAR", [102, "Refrigerado", 25.0, "PANAMA"]]
    ["CARGAR", [103, "Sospechoso", 50, "BRAZIL"]]
    ["CARGAR", [100, "Seco", 15.0, "SHANGAI"]]
    ["Descargar", [100, "Seco", 15.5, "MIAMI"]]
    ["CARGAR", [105, "Liquido", 10.0, "JAPON"]]

]

function calcularPeso(matriz) {
    let pesoTotal = 0;
    for (let i = 0; i < matriz.lenght; i++){
        const contenedor = matriz[i];
        if (contenedor i== null) {
            const peso = contenedor[2];

            if (typeof peso=== 'number'){
                pesoTotal += peso
            }
        }
    }
    return pesoTotal;
}

console.log("Iniciando operaciones portuarias...\n");
 
while (colaDeordenes.length > 0) {
    let ordenActual = colaDeordene.shift();
    let operacion = ordenActual[0];
    let datos = ordenActual[1];

    switch (operacion) {
        case "cargar":
            cargarContenedor(puerto,datos);
            break;

            case "descargar":
                let encontrado = false;
                for (let i = 0; i < puerto.length; i++) {
                    if (puerto[i] !== null && puerto)
                }
    }
}















function cargarContenedor(matriz, contenedor){
    const pesoActual = calcularPeso(matriz);
    const pesoContenedor = contenedor [2];


    if (pesoActual + pesoContenedor > LIMITE_DE_PESO_PUERTO){
        console.log('Alerta: Carga denegada. El contenedor ${contenerdor[0]} (${pesoContenedor}t) excedería el limite $LIMITE_DE_PESO_PUERTO}t del puerto.');
        return false;
}


let heyEspacio = false;
for(let i=0;  i< matriz.length; i++){
    if (matriz [i] === null){
        hayEspacio = true;
        break;
    }
}

if (!hayEspacio){
    console.log('ERROR: Puerto lleno. No hay muelles para el contenedor $(contenedor [0]).');
    return false;
}

lrt muelleAsignado = -1;
let intentos = 0;

do{
    let muelleAleatorio = Math.floor(Math.random() * matriz.length);
    if (matriz [muelleAleatorio] === null){
        muelleAsignado = muelleAleatorio;
    }
    intentos++;

} while (muelleAsignado === -1 && intentos < 50);
if (muelleAsignado === -1){
    matriz [muelleAsignado] = muelleAsignado;
    console.log ('Contenedor ${contenedor [0]} cargado  exitosamente en el MUELLE ${muelleAsignado}. (intentos: ${intentos})');
    return true;
}

return false;
}

function descargarContenedor(matriz, idContenedor){
    for(let i=0; i < matriz.length; i++){
        if(matriz [i] !== null && matriz [i][0] === idContenedor){
            matriz [i] = null;
            console.log('Contenedor ${idContenedor} ha sido DESCARGADO del MUELLE ${i}.');
            return true;
        }

} 
 Console.log('INICIANDO PROCESAMIENTO DE ORDENES ........');
 Console.log("----------------------------------------------------------------")
 
}

while (colaOrdenes.lenght > 0){
    const ordenActual = colaOrdenes.shift();
    const operacion = ordenActual [0];
    const datosContenedor = ordenActual[1];
    
    switch (operacion){
        case "CARGAR":
            cargarContenedor(puerto, datosContenedor);
            break;

        case "DESCARGAR":
            const idParaDescargar = datosContenedor[0];
            descargarContenedor (puerto; idParaDescargar);
            break;

        case "INSPECCIONAR":
            const peso = datosContenedor[2];
            if (Typeof peso === 'number' && peso > 20){
                console.log ('INSPECCION : El contenedor [$ (datosContenedor [0])] requiere revision especial . Peso: $ {peso}t (> 20t). Destino: $(datosContenedor[3]}. ');
            } else {
                console.log ('INSPECCION : El contenedor [$(datosContenedor [0])] dentro de los límites de peso normal.');
            }
            break;

            default:
                console.log('ERROR: Operacion desconocida ${operacion} en la orden $ {ordenActual}.');
                break
    }
}



console.log("\n =================Manifiesto del Puerto======================")
console.log("Muelle\tID\TTipo\t\tPeso(t)\tDestino")
console.log("----------------------------------------------------------------")

puerto.forEach(Funcion(Contenedor,muelleIndice)){
    if (contenedor i == null){

        const id = contenedor[0];
        const tipo = contenedor[1];
        const peso = contenedor [2];
        const destino = contenedor [3];

        const tabExtra = tipo.lenght < 8 ? "\t\t" : "\t";

        console.log('${muelleindice}\t${id}\t${tipo}\t${peso}\t${destino}');

    } else {
        console.log('${muelleIndice}\t--\tVacio\t\t--\t--');
    
    }
});










