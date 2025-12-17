import scrapy
import pandas as pd

class Ejercicio3Spider(scrapy.Spider):
    name = "ejercicio_3"
    allowed_domains = ["es.wikipedia.org"]
    start_urls = ["https://es.wikipedia.org/wiki/FIFA"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.data=[]

    def parse(self, response):
        tablas = response.css("table.wikitable")
        tabla = tablas[1]
        for filas in tabla.css("tr"):
            columnas = filas.css("td")
            if len(columnas) >= 1:
                self.data.append({
                    "confederacion": columnas[0].css("::text").get(default="").strip()+" "+columnas[0].xpath("text()").get(default="").strip(),
                    "region": columnas[1].css("::text").get(default="").strip(),
                    "ano": columnas[2].css("::text").get(default="").strip(),
                    "miembros": columnas[3].css("::text").get(default="").strip(),
                    "sede": columnas[4].css("a::text").get(default="").strip(),
                    "presidente": columnas[5].css("a::text").get(default="").strip(),
                })
    
    def closed (self, reason):
        df = pd.DataFrame(self.data)
        df.to_excel("FIFA.xlsx", index=False)



