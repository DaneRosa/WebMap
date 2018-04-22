import folium
import pandas 

data = pandas.read_csv("volcanoes_usa.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

print("hello world")
#new machine test

def color_pro(elevation): #this will allow the elevation dictate color of the markers 
    if elevation < 1000:
        return 'green'
    elif  1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'
map = folium.Map(location=[38, -100], zoom_start=4, tiles="Mapbox Bright")
fg = folium.FeatureGroup(name="My Map")
for lt, ln, el in zip(lat, lon, elev): #this will have lt go through the first item in the first list , and have ln go through first item of second list etc.
                            # zip() lets you go through 1 by 1 
    fg.add_child(folium.Circle(location=[lt, ln], popup=str(el) + " m", fill_color=color_pro(el), fill=True, color=color_pro(el), fill_opacity=0.7))
                                                        #^ blank page if '' solve by popup=folium.Popup(str(el), parse_html+true)

fgp = folium.FeatureGroup(name="Population")


fg.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))



map.add_child(fg)
map.add_child(folium.LayerControl())
map.save("map1.html")

