
drop table if exists member;
create table member (
  id integer primary key autoincrement,
  username text not null unique,
  realname text not null,
  nickname text not null,
  email text not null,
  irc text,
  twitter text,
  github text,
  address text not null,
  key integer not null,
  adm integer not null
);

drop table if exists payment;
create table payment (
  id integer primary key autoincrement,
  username text,
  month integer,
  year integer,
  recorded integer,
  admin text
);

drop table if exists status;
create table status (
  id integer primary key autoincrement,
  state integer,
  message text,
  username text,
  thetime integer
);

DROP TABLE IF EXISTS events;
CREATE TABLE events (
       id integer primary key autoincrement, 
       name text not null, 
       type text not null, 
       timestamp integer, 
       extra text
);

DROP TABLE IF EXISTS treasurer;
CREATE TABLE treasurer (
       id integer primary key autoincrement,
       user text not null,
       begin integer not null, -- UNIX timestamp
       end integer -- UNIX timestamp
);
-- Tom 18th Feb 2014 -> AGM?? or maybe now
-- Ed -  well not yet. Might have to make treasurer functions available to all admins


DROP TABLE IF EXISTS balance;
CREATE TABLE balance (
       id integer primary key autoincrement,
       time integer not null, 
       balance text not null,
       user text not null
);

DROP TABLE IF EXISTS dismembered;
CREATE TABLE dismembered (
       id integer primary key autoincrement,
       user text not null,
       timestamp integer not null, -- UNIX timestamp
       reason text not null,
       date_reset integer, -- UNIX timestamp
       reason_reset text
);

DROP TABLE IF EXISTS door_codes;
CREATE TABLE door_codes (
       id integer primary key autoincrement,
       user text not null,
       code text not null,
       created integer not null,
       used integer
);   

DROP TABLE IF EXISTS email_events;
CREATE TABLE email_events (
       code text primary key,
       description text,
       def integer not null
       );

DROP TABLE IF EXISTS email_prefs;
CREATE TABLE email_prefs (
       user text not null,
       code text not null,
       pref integer not null
       );

DROP TABLE IF EXISTS application;
CREATE TABLE application (
       id integer primary key autoincrement,
       accepted integer not null default 0,
       username text not null unique,
       realname text not null,
       nickname text not null,
       email text not null,
       address text not null,
       received integer not null default 0,
       ignored integer not null default 0,
       ignored_by text
       );

DROP TABLE IF EXISTS url_codes;
CREATE TABLE url_codes (
       id integer primary key autoincrement,
       code text not null,
       username text not null
       );
