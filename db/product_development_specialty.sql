-- MySQL dump 10.13  Distrib 8.0.16, for Win64 (x86_64)
--
-- Host: localhost    Database: product_development
-- ------------------------------------------------------
-- Server version	8.0.16

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `specialty`
--

DROP TABLE IF EXISTS `specialty`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `specialty` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=91 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `specialty`
--

LOCK TABLES `specialty` WRITE;
/*!40000 ALTER TABLE `specialty` DISABLE KEYS */;
INSERT INTO `specialty` VALUES (1,'Clinical Social Worker'),(2,'Internist'),(3,'General Practitioner'),(4,'Dentist'),(5,'Family Physician'),(6,'Neurosurgeon'),(7,'Oncologist'),(8,'Otolaryngologist'),(9,'Family Nurse Practitioner'),(10,'Procedural Dermatologist'),(11,'Dermatologist'),(12,'Pediatric Nurse Practitioner'),(13,'Hepatologist'),(14,'Transplant Surgeon'),(15,'Endocrinologist'),(16,'Geriatrician'),(17,'Optometrist'),(18,'Pediatrician'),(19,'Pain Medicine Specialist'),(20,'Anesthesiologist'),(21,'Physician Assistant'),(22,'Chiropractor'),(23,'Gastroenterologist'),(24,'Rheumatologist'),(25,'Obstetrician and Gynecologist'),(26,'Urologist'),(27,'Oncological Surgeon'),(28,'Cardiologist'),(29,'Neurologist'),(30,'Critical Care Specialist'),(31,'Plastic Surgeon'),(32,'Gynecologist'),(33,'Nephrologist'),(34,'Infectious Disease Specialist'),(35,'Reproductive Endocrinologist'),(36,'Clinical Psychologist'),(37,'Counselor'),(38,'Mental Health Counselor'),(39,'Psychologist'),(40,'Allergist and Immunologist'),(41,'Orthopedic Surgeon'),(42,'Spinal Surgeon'),(43,'Hand Surgeon'),(44,'Surgeon'),(45,'Periodontist'),(46,'Addiction Medicine Specialist'),(47,'Nurse Practitioner'),(48,'Resident'),(49,'Pulmonologist'),(50,'Hematologist'),(51,'Psychiatrist'),(52,'Physical Medicine and Rehabilitation Specialist'),(53,'Oral and Maxillofacial Surgeon'),(54,'Specialist'),(55,'Colorectal Surgeon'),(56,'Neurophysiologist'),(57,'Sleep Medicine Specialist'),(58,'Ophthalmologist'),(59,'Hospitalist'),(60,'Physical Therapist'),(61,'Hematology and Oncology Specialist'),(62,'Occupational Therapist'),(63,'Emergency Physician'),(64,'Registered Nurse'),(65,'Audiologist'),(66,'Foot and Ankle Surgeon'),(67,'Podiatrist'),(68,'Obstetrician'),(69,'Endodontist'),(70,'Adult Health Nurse Practitioner'),(71,'Dietitian'),(72,'Psychiatric Nurse Practitioner'),(73,'Speech-Language Pathologist'),(74,'Preventive Medicine Specialist'),(75,'Orthodontist'),(76,'Occupational Medicine Specialist'),(77,'Independent Medical Examiner'),(78,'Nutritionist'),(79,'Pathologist'),(80,'Radiologist'),(81,'Vascular Surgeon'),(82,'Legal Medicine Specialist'),(83,'Social Worker'),(84,'Cardiac Electrophysiologist'),(85,'Medical Physician Assistant'),(86,'Vision Therapist'),(87,'Cardiothoracic Surgeon'),(88,'Diagnostic Ultrasound Radiologist'),(89,'Neuroradiologist'),(90,'Nuclear Medicine Physician');
/*!40000 ALTER TABLE `specialty` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-06-17 19:31:49
