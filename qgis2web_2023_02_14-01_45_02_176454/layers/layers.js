var wms_layers = [];


        var lyr_GoogleHybrid_0 = new ol.layer.Tile({
            'title': 'Google Hybrid',
            'type': 'base',
            'opacity': 1.000000,
            
            
            source: new ol.source.XYZ({
    attributions: ' ',
                url: 'https://mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z}'
            })
        });
var format_Floreras_1 = new ol.format.GeoJSON();
var features_Floreras_1 = format_Floreras_1.readFeatures(json_Floreras_1, 
            {dataProjection: 'EPSG:4326', featureProjection: 'EPSG:3857'});
var jsonSource_Floreras_1 = new ol.source.Vector({
    attributions: ' ',
});
jsonSource_Floreras_1.addFeatures(features_Floreras_1);cluster_Floreras_1 = new ol.source.Cluster({
  distance: 10,
  source: jsonSource_Floreras_1
});
var lyr_Floreras_1 = new ol.layer.Vector({
                declutter: true,
                source:cluster_Floreras_1, 
                style: style_Floreras_1,
                interactive: true,
                title: '<img src="styles/legend/Floreras_1.png" /> Florerías'
            });

lyr_GoogleHybrid_0.setVisible(true);lyr_Floreras_1.setVisible(true);
var layersList = [lyr_GoogleHybrid_0,lyr_Floreras_1];
lyr_Floreras_1.set('fieldAliases', {'id': 'id', 'clee': 'clee', 'nom_estab': 'nom_estab', 'raz_social': 'raz_social', 'codigo_act': 'codigo_act', 'nombre_act': 'nombre_act', 'per_ocu': 'per_ocu', 'tipo_vial': 'tipo_vial', 'nom_vial': 'nom_vial', 'tipo_v_e_1': 'tipo_v_e_1', 'nom_v_e_1': 'nom_v_e_1', 'tipo_v_e_2': 'tipo_v_e_2', 'nom_v_e_2': 'nom_v_e_2', 'tipo_v_e_3': 'tipo_v_e_3', 'nom_v_e_3': 'nom_v_e_3', 'numero_ext': 'numero_ext', 'letra_ext': 'letra_ext', 'edificio': 'edificio', 'edificio_e': 'edificio_e', 'numero_int': 'numero_int', 'letra_int': 'letra_int', 'tipo_asent': 'tipo_asent', 'nomb_asent': 'nomb_asent', 'tipoCenCom': 'tipoCenCom', 'nom_CenCom': 'nom_CenCom', 'num_local': 'num_local', 'cod_postal': 'cod_postal', 'cve_ent': 'cve_ent', 'entidad': 'entidad', 'cve_mun': 'cve_mun', 'municipio': 'municipio', 'cve_loc': 'cve_loc', 'localidad': 'localidad', 'ageb': 'ageb', 'manzana': 'manzana', 'telefono': 'telefono', 'correoelec': 'correoelec', 'www': 'www', 'tipoUniEco': 'tipoUniEco', 'latitud': 'latitud', 'longitud': 'longitud', 'fecha_alta': 'fecha_alta', });
lyr_Floreras_1.set('fieldImages', {'id': 'TextEdit', 'clee': 'TextEdit', 'nom_estab': 'TextEdit', 'raz_social': 'TextEdit', 'codigo_act': 'TextEdit', 'nombre_act': 'TextEdit', 'per_ocu': 'TextEdit', 'tipo_vial': 'TextEdit', 'nom_vial': 'TextEdit', 'tipo_v_e_1': 'TextEdit', 'nom_v_e_1': 'TextEdit', 'tipo_v_e_2': 'TextEdit', 'nom_v_e_2': 'TextEdit', 'tipo_v_e_3': 'TextEdit', 'nom_v_e_3': 'TextEdit', 'numero_ext': 'TextEdit', 'letra_ext': 'TextEdit', 'edificio': 'TextEdit', 'edificio_e': 'TextEdit', 'numero_int': 'TextEdit', 'letra_int': 'TextEdit', 'tipo_asent': 'TextEdit', 'nomb_asent': 'TextEdit', 'tipoCenCom': 'TextEdit', 'nom_CenCom': 'TextEdit', 'num_local': 'TextEdit', 'cod_postal': 'TextEdit', 'cve_ent': 'TextEdit', 'entidad': 'TextEdit', 'cve_mun': 'TextEdit', 'municipio': 'TextEdit', 'cve_loc': 'TextEdit', 'localidad': 'TextEdit', 'ageb': 'TextEdit', 'manzana': 'TextEdit', 'telefono': 'TextEdit', 'correoelec': 'TextEdit', 'www': 'TextEdit', 'tipoUniEco': 'TextEdit', 'latitud': 'TextEdit', 'longitud': 'TextEdit', 'fecha_alta': 'TextEdit', });
lyr_Floreras_1.set('fieldLabels', {'id': 'header label', 'clee': 'header label', 'nom_estab': 'header label', 'raz_social': 'header label', 'codigo_act': 'header label', 'nombre_act': 'header label', 'per_ocu': 'header label', 'tipo_vial': 'header label', 'nom_vial': 'header label', 'tipo_v_e_1': 'header label', 'nom_v_e_1': 'header label', 'tipo_v_e_2': 'header label', 'nom_v_e_2': 'header label', 'tipo_v_e_3': 'header label', 'nom_v_e_3': 'header label', 'numero_ext': 'header label', 'letra_ext': 'header label', 'edificio': 'header label', 'edificio_e': 'header label', 'numero_int': 'header label', 'letra_int': 'header label', 'tipo_asent': 'header label', 'nomb_asent': 'header label', 'tipoCenCom': 'header label', 'nom_CenCom': 'header label', 'num_local': 'header label', 'cod_postal': 'header label', 'cve_ent': 'header label', 'entidad': 'header label', 'cve_mun': 'header label', 'municipio': 'header label', 'cve_loc': 'header label', 'localidad': 'header label', 'ageb': 'header label', 'manzana': 'header label', 'telefono': 'header label', 'correoelec': 'header label', 'www': 'header label', 'tipoUniEco': 'header label', 'latitud': 'header label', 'longitud': 'header label', 'fecha_alta': 'header label', });
lyr_Floreras_1.on('precompose', function(evt) {
    evt.context.globalCompositeOperation = 'normal';
});