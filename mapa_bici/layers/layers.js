var wms_layers = [];


        var lyr_GoogleSatellite_0 = new ol.layer.Tile({
            'title': 'Google Satellite',
            'type': 'base',
            'opacity': 1.000000,
            
            
            source: new ol.source.XYZ({
    attributions: ' ',
                url: 'http://www.google.cn/maps/vt?lyrs=s@189&gl=cn&x={x}&y={y}&z={z}'
            })
        });
var format_Alcaldas_1 = new ol.format.GeoJSON();
var features_Alcaldas_1 = format_Alcaldas_1.readFeatures(json_Alcaldas_1, 
            {dataProjection: 'EPSG:4326', featureProjection: 'EPSG:3857'});
var jsonSource_Alcaldas_1 = new ol.source.Vector({
    attributions: ' ',
});
jsonSource_Alcaldas_1.addFeatures(features_Alcaldas_1);
var lyr_Alcaldas_1 = new ol.layer.Vector({
                declutter: true,
                source:jsonSource_Alcaldas_1, 
                style: style_Alcaldas_1,
                interactive: false,
                title: '<img src="styles/legend/Alcaldas_1.png" /> Alcaldías'
            });
var format_Infraestructuravialciclista_2 = new ol.format.GeoJSON();
var features_Infraestructuravialciclista_2 = format_Infraestructuravialciclista_2.readFeatures(json_Infraestructuravialciclista_2, 
            {dataProjection: 'EPSG:4326', featureProjection: 'EPSG:3857'});
var jsonSource_Infraestructuravialciclista_2 = new ol.source.Vector({
    attributions: ' ',
});
jsonSource_Infraestructuravialciclista_2.addFeatures(features_Infraestructuravialciclista_2);
var lyr_Infraestructuravialciclista_2 = new ol.layer.Vector({
                declutter: true,
                source:jsonSource_Infraestructuravialciclista_2, 
                style: style_Infraestructuravialciclista_2,
                interactive: true,
                title: '<img src="styles/legend/Infraestructuravialciclista_2.png" /> Infraestructura vial ciclista'
            });
var format_CicloestacionesdeECOBICI_3 = new ol.format.GeoJSON();
var features_CicloestacionesdeECOBICI_3 = format_CicloestacionesdeECOBICI_3.readFeatures(json_CicloestacionesdeECOBICI_3, 
            {dataProjection: 'EPSG:4326', featureProjection: 'EPSG:3857'});
var jsonSource_CicloestacionesdeECOBICI_3 = new ol.source.Vector({
    attributions: ' ',
});
jsonSource_CicloestacionesdeECOBICI_3.addFeatures(features_CicloestacionesdeECOBICI_3);
var lyr_CicloestacionesdeECOBICI_3 = new ol.layer.Vector({
                declutter: true,
                source:jsonSource_CicloestacionesdeECOBICI_3, 
                style: style_CicloestacionesdeECOBICI_3,
                interactive: true,
                title: '<img src="styles/legend/CicloestacionesdeECOBICI_3.png" /> Cicloestaciones de ECOBICI'
            });

