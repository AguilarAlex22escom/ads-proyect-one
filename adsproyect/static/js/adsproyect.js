document.addEventListener("DOMContentLoaded", function () {
    Main();
});

async function Main() {
    var div = document.querySelector(".div_botones");

    var btn_avance = document.createElement("BUTTON");
    var btn_conceptos = document.createElement("BUTTON");
    var btn_agregar_empleado = document.createElement("BUTTON");

    // Botón 1
    btn_avance.innerText = "Modificar porcentaje del avance";
    btn_avance.onclick = f1;
    btn_avance.className = "btn_principal";
    div.appendChild(btn_avance);

    // Botón 2
    btn_conceptos.innerText = "Ver el catálogo de conceptos"
    btn_conceptos.onclick = f1;
    btn_conceptos.className = "btn_principal";
    div.appendChild(btn_conceptos);


    // Nuevo elemento en tabla empleados
    // btn_agregar_empleado.innerText = "Agregar empleado";
    // btn_agregar_empleado.onclick = Agregar_Empleado;
    // div.appendChild(btn_agregar_empleado);


    GraficoDinero();
    GraficoMateriales();
    GraficoAvance();
}

async function GraficoDinero() {
    var datos = await ObtenerDatos("gobierno_metadata", undefined, undefined);

    // console.log('datos: ', datos[0]);
    // console.log('Progreso: ', datos[0]['general_progress']);
    // console.log('Presupuesto humano: ', datos[0]['general_budget']);
    // console.log('Presupuesto material: ', datos[0]['material_budget']);


    google.charts.load("current", { packages: ["corechart"] });
    google.charts.setOnLoadCallback(drawChart);
    function drawChart() {
        var data = new google.visualization.DataTable();
        data.addColumn('string', 'Completado');
        data.addColumn('number', 'Porcentaje');

        data.addRows([
            ['Mano de obra', datos[0]['general_budget']],
            ['Material', datos[0]['material_budget']],
        ]);

        var options = {
            title: 'Presupuesto',
            legend: 'none',
        };

        var chart = new google.visualization.PieChart(document.getElementById('presupuesto_chart'));
        chart.draw(data, options);
    }
}

async function GraficoMateriales() {
    var ladrillo = await ObtenerDatos("gobierno_ladrillo", undefined, undefined);
    var mezcla = await ObtenerDatos("gobierno_mezcla", undefined, undefined);
    var cable = await ObtenerDatos("gobierno_cable", undefined, undefined);

    // console.log('ladrillo: ', ladrillo[0]['quantity']);
    // console.log('mezcla: ', mezcla[0]['quantity']);
    // console.log('cable: ', cable[0]['quantity']);

    google.charts.load('current', { 'packages': ['bar'] });
    google.charts.setOnLoadCallback(drawChart);

    function drawChart() {
        var data = google.visualization.arrayToDataTable([
            ['Gobierno', 'Restante', 'Usados'],
            ['Ladrillos', ladrillo[0]['quantity'] - ladrillo[0]['used'], ladrillo[0]['used'],],
            ['Mezcla', mezcla[0]['quantity'] - mezcla[0]['used'], mezcla[0]['used'],],
            ['Cable', cable[0]['quantity'] - cable[0]['used'], cable[0]['used'],],
        ]);
        // var data = google.visualization.arrayToDataTable([
        //     ['', 'Ladrillos', 'Mezcla', 'Cable'],
        //     ['Gobierno', ladrillo[0]['quantity'], mezcla[0]['quantity'], cable[0]['quantity']],
        //     // ['ED1', 110, 60, 25],
        //     // ['ED2', 60, 110, 30],
        //     // ['ED3', 30, 54, 50],
        // ]);

        var options = {
            chart: {
                title: 'Uso de materiales',
                subtitle: 'Tabla comparativa de materiales',
            },
            isStacked: true,
            // colors: ['#d95f02',]
        };

        var chart = new google.charts.Bar(document.getElementById('material_chart'));

        chart.draw(data, options);
    }
}

async function GraficoAvance() {
    var datos = await ObtenerDatos("gobierno_metadata", undefined, undefined);
    console.log('datos: ', datos[0]);
    console.log('aplanado_progress: ', datos[0]['aplanado_progress']);
    console.log('cimentacion_progress: ', datos[0]['cimentacion_progress']);
    console.log('detalles_progress: ', datos[0]['detalles_progress']);
    console.log('electrica_progress: ', datos[0]['electrica_progress']);
    console.log('hidrica_progress: ', datos[0]['hidrica_progress']);
    console.log('mobiliario_progress: ', datos[0]['mobiliario_progress']);
    console.log('general: ', (datos[0]['aplanado_progress'] + datos[0]['cimentacion_progress'] + datos[0]['detalles_progress'] + datos[0]['electrica_progress'] + datos[0]['hidrica_progress'] + datos[0]['mobiliario_progress'])/6);


    google.charts.load('current', { 'packages': ['bar'] });
    google.charts.setOnLoadCallback(drawChart);

    function drawChart() {
        var data = google.visualization.arrayToDataTable([
            ['Genre', 'Aplanado', 'Cimentación','Detalles','Electrica','Hidrica','Mobiliario', 'Restante'],
            
            ['Gobierno', datos[0]['aplanado_progress']/6, datos[0]['cimentacion_progress']/6, datos[0]['detalles_progress']/6, datos[0]['electrica_progress']/6, datos[0]['hidrica_progress']/6, datos[0]['mobiliario_progress']/6, 100-((datos[0]['aplanado_progress'] + datos[0]['cimentacion_progress'] + datos[0]['detalles_progress'] + datos[0]['electrica_progress'] + datos[0]['hidrica_progress'] + datos[0]['mobiliario_progress'])/6)],
        ]);

        var options_fullStacked = {
            isStacked: 'percent',
            height: 300,
            legend: { position: 'top', maxLines: 3 },
            hAxis: {
                minValue: 0,
                ticks: [0, .5, 1]
            }
        };


        var chart = new google.visualization.BarChart(document.getElementById("progreso_chart"));
        chart.draw(data, options_fullStacked);
    }
}

function f1() {
    alert("Función pendiente");
}

function Agregar_Empleado() {
    var tabla_empleados = document.querySelector(".div_tabla_empleados");
    var elemento_nombre = document.createElement("td");
    var elemento_categoria = document.createElement("td");
    elemento_nombre.innerText = "Pedrito";
    elemento_categoria.innerText = "Sola";
    tabla_empleados.appendChild(elemento_nombre);
    tabla_empleados.appendChild(elemento_categoria);
}

async function ObtenerDatos(nombre_dato, tipo, param) {
    //nombre_dato = nombre a búscar dentro de la url
    //tipo = el nombre del parametro a búscar
    //param = el valor del parametro que se quiera búscar
    if (tipo === undefined) {
        tipo = "";
    } else {
        tipo = "&" + tipo;
    }
    if (param === undefined) {
        param = "";
    } else {
        param = "=" + param;
    }
    const url = "/api/v2/" + nombre_dato + "/?limit=999" + tipo + param;
    try {
        const response = await fetch(url);
        if (!response.ok) {
            // throw new Error(`HTTP error! Status: ${response.status}`);
            return response.ok;
        } else {
            const data = await response.json();

            return data['items'];
        }
    } catch (error) {
        var errorMessage = "Ha ocurrido el siguiente error: " + error;
        var errorElement = document.createElement("div");
        errorElement.className = "error-message";
        errorElement.textContent = errorMessage;
        document.body.appendChild(errorElement);
    }
}