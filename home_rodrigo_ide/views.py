from django.shortcuts import render

# Create your views here.

def inicio(request):

    return render(request, "home_rodrigo_ide/index.html")

def peliculas_accion(request):

    peliculas = [
        {"nombre":"The Avengers: Los Vengadores", "año":2012, "imagen":"images/accion_1.jpeg"},
        {"nombre":"Iron Man. El Hombre de Hierro", "año":2008, "imagen":"images/accion_2.jpg"},
        {"nombre":"Iron Man 2", "año":2010, "imagen":"images/accion_3.jpg"},
        {"nombre":"Capitán América: El primer vengador", "año":2011, "imagen":"images/accion_4.jpg"},
        {"nombre":"Hulk, el hombre increible", "año":2008, "imagen":"images/accion_5.jpg"},
        {"nombre":"Thor", "año":2011, "imagen":"images/accion_6.jpg"},
        {"nombre":"X-Men orígenes: Wolverine", "año":2009, "imagen":"images/accion_7.jpg"},
        {"nombre":"X-Men: Primera generación", "año":2011, "imagen":"images/accion_8.jpg"},
        {"nombre":"X-Men", "año":2000, "imagen":"images/accion_9.jpg"},
        {"nombre":"X-Men 2", "año":2003, "imagen":"images/accion_10.jpg"}
    ]

    return render(request, "home_rodrigo_ide/peliculas_accion.html", {"pelicula":peliculas})

def peliculas_terror(request):

    peliculas = [
            {"nombre":"El legado del diablo", "año":2018, "imagen":"images/terror_1.jpg"},
            {"nombre":"El extraño", "año":2016, "imagen":"images/terror_2.jpg"},
            {"nombre":"Posesión infernal", "año":2013, "imagen":"images/terror_3.jpg"},
            {"nombre":"Exterminio", "año":2002, "imagen":"images/terror_4.jpg"},
            {"nombre":"Estación zombi. Tren a Busan", "año":2016, "imagen":"images/terror_5.jpg"},
            {"nombre":"La enviada del mal", "año":2015, "imagen":"images/terror_6.jpg"},
            {"nombre":"Fenómeno siniestro", "año":2011, "imagen":"images/terror_7.jpg"},
            {"nombre":"[REC]", "año":2007, "imagen":"images/terror_8.jpg"},
            {"nombre":"La posesión de Verónica", "año":2017, "imagen":"images/terror_9.jpg"},
            {"nombre":"La cabaña del terror", "año":2011, "imagen":"images/terror_10.jpg"}
        ]

    return render(request, "home_rodrigo_ide/peliculas_terror.html", {"pelicula":peliculas})