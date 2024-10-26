-- MySQL dump 10.13  Distrib 8.0.39, for Linux (x86_64)
--
-- Host: localhost    Database: financial_data
-- ------------------------------------------------------
-- Server version	8.0.39-0ubuntu0.24.04.2

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `CAL`
--

DROP TABLE IF EXISTS `CAL`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `CAL` (
  `adsh` char(20) NOT NULL,
  `grp` tinyint NOT NULL,
  `arc` tinyint NOT NULL,
  `negative` tinyint(1) NOT NULL,
  `ptag` varchar(256) NOT NULL,
  `pversion` varchar(20) NOT NULL,
  `ctag` varchar(256) NOT NULL,
  `cversion` varchar(20) NOT NULL,
  PRIMARY KEY (`adsh`,`grp`,`arc`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `CAL`
--

LOCK TABLES `CAL` WRITE;
/*!40000 ALTER TABLE `CAL` DISABLE KEYS */;
/*!40000 ALTER TABLE `CAL` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `DIM`
--

DROP TABLE IF EXISTS `DIM`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `DIM` (
  `dimhash` char(32) NOT NULL,
  `segments` varchar(1024) NOT NULL,
  `segt` tinyint(1) NOT NULL,
  PRIMARY KEY (`dimhash`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `DIM`
--

LOCK TABLES `DIM` WRITE;
/*!40000 ALTER TABLE `DIM` DISABLE KEYS */;
/*!40000 ALTER TABLE `DIM` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `NUM`
--

DROP TABLE IF EXISTS `NUM`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `NUM` (
  `adsh` char(20) NOT NULL,
  `tag` varchar(256) NOT NULL,
  `version` varchar(20) NOT NULL,
  `ddate` date NOT NULL,
  `qtrs` int NOT NULL,
  `uom` varchar(20) NOT NULL,
  `dimh` char(32) NOT NULL,
  `iprx` int NOT NULL,
  `value` decimal(20,4) DEFAULT NULL,
  `footnote` varchar(512) DEFAULT NULL,
  `footlen` int NOT NULL,
  `dimn` tinyint DEFAULT NULL,
  `coreg` varchar(256) DEFAULT NULL,
  `durp` float NOT NULL,
  `datp` float NOT NULL,
  `dcml` smallint NOT NULL,
  PRIMARY KEY (`adsh`,`tag`,`version`,`ddate`,`qtrs`,`uom`,`dimh`,`iprx`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `NUM`
--

LOCK TABLES `NUM` WRITE;
/*!40000 ALTER TABLE `NUM` DISABLE KEYS */;
/*!40000 ALTER TABLE `NUM` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `PRE`
--

DROP TABLE IF EXISTS `PRE`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `PRE` (
  `adsh` char(20) NOT NULL,
  `report` int NOT NULL,
  `line` int NOT NULL,
  `stmt` char(2) NOT NULL,
  `inpth` tinyint(1) NOT NULL,
  `tag` varchar(256) NOT NULL,
  `version` varchar(20) NOT NULL,
  `prole` varchar(50) NOT NULL,
  `plabel` varchar(512) NOT NULL,
  `negating` tinyint(1) NOT NULL,
  PRIMARY KEY (`adsh`,`report`,`line`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `PRE`
--

LOCK TABLES `PRE` WRITE;
/*!40000 ALTER TABLE `PRE` DISABLE KEYS */;
/*!40000 ALTER TABLE `PRE` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `REN`
--

DROP TABLE IF EXISTS `REN`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `REN` (
  `adsh` char(20) NOT NULL,
  `report` int NOT NULL,
  `rfile` char(1) NOT NULL,
  `menucat` char(2) DEFAULT NULL,
  `shortname` varchar(512) NOT NULL,
  `longname` varchar(512) NOT NULL,
  `roleuri` varchar(255) NOT NULL,
  `parentroleuri` varchar(255) DEFAULT NULL,
  `parentreport` int DEFAULT NULL,
  `ultparentrpt` int DEFAULT NULL,
  PRIMARY KEY (`adsh`,`report`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `REN`
--

LOCK TABLES `REN` WRITE;
/*!40000 ALTER TABLE `REN` DISABLE KEYS */;
/*!40000 ALTER TABLE `REN` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `SUB`
--

DROP TABLE IF EXISTS `SUB`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `SUB` (
  `adsh` char(20) NOT NULL,
  `cik` int NOT NULL,
  `name` varchar(150) NOT NULL,
  `sic` int DEFAULT NULL,
  `countryba` char(2) NOT NULL,
  `stprba` char(2) DEFAULT NULL,
  `cityba` varchar(30) NOT NULL,
  `zipba` varchar(10) DEFAULT NULL,
  `bas1` varchar(40) DEFAULT NULL,
  `bas2` varchar(40) DEFAULT NULL,
  `baph` varchar(12) DEFAULT NULL,
  `countryma` char(2) DEFAULT NULL,
  `stprma` char(2) DEFAULT NULL,
  `cityma` varchar(30) DEFAULT NULL,
  `zipma` varchar(10) DEFAULT NULL,
  `mas1` varchar(40) DEFAULT NULL,
  `mas2` varchar(40) DEFAULT NULL,
  `countryinc` char(2) NOT NULL,
  `stprinc` char(2) DEFAULT NULL,
  `ein` char(10) DEFAULT NULL,
  `former` varchar(150) DEFAULT NULL,
  `changed` char(8) DEFAULT NULL,
  `afs` char(5) DEFAULT NULL,
  `wksi` tinyint(1) NOT NULL,
  `fye` char(4) NOT NULL,
  `form` varchar(20) NOT NULL,
  `period` date NOT NULL,
  `fy` year NOT NULL,
  `fp` char(2) NOT NULL,
  `filed` date NOT NULL,
  `accepted` datetime NOT NULL,
  `prevrpt` tinyint(1) NOT NULL,
  `detail` tinyint(1) NOT NULL,
  `instance` varchar(32) NOT NULL,
  `nciks` int NOT NULL,
  `aciks` varchar(120) DEFAULT NULL,
  `pubfloatusd` decimal(15,2) DEFAULT NULL,
  `floatdate` date DEFAULT NULL,
  `floataxis` varchar(255) DEFAULT NULL,
  `floatmems` int DEFAULT NULL,
  PRIMARY KEY (`adsh`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `SUB`
--

LOCK TABLES `SUB` WRITE;
/*!40000 ALTER TABLE `SUB` DISABLE KEYS */;
/*!40000 ALTER TABLE `SUB` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `TAG`
--

DROP TABLE IF EXISTS `TAG`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `TAG` (
  `tag` varchar(256) NOT NULL,
  `version` varchar(20) NOT NULL,
  `custom` tinyint(1) NOT NULL,
  `abstract` tinyint(1) NOT NULL,
  `datatype` varchar(20) DEFAULT NULL,
  `iord` char(1) NOT NULL,
  `crdr` char(1) DEFAULT NULL,
  `tlabel` varchar(512) DEFAULT NULL,
  `doc` varchar(2048) DEFAULT NULL,
  PRIMARY KEY (`tag`,`version`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `TAG`
--

LOCK TABLES `TAG` WRITE;
/*!40000 ALTER TABLE `TAG` DISABLE KEYS */;
/*!40000 ALTER TABLE `TAG` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `TXT`
--

DROP TABLE IF EXISTS `TXT`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `TXT` (
  `adsh` char(20) NOT NULL,
  `tag` varchar(256) NOT NULL,
  `version` varchar(20) NOT NULL,
  `ddate` date NOT NULL,
  `qtrs` int NOT NULL,
  `iprx` int NOT NULL,
  `lang` varchar(5) NOT NULL,
  `dcml` smallint NOT NULL,
  `durp` float NOT NULL,
  `datp` float NOT NULL,
  `dimh` char(32) NOT NULL,
  `dimn` tinyint DEFAULT NULL,
  `coreg` varchar(256) DEFAULT NULL,
  `escaped` tinyint(1) NOT NULL,
  `srclen` smallint NOT NULL,
  `txtlen` smallint DEFAULT NULL,
  `footnote` varchar(512) DEFAULT NULL,
  `footlen` smallint DEFAULT NULL,
  `context` varchar(255) NOT NULL,
  `value` varchar(2048) DEFAULT NULL,
  PRIMARY KEY (`adsh`,`tag`,`version`,`ddate`,`qtrs`,`iprx`,`dimh`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `TXT`
--

LOCK TABLES `TXT` WRITE;
/*!40000 ALTER TABLE `TXT` DISABLE KEYS */;
/*!40000 ALTER TABLE `TXT` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-10-25 12:50:21
