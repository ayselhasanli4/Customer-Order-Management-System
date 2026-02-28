create table musterii(
musteri_id int primary key,
ad varchar2(20),
seher varchar2(20));

insert into musterii values(&musteri_id,'&ad','&seher');
select * from musterii;
commit;

create table sifaris(
sifaris_id int primary key,
musteri_id int,
tarix varchar2(20),
mebleg int,
foreign key (musteri_id) references musterii (musteri_id));
insert into sifaris values(&sifaris_id,&musteri_id,'&tarix',&mebleg);
select * from sifaris;
commit;
