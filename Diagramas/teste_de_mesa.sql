DROP TABLE IF EXISTS `regex_agrupamento`;
CREATE TABLE IF NOT EXISTS `regex_agrupamento` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `linha` int(11) NOT NULL,
  `teste_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `regex_dicionarioparametros_fk_teste_id_2b12f321` (`teste_id`)
) ENGINE=MyISAM AUTO_INCREMENT=117 DEFAULT CHARSET=latin1;


DROP TABLE IF EXISTS `regex_agrupamentoindex`;
CREATE TABLE IF NOT EXISTS `regex_agrupamentoindex` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `entrada` varchar(1000) NOT NULL,
  `valor` varchar(1000) DEFAULT NULL,
  `agrupamento_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `regex_agrupamentoindex_entrada_f416f6fd` (`entrada`),
  KEY `regex_agrupamentoindex_valor_49655e75` (`valor`),
  KEY `regex_agrupamentoindex_agrupamento_id_0a1fdacf` (`agrupamento_id`)
) ENGINE=MyISAM AUTO_INCREMENT=358 DEFAULT CHARSET=latin1;


DROP TABLE IF EXISTS `regex_casoteste`;
CREATE TABLE IF NOT EXISTS `regex_casoteste` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `data_caso_teste` datetime(6) NOT NULL,
  `programa_o_id` bigint(20) NOT NULL,
  `programa_p_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `regex_casoteste_fk_programa_o_id_ee2fec4e` (`programa_o_id`),
  KEY `regex_casoteste_fk_programa_p_id_bf261f00` (`programa_p_id`)
) ENGINE=MyISAM AUTO_INCREMENT=37 DEFAULT CHARSET=latin1;


DROP TABLE IF EXISTS `regex_dadosteste`;
CREATE TABLE IF NOT EXISTS `regex_dadosteste` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `data` datetime(6) NOT NULL,
  `linha` varchar(1000) NOT NULL,
  `variavel_p` varchar(1000) NOT NULL,
  `dado_hexa_p` varchar(1000) NOT NULL,
  `teste_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `regex_dadosteste_fk_teste_id_4105eae9` (`teste_id`)
) ENGINE=MyISAM AUTO_INCREMENT=103 DEFAULT CHARSET=latin1;


DROP TABLE IF EXISTS `regex_employee`;
CREATE TABLE IF NOT EXISTS `regex_employee` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `seu_codigo` varchar(1000) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;


DROP TABLE IF EXISTS `regex_programao`;
CREATE TABLE IF NOT EXISTS `regex_programao` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `dt_codificacao` datetime(6) NOT NULL,
  `codigo_o` varchar(1000) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=37 DEFAULT CHARSET=latin1;


DROP TABLE IF EXISTS `regex_programap`;
CREATE TABLE IF NOT EXISTS `regex_programap` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `dt_codificacao` datetime(6) NOT NULL,
  `codigo_p` varchar(1000) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=37 DEFAULT CHARSET=latin1;


DROP TABLE IF EXISTS `regex_testedemesa`;
CREATE TABLE IF NOT EXISTS `regex_testedemesa` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `data_teste` datetime(6) NOT NULL,
  `caso_teste_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `regex_testedemesa_fk_caso_teste_id_7889b305` (`caso_teste_id`)
) ENGINE=MyISAM AUTO_INCREMENT=37 DEFAULT CHARSET=latin1;
