create table if not exists games
(
    id               serial
        constraint games_pk
            primary key,
    name             varchar(100),
    word             integer not null,
    created_datetime timestamp default now(),
    updated_datetime timestamp
);

alter table games
    owner to simpu;

create trigger games_update_datetime
    before update
    on games
    for each row
execute procedure update_datetime();

create table if not exists words
(
    id               serial
        constraint words_pk
            primary key,
    word             varchar(100) not null,
    created_datetime timestamp default now(),
    updated_datetime timestamp,
    approved         boolean   default false
);

alter table words
    owner to simpu;

create trigger words_update_datetime
    before update
    on words
    for each row
execute procedure update_datetime();

