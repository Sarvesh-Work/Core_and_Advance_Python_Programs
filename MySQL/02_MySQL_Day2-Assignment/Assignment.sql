mysql> CREATE DATABASE StudentManagementSystem;
Query OK, 1 row affected (0.01 sec)

mysql> USE StudentManagementSystem;
Database changed

 -- Create Student table
mysql> CREATE TABLE Student (
    -> StudentID INT PRIMARY KEY,          -- Unique identifier for each student
    -> FirstName VARCHAR(50),             -- Student's first name
    -> LastName VARCHAR(50),              -- Student's last name
    -> DateOfBirth DATE,                  -- Student's date of birth
    -> Gender CHAR(1),                    -- Student's gender (M/F)
    -> Email VARCHAR(100),                -- Student's email address
    -> Phone VARCHAR(15)                  -- Student's phone number
    -> );
Query OK, 0 rows affected (0.02 sec)

 -- Create Course table
mysql> CREATE TABLE Course (
    -> CourseID INT PRIMARY KEY,          -- Unique identifier for each course
    -> CourseTitle VARCHAR(100),          -- Title of the course
    -> Credits INT                        -- Number of credits for the course
    -> );
Query OK, 0 rows affected (0.02 sec)

 -- Create Instructor table
mysql> CREATE TABLE Instructor (
    -> InstructorID INT PRIMARY KEY,      -- Unique identifier for each instructor
    -> FirstName VARCHAR(50),             -- Instructor's first name
    -> LastName VARCHAR(50),              -- Instructor's last name
    -> Email VARCHAR(100)                 -- Instructor's email address
    -> );
Query OK, 0 rows affected (0.02 sec)

-- Create Enrollment table with foreign keys
mysql> CREATE TABLE Enrollment (
    -> EnrollmentID INT PRIMARY KEY,      -- Unique identifier for each enrollment
    -> EnrollmentDate DATE,               -- Date of enrollment
    -> StudentID INT,                     -- References Student table
    -> CourseID INT,                      -- References Course table
    -> InstructorID INT,                  -- References Instructor table
    -> FOREIGN KEY (StudentID) REFERENCES Student(StudentID),
    -> FOREIGN KEY (CourseID) REFERENCES Course(CourseID),
    -> FOREIGN KEY (InstructorID) REFERENCES Instructor(InstructorID)
    -> );
Query OK, 0 rows affected (0.03 sec)

-- Create Score table with foreign keys
mysql> CREATE TABLE Score (
    -> ScoreID INT PRIMARY KEY,           -- Unique identifier for each score record
    -> CourseID INT,                      -- References Course table
    -> StudentID INT,                     -- References Student table
    -> DateOfExam DATE,                   -- Date of examination
    -> CreditObtained DECIMAL(4,2),       -- Score obtained (max 99.99)
    -> FOREIGN KEY (CourseID) REFERENCES Course(CourseID),
    -> FOREIGN KEY (StudentID) REFERENCES Student(StudentID)
    -> );
Query OK, 0 rows affected (0.03 sec)

 -- Create Feedback table with foreign key
mysql> CREATE TABLE Feedback (
    -> FeedbackID INT PRIMARY KEY,        -- Unique identifier for each feedback
    -> StudentID INT,                     -- References Student table
    -> Date DATE,                         -- Date of feedback
    -> InstructorName VARCHAR(100),       -- Name of instructor being reviewed
    -> Feedback TEXT,                     -- Feedback comments
    -> FOREIGN KEY (StudentID) REFERENCES Student(StudentID)
    -> );
Query OK, 0 rows affected (0.03 sec)

 -- Insert sample data into Student table
