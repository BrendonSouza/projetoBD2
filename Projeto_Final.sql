CREATE DATABASE  IF NOT EXISTS `bd_metrica_ate` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;
USE `bd_metrica_ate`;
-- MariaDB dump 10.19  Distrib 10.4.24-MariaDB, for Win64 (AMD64)
--
-- Host: 127.0.0.1    Database: bd_metrica_ate
-- ------------------------------------------------------
-- Server version	10.4.24-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `caso_teste`
--

DROP TABLE IF EXISTS `caso_teste`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `caso_teste` (
  `id_ct` int(11) NOT NULL AUTO_INCREMENT,
  `id_po` int(11) DEFAULT NULL,
  `id_pp` int(11) DEFAULT NULL,
  PRIMARY KEY (`id_ct`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `dados_tm_o`
--

DROP TABLE IF EXISTS `dados_tm_o`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dados_tm_o` (
  `id_dados` int(11) NOT NULL AUTO_INCREMENT,
  `variavel` text DEFAULT NULL,
  `valor` text DEFAULT NULL,
  `id_tm` int(11) DEFAULT NULL,
  `id_linha` int(11) DEFAULT NULL,
  PRIMARY KEY (`id_dados`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `dados_tm_p`
--

DROP TABLE IF EXISTS `dados_tm_p`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dados_tm_p` (
  `id_dados` int(11) NOT NULL AUTO_INCREMENT,
  `variavel` text DEFAULT NULL,
  `valor` text DEFAULT NULL,
  `id_tm` int(11) DEFAULT NULL,
  `id_linha` int(11) DEFAULT NULL,
  PRIMARY KEY (`id_dados`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `linha`
--

DROP TABLE IF EXISTS `linha`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `linha` (
  `id_linha` int(11) NOT NULL AUTO_INCREMENT,
  `numero` int(11) DEFAULT NULL,
  `codigo` text DEFAULT NULL,
  PRIMARY KEY (`id_linha`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `programa_o`
--

DROP TABLE IF EXISTS `programa_o`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `programa_o` (
  `id_po` int(11) NOT NULL AUTO_INCREMENT,
  `data_codificacao` varchar(20) DEFAULT NULL,
  `codigo` text DEFAULT NULL,
  PRIMARY KEY (`id_po`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `programa_p`
--

DROP TABLE IF EXISTS `programa_p`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `programa_p` (
  `id_pp` int(11) NOT NULL AUTO_INCREMENT,
  `data_codificacao` varchar(20) DEFAULT NULL,
  `codigo` text DEFAULT NULL,
  PRIMARY KEY (`id_pp`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `teste_mesa`
--

DROP TABLE IF EXISTS `teste_mesa`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `teste_mesa` (
  `id_tm` int(11) NOT NULL AUTO_INCREMENT,
  `id_ct` int(11) DEFAULT NULL,
  `data_tm` datetime DEFAULT NULL,
  PRIMARY KEY (`id_tm`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping events for database 'bd_metrica_ate'
--

--
-- Dumping routines for database 'bd_metrica_ate'
--
/*!50003 DROP PROCEDURE IF EXISTS `deleta_tm` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'NO_ZERO_IN_DATE,NO_ZERO_DATE,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `deleta_tm`(IN p_id_tm INT)
BEGIN

DELETE FROM programa_o WHERE id_po IN (SELECT id_po FROM caso_teste WHERE id_ct IN (SELECT id_ct FROM teste_mesa WHERE id_tm = p_id_tm));
DELETE FROM programa_p WHERE id_pp IN (SELECT id_pp FROM caso_teste WHERE id_ct IN (SELECT id_ct FROM teste_mesa WHERE id_tm = p_id_tm));
DELETE FROM caso_teste WHERE id_ct IN (SELECT id_ct FROM teste_mesa WHERE id_tm = p_id_tm);
DELETE FROM linha WHERE id_linha IN (SELECT id_linha FROM dados_tm_o WHERE id_tm = p_id_tm);
DELETE FROM linha WHERE id_linha IN (SELECT id_linha FROM dados_tm_P WHERE id_tm = p_id_tm);
DELETE FROM dados_tm_o WHERE id_tm = p_id_tm;
DELETE FROM dados_tm_p WHERE id_tm = p_id_tm;
DELETE FROM teste_mesa WHERE id_tm = p_id_tm;

END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `insere_dados` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'NO_ZERO_IN_DATE,NO_ZERO_DATE,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `insere_dados`(IN p_var TEXT, IN p_value TEXT, IN p_id_tm INT, IN p_id_linha INT, IN p_c INT)
BEGIN

IF p_c = 0 THEN
	INSERT INTO dados_tm_o (variavel, valor, id_tm, id_linha) VALUES (p_var, p_value, p_id_tm, p_id_linha);
ELSE 
	INSERT INTO dados_tm_p (variavel, valor, id_tm, id_linha) VALUES (p_var, p_value, p_id_tm, p_id_linha);
END IF;

END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-07-14 23:57:33
