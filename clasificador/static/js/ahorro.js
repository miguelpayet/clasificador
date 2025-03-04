import { generarTabla, procesarEvento } from './crear_tabla.js';

function generarRespuesta(registros) {
    const columnas = ['mes', 'año', 'nombre', 'moneda', 'debe', 'haber']
    const formatear = ['debe', 'haber']
    return new Promise((resolve, reject) => {
        try {
            const result = generarTabla(registros, columnas, formatear);
            resolve(result);
        } catch (error) {
            reject(error);
        }
    });
}

document.getElementById('search-form').addEventListener('submit', function (e) {
    const formData = new FormData(this);
    return procesarEvento(e, formData, this.action, generarRespuesta);
});
