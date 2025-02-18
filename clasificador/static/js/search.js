function actualizarClaseGasto(valor, id) {
    console.log('ID:', id);
    fetch('/app/gasto/id/' + id + '/', {
        method: 'PATCH',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken'),
            'X-Requested-With': 'XMLHttpRequest'
        },
        body: JSON.stringify({ 'idclase': valor })
    })
        .then(response => {
            if (response.status !== 200) {
                throw Error('Error en la respuesta: ' + response.status);
            }
            return response;
        })
        .then(response => {
            console.log(response);
            return response.json()
        })
        .then(responseData => {
            if (responseData.error) {
                throw Error('Errores: ' + responseData.error);
            }
            if (responseData.message) {
                console.log('Mensaje:', responseData.message);
            }
        })
        .catch(manejarError);
}

function colocarError(error) {
    document.getElementById('error').innerHTML = '<p>' + error + '</p>';
    console.log(error)
}

function crearElementoSelect(dataClases) {
    try {
        const selectElement = document.createElement('select');
        dataClases.forEach((item, index) => {
            const optionElement = document.createElement('option');
            optionElement.value = item.id;
            optionElement.textContent = item.nombre;
            selectElement.appendChild(optionElement);
        });
        return selectElement;
    } catch (error) {
        manejarError(error);
    }
}

function generarRespuesta(registros) {
    return obtenerClasesDeGasto()
        .then(clasesGasto => crearElementoSelect(clasesGasto))
        .then((elemClasesGasto) => { return generarTabla(registros, elemClasesGasto) })
        .catch((error) => {
            return manejarError(error);
        });
}

function generarTabla(registros, elemClasesGasto) {
    if (Array.isArray(registros) && registros.length === 0) {
        throw Error("No hay registros.");
    }
    const headerRow = document.createElement("tr");
    const headers = Object.keys(registros[0]);
    const tabla = document.createElement("table");
    const thead = document.createElement("thead");
    headers.forEach(header => {
        const th = document.createElement("th");
        th.textContent = header.charAt(0).toUpperCase() + header.slice(1);
        headerRow.appendChild(th);
    });
    thead.appendChild(headerRow);
    tabla.appendChild(thead);
    const tbody = document.createElement("tbody");
    registros.forEach(item => {
        const row = document.createElement('tr');
        Object.values(item).forEach(value => {
            const cell = document.createElement('td');
            cell.textContent = value;
            row.appendChild(cell);
        });
        const cellClases = document.createElement('td');
        const selectElement = elemClasesGasto.cloneNode(true);
        selectElement.value = item.idclase;
        selectElement.addEventListener('change', function (event) {
            actualizarClaseGasto(event.target.value, item.id);
            console.log('Nuevo valor seleccionado:', event.target.value);
        });
        cellClases.appendChild(selectElement);
        row.appendChild(cellClases);
        tbody.appendChild(row);
    });
    tabla.appendChild(tbody);
    return tabla
}

function getCookie(name) {
    var value = "; " + document.cookie;
    var parts = value.split("; " + name + "=");
    if (parts.length == 2) return parts.pop().split(";").shift();
}

function manejarError(error) {
    console.error('Error en la generación de tabla:', error);
    colocarError(error || Error('Error desconocido'));
}

async function obtenerClasesDeGasto() {
    const metaHeader = document.getElementById('ubicacion-script');
    const clasesUrl = metaHeader.getAttribute('content');
    try {
        const response = await fetch(clasesUrl, { headers: { 'X-Requested-With': 'XMLHttpRequest', } });
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        const dataClases = await response.json();
        if (!dataClases) {
            throw (new Error('No se proporcionó respuesta para el select'));
        }
        if (!dataClases.registros) {
            throw (new Error('No se proporcionó registros para el select'));
        }
        if (!Array.isArray(dataClases.registros)) {
            throw (new Error('Los datos proporcionados no son un arreglo válido'));
        }
        if (dataClases.registros.length === 0) {
            throw (new Error('El arreglo de datos está vacío'));
        }
        return dataClases.registros;
    } catch (error) {
        manejarError(error);
        throw error;
    }
}

document.getElementById('search-form').addEventListener('submit', function (e) {
    e.preventDefault();
    const formData = new FormData(this);
    colocarError("")
    fetch(this.action, {
        method: 'POST',
        body: formData,
        headers: { 'X-Requested-With': 'XMLHttpRequest', }
    })
        .then(response => response.json())
        .then(responseData => {
            if (responseData.errores) {
                throw Error('Errores: ' + responseData.errores);
            }
            return responseData;
        })
        .then(responseData => {
            if (typeof responseData.registros === 'string') {
                registros = JSON.parse(responseData.registros);
            } else {
                registros = responseData.registros;
            }
            if (Array.isArray(registros) && registros.length === 0) {
                throw Error("No se obtuvo datos de consulta.");
            }
            return registros;
        })
        .then(registros => {
            generarRespuesta(registros)
                .then(resultado => document.getElementById('resultado').appendChild(resultado))
                .catch(error => manejarError(error));
        })
        .catch(manejarError);
});
