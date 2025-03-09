export function colocarError(error) {
    document.getElementById('error').innerHTML = '<p>' + error + '</p>';
    console.log(error)
}

function formatear_numero(cadena) {
    const valor = parseFloat(cadena);
    if (Number.isNaN(valor) || valor == 0) {
        resultado = '';
    } else {
        resultado = new Intl.NumberFormat(navigator.language, {
            minimumFractionDigits: 2,
            maximumFractionDigits: 2,
        }).format(valor);
    }
    return resultado
}

export function generarTabla(registros, columnas, columnas_fmt, elemClasesGasto = null, callback = null) {
    if (!Array.isArray(registros) || registros.length === 0) {
        throw new Error("No hay registros.");
    }
    const tabla = document.createElement("table");
    const thead = document.createElement("thead");
    const tbody = document.createElement("tbody");
    const headers = Object.keys(registros[0]).filter(header => columnas.includes(header));
    const headerRow = document.createElement("tr");
    headers.forEach(header => {
        const th = document.createElement("th");
        th.textContent = header;
        headerRow.appendChild(th);
    });
    thead.appendChild(headerRow);
    tabla.appendChild(thead);
    registros.forEach(item => {
        const row = document.createElement("tr");
        columnas.forEach(columna => {
            const cell = document.createElement("td");
            const isFormatted = columnas_fmt && columnas_fmt.includes(columna);
            cell.textContent = isFormatted ? formatear_numero(item[columna]) : item[columna];
            cell.className = isFormatted ? 'valor-numerico' : 'valor';
            row.appendChild(cell);
        });
        if (callback && elemClasesGasto) {
            callback(elemClasesGasto, row, item, row);
        }
        tbody.appendChild(row);
    });
    tabla.appendChild(tbody);
    return tabla;
}

export function getCookie(name) {
    var value = "; " + document.cookie;
    var parts = value.split("; " + name + "=");
    if (parts.length == 2) return parts.pop().split(";").shift();
}

export function manejarError(error) {
    console.error('Error en la generación de tabla:', error);
    colocarError(error || Error('Error desconocido'));
}

export function procesarEvento(e, formData, accion, generadorRespuesta) {
    console.log(accion);
    e.preventDefault();
    colocarError("")
    fetch(accion, {
        method: 'POST',
        body: formData,
        headers: { 'X-Requested-With': 'XMLHttpRequest', }
    })
        .then(response => {
            if (!response.ok) {
                throw new Error(`Error en la solicitud: ${response.status} ${response.statusText}`);
            }
            return response.json();
        })
        .then(responseData => {
            if (responseData.errores) {
                throw Error('Errores: ' + responseData.errores);
            }
            return responseData.registros;
        })
        .then(registros => {
            if (!registros || (Array.isArray(registros) && registros.length === 0)) {
                throw new Error("No se obtuvo datos de consulta.");
            }
            if (typeof registros === 'string') {
                registros = JSON.parse(registros);
            }
            return registros;
        })
        .then(registros => {
            generadorRespuesta(registros)
                .then(resultado => {
                    document.getElementById('resultado').innerHTML = '';
                    document.getElementById('resultado').appendChild(resultado)
                })
                .catch(error => manejarError(error));
        })
        .catch(manejarError);
    return false;
}