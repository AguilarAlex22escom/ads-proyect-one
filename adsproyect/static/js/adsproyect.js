document.addEventListener("DOMContentLoaded", (event) => {
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
    btn_agregar_empleado.innerText = "Agregar empleado";
    btn_agregar_empleado.onclick = Agregar_Empleado;
    div.appendChild(btn_agregar_empleado);


    GraficoDinero();
    GraficoMateriales();
}

function GraficoDinero() {
    google.charts.load("current", { packages: ["corechart"] });
    google.charts.setOnLoadCallback(drawChart);
    function drawChart() {
        var data = new google.visualization.DataTable();
        data.addColumn('string', 'Completado');
        data.addColumn('number', 'Porcentaje');

        data.addRows([
            ['Material', 30],
            ['Material', 50],
        ]);

        var options = {
            title: 'Presupuesto',
            legend: 'none',
        };

        var chart = new google.visualization.PieChart(document.getElementById('progress_chart'));
        chart.draw(data, options);
    }
}

function GraficoMateriales() {
    google.charts.load('current', { 'packages': ['bar'] });
    google.charts.setOnLoadCallback(drawChart);

    function drawChart() {
        var data = google.visualization.arrayToDataTable([
            ['', 'Ladrillos', 'Mezcla', 'Cable'],
            ['Gobierno', 1000, 400, 200],
            ['ED1', 1170, 460, 250],
            ['ED2', 660, 1120, 300],
            ['ED3', 1030, 540, 350]
        ]);

        var options = {
            chart: {
                title: 'Uso de materiales',
                subtitle: 'Tabla comparativa de materiales',
            }
        };

        var chart = new google.charts.Bar(document.getElementById('material_chart'));

        chart.draw(data, google.charts.Bar.convertOptions(options));
    }
}

function f1() {
    alert("Función pendiente");
}

function Agregar_Empleado(){
    var tabla_empleados = document.querySelector(".div_tabla_empleados");
    var elemento_nombre = document.createElement("td");
    var elemento_categoria = document.createElement("td");
    elemento_nombre.innerText = "Pedrito";
    elemento_categoria.innerText = "Sola";
    tabla_empleados.appendChild(elemento_nombre);
    tabla_empleados.appendChild(elemento_categoria);
}