mysql> INSERT INTO Student VALUES
    -> (1, 'John', 'Doe', '2000-05-15', 'M', 'john.doe@email.com', '555-0101'),
    -> (2, 'Jane', 'Smith', '2001-08-22', 'F', 'jane.smith@email.com', '555-0102'),
    -> (3, 'Mike', 'Johnson', '1999-12-10', 'M', 'mike.j@email.com', '555-0103'),
    -> (4, 'Sarah', 'Williams', '2000-03-25', 'F', 'sarah.w@email.com', '555-0104'),
    -> (5, 'Tom', 'Brown', '2001-06-30', 'M', 'tom.b@email.com', '555-0105');
Query OK, 5 rows affected (0.01 sec)
Records: 5  Duplicates: 0  Warnings: 0

 -- Insert sample data into Course table
mysql> INSERT INTO Course VALUES
    -> (101, 'Introduction to Programming', 3),
    -> (102, 'Database Systems', 4),
    -> (103, 'Web Development', 3),
    -> (104, 'Mathematics', 4),
    -> (105, 'Computer Networks', 3);
Query OK, 5 rows affected (0.01 sec)
Records: 5  Duplicates: 0  Warnings: 0

 -- Insert sample data into Instructor table
mysql> INSERT INTO Instructor VALUES
    -> (1001, 'Robert', 'Wilson', 'robert.w@edu.com'),
    -> (1002, 'Mary', 'Davis', 'mary.d@edu.com'),
    -> (1003, 'James', 'Taylor', 'james.t@edu.com'),
    -> (1004, 'Linda', 'Moore', 'linda.m@edu.com'),
    -> (1005, 'David', 'Anderson', 'david.a@edu.com');
Query OK, 5 rows affected (0.01 sec)
Records: 5  Duplicates: 0  Warnings: 0

 -- Insert sample data into Enrollment table
mysql> INSERT INTO Enrollment VALUES
    -> (1, '2025-01-15', 1, 101, 1001),    -- John in Intro Programming with Robert
    -> (2, '2025-01-15', 2, 102, 1002),    -- Jane in Database Systems with Mary
    -> (3, '2025-01-16', 3, 103, 1003),    -- Mike in Web Dev with James
    -> (4, '2025-01-16', 4, 104, 1004),    -- Sarah in Mathematics with Linda
    -> (5, '2025-01-17', 5, 105, 1005);    -- Tom in Networks with David
Query OK, 5 rows affected (0.01 sec)
Records: 5  Duplicates: 0  Warnings: 0

 -- Insert sample data into Score table
mysql> INSERT INTO Score VALUES
    -> (1, 101, 1, '2025-02-20', 85.50),   -- John's programming score
    -> (2, 102, 2, '2025-02-21', 92.00),   -- Jane's database score
    -> (3, 103, 3, '2025-02-22', 78.50),   -- Mike's web dev score
    -> (4, 104, 4, '2025-02-23', 95.75),   -- Sarah's math score
    -> (5, 105, 5, '2025-02-24', 88.25);   -- Tom's network score
Query OK, 5 rows affected (0.01 sec)
Records: 5  Duplicates: 0  Warnings: 0

 -- Insert sample data into Feedback table
mysql> INSERT INTO Feedback VALUES
    -> (1, 1, '2025-02-25', 'Robert Wilson', 'Great teaching style'),
    -> (2, 2, '2025-02-25', 'Mary Davis', 'Very helpful instructor'),
    -> (3, 3, '2025-02-26', 'James Taylor', 'Clear explanations'),
    -> (4, 4, '2025-02-26', 'Linda Moore', 'Excellent course structure'),
    -> (5, 5, '2025-02-27', 'David Anderson', 'Good practical examples');
Query OK, 5 rows affected (0.01 sec)
Records: 5  Duplicates: 0  Warnings: 0

 -- Retrieve and display data from Student table
