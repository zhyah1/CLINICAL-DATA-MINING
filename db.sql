/*
SQLyog Community v13.0.1 (64 bit)
MySQL - 5.5.20-log : Database - clinicaldata
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`clinicaldata` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `clinicaldata`;

/*Table structure for table `booking` */

DROP TABLE IF EXISTS `booking`;

CREATE TABLE `booking` (
  `book_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `schedule` int(11) NOT NULL,
  `date` varchar(50) NOT NULL,
  `status` varchar(50) NOT NULL,
  PRIMARY KEY (`book_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `booking` */

insert  into `booking`(`book_id`,`user_id`,`schedule`,`date`,`status`) values 
(1,4,1,'2021-12-28','booked');

/*Table structure for table `chat` */

DROP TABLE IF EXISTS `chat`;

CREATE TABLE `chat` (
  `chat_id` int(11) NOT NULL AUTO_INCREMENT,
  `from_id` int(11) NOT NULL,
  `to_id` int(11) NOT NULL,
  `message` varchar(100) NOT NULL,
  `date` varchar(30) NOT NULL,
  PRIMARY KEY (`chat_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `chat` */

/*Table structure for table `doctor` */

DROP TABLE IF EXISTS `doctor`;

CREATE TABLE `doctor` (
  `d_id` int(11) NOT NULL AUTO_INCREMENT,
  `l_id` int(11) NOT NULL,
  `hospital_id` int(11) NOT NULL,
  `first_name` varchar(40) NOT NULL,
  `last_nmae` varchar(40) NOT NULL,
  `dept_name` varchar(40) NOT NULL,
  `gender` varchar(40) NOT NULL,
  `qualification` varchar(30) NOT NULL,
  `dob` varchar(40) NOT NULL,
  `experiance` varchar(30) NOT NULL,
  `place` varchar(35) NOT NULL,
  `post` varchar(35) NOT NULL,
  `pin` bigint(20) NOT NULL,
  `email` varchar(40) NOT NULL,
  `contact` bigint(20) NOT NULL,
  PRIMARY KEY (`d_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `doctor` */

insert  into `doctor`(`d_id`,`l_id`,`hospital_id`,`first_name`,`last_nmae`,`dept_name`,`gender`,`qualification`,`dob`,`experiance`,`place`,`post`,`pin`,`email`,`contact`) values 
(1,3,1,'siya','hul haque','ent','male','mbbs,md','23-12-2001','2 year','nbr','van',0,'',0),
(3,10,2,'kiran','cs','Skin','male','mbbs,md','','4 years','nilambur','chungathara',679334,'kiransubru@gmail.com',7034818081),
(4,11,2,'martin','jos','ENT','male','mbbs','2021-12-07','2 years','nilambur','chungathara',679334,'martinjos@gmail.com',7867766877),
(5,12,2,'ajmal','th','nephrology','male','mbbs,md','2021-03-30','3 years','nilambur','chungathara',679334,'ajuajmal@gmail.com',7034818081);

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_name` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `type` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`id`,`user_name`,`password`,`type`) values 
(1,'siya','siya1234','admin'),
(2,'angel','angelmari','admin'),
(3,'aswin','aswin1234','doctor'),
(4,'kiran','kiran1234','doctor'),
(5,'aseed','aseed1234','doctor'),
(6,'aseed','aseed1234','doctor'),
(7,'aaa','aaa','doctor'),
(10,'kiran','kiran1234','doctor'),
(11,'martin','martin1234','doctor'),
(12,'ajmal','ajmal1234','doctor');

/*Table structure for table `medicine` */

DROP TABLE IF EXISTS `medicine`;

CREATE TABLE `medicine` (
  `medicine_id` int(11) NOT NULL AUTO_INCREMENT,
  `doctor_id` int(11) NOT NULL,
  `drug_name` varchar(50) NOT NULL,
  `exp_date` varchar(50) NOT NULL,
  `manfac_date` varchar(30) NOT NULL,
  `description` varchar(100) NOT NULL,
  PRIMARY KEY (`medicine_id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=latin1;

/*Data for the table `medicine` */

insert  into `medicine`(`medicine_id`,`doctor_id`,`drug_name`,`exp_date`,`manfac_date`,`description`) values 
(5,3,'para','23-02-2014','23-02-2012','2 years'),
(13,3,'ewwgawe','23-02-2012','23-02-2010','pani vannal kazhikkendath');

/*Table structure for table `report` */

DROP TABLE IF EXISTS `report`;

CREATE TABLE `report` (
  `report_id` int(50) NOT NULL AUTO_INCREMENT,
  `user_id` int(30) NOT NULL,
  `doctor_id` int(25) NOT NULL,
  `date` varchar(35) NOT NULL,
  `report` varchar(100) NOT NULL,
  PRIMARY KEY (`report_id`)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=latin1;

/*Data for the table `report` */

insert  into `report`(`report_id`,`user_id`,`doctor_id`,`date`,`report`) values 
(21,4,10,'30-04-2021','good'),
(22,4,3,'2021-12-31','login.html'),
(23,4,3,'2021-12-31','login.html'),
(24,4,3,'2021-12-31','login.html'),
(25,4,3,'2021-12-31','login.html'),
(26,4,3,'2021-12-31','login.html'),
(27,4,3,'2021-12-31','login.html'),
(28,4,3,'2021-12-31','login.html');

/*Table structure for table `schedule` */

DROP TABLE IF EXISTS `schedule`;

CREATE TABLE `schedule` (
  `s_id` int(11) NOT NULL AUTO_INCREMENT,
  `doctor_id` int(11) NOT NULL,
  `date` varchar(30) NOT NULL,
  `from_time` varchar(200) NOT NULL,
  `to_time` varchar(200) NOT NULL,
  PRIMARY KEY (`s_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `schedule` */

insert  into `schedule`(`s_id`,`doctor_id`,`date`,`from_time`,`to_time`) values 
(1,11,'2021-12-03','0000-00-00 00:00:00','0000-00-00 00:00:00'),
(2,11,'2021-11-30','16:58','18:56'),
(3,11,'2021-12-08','10:36','11:36'),
(4,11,'2021-12-06','10:01','12:01'),
(5,10,'2019-12-18','13:30','16:31');

/*Table structure for table `user` */

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `l_id` int(11) NOT NULL,
  `first_name` varchar(50) NOT NULL,
  `last_name` varchar(50) NOT NULL,
  `gender` varchar(50) NOT NULL,
  `dob` varchar(50) NOT NULL,
  `place` varchar(50) NOT NULL,
  `post` varchar(50) NOT NULL,
  `pin` bigint(20) NOT NULL,
  `email` varchar(50) NOT NULL,
  `contact` bigint(20) NOT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `user` */

insert  into `user`(`user_id`,`l_id`,`first_name`,`last_name`,`gender`,`dob`,`place`,`post`,`pin`,`email`,`contact`) values 
(1,4,'aseed','akram','female','23-12-2000','chungathara','vaniyambalam',7657,'aseedakku@gmail.com',9876568968);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
