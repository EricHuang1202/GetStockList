/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 50712
Source Host           : localhost:3306
Source Database       : StockCrawler

Target Server Type    : MYSQL
Target Server Version : 50712
File Encoding         : 65001

Date: 2017-12-07 09:52:28
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for StockList
-- ----------------------------
DROP TABLE IF EXISTS `StockList`;
CREATE TABLE `StockList` (
  `StockId` varchar(10) NOT NULL,
  `Name` varchar(50) NOT NULL,
  `ListingDate` date DEFAULT NULL,
  `Industry` varchar(100) DEFAULT NULL,
  `Kind` varchar(50) DEFAULT NULL,
  `CreateDate` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`StockId`,`Name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
