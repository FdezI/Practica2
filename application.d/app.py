import web
from web import form
from mandelbrot import *

urls = (
    '/(.*)', 'fractal'
)

app = web.application(urls, globals())

render = web.template.render('templates/')

# Tratando el notfound
def notfound():
    return web.notfound(render.notfound())
app.notfound = notfound

############## Formularios ################

# Datos de usuario
myForm = form.Form(
    form.Textbox('Username', form.notnull),
    form.Password('Password', form.notnull),
    form.Textbox('Age', form.regexp('\d+', 'Your age must be a number'), form.Validator('You cannot be less of 3 years old', lambda x:int(x)>3)),
    form.Textarea('Comments'))

# Datos de fractal
fractalForm = form.Form( 
    form.Textbox("x1", description = "x1:", value="-2.0"),
    form.Textbox("y1", description = "y1:", value="-3.0"),
    form.Textbox("x2", description = "x2:", value="2.0"),
    form.Textbox("y2", description = "y2:", value="3.0"),
    form.Textbox("wide", description = "Wide(pixels):", value="500"),
    form.Textbox("iterations", description = "Max. Iterations:", value="255"),  
    form.Dropdown('palet', [('blue', 'Blues'), ('bw', "Black & White"), ('gray', "Grays"), ('random', 'Random'), ('random2', 'Random2')], description="Palet:")) 

############## CLASES ################

class fractal:
        
    def GET(self, name):
        form = fractalForm()
        return render.formtest(form)
    
    def POST(self, name):
        form = fractalForm()
        
        palet = [(255, 255, 255), (173, 205, 244), (255, 255, 255)]
        nColors = 15
                
        if form.validates():
            if (form.d.palet == "blue"):
                palet = [(255, 255, 255), (173, 205, 244), (255, 255, 255)]
                nColors = 15
            elif (form.d.palet == "bw"):
                palet = [(0, 0, 0), (255, 255, 255)]
                nColors = 2
            elif (form.d.palet == "random"):
                palet = [(255, 0, 0), (255, 255, 0), (255, 0, 255), (0, 255, 0), (0, 255, 255), (0, 0, 255)]
                nColors = 6
            elif (form.d.palet == "random2"):
                palet = [(255, 0, 0), (255, 255, 0), (255, 0, 255), (0, 255, 0), (0, 255, 255), (0, 0, 255)]
                nColors = 18
            elif (form.d.palet == "gray"):
                palet = [(0, 0, 0), (255, 255, 255)]
                nColors = 10
            
            fileName = "static/mandelbrot.png"
            
            renderizaMandelbrotBonito(float(form.d.x1), float(form.d.y1), float(form.d.x2), float(form.d.y2), int(form.d.wide), int(form.d.iterations), fileName, palet, nColors);
            
            
            return render.formtest(form, fileName)
        
        else:
            return render.formtest(form)
        
if __name__ == "__main__":
    app.run()