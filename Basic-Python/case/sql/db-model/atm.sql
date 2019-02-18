/*
 Navicat Premium Data Transfer

 Source Server         : full-stack
 Source Server Type    : MySQL
 Source Server Version : 50725
 Source Host           : localhost
 Source Database       : mydb

 Target Server Type    : MySQL
 Target Server Version : 50725
 File Encoding         : utf-8

 Date: 02/19/2019 08:07:59 AM
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
--  Table structure for `atm`
-- ----------------------------
DROP TABLE IF EXISTS `atm`;
CREATE TABLE `atm` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT 'id号',
  `name` varchar(32) NOT NULL COMMENT '登录名',
  `password` varchar(20) NOT NULL COMMENT '密码',
  `balance` decimal(10,2) DEFAULT '0.00' COMMENT '余额',
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;

-- ----------------------------
--  Records of `atm`
-- ----------------------------
BEGIN;
INSERT INTO `atm` VALUES ('1', 'n1', '111111', '550.00'), ('2', 'n2', '111111', '200.00'), ('3', 'n3', '111111', '300.00'), ('4', 'n4', '111111', '400.00'), ('5', 'n5', '111111', '500.00');
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;