mysql> SELECT * FROM Student;
+-----------+-----------+----------+------------+--------+---------------------+----------+
| StudentID | FirstName | LastName | DateOfBirth| Gender | Email               | Phone    |
+-----------+-----------+----------+------------+--------+---------------------+----------+
| 1         | John      | Doe      | 2000-05-15 | M      | john.doe@email.com  | 555-0101 |
| 2         | Jane      | Smith    | 2001-08-22 | F      | jane.smith@email.com| 555-0102 |
| 3         | Mike      | Johnson  | 1999-12-10 | M      | mike.j@email.com    | 555-0103 |
| 4         | Sarah     | Williams | 2000-03-25 | F      | sarah.w@email.com   | 555-0104 |
| 5         | Tom       | Brown    | 2001-06-30 | M      | tom.b@email.com     | 555-0105 |
+-----------+-----------+----------+------------+--------+---------------------+----------+
5 rows in set (0.00 sec)

 -- Retrieve and display data from Course table
mysql> SELECT * FROM Course;
+----------+--------------------------+---------+
| CourseID | CourseTitle             | Credits |
+----------+--------------------------+---------+
| 101      | Introduction to Programming | 3     |
| 102      | Database Systems         | 4       |
| 103      | Web Development          | 3       |
| 104      | Mathematics              | 4       |
| 105      | Computer Networks        | 3       |
+----------+--------------------------+---------+
5 rows in set (0.00 sec)

 -- Retrieve and display data from Instructor table
mysql> SELECT * FROM Instructor;
+--------------+-----------+----------+------------------+
| InstructorID | FirstName | LastName | Email            |
+--------------+-----------+----------+------------------+
| 1001         | Robert    | Wilson   | robert.w@edu.com |
| 1002         | Mary      | Davis    | mary.d@edu.com   |
| 1003         | James     | Taylor   | james.t@edu.com  |
| 1004         | Linda     | Moore    | linda.m@edu.com  |
| 1005         | David     | Anderson | david.a@edu.com  |
+--------------+-----------+----------+------------------+
5 rows in set (0.00 sec)

-- Retrieve and display data from Enrollment table
mysql> SELECT * FROM Enrollment;
+--------------+----------------+-----------+----------+--------------+
| EnrollmentID | EnrollmentDate | StudentID | CourseID | InstructorID |
+--------------+----------------+-----------+----------+--------------+
| 1            | 2025-01-15     | 1         | 101      | 1001         |
| 2            | 2025-01-15     | 2         | 102      | 1002         |
| 3            | 2025-01-16     | 3         | 103      | 1003         |
| 4            | 2025-01-16     | 4         | 104      | 1004         |
| 5            | 2025-01-17     | 5         | 105      | 1005         |
+--------------+----------------+-----------+----------+--------------+
5 rows in set (0.00 sec)

-- Retrieve and display data from Score table
mysql> SELECT * FROM Score;
+---------+----------+-----------+------------+---------------+
| ScoreID | CourseID | StudentID | DateOfExam | CreditObtained|
+---------+----------+-----------+------------+---------------+
| 1       | 101      | 1         | 2025-02-20 | 85.50         |
| 2       | 102      | 2         | 2025-02-21 | 92.00         |
| 3       | 103      | 3         | 2025-02-22 | 78.50         |
| 4       | 104      | 4         | 2025-02-23 | 95.75         |
| 5       | 105      | 5         | 2025-02-24 | 88.25         |
+---------+----------+-----------+------------+---------------+
5 rows in set (0.00 sec)

-- Retrieve and display data from Feedback table
mysql> SELECT * FROM Feedback;
+------------+-----------+------------+----------------+-----------------------+
| FeedbackID | StudentID | Date       | InstructorName | Feedback              |
+------------+-----------+------------+----------------+-----------------------+
| 1          | 1         | 2025-02-25 | Robert Wilson  | Great teaching style  |
| 2          | 2         | 2025-02-25 | Mary Davis     | Very helpful instructor|
| 3          | 3         | 2025-02-26 | James Taylor   | Clear explanations    |
| 4          | 4         | 2025-02-26 | Linda Moore    | Excellent course structure|
| 5          | 5         | 2025-02-27 | David Anderson | Good practical examples|
+------------+-----------+------------+----------------+-----------------------+
5 rows in set (0.00 sec)