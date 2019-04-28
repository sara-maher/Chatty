DELIMITER $$
--
-- Procedures
--
CREATE DEFINER=`root`@`localhost` PROCEDURE `AddUser` (IN `name` CHAR(50), IN `pass` CHAR(50))  NO SQL
INSERT INTO user(UserName, Password)
VALUES(name, pass)$$

DELIMITER ;

-- --------------------------------------------------------