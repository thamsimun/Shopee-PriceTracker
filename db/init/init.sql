CREATE DATABASE IF NOT EXISTS `User`;
CREATE DATABASE IF NOT EXISTS `Price`;

USE User;

CREATE TABLE IF NOT EXISTS `UserProfile` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_name` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_name` (`user_name`)
);

CREATE TABLE IF NOT EXISTS `UserItems` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_name` varchar(255) NOT NULL,
  `item_id` bigint NOT NULL,
  `deleted` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_name` (`user_name`,`item_id`)
);

USE Price;

CREATE TABLE IF NOT EXISTS `ItemInfo` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `item_id` bigint NOT NULL,
  `item_name` varchar(255) NOT NULL,
  `shop_id` bigint NOT NULL,
  `price` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `item_id` (`item_id`)
);

CREATE TABLE IF NOT EXISTS `ItemPrice` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `item_id` bigint NOT NULL,
  `price` int NOT NULL,
  `time` datetime NOT NULL,
  PRIMARY KEY (`id`)
);
  
CREATE TABLE IF NOT EXISTS `FlashSale` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `promotion_id` bigint NOT NULL,
  `item_id` bigint NOT NULL,
  `item_name` varchar(255) NOT NULL,
  `shop_id` bigint NOT NULL,
  `price` int NOT NULL,
  `time` timestamp NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `item_id` (`item_id`)
);

CREATE INDEX idx1 on ItemPrice (`item_id`);
CREATE INDEX idx1 on ItemInfo (`item_id`);

