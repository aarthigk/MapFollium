import folium
#m=folium.Map(location=[51.5591148,-1.79793],zoom_start=12)

m=folium.Map(location=[6.4516082,3.4070867],zoom_start=12)
tooltip ="Click me tooltip"
folium.Marker([6.4516082,3.4070867],
              popup='<strong>Location one</strong>',
              tooltip=tooltip).add_to(m)

m.save('map.html')#6.4516082,3.4070867,18z