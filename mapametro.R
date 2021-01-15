#Mapas del Metro

##Paquetería necesaria
if(!require('pacman')) install.packages('pacman')
pacman::p_load(tidyverse,utils, viridis,sf,ggspatial)


###Se carga la cartografía de colonias y alcaldías
col<-st_read("https://datos.cdmx.gob.mx/explore/dataset/coloniascdmx/download/?format=geojson&timezone=America/Mexico_City&lang=es")
alc<-st_read("https://datos.cdmx.gob.mx/explore/dataset/limite-de-las-alcaldias/download/?format=geojson&timezone=America/Mexico_City&lang=es")  
lineas<-st_read("https://datos.cdmx.gob.mx/explore/dataset/lineas-de-metro/download/?format=geojson&timezone=America/Mexico_City&lang=es")



##Colores de las líneas
#Aquellas líneas sin servicio quedarán en color gris
##Las líneas en servicio llevan su color normal

lineas<-lineas%>%
   mutate(color=ifelse(name=="Línea 1" | name=="Línea 2" | 
                         name=="Línea 3","#C2C2C2",
                       ##Líneas en servicio
                              ifelse(name=="Línea 4","#7bc7ba",
                                     ifelse(name=="Línea 5", "#ffdb25",
                                     ifelse(name=="Línea 6","#e82428",
                                ifelse(name=="Línea 7","#f17c2f",
                                     ifelse(name=="Línea 8","#00a263",
                                            ifelse(name=="Línea 9","#581c00",
                                                   ifelse(name=="Línea A", "#8f248e",
                                                          ifelse(name=="Línea B","#018751",
                                                                 ifelse(name=="Línea 12","#b69c51","")))))))))))

##Construir variable de estatus para poder filtrar
lineas<-lineas%>%
  mutate(estatus=ifelse(color=="#C2C2C2","Fuera de servicio","En servicio"))


##Primer mapa. Con líneas sin servicio en gris
ggplot() +
  ##Capas
  #Colonias
  geom_sf(data=col,fill=NA, color=alpha("#F5F5F5",0.1))+
  #Alcaldías
  geom_sf(data=alc,fill=NA, color=alpha("#F5F5F5",0.2),size=0.5)+
   #Líneas del metro
  geom_sf(data=lineas,fill=NA,color=lineas$color,size=1)+
##Escala y rosa de los vientos
#annotation_scale() +
 # annotation_north_arrow(location='tr')+
  # agrega títulos, notas y fuente
  labs(title = "Líneas activas e inactivas del Metro",
       caption = "Nota:
Aquellas líneas en color gris son las que actualmente se encuentran fuera de
servicio derivado del incendio en el PCC del Metro.
Fuente: @claudiodanielpc con datos del Gobierno de la Ciudad de México. 
Agencia Digital de Información Pública (ADIP)") +
  ##Poner bonito
  theme(plot.title = element_text(hjust = 0, size=20,face="bold",
                                  color="white"),
        plot.subtitle = element_text(hjust = 0, size=15, face="italic", 
                                     color="white"),
        plot.caption = element_text(hjust = 0,size=8, color="white"),
        legend.position = "none",
        axis.text = element_blank(),
        axis.title = element_blank(),
        panel.background=element_rect(fill = "#25426a", colour = "#25426a"),
        panel.grid.minor=element_blank(),
        panel.border=element_blank(),panel.grid.major=element_blank(),
        plot.background= element_rect(fill = "#25426a", colour = "#25426a"),
        legend.title = element_text(face="bold"),
        legend.title.align = 0.5,
        text=element_text(size=20))

##Salvar

ggsave("mapametro1.png",height = 8,width = 8, units="in",dpi=300)

##Segundo mapa. Sin las líneas fuera de servicio
lineas<-lineas%>%
  filter(estatus=="En servicio")


ggplot() +
  ##Capas
  #Colonias
  geom_sf(data=col,fill=NA, color=alpha("#F5F5F5",0.1))+
  #Alcaldías
  geom_sf(data=alc,fill=NA, color=alpha("#F5F5F5",0.2),size=0.5)+
  #Líneas del metro
  geom_sf(data=lineas,fill=NA,color=lineas$color,size=1)+
  ##Escala y rosa de los vientos
  #annotation_scale() +
  #annotation_north_arrow(location='tr')+
  # agrega títulos, notas y fuente
  labs(title = "Líneas en servicio del Metro",
       caption = "Nota:
Aquellas líneas que actualmente se encuentran fuera de servicio derivado 
del incendio en el PCC del Metro fueron omitidas.
Fuente: @claudiodanielpc con datos del Gobierno de la Ciudad de México. 
Agencia Digital de Información Pública (ADIP)") +
  ##Poner bonito
  theme(plot.title = element_text(hjust = 0, size=20,face="bold",
                                  color="white"),
        plot.subtitle = element_text(hjust = 0, size=15, face="italic", 
                                     color="white"),
        plot.caption = element_text(hjust = 0,size=8, color="white"),
        legend.position = "none",
        axis.text = element_blank(),
        axis.title = element_blank(),
        panel.background=element_rect(fill = "#25426a", colour = "#25426a"),
        panel.grid.minor=element_blank(),
        panel.border=element_blank(),panel.grid.major=element_blank(),
        plot.background= element_rect(fill = "#25426a", colour = "#25426a"),
        legend.title = element_text(face="bold"),
        legend.title.align = 0.5,
        text=element_text(size=20))

##Salvar

ggsave("mapametro2.png",height = 8,width = 8, units="in",dpi=300)
