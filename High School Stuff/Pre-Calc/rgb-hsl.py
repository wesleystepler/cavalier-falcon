def chroma(r,g,b):
    return max(r,g,b) - min(r,g,b)
    

def hue(r,g,b):
    c = chroma(r,g,b)

    if max(r,g,b) == r:
        return ((g-b)/c) % 6 * 60
    
    elif max(r,g,b) == g:
        return((b-r)/c) + 2 * 60
    elif max(r,g,b) == b:
        return((r-g)/c) + 4 * 60

def lightness(r,g,b):
    return ( ((max(r,g,b) + min(r,g,b) )/2)/255)

def saturation(r,g,b):
    c = chroma(r,g,b)
    l = lightness(r,g,b)

    return (c/(1 - abs( (2*l)-1) ))/255

def hsl(r,g,b):
    c = chroma(r,g,b)
    h = hue(r,g,b)
    s = saturation(r,g,b)
    l = lightness(r,g,b)
    return (c,h,s,l)

print(hsl(150,50,75))

    