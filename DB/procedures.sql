--
-- Database: `chatroom`
--

DELIMITER $$
--
-- Procedures
--
CREATE DEFINER=`root`@`localhost` PROCEDURE `AddMember` (IN `userName` CHAR(50), IN `roomID` INT)  NO SQL
INSERT INTO userchatroom(UserName,RoomID) VALUES (userName,roomID)$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `AddUser` (IN `name` CHAR(50), IN `pass` CHAR(50))  NO SQL
INSERT INTO user(UserName, Password)
VALUES(name, pass)$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `CreateChatRoom` (IN `chatname` CHAR(50), IN `port` INT)  NO SQL
INSERT INTO chatroom (Name,Port) VALUES (chatname,port)$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `ExitChatRoom` (IN `userName` CHAR(50), IN `roomID` INT)  NO SQL
DELETE FROM userchatroom WHERE
userchatroom.UserName = userName AND
userchatroom.RoomID = roomID$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `GetChatRoomPort` (IN `roomID` INT)  NO SQL
SELECT Port FROM chatroom WHERE
chatroom.ID = roomID$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `RemoveChatRoom` (IN `roomID` INT)  NO SQL
DELETE FROM chatroom WHERE
chatroom.ID = roomID$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `ViewChatRooms` (IN `userName` CHAR(50))  NO SQL
SELECT * FROM userchatroom WHERE
userchatroom.UserName = userName$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `ViewMembers` (IN `roomID` INT)  NO SQL
SELECT * FROM userchatroom WHERE
userchatroom.RoomID = roomID$$

DELIMITER ;