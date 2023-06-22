-- MySQL dump 10.13  Distrib 5.7.17, for Win64 (x86_64)
--
-- Host: localhost    Database: TRUONGHOC1
-- ------------------------------------------------------
-- Server version	5.7.20-log

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
DROP DATABASE IF EXISTS `TRUONGHOC1`;
CREATE DATABASE IF NOT EXISTS `TRUONGHOC1` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `TRUONGHOC1`;

--
-- Table structure for table `TRUONG`
--

DROP TABLE IF EXISTS `TRUONG`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `TRUONG` (
  `MATR` varchar(7) NOT NULL,
  `TENTR` varchar(100) NOT NULL,
  `DCHITR` varchar(300) DEFAULT NULL,
  PRIMARY KEY (`MATR`)    -- CLUSTERED INDEX
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `HS`
--

DROP TABLE IF EXISTS `HS`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `HS` (
  `MAHS` varchar(8) NOT NULL,
  `HO` varchar(30) DEFAULT NULL,
  `TEN` varchar(30) DEFAULT NULL,
  `CCCD` varchar(12) DEFAULT NULL,
  `NTNS` date DEFAULT NULL,
  `DCHI_HS` varchar(300) DEFAULT NULL,
  PRIMARY KEY (`MAHS`),         -- CLUSTERED INDEX
  UNIQUE (`CCCD`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `HOC`
--

DROP TABLE IF EXISTS `HOC`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `HOC` (
  `MATR` varchar(7) NOT NULL,
  `MAHS` varchar(8) NOT NULL,
  `NAMHOC` varchar(10) NOT NULL,
  `DIEMTB` real DEFAULT NULL,
  `XEPLOAI` varchar(20) DEFAULT NULL,
  `KQUA` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`MATR`, `MAHS`, `NAMHOC`), -- CLUSTERED INDEX
  FOREIGN KEY (`MATR`) REFERENCES `TRUONG` (`MATR`),
  FOREIGN KEY (`MAHS`) REFERENCES `HS` (`MAHS`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


