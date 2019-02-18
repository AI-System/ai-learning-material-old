/*
 Navicat Premium Data Transfer

 Source Server         : full-stack
 Source Server Type    : MySQL
 Source Server Version : 50725
 Source Host           : localhost
 Source Database       : blogdb

 Target Server Type    : MySQL
 Target Server Version : 50725
 File Encoding         : utf-8

 Date: 02/18/2019 09:37:15 AM
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
--  Table structure for `blog`
-- ----------------------------
DROP TABLE IF EXISTS `blog`;
CREATE TABLE `blog` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT 'id号',
  `title` varchar(100) NOT NULL COMMENT '标题',
  `abstract` varchar(200) NOT NULL COMMENT '摘要',
  `content` text NOT NULL COMMENT '博文内容',
  `uid` int(10) unsigned DEFAULT NULL COMMENT '用户标识',
  `pcount` int(10) unsigned DEFAULT '0' COMMENT '点赞数',
  `flag` tinyint(3) unsigned DEFAULT '0' COMMENT '状态 (默)0新建，1发布，2删除',
  `cdate` datetime DEFAULT NULL COMMENT '创建时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;

-- ----------------------------
--  Records of `blog`
-- ----------------------------
BEGIN;
INSERT INTO `blog` VALUES ('1', 'title1', 'abstract1', 'content1', '1', '10', '0', '2019-02-01 21:11:00'), ('2', 'title2', 'abstrac2', 'content2', '2', '20', '0', '2019-02-02 21:11:00'), ('3', 'title3', 'abstract3', 'content3', '3', '30', '0', '2019-02-03 21:11:00'), ('4', 'title4', 'abstract4', 'content4', '4', '40', '0', '2019-02-04 21:11:00'), ('5', 'title5', 'abstract5', 'content5', '5', '50', '0', '2019-02-05 21:11:00'), ('6', 'title6', 'abstract6', 'content6', '6', '60', '0', '2019-02-06 21:11:00'), ('7', 'title7', 'abstract7', 'content7', '7', '70', '0', '2019-02-07 21:11:00'), ('8', 'title8', 'abstract8', 'content8', '8', '80', '0', '2019-02-08 21:11:00'), ('9', 'title9', 'abstract9', 'content9', '9', '90', '0', '2019-02-09 21:11:00'), ('10', 'title10', 'abstract10', 'content10', '10', '100', '0', '2019-02-10 21:11:00');
COMMIT;

-- ----------------------------
--  Table structure for `users`
-- ----------------------------
DROP TABLE IF EXISTS `users`;
CREATE TABLE `users` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT 'id号',
  `name` varchar(32) NOT NULL COMMENT '姓名',
  `email` varchar(100) DEFAULT NULL COMMENT '邮箱地址',
  `cdate` datetime DEFAULT NULL COMMENT '注册时间',
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;

-- ----------------------------
--  Records of `users`
-- ----------------------------
BEGIN;
INSERT INTO `users` VALUES ('6', 'p1', 'p1@qq.com', '2019-02-01 11:11:00'), ('7', 'p2', 'p2@qq.com', '2019-02-02 11:11:00'), ('8', 'p3', 'p3@qq.com', '2019-02-03 11:11:00'), ('9', 'p4', 'p4@qq.com', '2019-02-04 11:11:00'), ('10', 'p5', 'p5@qq.com', '2019-02-05 11:11:00');
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;
