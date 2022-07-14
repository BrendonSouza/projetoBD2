def exec_script(lines, create_var, exec_code): 
    # Percorre as linhas do programa que são passadas por parâmetro 
    for i in range(len(lines)-1):
        # variável que recebe linhas executáveis do programa 
        code_run_line = '\n'
        # Concatenação do código que monta a execução linha por linha do programa 
        if lines[i+1].startswith(' '):
            code_run_line += '    '
            code_run_line += 'for key, item in create_var.items():\n'
            code_run_line += '    '
            code_run_line += '    create_var[key] = eval(key)\n'
            code_run_line += '    '
            code_run_line += 'exec_code.append(copy.deepcopy(create_var))\n'

        else:
            code_run_line += 'for key, item in create_var.items():\n'
            code_run_line += '    create_var[key] = eval(key)\n'
            code_run_line += 'exec_code.append(copy.deepcopy(create_var))\n'
        # Adiconando o código na posição especificada em i 
        lines[i] += code_run_line
    # retornando as linhas 
    return lines