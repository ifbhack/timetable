BEGIN TRANSACTION;
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
	"lessonID"	INTEGER NOT NULL UNIQUE,
	"unitPK"	INTEGER NOT NULL,
	"unitRoom"	TEXT NOT NULL,
	"day"	TEXT NOT NULL CHECK(length("day") < 4),
	"start"	INTEGER NOT NULL,
	"end"	INTEGER NOT NULL,
	FOREIGN KEY("unitPK") REFERENCES "Unit"("unitPK"),
	PRIMARY KEY("lessonID" AUTOINCREMENT)
);
INSERT INTO "Student" ("studentID","Name","Contact") VALUES (1,'John Lenkins','hola.scam@yahoo.com');
INSERT INTO "Student" ("studentID","Name","Contact") VALUES (2,'Rebecca Sebastien','rebecca@gmail.com');
INSERT INTO "HaveUnit" ("studentID","lessonID") VALUES (1,1);
INSERT INTO "Unit" ("unitPK","unitID","unitName") VALUES (1,'IFB104','Building IT Systems');
INSERT INTO "Unit" ("unitPK","unitID","unitName") VALUES (2,'IFB105','Database Management');
INSERT INTO "Unit" ("unitPK","unitID","unitName") VALUES (3,'IFB103','IT Design');
INSERT INTO "Unit" ("unitPK","unitID","unitName") VALUES (4,'IFB102','Introduction to Computer Systems');
INSERT INTO "Lessons" ("lessonID","unitPK","unitRoom","day","start","end") VALUES (1,1,'GP-D301','THU',13,15);
COMMIT;
