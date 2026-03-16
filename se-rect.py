from tkinter import Tk, filedialog
Tk().withdraw()
while True:
    r=int(input("r: "))#r is an alternative to border-radius in CSS, higher r equals softer edges
    x=max(r,int(input("x: ")))#x is the width, minimal width is fixed to r
    y=max(r,int(input("y: ")))#y is the height, minimal height is fixed to r
    result=f"""<svg height="{y}"viewBox="0 -960 {40*x*(24/r)} {40*y*(24/r)}"preserveAspectRatio="none"width="{x}"fill="#e3e3e3"version="1.1"id="svg1"xmlns="http://www.w3.org/2000/svg"xmlns:svg="http://www.w3.org/2000/svg"><path id="path2"style="fill:#1b1b1b;fill-opacity:1;stroke-width:40"d="m 480,-953.35938 c -86.66578,0 -173.3334,6.66668 -240,20 C 106.6668,-906.69274 53.307264,-853.33534 26.640625,-720 c -13.333319,66.66766 -20.0000668,153.33415 -20,240 v {40*y*(24/r)-960} c 6.68e-5,86.6658 6.666413,173.3331 20,240 26.667173,133.3337 80.024045,186.6927 213.359375,213.3593 66.66766,13.3334 153.33415,20.0001 240,20 h {40*x*(24/r)-960} c 86.666,0 173.333,-6.6664 240,-20 133.334,-26.6671 186.693,-80.024 213.359,-213.3593 13.334,-66.6677 20,-153.3342 20,-240 V -480 c 0,-86.66585 -6.666,-173.33314 -20,-240 -26.667,-133.33373 -80.024,-186.69274 -213.359,-213.35938 -66.668,-13.33332 -153.334,-20 -240,-20 z"/><defs id="defs1"/></svg>"""
    print(result)
    save=(input("Save as TXT? [Y/N]: ")).upper()
    if save=="YES" or save=="Y":
        path=filedialog.asksaveasfilename(defaultextension=".txt",filetypes=[("Raw text file","*.txt")])
        if path:open(path,"w").write(result)
    input()
