/*
SQLyog Community v13.1.6 (64 bit)
MySQL - 10.4.10-MariaDB : Database - bitvantage
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`bitvantage` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `bitvantage`;

/*Table structure for table `advisor` */

DROP TABLE IF EXISTS `advisor`;

CREATE TABLE `advisor` (
  `advisor_id` int(20) NOT NULL AUTO_INCREMENT,
  `login_id` int(20) DEFAULT NULL,
  `name` varchar(50) DEFAULT NULL,
  `place` varchar(50) DEFAULT NULL,
  `phone` varchar(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `work_exp` varchar(50) DEFAULT NULL,
  `proff_certificate` varchar(1000) DEFAULT NULL,
  PRIMARY KEY (`advisor_id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `advisor` */

insert  into `advisor`(`advisor_id`,`login_id`,`name`,`place`,`phone`,`email`,`work_exp`,`proff_certificate`) values 
(1,2,'Druvraj','Idukki','2255','druv@gmail.com','2 years','static/00bffba0-f363-48d7-aba0-e36497bfdf53BitVantage.pdf'),
(2,3,'gj','asa','sa','dd@gmail.com','de','static/00bffba0-f363-48d7-aba0-e36497bfdf53BitVantage.pdf'),
(3,4,'yg','hb','jb','dsd@gamil.com','y','static/00bffba0-f363-48d7-aba0-e36497bfdf53BitVantage.pdf'),
(4,10,'john wick','NY','9867453423','john@gmail.com','xoxo','static/bd42693d-a58f-4f17-93b9-31526f79444eproperty-slide-2.jpg');

/*Table structure for table `chat` */

DROP TABLE IF EXISTS `chat`;

CREATE TABLE `chat` (
  `chat_id` int(20) NOT NULL AUTO_INCREMENT,
  `sender_id` int(20) DEFAULT NULL,
  `receiver_id` int(20) DEFAULT NULL,
  `sender_type` varchar(50) DEFAULT NULL,
  `receiver_type` varchar(50) DEFAULT NULL,
  `message` varchar(50) DEFAULT NULL,
  `date` varchar(50) DEFAULT NULL,
  `time` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`chat_id`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `chat` */

insert  into `chat`(`chat_id`,`sender_id`,`receiver_id`,`sender_type`,`receiver_type`,`message`,`date`,`time`) values 
(1,1,1,'user','advisor','heloo','44','44'),
(2,1,1,'advisor','user','hii','2024-11-14','16:45:14'),
(3,1,1,'advisor','user','ok','2024-11-14','16:45:23'),
(4,1,1,'advisor','user','jhjhn','2024-11-19','15:36:38'),
(5,6,1,'user','advisor','ghfghgh','2024-11-21','14:43:51');

/*Table structure for table `complaint` */

DROP TABLE IF EXISTS `complaint`;

CREATE TABLE `complaint` (
  `complaint_id` int(20) NOT NULL AUTO_INCREMENT,
  `sender_id` int(20) DEFAULT NULL,
  `title` varchar(50) DEFAULT NULL,
  `description` varchar(50) DEFAULT NULL,
  `reply` varchar(50) DEFAULT NULL,
  `date` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`complaint_id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `complaint` */

insert  into `complaint`(`complaint_id`,`sender_id`,`title`,`description`,`reply`,`date`) values 
(1,2,'fdg','fg','okk','33'),
(2,2,'oop','pooop','we will take care of it','2024-11-13'),
(3,2,'jkjkfr','jebdheb','pending','2024-11-19'),
(4,6,'abcd','abcdefghi','pending','2024-11-20');

/*Table structure for table `fee` */

DROP TABLE IF EXISTS `fee`;

CREATE TABLE `fee` (
  `fee_id` int(20) NOT NULL AUTO_INCREMENT,
  `advisor_id` int(20) DEFAULT NULL,
  `amount` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`fee_id`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `fee` */

insert  into `fee`(`fee_id`,`advisor_id`,`amount`) values 
(2,1,'500'),
(3,1,'3000'),
(5,4,'10000');

/*Table structure for table `feedback` */

DROP TABLE IF EXISTS `feedback`;

CREATE TABLE `feedback` (
  `feedback_id` int(20) NOT NULL AUTO_INCREMENT,
  `sender_id` int(20) DEFAULT NULL,
  `feedback` varchar(50) DEFAULT NULL,
  `date` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`feedback_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `feedback` */

insert  into `feedback`(`feedback_id`,`sender_id`,`feedback`,`date`) values 
(1,6,'gooddddd','2024-11-20');

/*Table structure for table `inv_recomendations` */

DROP TABLE IF EXISTS `inv_recomendations`;

CREATE TABLE `inv_recomendations` (
  `inv_id` int(20) NOT NULL AUTO_INCREMENT,
  `advisor_id` int(20) DEFAULT NULL,
  `video` varchar(1000) DEFAULT NULL,
  `title` varchar(50) DEFAULT NULL,
  `description` varchar(50) DEFAULT NULL,
  `date` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`inv_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `inv_recomendations` */

insert  into `inv_recomendations`(`inv_id`,`advisor_id`,`video`,`title`,`description`,`date`) values 
(1,1,'static/fe5614c3-86c8-4493-aafd-57e97066e354reminder.png','ttttt','ddddddddddddd','2024-11-13'),
(2,1,'static/89d6db8a-61a0-4664-bd87-2c8b9658227512041412_1920_1080_25fps.mp4','hdjhs','djnd','2024-11-19');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `login_id` int(20) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL,
  `usertype` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=MyISAM AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`login_id`,`username`,`password`,`usertype`) values 
(1,'admin','admin','admin'),
(2,'druv','druv','advisor'),
(3,'as','s','rejected'),
(4,'gc','tfgf','advisor'),
(5,'user','user','user'),
(6,'bili','bili','user'),
(7,'jsjs','bssb','user'),
(8,'bili','bili','user'),
(9,'','','user'),
(10,'mr.wick','mr.wick','advisor');

/*Table structure for table `notification` */

DROP TABLE IF EXISTS `notification`;

CREATE TABLE `notification` (
  `notification_id` int(20) NOT NULL AUTO_INCREMENT,
  `sender_id` int(20) DEFAULT NULL,
  `notification` varchar(50) DEFAULT NULL,
  `date` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`notification_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `notification` */

insert  into `notification`(`notification_id`,`sender_id`,`notification`,`date`) values 
(1,1,'abcdefg','2024-11-13'),
(2,2,'tytytyty','2024-11-13'),
(3,1,'Bitcoin values increasing','2025-01-16');

/*Table structure for table `payment` */

DROP TABLE IF EXISTS `payment`;

CREATE TABLE `payment` (
  `payment_id` int(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(20) DEFAULT NULL,
  `advisor_id` int(20) DEFAULT NULL,
  `amount` varchar(50) DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  `date` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`payment_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `payment` */

insert  into `payment`(`payment_id`,`user_id`,`advisor_id`,`amount`,`status`,`date`) values 
(1,1,1,'100','paid','33'),
(2,2,1,'200','2024-11-21','paid'),
(3,2,1,'5000','2024-11-21','paid');

/*Table structure for table `rating` */

DROP TABLE IF EXISTS `rating`;

CREATE TABLE `rating` (
  `rating_id` int(20) NOT NULL AUTO_INCREMENT,
  `sender_id` int(20) DEFAULT NULL,
  `rating` varchar(50) DEFAULT NULL,
  `review` varchar(50) DEFAULT NULL,
  `date` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`rating_id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `rating` */

insert  into `rating`(`rating_id`,`sender_id`,`rating`,`review`,`date`) values 
(1,2,'5','gooood','2024-11-13'),
(3,2,'3','goodd','2024-11-19'),
(4,6,'3.0','good','2024-11-20');

/*Table structure for table `request` */

DROP TABLE IF EXISTS `request`;

CREATE TABLE `request` (
  `request_id` int(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(20) DEFAULT NULL,
  `advisor_id` int(20) DEFAULT NULL,
  `date` varchar(50) DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  `amount` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`request_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `request` */

insert  into `request`(`request_id`,`user_id`,`advisor_id`,`date`,`status`,`amount`) values 
(1,2,1,'2024-11-22','request accepted','5000'),
(2,2,2,'2024-11-22','pending','pending');

/*Table structure for table `user` */

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `user_id` int(20) NOT NULL AUTO_INCREMENT,
  `login_id` int(20) DEFAULT NULL,
  `name` varchar(50) DEFAULT NULL,
  `phone` varchar(50) DEFAULT NULL,
  `gender` varchar(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `place` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `user` */

insert  into `user`(`user_id`,`login_id`,`name`,`phone`,`gender`,`email`,`place`) values 
(1,5,'ss','ss','ss','ss','ss'),
(2,6,'bili','bili@gmail.com','FEMALE','thrissur','1212121212'),
(3,7,'sndn','1646','MALE','sjjs','jsje'),
(4,8,'bili','1212121212','FEMALE','bili@gmail.com','thrissur'),
(5,9,'','','null','','');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
