divisor_de_minuto = 60
divisor_de_hora = 3600

def make_readable(seconds):
    if type(seconds) == int and seconds > -1:        
        horas = seconds // divisor_de_hora
        minutos = (seconds % divisor_de_hora) // divisor_de_minuto
        segundos = seconds % divisor_de_minuto
        txt = "{0:02}:{1:02}:{2:02}"        
        tempo = txt.format(horas,minutos,segundos)          
    else:
        return "Não é numero"
    return tempo

## Divisão inteira
## print(7 / 3)   # Saída: 2.333...
## print(7 // 3)  # Saída: 2

tempo = make_readable(359999)
print(tempo)