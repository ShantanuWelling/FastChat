-- MySQL dump 10.13  Distrib 8.0.31, for macos13.0 (arm64)
--
-- Host: localhost    Database: FASTCHAT
-- ------------------------------------------------------
-- Server version	8.0.31

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
-- Current Database: `FASTCHAT`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `FASTCHAT` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `FASTCHAT`;

--
-- Table structure for table `CLIENTS`
--

DROP TABLE IF EXISTS `CLIENTS`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `CLIENTS` (
  `name` varchar(255) NOT NULL,
  `password` varchar(255) DEFAULT NULL,
  `port` int DEFAULT NULL,
  `pkey` longtext,
  PRIMARY KEY (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `CLIENTS`
--

LOCK TABLES `CLIENTS` WRITE;
/*!40000 ALTER TABLE `CLIENTS` DISABLE KEYS */;
INSERT INTO `CLIENTS` VALUES ('GH0','6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b',6924,'Krwd0TakKiXhKnUK'),('GH1','6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b',6924,'Z823z7UfLkQkSHTx');
/*!40000 ALTER TABLE `CLIENTS` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `GROUP1`
--

DROP TABLE IF EXISTS `GROUP1`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `GROUP1` (
  `groupname` varchar(255) DEFAULT NULL,
  `admin` varchar(255) DEFAULT NULL,
  `member` longtext
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `GROUP1`
--

LOCK TABLES `GROUP1` WRITE;
/*!40000 ALTER TABLE `GROUP1` DISABLE KEYS */;
/*!40000 ALTER TABLE `GROUP1` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `IMAGES`
--

DROP TABLE IF EXISTS `IMAGES`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `IMAGES` (
  `sender` varchar(255) DEFAULT NULL,
  `reciever` varchar(255) DEFAULT NULL,
  `message` longtext
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `IMAGES`
--

LOCK TABLES `IMAGES` WRITE;
/*!40000 ALTER TABLE `IMAGES` DISABLE KEYS */;
/*!40000 ALTER TABLE `IMAGES` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `OFFLINE`
--

DROP TABLE IF EXISTS `OFFLINE`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `OFFLINE` (
  `sender` varchar(255) DEFAULT NULL,
  `reciever` varchar(255) DEFAULT NULL,
  `message` longtext
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `OFFLINE`
--

LOCK TABLES `OFFLINE` WRITE;
/*!40000 ALTER TABLE `OFFLINE` DISABLE KEYS */;
/*!40000 ALTER TABLE `OFFLINE` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `PORTS`
--

DROP TABLE IF EXISTS `PORTS`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `PORTS` (
  `portnumber` int NOT NULL,
  `numcon` int DEFAULT NULL,
  `connected` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`portnumber`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `PORTS`
--

LOCK TABLES `PORTS` WRITE;
/*!40000 ALTER TABLE `PORTS` DISABLE KEYS */;
INSERT INTO `PORTS` VALUES (6924,1,'T'),(6925,0,'F'),(6926,0,'F'),(6927,0,'F'),(6928,0,'F');
/*!40000 ALTER TABLE `PORTS` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `TIME`
--

DROP TABLE IF EXISTS `TIME`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `TIME` (
  `message` longtext,
  `time` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `TIME`
--

LOCK TABLES `TIME` WRITE;
/*!40000 ALTER TABLE `TIME` DISABLE KEYS */;
INSERT INTO `TIME` VALUES ('GH0: hello','17:18:19.262762'),('GH0: hello','17:18:19.262966'),('GH1: hello','17:18:19.263006'),('GH1: hello','17:18:19.262781'),('GH1: hello0','17:18:19.287870'),('GH1: hello1','17:18:19.308876'),('GH1: hello2','17:18:19.330713'),('GH1: hello3','17:18:19.352796'),('GH1: hello4','17:18:19.377979'),('GH1: hello0','17:18:20.345644'),('GH0: hello0','17:18:20.371421'),('GH0: hello1','17:18:20.400482'),('GH0: hello2','17:18:20.421965'),('GH0: hello3','17:18:20.444220'),('GH0: hello4','17:18:20.465246');
/*!40000 ALTER TABLE `TIME` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-11-25 17:23:23
