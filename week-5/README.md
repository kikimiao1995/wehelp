## Demand - 2 SQL Create database and table
- 建立一個新的資料庫， 取名字為 website。
    
    ```mysql
    CREATE DATABASE website;
    SHOW DATABASES;                                 # 顯示所有的資料庫
    USE website;                                    # 切換資料庫
    ```
    - 沒有 `USE [database]` 會報錯，ERROR 1046 (3D000): No database selected。
    
- 建立會員資料表，取名字為 member
    
    ```mysql
    CREATE TABLE member (
        id BIGINT NOT NULL AUTO_INCREMENT,
        PRIMARY KEY(id),
        name VARCHAR(255) NOT NULL,
        username VARCHAR(255) NOT NULL,
        password VARCHAR(255) NOT NULL,
        follower_count INT UNSIGNED NOT NULL DEFAULT 0,
        time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
    );
    ```
    
    - 顯示目前資料庫下的所有 tables `SHOW TABLES;`
    - 檢查 table 的欄位 `DESC <table_name>;` or `DESCRIBE <table_name>;`
    - 刪除 table `DROP TABLE <table_name>;`


## Demand - 3 SQL CRUD
- 使用 INSERT 指令新增一筆資料到 member 資料表中，這筆資料的 username 和 password 欄位必須是 test。接著繼續新增至少 4 筆隨意的資料。

    ```sql
    INSERT INTO member (name, username, password)
    VALUES ('test', 'test123', 'test'), ('react', 'react123', '2013'),('golang', 'golang123', '2009'), ('flask', 'flask123', '2010'), ('linux', 'linux123', '1991');
    
    INSERT INTO member (name, username, password) VALUES ('test', 'test', 'test');
    INSERT INTO member (name, username, password) VALUES ('react', 'react123', '2013');
    INSERT INTO member (name, username, password) VALUES ('golang', 'golang123', '2009');
    INSERT INTO member (name, username, password) VALUES ('flask', 'flask123', '2010');
    INSERT INTO member (name, username, password) VALUES ('linux', 'linux123', '1991');
    ```
    
    - `delete from member where name='flask';` 沒有加 where 條件會刪除table中的所有資料！    
    
- 使用 SELECT 指令取得所有在 member 資料表中的會員資料。
    ```mysql
    SELECT * FROM member;
    ```

- 使用 SELECT 指令取得所有在 member 資料表中的會員資料，並按照 time 欄位，由近到遠排序。
  
    `ORDER BY ASC|DESC`, default = ASC (遞增)
   
    ```mysql
    SELECT * FROM member ORDER BY time DESC;
    ```

- 使用 SELECT 指令取得 member 資料表中第 2 ~ 4 共三筆資料，並按照 time 欄位，由近到遠排序。( 並非編號 2、3、4 的資料，而是排序後的第 2 ~ 4 筆資料 )

    ```mysql
    SELECT *
    FROM member
    ORDER BY time DESC
    LIMIT 1, 3;
    ```
    
    ```mysql
    SELECT *
    FROM member
    ORDER BY time DESC
    LIMIT 3 OFFSET 1;
    ```

    ```mysql
    WITH OrderedMember AS
    (
        SELECT *,
        ROW_NUMBER() OVER (ORDER BY time DESC) AS RowNumber
        FROM member
    ) 
    SELECT *
    FROM OrderedMember
    WHERE RowNumber BETWEEN 2 AND 4;
    ```

- 使用 SELECT 指令取得欄位 username 是 test 的會員資料。
    
    ```mysql
    SELECT *
    FROM member
    WHERE username='test';
    ```

- 使用 SELECT 指令取得欄位 username 是 test、且欄位 password 也是 test 的資料。

    ```mysql
    SELECT *
    FROM member
    WHERE username='test' and password='test';
    ```
  
- 使用 UPDATE 指令更新欄位 username 是 test 的會員資料，將資料中的 name 欄位改成 test2。
    
    ```mysql
    UPDATE member
    SET name = 'test2'
    WHERE username='test';
    ```
    - `select * from member where name='test2'`

## Demand - 4 SQL Aggregate Functions

- 取得 member 資料表中，總共有幾筆資料 ( 幾位會員 )。
    
    ```mysql
    SELECT COUNT(id)
    FROM member;
    ```
    
- 取得 member 資料表中，所有會員 follower_count 欄位的總和。

    ```mysql
    SELECT SUM(follower_count)
    FROM member;
    ```
    
- 取得 member 資料表中，所有會員 follower_count 欄位的平均數。

    ```mysql
    SELECT AVG(follower_count)
    FROM member;
    ```

## Demand - 5 SQL JOIN

- 建立 table
    ```mysql
    CREATE TABLE message(
        id BIGINT NOT NULL AUTO_INCREMENT,
        member_id BIGINT NOT NULL,
        content VARCHAR(255) NOT NULL,
        like_count INT UNSIGNED NOT NULL DEFAULT 0,
        time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
        PRIMARY KEY(id),
        FOREIGN KEY (member_id) REFERENCES member(id)
    );
    
    INSERT INTO message (member_id, content, like_count) VALUES (2, 'React is the best !', 100);
    INSERT INTO message (member_id, content, like_count) VALUES (3, 'Go is the best !', 1000);
    INSERT INTO message (member_id, content, like_count) VALUES (3, 'Go is an open source programming language supported by Google', 1000);
    INSERT INTO message (member_id, content, like_count) VALUES (5, 'Linux is the best !', 1000);
    INSERT INTO message (member_id, content, like_count) VALUES (1, 'test test 123!', 1000);
    INSERT INTO message (member_id, content, like_count) VALUES (1, 'test test 456!', 200);
    ```
    
- 使用 SELECT 搭配 JOIN 語法，取得所有留言，結果須包含留言者會員的姓名。

    ```mysql
    SELECT message.content, member.name
    FROM message
    INNER JOIN member
    ON message.member_id = member.id;
    ```

- 使用 SELECT 搭配 JOIN 語法，取得 member 資料表中欄位 username 是 test 的所有留言，資料中須包含留言者會員的姓名。

    ```mysql
    SELECT message.content, member.name
    FROM message
    INNER JOIN member ON message.member_id = member.id
    WHERE member.username = 'test';
    ```

- 使用 SELECT、SQL Aggregate Functions 搭配 JOIN 語法，取得 member 資料表中欄位 username 是 test 的所有留言平均按讚數。
    
    ```mysql
    SELECT AVG(message.like_count), member.username
    FROM message
    INNER JOIN member ON message.member_id = member.id
    WHERE member.username = 'test';
    ```

- 匯出資料庫中的資料
    
    ```linux
    docker exec -it mysql1 mysqldump -uroot -pmysql1pwd website > Documents/data.sql
    ```
    