lyr_GoogleSatellite_0.setVisible(true);lyr_Alcaldas_1.setVisible(true);lyr_Infraestructuravialciclista_2.setVisible(true);lyr_CicloestacionesdeECOBICI_3.setVisible(true);
var layersList = [lyr_GoogleSatellite_0,lyr_Alcaldas_1,lyr_Infraestructuravialciclista_2,lyr_CicloestacionesdeECOBICI_3];
lyr_Alcaldas_1.set('fieldAliases', {'X_id': 'X_id', 'id': 'id', 'nomgeo': 'nomgeo', 'cve_mun': 'cve_mun', 'cve_ent': 'cve_ent', 'cvegeo': 'cvegeo', 'g_pnt_2': 'g_pnt_2', 'geo_shp': 'geo_shp', 'municip': 'municip', });
lyr_Infraestructuravialciclista_2.set('fieldAliases', {'ID_TRAMO': 'ID_TRAMO', 'ID_PROY': 'ID_PROY', 'NOMBRE': 'NOMBRE', 'TIPO_IC': 'TIPO_IC', 'ALCALDIA': 'ALCALDIA', 'VIALIDAD': 'VIALIDAD', 'TIPO_VIA': 'TIPO_VIA', 'ESTADO': 'ESTADO', 'INSTANCIA': 'INSTANCIA', 'A_HABILITA': 'A_HABILITA', 'A_LICITA': 'A_LICITA', 'LONG_KM': 'LONG_KM', });
lyr_CicloestacionesdeECOBICI_3.set('fieldAliases', {'SISTEMA': 'SISTEMA', 'Num_Cicloe': 'Num_Cicloe', 'Nombre': 'Nombre', 'Calle_Prin': 'Calle_Prin', 'Calle_Secu': 'Calle_Secu', 'Colonia': 'Colonia', 'Alcaldia': 'Alcaldia', 'Tipo_CE': 'Tipo_CE', 'Candados': 'Candados', });
lyr_Alcaldas_1.set('fieldImages', {'X_id': 'Range', 'id': 'Range', 'nomgeo': 'TextEdit', 'cve_mun': 'Range', 'cve_ent': 'Range', 'cvegeo': 'Range', 'g_pnt_2': 'TextEdit', 'geo_shp': 'TextEdit', 'municip': 'Range', });
lyr_Infraestructuravialciclista_2.set('fieldImages', {'ID_TRAMO': 'TextEdit', 'ID_PROY': 'TextEdit', 'NOMBRE': 'TextEdit', 'TIPO_IC': 'TextEdit', 'ALCALDIA': 'TextEdit', 'VIALIDAD': 'TextEdit', 'TIPO_VIA': 'TextEdit', 'ESTADO': 'TextEdit', 'INSTANCIA': 'TextEdit', 'A_HABILITA': 'TextEdit', 'A_LICITA': 'TextEdit', 'LONG_KM': 'TextEdit', });
lyr_CicloestacionesdeECOBICI_3.set('fieldImages', {'SISTEMA': 'TextEdit', 'Num_Cicloe': 'TextEdit', 'Nombre': 'TextEdit', 'Calle_Prin': 'TextEdit', 'Calle_Secu': 'TextEdit', 'Colonia': 'TextEdit', 'Alcaldia': 'TextEdit', 'Tipo_CE': 'TextEdit', 'Candados': 'TextEdit', });
lyr_Alcaldas_1.set('fieldLabels', {'X_id': 'no label', 'id': 'no label', 'nomgeo': 'no label', 'cve_mun': 'no label', 'cve_ent': 'no label', 'cvegeo': 'no label', 'g_pnt_2': 'no label', 'geo_shp': 'no label', 'municip': 'no label', });
lyr_Infraestructuravialciclista_2.set('fieldLabels', {'ID_TRAMO': 'header label', 'ID_PROY': 'header label', 'NOMBRE': 'header label', 'TIPO_IC': 'header label', 'ALCALDIA': 'header label', 'VIALIDAD': 'header label', 'TIPO_VIA': 'header label', 'ESTADO': 'header label', 'INSTANCIA': 'header label', 'A_HABILITA': 'no label', 'A_LICITA': 'no label', 'LONG_KM': 'no label', });
lyr_CicloestacionesdeECOBICI_3.set('fieldLabels', {'SISTEMA': 'header label', 'Num_Cicloe': 'header label', 'Nombre': 'header label', 'Calle_Prin': 'header label', 'Calle_Secu': 'header label', 'Colonia': 'header label', 'Alcaldia': 'header label', 'Tipo_CE': 'header label', 'Candados': 'header label', });
lyr_CicloestacionesdeECOBICI_3.on('precompose', function(evt) {
    evt.context.globalCompositeOperation = 'normal';
});