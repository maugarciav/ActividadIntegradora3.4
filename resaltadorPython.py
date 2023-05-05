import re

# Definimos los patrones para:
# 1. Palabras reservadas
# 2. Literales  (numeros, variables, comentarios, string)
# 3. Operadores
# 4. Delimitadores
# 5. Funciones integradas

def analisador(code):
    
    contentcode = code 
    # 1. Palabras reservadas
    palabra_reservadas_pattern = r'\b(?<!\w)(False|await|else|import|pass|None|break|except|in|raise|True|class|finally|is|return|and|continue|for|lambda|try|as|def|from|nonlocal|while|assert|global|not|with|async|elif|if|or|yield|print)\b'

    # 2. Literales  
    # ------ Numeros
    numeros_pattern = r'[-]?\d+[.]?\d*([eE][-]?\d+)?'
    # ------ Variables
    # variables_pattern = r'[A-Za-z][\w]*'
    variables_pattern = r'(?<!#)[A-Za-z][\w]*'

    # ------ String
    string_pattern = r'"([^"]*)"'

    # ------ Comentario
    comment_pattern = r'#.*'

    # 3. Operadores
    operadores_pattern = r'(>>|<<|<=|>=|==|=|!=|\+|\-|\*|\*\*|/|//|%|@|&|\||\^|~|<|>)'

    # 4. Delimitadores
    delimitadores_pattern = r'(\'|\"|\(|\)|\[|\]|\{|\}|,|:|\.|;|@)'

    # 5. Funciones integradas
    funciones_integradas_pattern = r'\b(?<!\w)(abs|aiter|all|any|anext|ascii|bin|bool|breakpoint|bytearray|bytes|callable|chr|classmethod|compile|complex|delattr|dict|dir|divmod|enumerate|eval|exec|filter|float|format|frozenset|getattr|globals|hasattr|hash|help|hex|id|input|int|isinstance|issubclass|iter|len|list|locals|map|max|memoryview|min|next|object|oct|open|ord|pow|print|property|range|repr|reversed|round|set|setattr|slice|sorted|staticmethod|str|sum|super|tuple|type|vars|zip|__import__)\b' 

    # Búsqueda de coincidencias
    comentarios = []
    strings = []
    palabras_reservadas = []
    delimitadores = []
    operadores = []
    numeros = []
    variables = []
    funciones_integradas = []


    for m in re.finditer(string_pattern, code):
        strings.append(m.group(0))
    code = re.sub(string_pattern, ' ', code)   

    for m in re.finditer(comment_pattern, code):
        comentarios.append(m.group(0))
    code = re.sub(comment_pattern, ' ', code)

    for m in re.finditer(funciones_integradas_pattern, code):
        funciones_integradas.append(m.group(0))
    code = re.sub(funciones_integradas_pattern, ' ', code)

    for m in re.finditer(palabra_reservadas_pattern, code):
        palabras_reservadas.append(m.group(0))
    code = re.sub(palabra_reservadas_pattern, ' ', code)

    for m in re.finditer(delimitadores_pattern, code):
        delimitadores.append(m.group(0))
    code = re.sub(delimitadores_pattern, ' ', code)   

    for m in re.finditer(operadores_pattern, code):
        operadores.append(m.group(0))
    code = re.sub(operadores_pattern, ' ', code)    
        
    for m in re.finditer(numeros_pattern, code):
        numeros.append(m.group(0))
    code = re.sub(numeros_pattern, ' ', code)    

    for m in re.finditer(variables_pattern, code):
        variables.append(m.group(0))
    code = re.sub(variables_pattern, ' ', code)   


    colores = {
    'comentarios': 'orange',
    'palabras_reservadas': 'blue',
    'delimitadores': 'black',
    'operadores': 'green',
    'numeros': 'purple',
    'variables': 'red',
    'funciones_integradas': 'pink',
    'strings' : 'brown'
    }   


    #Creamos HTML y agregamos el codigo con sus clases
    html = '<html><head><style>{}</style></head><body>Actividad Integradora 3.4 Resaltador de sintaxis (evidencia de competencia) <br/> <br/> Colores: <br/><span class="comentarios">Comentarios</span><br/><span class="palabras_reservadas"> Palabras reservadas </span> <br/> <span class="delimitadores"> Delimitadores </span> <br/> <span class="operadores"> Operadores </span> <br/> <span class="numeros"> Numeros </span> <br/><span class="variables"> Variables </span> <br/> <span class="funciones_integradas"> Funciones Integradas </span> <br/><span class="strings"> Strings </span><br/><br/><br/><span>Codigo:</span>{}</body></html>'
    css = ''
    for categoria, color in colores.items():
        css += '.{} {{ color: {}; }}\n'.format(categoria.replace(' ', '-'), color)

    codigo_html = '<pre>{}</pre>'.format(contentcode)
    


    for token in comentarios:
        if '<span class="comentarios">' + token + '</span>' not in codigo_html:
            codigo_html = codigo_html.replace(token, '<span class="comentarios">{}</span>'.format(token))

    for token in strings:
        if '<span class="strings">' + token + '</span>' not in codigo_html:
            codigo_html = codigo_html.replace(token, '<span class="strings">{}</span> '.format(token))


    for token in palabras_reservadas:
        if '<span class="palabras_reservadas">' + token + '</span>' not in codigo_html:
            codigo_html = codigo_html.replace(token, '<span class="palabras_reservadas">{}</span>'.format(token))
            

    for token in funciones_integradas:
        if '<span class="funciones_integradas">' + token + '</span>' not in codigo_html:
            codigo_html = codigo_html.replace(token , '<span class="funciones_integradas">{}</span>'.format(token))
            
                
    for token in delimitadores:
        if '<span class="delimitadores">' + token + '</span>' not in codigo_html:
            codigo_html = codigo_html.replace(token + ' ', '<span class="delimitadores">{}</span> '.format(token))
            

    for token in operadores:
        if '<span class="operadores">' + token + '</span>' not in codigo_html:
            codigo_html = codigo_html.replace(token + ' ' , '<span class="operadores">{}</span>'.format(token + ' '))       
    
    for token in variables:
        pattern = r'\b{}\b'.format(token)
        if '<span class="variables">' + token + '</span>' not in codigo_html:
            codigo_html = re.sub(pattern, '<span class="variables">{}</span>'.format(token), codigo_html)


    for token in numeros:
        if '<span class="numeros">' + token + '</span>' not in codigo_html:
            codigo_html = codigo_html.replace(token, '<span class="numeros">{}</span>'.format(token))
        
    html = html.format(css, codigo_html)

    with open('pythonColores.html', 'w') as f:
        f.write(html)



print("Nombre del archivo que quiere analisar: ")
input = input()
with open (input, 'r') as f:
    contents = f.read()
    analisador(contents)



