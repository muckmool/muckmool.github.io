-- MySQL dump 10.13  Distrib 8.0.28, for Win64 (x86_64)
--
-- Host: localhost    Database: db_test
-- ------------------------------------------------------
-- Server version	8.0.28

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `book1`
--

DROP TABLE IF EXISTS `book1`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `book1` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `SEQ` int DEFAULT NULL,
  `YEAR` varchar(45) DEFAULT NULL,
  `MONTH` varchar(45) DEFAULT NULL,
  `DAY` varchar(45) DEFAULT NULL,
  `COUNT` varchar(45) DEFAULT NULL,
  `B_HANJA` varchar(300) DEFAULT NULL,
  `UM` varchar(300) DEFAULT NULL,
  `B_HANGUL` varchar(300) DEFAULT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `ID_UNIQUE` (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `book1`
--

LOCK TABLES `book1` WRITE;
/*!40000 ALTER TABLE `book1` DISABLE KEYS */;
INSERT INTO `book1` VALUES (1,1,'1592','1','1','1','初一日壬戌。晴。曉。舍弟汝弼及姪子菶，豚薈來話。但離天只。再過南中。不勝懷恨之至。○兵使軍官李敬信。來納兵使簡及歲物，長片箭雜物。','초일일임술。청。효。사제여필급질자봉，돈회래화。단리천지。재과남중。불승회한지지。○병사군관리경신。래납병사간급세물，장편전잡물。','초일일 임술. 맑음. 새벽에 동생 여필, 조카 봉, 아들 회가 와서 이야기했다. 어머니를 떠나 다시 이 남쪽에서 지내니 어머니를 보고 싶은 마음 이기지 못하겠다. 병사군관 이경신이 병사의 편지와 새해선물로 장편전 등의 물건을 가지고 왔다.'),(2,2,'1592','1','2','1','初二日癸亥。晴。以國忌不坐。與金仁甫話。','초이일계해。청。이국기불좌。여김인보화。','2일 계해. 맑음. 국가의 기념일이라 공무를 보지 않았다. 김인보와 같이 이야기 했다.'),(3,3,'1592','1','3','1','初三日甲子。晴。出東軒。別防點考。題送各官浦公事。','초삼일갑자。청。출동헌。별방점고。제송각관포공사。','3일 갑자. 맑음. 동헌에 나가 별방군을 점고하였다. 각 관포에 공문을 보냈다.'),(4,4,'1592','1','4','1','初四日乙丑。晴。坐東軒公事。','초사일을축。청。좌동헌공사。','4일 을축. 맑음. 동헌에 나가 공무를 보았다.'),(5,5,'1592','1','5','1','初五日丙寅。晴。仍在後東軒公事。','초오일병인。청。잉재후동헌공사。','5일 병인. 맑음. 후동헌에서 공무를 보았다.'),(6,6,'1592','1','6','1','初六日丁卯。晴。出東軒公事。','초륙일정묘。청。출동헌공사。','6일 정묘. 맑음. 동헌에 나가 공무를 보았다.'),(7,7,'1592','1','7','1','初七日戊辰。朝晴。晩雨雪交下終日。菶姪往牙山。○南原陪箋儒生入來。','초칠일무진。조청。만우설교하종일。봉질왕아산。○남원배전유생입래。',' 7일 무진. 아침에는 맑다가 저녁때가 되어 비와 눈이 교차하며 종일 내렸다. 조카 봉이 아산으로 갔다. 남원으로 전문을 가져갈 유생이 들어왔다.'),(8,8,'1592','1','8','1','初八日己巳。晴。出客舍東軒公事。','초팔일기사。청。출객사동헌공사。','8일 기사. 맑음. 객사동헌에 나가서 공무를 보았다.'),(9,9,'1592','1','9','1','初九日庚午。晴。早食後出客舍東軒。封箋文拜送','초구일경오。청。조식후출객사동헌。봉전문배송','9일 경오. 맑음. 아침을 먹은 후 객사동헌에 나갔다. 전문을 봉하여 보냈다.'),(10,10,'1592','1','10','1','初十日辛未。終日雨雨。防踏新僉使入來','초십일신미。종일우우。방답신첨사입래','10일 신미. 종일 비가 내렸다. 새로 온 방답첨사가 들어왔다.'),(11,11,'1592','1','11','1','十一日壬申。小雨終日。晩出東軒公事。李鳳壽往見先生院浮石處。來告已鑿穴大石十七塊云。西門外壕子四把許頹圮。○與沈士立話。','십일일임신。소우종일。만출동헌공사。리봉수왕견선생원부석처。래고이착혈대석십칠괴운。서문외호자사파허퇴비。○여침사립화。','11일. 임신. 종일 가는 비가 내렸다. 늦게 동헌에 나가 공무를 보았다. 이봉수가 선생원 부석처에 가서 보고와서 말했다. 구멍 뚫린 대석 17 덩이를 옮겼다고 했다. 서문 바깥 해자가 네 발이나 무너졌다고 한다. 침사립과 이야기 했다.'),(12,12,'1592','1','12','1','十二日癸酉。陰雨不霽。食後出客舍東軒。本營及各浦鎭撫優等試射','십이일계유。음우불제。식후출객사동헌。본영급각포진무우등시사','12일. 계유. 흐리고 비가 왔고 개지는 않았다. 식사 후에 객사동헌에 나갔다. 본영의 각 포 진무들의 활쏘기 우등을 가리는 시험을 실시했다.'),(13,13,'1592','1','13','1','十三日甲戌。朝陰。出東軒公事。','십삼일갑술。조음。출동헌공사。','13일 갑술. 아침에 흐림. 동헌에 나가 공무를 보았다.');
/*!40000 ALTER TABLE `book1` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-06-17 22:35:44
