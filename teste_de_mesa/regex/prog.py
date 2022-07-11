def exec_script(lines, create_var, exec_code): 
    for i in range(len(lines)-1):
        code_run_line = '\n'
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

        lines[i] += code_run_line

    return lines