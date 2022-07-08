/* modelo logico: */

CREATE TABLE teste_mesa (
    id_teste_mesa int(4) PRIMARY KEY,
    data_teste_mesa date,
    fk_caso_teste_id_caso_teste int(4)
);

CREATE TABLE dados (
    id_dados int(4) PRIMARY KEY,
    linha varchar(5),
    variavel_p varchar(100),
    dado_hex_p varchar(100),
    adicionado datetime,
    fk_teste_mesa_id_teste_mesa int(4)
);

CREATE TABLE caso_teste (
    id_caso_teste int(4) PRIMARY KEY,
    fk_programa_o_id_programa_o int(4),
    fk_programa_p_id_programa_p int(4)
);

CREATE TABLE programa_p (
    id_programa_p int(4) PRIMARY KEY,
    data_implementacao date,
    codigo_programa_p text
);

CREATE TABLE programa_o (
    id_programa_o int(4) PRIMARY KEY,
    data_implementacao date,
    codigo_programa_p text
);

CREATE TABLE dicionario_parametros (
    id_dicionario int(4) PRIMARY KEY,
    numero_linha numeric,
    fk_teste_mesa_id_teste_mesa int(4)
);

CREATE TABLE valor_parametro (
    id_valor_parametro int(4) PRIMARY KEY,
    parametro varchar(100),
    valor varchar(100),
    fk_dicionario_parametros_id_dicionario int(4)
);
 
ALTER TABLE teste_mesa ADD CONSTRAINT FK_teste_mesa_2
    FOREIGN KEY (fk_caso_teste_id_caso_teste)
    REFERENCES caso_teste (id_caso_teste);
 
ALTER TABLE teste_mesa ADD CONSTRAINT FK_teste_mesa_3
    FOREIGN KEY (fk_dados_id_dados)
    REFERENCES dados (id_dados);
 
ALTER TABLE dados ADD CONSTRAINT FK_dados_2
    FOREIGN KEY (fk_teste_mesa_id_teste_mesa)
    REFERENCES teste_mesa (id_teste_mesa);
 
ALTER TABLE caso_teste ADD CONSTRAINT FK_caso_teste_2
    FOREIGN KEY (fk_programa_o_id_programa_o)
    REFERENCES programa_o (id_programa_o);
 
ALTER TABLE caso_teste ADD CONSTRAINT FK_caso_teste_3
    FOREIGN KEY (fk_programa_p_id_programa_p)
    REFERENCES programa_p (id_programa_p);
 
ALTER TABLE dicionario_parametros ADD CONSTRAINT FK_dicionario_parametros_2
    FOREIGN KEY (fk_teste_mesa_id_teste_mesa)
    REFERENCES teste_mesa (id_teste_mesa);
 
ALTER TABLE valor_parametro ADD CONSTRAINT FK_valor_parametro_1
    FOREIGN KEY (fk_dicionario_parametros_id_dicionario)
    REFERENCES dicionario_parametros (id_dicionario);