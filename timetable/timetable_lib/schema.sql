BEGIN TRANSACTION;

-- Drop all tables
DROP TABLE IF EXISTS "HaveUnit";
DROP TABLE IF EXISTS "Lessons";
DROP TABLE IF EXISTS "Unit";
DROP TABLE IF EXISTS "Student";

-- Create tables
CREATE TABLE IF NOT EXISTS "Student" (
	"studentID"	INTEGER NOT NULL UNIQUE,
	"Name"	INTEGER NOT NULL,
	"Contact"	TEXT UNIQUE,
	PRIMARY KEY("studentID")
);
CREATE TABLE IF NOT EXISTS "HaveUnit" (
	"studentID"	INTEGER NOT NULL,
	"lessonID"	INTEGER NOT NULL,
	FOREIGN KEY("studentID") REFERENCES "Student"("studentID"),
	FOREIGN KEY("lessonID") REFERENCES "Lessons"("lessonID"),
	PRIMARY KEY("studentID","lessonID")
);
CREATE TABLE IF NOT EXISTS "Unit" (
	"unitPK"	INTEGER NOT NULL UNIQUE,
	"unitID"	TEXT NOT NULL UNIQUE,
	"unitName"	TEXT NOT NULL UNIQUE,
	PRIMARY KEY("unitPK" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "Lessons" (
	"lessonID"	INTEGER NOT NULL,
	"classID"	INTEGER NOT NULL,
	"unitPK"	INTEGER NOT NULL,
	"unitRoom"	TEXT NOT NULL,
	"day"	TEXT NOT NULL CHECK(length("day") < 4),
	"start"	INTEGER NOT NULL,
	"end"	INTEGER NOT NULL,
	UNIQUE("classID","unitPK"),
	FOREIGN KEY("unitPK") REFERENCES "Unit"("unitPK"),
	PRIMARY KEY("lessonID")
);

-- Populate tables
INSERT INTO "Student" ("studentID","Name","Contact") VALUES (1,'John Lenkins','hola.scam@yahoo.com');
INSERT INTO "Student" ("studentID","Name","Contact") VALUES (2,'Rebecca Sebastien','rebecca@gmail.com');
INSERT INTO "Unit" ("unitPK","unitID","unitName") VALUES (1,'IFB104','Building IT Systems');
INSERT INTO "Unit" ("unitPK","unitID","unitName") VALUES (2,'IFB105','Database Management');
INSERT INTO "Unit" ("unitPK","unitID","unitName") VALUES (3,'IFB103','IT Design');
INSERT INTO "Unit" ("unitPK","unitID","unitName") VALUES (4,'IFB102','Introduction to Computer Systems');
INSERT INTO "Unit" ("unitPK","unitID","unitName") VALUES (5,'CAB201','Programming Principles');
INSERT INTO "Unit" ("unitPK","unitID","unitName") VALUES (6,'CAB202','Microprocessors and Digital Systems');
INSERT INTO "Unit" ("unitPK","unitID","unitName") VALUES (7,'CAB240','Information Security');
INSERT INTO "Unit" ("unitPK","unitID","unitName") VALUES (8,'IAB207','Rapid Web Application Development');
INSERT INTO "Lessons" ("lessonID","classID","unitPK","unitRoom","day","start","end") VALUES (1,1,1,'GP-D301','THU',13,15);
INSERT INTO "Lessons" ("lessonID","classID","unitPK","unitRoom","day","start","end") VALUES (2,5,4,'','',0,0); -- CAB201
INSERT INTO "Lessons" ("lessonID","classID","unitPK","unitRoom","day","start","end") VALUES (3,6,1,'','',0,0); -- CAB202
INSERT INTO "Lessons" ("lessonID","classID","unitPK","unitRoom","day","start","end") VALUES (4,6,18,'','',0,0); -- CAB202
INSERT INTO "Lessons" ("lessonID","classID","unitPK","unitRoom","day","start","end") VALUES (5,7,2,'','',0,0); -- CAB240
INSERT INTO "Lessons" ("lessonID","classID","unitPK","unitRoom","day","start","end") VALUES (6,8,5,'','',0,0); -- IAB207
INSERT INTO "HaveUnit" ("studentID", "lessonID") VALUES (1,5);
INSERT INTO "HaveUnit" ("studentID","lessonID") VALUES (1,1);
COMMIT;
