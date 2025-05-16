def rgb(r, g, b):
    ## Jeito junior de escrever
    # if r > 255:
    #     r = 255
    # elif r < 0:
    #     r = 0
    # if g > 255:
    #     g = 255
    # elif g < 0:
    #     g = 0
    # if b > 255:
    #     b = 255
    # elif b < 0:
    #     b = 0

    ## Jeito pleno de escrever
    r = min(max(r, 0), 255)
    g = min(max(g, 0), 255)
    b = min(max(b, 0), 255)
    txt = "{0:02X}{1:02X}{2:02X}"
    hexa = txt.format(r,g,b)
    
    print(hexa)    

cores_rgb = rgb(-20,275,125)
