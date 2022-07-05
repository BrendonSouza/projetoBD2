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