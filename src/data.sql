-- MySQL dump 10.16  Distrib 10.1.26-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: db
-- ------------------------------------------------------
-- Server version	10.1.26-MariaDB-0+deb9u1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` varchar(0) DEFAULT NULL,
  `name` varchar(0) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` varchar(0) DEFAULT NULL,
  `group_id` varchar(0) DEFAULT NULL,
  `permission_id` varchar(0) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` tinyint(4) DEFAULT NULL,
  `content_type_id` tinyint(4) DEFAULT NULL,
  `codename` varchar(18) DEFAULT NULL,
  `name` varchar(23) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,1,'add_logentry','Can add log entry'),(2,1,'change_logentry','Can change log entry'),(3,1,'delete_logentry','Can delete log entry'),(4,1,'view_logentry','Can view log entry'),(5,2,'add_permission','Can add permission'),(6,2,'change_permission','Can change permission'),(7,2,'delete_permission','Can delete permission'),(8,2,'view_permission','Can view permission'),(9,3,'add_group','Can add group'),(10,3,'change_group','Can change group'),(11,3,'delete_group','Can delete group'),(12,3,'view_group','Can view group'),(13,4,'add_user','Can add user'),(14,4,'change_user','Can change user'),(15,4,'delete_user','Can delete user'),(16,4,'view_user','Can view user'),(17,5,'add_contenttype','Can add content type'),(18,5,'change_contenttype','Can change content type'),(19,5,'delete_contenttype','Can delete content type'),(20,5,'view_contenttype','Can view content type'),(21,6,'add_session','Can add session'),(22,6,'change_session','Can change session'),(23,6,'delete_session','Can delete session'),(24,6,'view_session','Can view session'),(25,7,'add_tweet','Can add tweet'),(26,7,'change_tweet','Can change tweet'),(27,7,'delete_tweet','Can delete tweet'),(28,7,'view_tweet','Can view tweet');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` tinyint(4) DEFAULT NULL,
  `password` varchar(78) DEFAULT NULL,
  `last_login` varchar(10) DEFAULT NULL,
  `is_superuser` tinyint(4) DEFAULT NULL,
  `username` varchar(8) DEFAULT NULL,
  `first_name` varchar(0) DEFAULT NULL,
  `email` varchar(0) DEFAULT NULL,
  `is_staff` tinyint(4) DEFAULT NULL,
  `is_active` tinyint(4) DEFAULT NULL,
  `date_joined` varchar(10) DEFAULT NULL,
  `last_name` varchar(0) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$180000$X0jI49JxZ3e4$JEQKrA04yGoygnquoPBfYKoB5YFTyGkmYtOq6FWfjRk=','2020-02-24',1,'shady','','',1,1,'2020-02-24',''),(2,'pbkdf2_sha256$150000$e5JKMwWnv4F5$o4AsoU36vTp3dVoXvCXfgZApyPzz1/3B+hzL/JOr3QI=','',0,'jotaro','','',1,1,'',''),(3,'pbkdf2_sha256$150000$0dzZrp4m9Yts$p9em5KCb+E1Q3rgxu6/cMIW3Fuqtcu2mJ7JK5Fqgnm4=','2020-04-11',1,'Hopsin01','','',1,1,'2020-03-19','');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` varchar(0) DEFAULT NULL,
  `user_id` varchar(0) DEFAULT NULL,
  `group_id` varchar(0) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` varchar(0) DEFAULT NULL,
  `user_id` varchar(0) DEFAULT NULL,
  `permission_id` varchar(0) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` tinyint(4) DEFAULT NULL,
  `action_time` varchar(10) DEFAULT NULL,
  `object_id` tinyint(4) DEFAULT NULL,
  `object_repr` varchar(140) DEFAULT NULL,
  `change_message` varchar(39) DEFAULT NULL,
  `content_type_id` tinyint(4) DEFAULT NULL,
  `user_id` tinyint(4) DEFAULT NULL,
  `action_flag` tinyint(4) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2020-02-28',1,'sdgtbhrntntntgdhn','[{\"added\": {}}]',7,1,1),(2,'2020-02-28',1,'sdgtbhrntntntgdhn','',7,1,3),(3,'2020-02-28',2,'gfjmymkymscscschslocslocsicjscjscjscjscjcojscojscojscjsocjpscojspocjspcjpcojspocjspcjcojspcjpsocjpcjoscjpsocjposcj[sck[pck[paxkqopxjqoihywiu','[{\"added\": {}}]',7,1,1),(4,'2020-02-28',2,'gfjmymkymscscschslocslocsicjscjscjscjscjcojscojscojscjsocjpscojspocjspcjpcojspocjspcjcojspcjpsocjpcjoscjpsocjposcj[sck[pck[paxkqopxjqoihywiu','[]',7,1,2),(5,'2020-02-28',3,'gggggggggggggggggggggggggggggggg','[{\"added\": {}}]',7,1,1),(6,'2020-02-29',4,'bhalo guu','[{\"added\": {}}]',7,1,1),(7,'2020-02-29',5,'abc','[{\"added\": {}}]',7,1,1),(8,'2020-02-29',5,'abc','',7,1,3),(9,'2020-02-29',6,'abc','[{\"added\": {}}]',7,1,1),(10,'2020-02-29',6,'abc','',7,1,3),(11,'2020-02-29',2,'jotaro','[{\"added\": {}}]',4,1,1),(12,'2020-02-29',10,'noriyaki kakeoyin 2222','[{\"changed\": {\"fields\": [\"User\"]}}]',7,1,2),(13,'2020-04-11',2,'jotaro','[{\"changed\": {\"fields\": [\"is_staff\"]}}]',4,3,2);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` tinyint(4) DEFAULT NULL,
  `app_label` varchar(12) DEFAULT NULL,
  `model` varchar(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(6,'sessions','session'),(7,'tweets','tweet');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` tinyint(4) DEFAULT NULL,
  `app` varchar(12) DEFAULT NULL,
  `name` varchar(40) DEFAULT NULL,
  `applied` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2020-02-24'),(2,'auth','0001_initial','2020-02-24'),(3,'admin','0001_initial','2020-02-24'),(4,'admin','0002_logentry_remove_auto_add','2020-02-24'),(5,'admin','0003_logentry_add_action_flag_choices','2020-02-24'),(6,'contenttypes','0002_remove_content_type_name','2020-02-24'),(7,'auth','0002_alter_permission_name_max_length','2020-02-24'),(8,'auth','0003_alter_user_email_max_length','2020-02-24'),(9,'auth','0004_alter_user_username_opts','2020-02-24'),(10,'auth','0005_alter_user_last_login_null','2020-02-24'),(11,'auth','0006_require_contenttypes_0002','2020-02-24'),(12,'auth','0007_alter_validators_add_error_messages','2020-02-24'),(13,'auth','0008_alter_user_username_max_length','2020-02-24'),(14,'auth','0009_alter_user_last_name_max_length','2020-02-24'),(15,'auth','0010_alter_group_name_max_length','2020-02-24'),(16,'auth','0011_update_proxy_permissions','2020-02-24'),(17,'sessions','0001_initial','2020-02-24'),(18,'tweets','0001_initial','2020-02-28'),(19,'tweets','0002_auto_20200228_1507','2020-02-28'),(20,'tweets','0003_auto_20200228_1515','2020-02-28'),(21,'tweets','0004_tweet_user','2020-02-28'),(22,'tweets','0005_auto_20200228_1522','2020-02-28'),(23,'tweets','0006_auto_20200229_0724','2020-02-29'),(24,'tweets','0007_auto_20200411_2129','2020-04-11');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(32) DEFAULT NULL,
  `session_data` varchar(252) DEFAULT NULL,
  `expire_date` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('zr19llesclatns8buj9s3p3wpp6qp2am','OTA1MGE0YzllNTFmMzJiNThhMGIzODQ2ZjAyM2M4MmU1NzczNGY4NTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI1ZTFmNjIwYWUzMTA3NTRlYWQ2ODEzOThjMDA4MzQ3ZTcwZTNlZmRiIn0=','2020-03-09'),('laacckccauqi20kgbmqwt3pt8gmgmfsx','YmM0YjlmZDFiMGIzZGJiYTQ1NDBlYjVkM2U5NDg2NjZlYmM4ZGMzMzp7Il9hdXRoX3VzZXJfaWQiOiIzIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI2NmJiYThmZDcyNzU5NWQ4Nzk3ZDY0M2U5NzA4OWI5YzMwNzEzMzgyIn0=','2020-04-02'),('kegji871zofia1s4uzdhx8ew0dwtc3d3','YmM0YjlmZDFiMGIzZGJiYTQ1NDBlYjVkM2U5NDg2NjZlYmM4ZGMzMzp7Il9hdXRoX3VzZXJfaWQiOiIzIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI2NmJiYThmZDcyNzU5NWQ4Nzk3ZDY0M2U5NzA4OWI5YzMwNzEzMzgyIn0=','2020-04-15'),('rze4gn6b9w5g9ysfue5idv496lm75p3h','YmM0YjlmZDFiMGIzZGJiYTQ1NDBlYjVkM2U5NDg2NjZlYmM4ZGMzMzp7Il9hdXRoX3VzZXJfaWQiOiIzIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI2NmJiYThmZDcyNzU5NWQ4Nzk3ZDY0M2U5NzA4OWI5YzMwNzEzMzgyIn0=','2020-04-25');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sqlite_sequence`
--

DROP TABLE IF EXISTS `sqlite_sequence`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sqlite_sequence` (
  `name` varchar(19) DEFAULT NULL,
  `seq` tinyint(4) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sqlite_sequence`
--

LOCK TABLES `sqlite_sequence` WRITE;
/*!40000 ALTER TABLE `sqlite_sequence` DISABLE KEYS */;
INSERT INTO `sqlite_sequence` VALUES ('django_migrations',24),('django_admin_log',13),('django_content_type',7),('auth_permission',28),('auth_user',3),('auth_group',0),('tweets_tweet',29);
/*!40000 ALTER TABLE `sqlite_sequence` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tweets_tweet`
--

DROP TABLE IF EXISTS `tweets_tweet`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tweets_tweet` (
  `id` tinyint(4) DEFAULT NULL,
  `timestamp` varchar(10) DEFAULT NULL,
  `updated` varchar(10) DEFAULT NULL,
  `user_id` tinyint(4) DEFAULT NULL,
  `content` varchar(140) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tweets_tweet`
--

LOCK TABLES `tweets_tweet` WRITE;
/*!40000 ALTER TABLE `tweets_tweet` DISABLE KEYS */;
INSERT INTO `tweets_tweet` VALUES (3,'2020-02-28','2020-02-28',1,'gggggggggggggggggggggggggggggggg'),(4,'2020-02-29','2020-02-29',1,'bhalo guu'),(6,'2020-02-29','2020-02-29',1,'rrrrrrrrrrrrrrrrrrrrrr'),(7,'2020-02-29','2020-02-29',1,'frogs are cool'),(8,'2020-02-29','2020-03-01',1,'EA sports To the GAMOOOOOOOOOOOOOOOOO'),(9,'2020-02-29','2020-03-01',1,'jon pierre polnarefu desu ja'),(10,'2020-02-29','2020-02-29',2,'noriyaki kakeoyin 2222'),(11,'2020-03-01','2020-03-01',1,'joseph joestar'),(12,'2020-03-01','2020-03-01',1,'jonathan joestar'),(13,'2020-03-01','2020-03-01',1,'kikipopo'),(14,'2020-03-19','2020-03-19',3,'lofi hiphop'),(15,'2020-04-01','2020-04-01',3,'mudamufamuda muda'),(16,'2020-04-01','2020-04-01',3,'BHALO ACHIS NAKI !!!!'),(17,'2020-04-01','2020-04-01',3,'BHALO ACHIS NAKI !!!!'),(18,'2020-04-01','2020-04-01',3,'Guu Kha'),(19,'2020-04-01','2020-04-01',3,'REEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE'),(20,'2020-04-02','2020-04-02',3,'kaku keno kalo'),(21,'2020-04-02','2020-04-02',3,'ANNTA TACHII'),(22,'2020-04-02','2020-04-02',3,'SYLVIA'),(23,'2020-04-02','2020-04-02',3,'GHEHE'),(24,'2020-04-02','2020-04-02',3,'Honto Des ?'),(25,'2020-04-03','2020-04-03',3,'chunchunmaru'),(26,'2020-04-03','2020-04-03',3,'sgsffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffggggggggggggg'),(27,'2020-04-03','2020-04-03',3,'ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff'),(28,'2020-04-03','2020-04-03',3,'fffffffffffffffffff'),(29,'2020-04-03','2020-04-03',3,'suigfisvgiugsigisugisfffnfhfghfhfghfghfghbfggggggggggggggggghhhhhhhhhhhhhhhhhhhhhhhhdfffffffffffffffffffffffffffhhhhhhhhhhhhhhhhhhhhhhhhhhhh');
/*!40000 ALTER TABLE `tweets_tweet` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-08-22 15:20:28
