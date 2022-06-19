/* modelo logico: */

CREATE TABLE teste_mesa (
    id_teste_mesa int(4) PRIMARY KEY,
    data_teste_mesa date,
    fk_caso_teste_id_caso_teste int(4),
    fk_dados_id_dados int(4)
);

CREATE TABLE dados (
    id_dados int(4) PRIMARY KEY,
    linha varchar(5),
    num_equacao varchar(1),
    variavel_o varchar(100),
    dado_hexa_o varchar(100),
    variavel_p varchar(100),
    dado_hex_p varchar(100),
    id_var int(4)
);

CREATE TABLE caso_teste (
    id_caso_teste int(4) PRIMARY KEY,
    fk_programa_o_id_programa_o int(4),
    fk_programa_p_id_programa_p int(4)
);

CREATE TABLE valores_teste (
    id_valores_teste int(4) PRIMARY KEY,
    parametro varchar(100),
    valor varchar(100),
    fk_caso_teste_id_caso_teste int(4)
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
 
ALTER TABLE teste_mesa ADD CONSTRAINT FK_teste_mesa_2
    FOREIGN KEY (fk_caso_teste_id_caso_teste)
    REFERENCES caso_teste (id_caso_teste);
 
ALTER TABLE teste_mesa ADD CONSTRAINT FK_teste_mesa_3
    FOREIGN KEY (fk_dados_id_dados)
    REFERENCES dados (id_dados);
 
ALTER TABLE caso_teste ADD CONSTRAINT FK_caso_teste_2
    FOREIGN KEY (fk_programa_o_id_programa_o)
    REFERENCES programa_o (id_programa_o);
 
ALTER TABLE caso_teste ADD CONSTRAINT FK_caso_teste_3
    FOREIGN KEY (fk_programa_p_id_programa_p)
    REFERENCES programa_p (id_programa_p);
 
ALTER TABLE valores_teste ADD CONSTRAINT FK_valores_teste_2
    FOREIGN KEY (fk_caso_teste_id_caso_teste)
    REFERENCES caso_teste (id_caso_teste);