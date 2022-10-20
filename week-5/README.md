#week-5

##要求二

// 1. 建立一個新的資料庫，取名字為 website。
// 2. 在資料庫中，建立會員資料表，取名字為 member。資料表必須包含以下欄位設定:
create table member(
	id bigint primary key auto_increment,
	name varchar(255) not null,
	username varchar(255) not null,
	password varchar(255) not null,
	follower_count int unsigned not null default 0,
	time datetime not null DEFAULT CURRENT_TIMESTAMP
);

##要求三

// 使用 INSERT 指令新增一筆資料到 member 資料表中，這筆資料的 username 和 password 欄位必須是 test。接著繼續新增至少 4 筆隨意的資料。
insert into member(id,name,username,password,follower_count)values(1,'大郎','test','test',100);
insert into member(id,name,username,password,follower_count)values(2,'二郎','bro2','222',200);
insert into member(id,name,username,password,follower_count)values(3,'三郎','bro3','333',300);
insert into member(id,name,username,password,follower_count)values(4,'四郎','bro4','444',400);
insert into member(id,name,username,password,follower_count)values(5,'五郎','bro5','555',500);

// 使用 SELECT 指令取得所有在 member 資料表中的會員資料。
select *from member;

// 使用 SELECT 指令取得 member 資料表中第 2 ~ 4 共三筆資料，並按照 time 欄位，由近到遠排序。( 並非編號 2、3、4 的資料，而是排序後的第 2 ~ 4 筆資料 )
select *from member
ORDER BY time
limit 1,3;

// 使用 SELECT 指令取得欄位 username 是 test 的會員資料。
select *from member WHERE username='test';

//使用 SELECT 指令取得欄位 username 是 test、且欄位 password 也是 test 的資料。
select *from member WHERE username='test' and password='test';

//使用 UPDATE 指令更新欄位 username 是 test 的會員資料，將資料中的 name 欄位改成 test2。
UPDATE member SET name='test2' WHERE username='test';

##要求四

// 取得 member 資料表中，總共有幾筆資料 ( 幾位會員 )。
SELECT COUNT(id)
FROM member;
// 取得 member 資料表中，所有會員 follower_count 欄位的總和。
SELECT SUM(follower_count)
FROM member;
// 取得 member 資料表中，所有會員 follower_count 欄位的平均數。
SELECT AVG(follower_count)
FROM member;

##要求五

// 在資料庫中，建立新資料表紀錄留言資訊，取名字為 message。資料表中必須包含以下欄位設定:
create table message(
	id bigint primary key auto_increment,
	member_id bigint not null,
	content varchar(255) not null,
	like_count int unsigned not null default 0,
	time datetime not null DEFAULT CURRENT_TIMESTAMP
);

ALTER TABLE message ADD FOREIGN KEY(member_id) REFERENCES member(id);

insert into message(id,member_id,content,like_count)values(1,3,'好棒',1);
insert into message(id,member_id,content,like_count)values(2,5,'加油',1);
insert into message(id,member_id,content,like_count)values(3,1,'好吃',1);
insert into message(id,member_id,content,like_count)values(4,4,'討厭',1);
insert into message(id,member_id,content,like_count)values(5,2,'不好',1);
insert into message(id,member_id,content,like_count)values(6,1,'不好',3);
select *from message;

// 使用 SELECT 搭配 JOIN 語法，取得所有留言，結果須包含留言者會員的姓名。
SELECT
member.id,member.name,message.content,message.time
FROM message
INNER JOIN member
ON message.member_id=member.id;

// 使用 SELECT 搭配 JOIN 語法，取得 member 資料表中欄位 username 是 test 的所有留言，資料中須包含留言者會員的姓名。
SELECT
member.id,member.name,message.content,message.time
FROM message
INNER JOIN member
ON message.member_id=member.id and username='test';

// 使用 SELECT、SQL Aggregate Functions 搭配 JOIN 語法，取得 member 資料表中欄位 username 是 test 的所有留言平均按讚數。
SELECT AVG(message.like_count)
FROM message
INNER JOIN member
ON message.member_id=member.id and username='test';
