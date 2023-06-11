import mysql.connector

try:
    con = mysql.connector.connect(
        host='localhost',
        database='trabalhopoo',
        user='root',
        password='dev357lucas?00011()&&@##klgQWASD')
    inserir_valor = """insert into usuario
                           (id, senha, nome, idade)
                           values
                           (800, 12346, 'lucas', 15)
                           """
    cursor = con.cursor()
    cursor.execute(inserir_valor)
    con.commit()
    print(cursor.rowcount, "registros inseridos na tabela!")
    cursor.close()
finally:
    if (con.is_connected()):
        cursor.close()
        con.close()
        print("Conexão Encerrada!")