CREATE TABLE dados_tm (
	id INT(8) NOT NULL,
	linha VARCHAR(5),
	num_equacao VARCHAR(1),
	var_o VARCHAR(20),
	dado_exa_o VARCHAR(20),
	CONSTRAINT dados_tm_pk PRIMARY KEY (id)
);

CREATE TABLE valores_ct (
	id_dados_t INT(8) NOT NULL,
	parametro VARCHAR(20),
	valor VARCHAR(20),
	id_caso_teste_caso_teste INT(11),
	CONSTRAINT valores_ct_pk PRIMARY KEY (id_dados_t)
);

CREATE TABLE caso_teste (
	id_caso_teste INT(11) NOT NULL,
	id_p_programa_p INT(11),
	id_o_programa_o INT(11),
	CONSTRAINT caso_teste_pk PRIMARY KEY (id_caso_teste)
);

CREATE TABLE teste_mesa (
	id_teste_mesa INT(11) NOT NULL,
	dt_teste_mesa date,
	id_dados INT(11),
	id_caso_teste_caso_teste INT(11),
	id_dados_tm INT(8),
	CONSTRAINT teste_mesa_pk PRIMARY KEY (id_teste_mesa)
);

CREATE TABLE programa_o (
	id_o INT(11) NOT NULL,
	dt_codificacao date,
	codigo_o text,
	CONSTRAINT programa_o_pk PRIMARY KEY (id_o)
);

CREATE TABLE programa_p (
	id_p INT(11) NOT NULL,
	dt_codificacao date,
	codigo_p text,
	CONSTRAINT programa_p_pk PRIMARY KEY (id_p)
);


ALTER TABLE valores_ct ADD CONSTRAINT caso_teste_fk FOREIGN KEY (id_caso_teste_caso_teste)
REFERENCES caso_teste (id_caso_teste);

ALTER TABLE caso_teste ADD CONSTRAINT programa_p_fk FOREIGN KEY (id_p_programa_p)
REFERENCES programa_p (id_p);

ALTER TABLE caso_teste ADD CONSTRAINT programa_o_fk FOREIGN KEY (id_o_programa_o)
REFERENCES programa_o (id_o);

ALTER TABLE teste_mesa ADD CONSTRAINT caso_teste_fk FOREIGN KEY (id_caso_teste_caso_teste)
REFERENCES caso_teste (id_caso_teste);

ALTER TABLE teste_mesa ADD CONSTRAINT dados_tm_fk FOREIGN KEY (id_dados_tm)
REFERENCES dados_tm (id);