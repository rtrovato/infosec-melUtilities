CREATE TABLE `mel_funcionarios` (
  `user_id` int NOT NULL AUTO_INCREMENT COMMENT 'primary key',
  `create_time` datetime DEFAULT NULL COMMENT 'create time',
  `update_time` datetime DEFAULT NULL COMMENT 'update time',
  `nomecompleto` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL COMMENT 'eMail Profissional',
  `departamento` varchar(255) DEFAULT NULL COMMENT 'Nome Departamento',
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8


CREATE TABLE `mel_review_result` (
  `id` int NOT NULL AUTO_INCREMENT COMMENT 'primary key',
  `create_time` datetime DEFAULT NULL COMMENT 'create time',
  `update_time` datetime DEFAULT NULL COMMENT 'update time',
  `name_db` varchar(255) DEFAULT NULL COMMENT 'Nome do Banco de Dados',
  `email_owner_db` varchar(255) DEFAULT NULL COMMENT 'Nome do Banco de Dados',
  `email_owner_manager` varchar(255) DEFAULT NULL COMMENT 'Nome do Banco de Dados',
  `classification_db` varchar(24) DEFAULT NULL COMMENT 'Nome do Banco de Dados',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci

ALTER TABLE "mel_hierarquia" ADD CONSTRAINT 'fk_func_id' KEY ('id') REFERENCES 'mel_funcionarios' ('id');  
ALTER TABLE "mel_hierarquia" ADD CONSTRAINT 'fk_gestor_id' KEY ('id') REFERENCES 'mel_funcionarios' ('id'); 
