/*
SQLyog Community Edition- MySQL GUI v7.01 
MySQL - 5.5.5-10.1.31-MariaDB : Database - spammail
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

CREATE DATABASE /*!32312 IF NOT EXISTS*/`spammail` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `spammail`;

/*Table structure for table `sendmail` */

DROP TABLE IF EXISTS `sendmail`;

CREATE TABLE `sendmail` (
  `sendermail` varchar(200) DEFAULT NULL,
  `recievermail` varchar(200) DEFAULT NULL,
  `message` varchar(200) DEFAULT NULL,
  `myprediction` varchar(200) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `sendmail` */

insert  into `sendmail`(`sendermail`,`recievermail`,`message`,`myprediction`) values (NULL,NULL,NULL,NULL);
insert  into `sendmail`(`sendermail`,`recievermail`,`message`,`myprediction`) values ('rkharatmol123@gmail.com','ssss','rkharatmol123@gmail.com',NULL);
insert  into `sendmail`(`sendermail`,`recievermail`,`message`,`myprediction`) values ('rkharatmol123@gmail.com','ss1','sss','not spam');
insert  into `sendmail`(`sendermail`,`recievermail`,`message`,`myprediction`) values ('rkharatmol123@gmail.com','ss1','Sunshine Quiz Wkly Q! Win a top Sony DVD player if u know which country Liverpool played in mid week? Txt ansr to 82277. ?1.50 ','spam');
insert  into `sendmail`(`sendermail`,`recievermail`,`message`,`myprediction`) values ('rkharatmol123@gmail.com','rkharatmol123@gmail.com','sqaddsd','not spam');
insert  into `sendmail`(`sendermail`,`recievermail`,`message`,`myprediction`) values ('geetanjalitambe95@gmail.com','ss1','qqqq','not spam');
insert  into `sendmail`(`sendermail`,`recievermail`,`message`,`myprediction`) values ('rkharatmol123@gmail.com','rkharatmol123@gmail.com','aaaa','not spam');
insert  into `sendmail`(`sendermail`,`recievermail`,`message`,`myprediction`) values ('rkharatmol123@gmail.com','ss1','cc','spam');
insert  into `sendmail`(`sendermail`,`recievermail`,`message`,`myprediction`) values ('rkharatmol123@gmail.com','rkharatmol123@gmail.com','cdfcdscfcd','not spam');
insert  into `sendmail`(`sendermail`,`recievermail`,`message`,`myprediction`) values ('fg','rkharatmol123@gmail.com','gggggg','not spam');
insert  into `sendmail`(`sendermail`,`recievermail`,`message`,`myprediction`) values ('fg','rkharatmol123@gmail.com','sxaxx','not spam');
insert  into `sendmail`(`sendermail`,`recievermail`,`message`,`myprediction`) values ('rkharatmol123@gmail.com','mahendra@gmail.com','The meeting is arranged at 12:00 pm today.','not spam');

/*Table structure for table `userdetails` */

DROP TABLE IF EXISTS `userdetails`;

CREATE TABLE `userdetails` (
  `name` varchar(200) DEFAULT NULL,
  `phone` varchar(200) DEFAULT NULL,
  `username` varchar(200) DEFAULT NULL,
  `password` varchar(200) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `userdetails` */

insert  into `userdetails`(`name`,`phone`,`username`,`password`) values ('rahul','9004850819','rkharatmol123@gmail.com','sss');
insert  into `userdetails`(`name`,`phone`,`username`,`password`) values ('S','9004850819','mahendra@gmail.com','123');
insert  into `userdetails`(`name`,`phone`,`username`,`password`) values ('admin','9004850819','mahendra','1233');
insert  into `userdetails`(`name`,`phone`,`username`,`password`) values ('admin','9004850819','fg','12');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
