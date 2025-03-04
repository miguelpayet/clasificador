import { generarTabla, getCookie, manejarError, procesarEvento } from './crear_tabla.js';

function actualizarClaseGasto(valor, id) {
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

function crearDropDownClases(elemClasesGasto, event, item, row) {
    const cellClases = document.createElement('td');
    const selectElement = elemClasesGasto.cloneNode(true);
    selectElement.value = item.idclase;
    selectElement.addEventListener('change', function (event) {
        actualizarClaseGasto(event.target.value, item.id);
        console.log('Nuevo valor seleccionado:', event.target.value);
    });
    cellClases.appendChild(selectElement);
    row.appendChild(cellClases);
}

function generarRespuesta(registros) {
    const columnas = ['id', 'fecha_proceso', 'descripcion', 'yapero', 'moneda', 'debe', 'haber']
    const formatear = ['debe', 'haber']
    return obtenerClasesDeGasto()
        .then(clasesGasto => crearElementoSelect(clasesGasto))
        .then((elemClasesGasto) => { return generarTabla(registros, columnas, formatear, elemClasesGasto, crearDropDownClases) })
        .catch((error) => {
            return manejarError(error);
        });
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
    const formData = new FormData(this);
    return procesarEvento(e, formData, this.action, generarRespuesta);
});
