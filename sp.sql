DELIMITER //
CREATE PROCEDURE insere_teste_de_mesa(teste_apelido text)
BEGIN

DECLARE id_programa_o INT;
DECLARE id_programa_p INT;


SET id_programa_o = (SELECT id FROM tbl_programa_o po where po.nome_teste_de_mesa = teste_apelido);
SET id_programa_p = (SELECT id FROM tbl_programa_p pp where pp.nome_teste_de_mesa = teste_apelido);
INSERT INTO tbl_teste_de_mesa(programa_o_id, programa_p_id) VALUES(id_programa_o, id_programa_p);
END//
DELIMITER ;


DELIMITER //
CREATE PROCEDURE insere_metricas(variavel_o text, valor_o text, linha_o, variavel_p text, valor_p text, linha_p text, apelido_teste text)
BEGIN
DECLARE id_teste int;
SET id_teste = (SELECT id FROM tbl_programa_o po where po.nome_teste_de_mesa = apelido_teste);
INSERT INTO tbl_metricas(variavel_o,valor_hexa_o,linha_o,variavel_p,valor_hexa_p,linha_p,id_teste_de_mesa) VALUES (variavel_o,valor_o,variavel_p,valor_p,linha,id_teste);
END //
DELIMITER ;
