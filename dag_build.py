import json
from codecs import open
from pprint import pprint

import tatsu


def simple_parse():
    grammar = open('dag_grammar.ebnf').read()

    parser = tatsu.compile(grammar, asmodel=True)
    ast = parser.parse(
    """
    dag teste
    owner Felipe
    start date dddddd

    # Inicio das operações:

    copy table original_table from health_db to original_table 
    
    run sql file transform12.sql 
    
    run bash file copy.sql

    # copiar arquivo original_table2 from health_db to staging_pii.original_table2

    # write google sheet 123abc in range text!aa:11 from query transform12.sql 


    """)
# owner: 'example_owner'
#     start_date: 2018-01-01  # or '2 days'
#     end_date: 2018-01-05
#     retries: 1
#     retry_delay_sec: 300
#   schedule_interval


    print('# SIMPLE PARSE')
    print('# AST')
    pprint(ast, width=20, indent=4)

    print('-'*50)

    def print_ast_node(node, indent=0):
        prefix = '    '*indent
        if isinstance(node, str):
            print(prefix+f'str: {node}' ) 
        elif isinstance(node, tuple):
            for i in node:
                print_ast_node(i, indent+1) 
        elif isinstance(node, list):
            print(prefix+'[')
            for i in node:
                print_ast_node(i, indent+1) 
            print(prefix+']')
        else:
            print(prefix+str(node))

    print_ast_node(ast)

    # print('# JSON')
    # print(json.dumps(ast, indent=4))


def main():
    simple_parse()


if __name__ == '__main__':
    main()