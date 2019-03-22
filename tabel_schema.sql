CREATE TABLE login_test.`accounts`(
 `user_no` int(11) unsigned NOT NULL AUTO_INCREMENT,
 `user_name` varchar(32) NOT NULL COMMENT '이름',
 `user_id` varchar(32) NOT NULL COMMENT '아이디',
 `user_password` varchar(300) NOT NULL COMMENT '패스워드',
 `user_email` varchar(32) NOT NULL COMMENT '이메일',
 `user_phone` varchar(32) NOT NULL COMMENT '전화번호',
 `create_at` datetime NOT NULL COMMENT '등록일',
 `active` tinyint(1) NOT NULL COMMENT '계정 확성 여부',
 PRIMARY KEY (`user_no`),
 UNIQUE KEY `user_id` (`user_id`),
 KEY `active` (`active`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COMMENT='acctouns';