import json
import os

from style import *

print(
    json.dumps(['a', 123, True]),
    json.dumps(['i\\hbar \\frac{\\partial \\Psi}{\\partial t} = -\\frac{\\hbar^2}{2m}\\frac{\\partial^2}{\\partial\\textbf{r}^2}\\Psi + \\text{V}(\\textbf{r}, t)\\Psi']) # schrödinger equation
)

def generate_tex_file(name: str, formula: str, parent_dir=PAREN_DIR_LATEX):
    """[DONE] Generates a `.tex` file with the requested LaTeX string, rendering it in a standalone format with 1mm margins on all sides. Must be run twice for the `.tex` file to be automatically run and the `.pdf` generated.   
    
    """
    
    # add custom dependency module later, so usepackage statements are added dynamically
    boilerplate_init = """
    \\documentclass[margin=1mm]{standalone}

    \\usepackage{amsmath}
    \\usepackage{amssymb}

    \\begin{document}

    \n \\( \\displaystyle """

    boilerplate_fin = """\\)\n
    \\end{document}
    """

    tex_code = boilerplate_init + formula + boilerplate_fin
    print(tex_code)

    # create dir
    if not os.path.exists(f'{parent_dir}/tex_{name}'): 
        os.makedirs(f'{parent_dir}/tex_{name}')

    with open(f'{parent_dir}/tex_{name}/{name}.tex', "w") as f:
        f.write(tex_code)

generate_tex_file('schroedinger_equation', 'i\\hbar \\frac{\\partial \\Psi}{\\partial t} = -\\frac{\\hbar^2}{2m}\\frac{\\partial^2}{\\partial\\textbf{r}^2}\\Psi + \\text{V}(\\textbf{r}, t)\\Psi')
generate_tex_file('einstein_genius', 'E = mc^2')