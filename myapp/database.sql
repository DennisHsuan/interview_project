-- --------------------------------------------------------
-- 主機:                           127.0.0.1
-- 伺服器版本:                        10.8.3-MariaDB - mariadb.org binary distribution
-- 伺服器作業系統:                      Win64
-- HeidiSQL 版本:                  11.3.0.6295
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- 傾印 interview 的資料庫結構
CREATE DATABASE IF NOT EXISTS `interview` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci */;
USE `interview`;

-- 傾印  資料表 interview.myapp_productmodel 結構
CREATE TABLE IF NOT EXISTS `myapp_productmodel` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `pname` varchar(30) COLLATE utf8mb4_unicode_ci NOT NULL,
  `pprice` int(11) NOT NULL,
  `pimage` varchar(40) COLLATE utf8mb4_unicode_ci NOT NULL,
  `pdescription` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- 正在傾印表格  interview.myapp_productmodel 的資料：~0 rows (近似值)
DELETE FROM `myapp_productmodel`;
/*!40000 ALTER TABLE `myapp_productmodel` DISABLE KEYS */;
INSERT INTO `myapp_productmodel` (`id`, `pname`, `pprice`, `pimage`, `pdescription`) VALUES
	(1, '美式咖啡', 50, 'americano.png', '低卡路里、燃燒脂肪、有助去水腫、促進腸胃魯動'),
	(2, '卡布奇諾', 75, 'cappuccino.png', '奶泡多，牛奶比例少，咖啡的味道較明顯'),
	(3, '拿鐵', 60, 'latte.png', '牛奶多，像是帶著咖啡味道的牛奶，咖啡味較為淡之，但口感十分柔順絲滑'),
	(4, '摩卡咖啡', 80, 'mocha.png', '拿鐵和摩卡咖啡最大的區別在於它是否含有巧克力糖漿');
/*!40000 ALTER TABLE `myapp_productmodel` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
