create table general (
 id INTEGER UNIQUE PRIMARY KEY,
 userhash BLOB UNIQUE,
 userid INTEGER,
 ship TEXT,
 time INT,
 version TEXT,
 fate TEXT,
 player TEXT,
 score INT,
 credits INT,
 respawns INT
 systems INT
);
create table users (
  id INTEGER PRIMARY KEY,
  userhash BLOB,
  options BLOB
);
create table enemy_stations_destroyed (
 id INTEGER PRIMARY KEY,
 userhash BLOB UNIQUE,
 userid INTEGER,
 station TEXT,
 count INTEGER
);
create table enemy_ships_destroyed (
 id INTEGER PRIMARY KEY,
 userhash BLOB UNIQUE,
 userid INTEGER,
 ship TEXT,
 count INTEGER
);
create table friendly_stations_destroyed (
 id INTEGER PRIMARY KEY,
 userhash BLOB UNIQUE,
 userid INTEGER,
 station TEXT,
 count INTEGER
);
create table friendly_ships_destroyed (
 id INTEGER PRIMARY KEY,
 userhash BLOB UNIQUE,
 userid INTEGER,
 ship TEXT,
 count INTEGER
);
create table commerce (
 id INTEGER PRIMARY KEY,
 userhash BLOB UNIQUE,
 arms INTEGER,
 luxury_goods INTEGER,
 goods_and_materials INTEGER,
 ships_equipment INTEGER,  
 medical_supplies INTEGER
);
create table weapons_fired (
 id INTEGER PRIMARY KEY,
 userhash BLOB UNIQUE,
 userid INTEGER,
 weapon TEXT,
 count INTEGER
);

