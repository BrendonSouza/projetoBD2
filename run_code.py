import copy as cp

def run_code(code, variables):
    new_code = cp.copy(code)
    
    for key in variables:
        new_code = new_code.replace(key, f'variables[\'{key}\']')

    exec(new_code)


if __name__ == '__main__':
    code = '''numero = 1
palavra = 'string'
teste = [1, 2, 3]
for i in range(3):
    teste[0] += 1
'''
    
    variables = {'numero': None, 'palavra': None, 'teste': None}
    run_code(code, variables)

    print(variables)