-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 172.17.0.2
-- Generation Time: Jul 11, 2022 at 02:06 PM
-- Server version: 8.0.29
-- PHP Version: 8.0.20

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `teste_de_mesa`
--

DELIMITER $$
--
-- Procedures
--
CREATE DEFINER=`root`@`%` PROCEDURE `insere_metricas` (IN `variavel_o` TEXT, IN `valor_o` TEXT, IN `linha_o` TEXT, IN `variavel_p` TEXT, IN `valor_p` TEXT, IN `linha_p` TEXT, IN `apelido_teste` TEXT)   BEGIN
DECLARE id_teste int;
SET id_teste = (SELECT id FROM tbl_programa_o po where po.nome_teste_de_mesa = apelido_teste);
INSERT INTO tbl_metricas(variavel_o,valor_hexa_o,linha_o,variavel_p,valor_hexa_p,linha_p,id_teste_de_mesa) VALUES (variavel_o,valor_o,linha_o,variavel_p,valor_p,linha_p,id_teste);
END$$

CREATE DEFINER=`root`@`%` PROCEDURE `insere_programa_o` (`programa_o` TEXT, `apelido` TEXT)   BEGIN
INSERT INTO tbl_programa_o (codigo_programa_o,nome_teste_de_mesa) VALUES (programa_o, apelido);
END$$

CREATE DEFINER=`root`@`%` PROCEDURE `insere_programa_p` (`programa_p` TEXT, `apelido` TEXT)   BEGIN
INSERT INTO tbl_programa_p (codigo_programa_p,nome_teste_de_mesa) VALUES (programa_p, apelido);
END$$

CREATE DEFINER=`root`@`%` PROCEDURE `insere_teste_de_mesa` (IN `teste_apelido` TEXT)   BEGIN

DECLARE id_programa_o INT;
DECLARE id_programa_p INT;

SET id_programa_o = (SELECT id FROM tbl_programa_o po where po.nome_teste_de_mesa = teste_apelido);
SET id_programa_p = (
SELECT id FROM tbl_programa_p pp where pp.nome_teste_de_mesa = teste_apelido);
INSERT INTO tbl_teste_de_mesa(programa_o_id, programa_p_id) VALUES(id_programa_o, id_programa_p);

END$$

DELIMITER ;

-- --------------------------------------------------------

--
-- Table structure for table `tbl_metricas`
--

CREATE TABLE `tbl_metricas` (
  `id` int NOT NULL,
  `variavel_o` text NOT NULL,
  `valor_hexa_o` text NOT NULL,
  `variavel_p` text NOT NULL,
  `valor_hexa_p` text NOT NULL,
  `linha_p` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci,
  `id_teste_de_mesa` int NOT NULL,
  `linha_o` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `tbl_metricas`
--

INSERT INTO `tbl_metricas` (`id`, `variavel_o`, `valor_hexa_o`, `variavel_p`, `valor_hexa_p`, `linha_p`, `id_teste_de_mesa`, `linha_o`) VALUES
(1, 'teste', '1', 'teste', '2', 'var teste =2', 4, 'var teste =1');

-- --------------------------------------------------------

--
-- Table structure for table `tbl_programa_o`
--

CREATE TABLE `tbl_programa_o` (
  `id` int NOT NULL,
  `codigo_programa_o` text NOT NULL,
  `criado_em` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `nome_teste_de_mesa` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `tbl_programa_o`
--

INSERT INTO `tbl_programa_o` (`id`, `codigo_programa_o`, `criado_em`, `nome_teste_de_mesa`) VALUES
(4, 'var teste =1', '2022-07-11 14:00:36', 'teste 5');

-- --------------------------------------------------------

--
-- Table structure for table `tbl_programa_p`
--

CREATE TABLE `tbl_programa_p` (
  `id` int NOT NULL,
  `codigo_programa_p` text NOT NULL,
  `criado_em` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `nome_teste_de_mesa` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `tbl_programa_p`
--

INSERT INTO `tbl_programa_p` (`id`, `codigo_programa_p`, `criado_em`, `nome_teste_de_mesa`) VALUES
(4, 'var teste =2', '2022-07-11 14:00:36', 'teste 5');

-- --------------------------------------------------------

--
-- Table structure for table `tbl_teste_de_mesa`
--

CREATE TABLE `tbl_teste_de_mesa` (
  `id` int NOT NULL,
  `criado_em` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `programa_o_id` int NOT NULL,
  `programa_p_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `tbl_teste_de_mesa`
--

INSERT INTO `tbl_teste_de_mesa` (`id`, `criado_em`, `programa_o_id`, `programa_p_id`) VALUES
(4, '2022-07-11 14:00:36', 4, 4);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `tbl_metricas`
--
ALTER TABLE `tbl_metricas`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_teste_de_mesa_id` (`id_teste_de_mesa`);

--
-- Indexes for table `tbl_programa_o`
--
ALTER TABLE `tbl_programa_o`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `nome` (`nome_teste_de_mesa`);

--
-- Indexes for table `tbl_programa_p`
--
ALTER TABLE `tbl_programa_p`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `nome` (`nome_teste_de_mesa`);

--
-- Indexes for table `tbl_teste_de_mesa`
--
ALTER TABLE `tbl_teste_de_mesa`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_programa_o_id` (`programa_o_id`),
  ADD KEY `fk_programa_p_id` (`programa_p_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `tbl_metricas`
--
ALTER TABLE `tbl_metricas`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `tbl_programa_o`
--
ALTER TABLE `tbl_programa_o`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `tbl_programa_p`
--
ALTER TABLE `tbl_programa_p`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `tbl_teste_de_mesa`
--
ALTER TABLE `tbl_teste_de_mesa`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `tbl_teste_de_mesa`
--
ALTER TABLE `tbl_teste_de_mesa`
  ADD CONSTRAINT `fk_programa_o_id` FOREIGN KEY (`programa_o_id`) REFERENCES `tbl_programa_o` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_programa_p_id` FOREIGN KEY (`programa_p_id`) REFERENCES `tbl_programa_p` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
