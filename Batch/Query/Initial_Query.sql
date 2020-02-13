-- 회사이름
CREATE TABLE public."WANT_COMP_NAME_TB"
(
    "COMP_NAME_ID" serial NOT NULL,
    "COMP_NAME_NM" character varying(80),
    PRIMARY KEY ("COMP_NAME_ID")
)
WITH (
    OIDS = FALSE
);

ALTER TABLE public."WANT_COMP_NAME_TB"
    OWNER to postgres;
-- ----------------------------------------------------
-- 회사이름 MAPPED

CREATE TABLE public."WANT_MAPPED_COMP_NAME_TB"
(
    "MAPPED_COMP_NAME_ID" serial NOT NULL,
    "COMP_NAME_ID" integer NOT NULL,    
    "MAPPED_COMP_NAME_NM" character varying(80),
    PRIMARY KEY ("MAPPED_COMP_NAME_ID"),
    FOREIGN KEY ("COMP_NAME_ID") REFERENCES public."WANT_COMP_NAME_TB"("COMP_NAME_ID")
)
WITH (
    OIDS = FALSE
);

ALTER TABLE public."WANT_COMP_NAME_TB"
    OWNER to postgres;

-- ----------------------------------------------------
-- TAG
CREATE TABLE public."WANT_TAG_TB"
(
    "TAG_ID" serial NOT NULL,
    "TAG_NM" character varying(80),
    PRIMARY KEY ("TAG_ID")
)
WITH (
    OIDS = FALSE
);

ALTER TABLE public."WANT_TAG_TB"
    OWNER to postgres;

-- -----------------------------------------------------
--  TAG MAPPED
CREATE TABLE public."WANT_MAPPED_TAG_TB"
(
    "MAPPED_TAG_ID" serial NOT NULL,
    "TAG_ID" integer NOT NULL,    
    "MAPPED_TAG_NM" character varying(80),
    PRIMARY KEY ("MAPPED_TAG_ID"),
    FOREIGN KEY ("TAG_ID") REFERENCES public."WANT_TAG_TB"("TAG_ID")
)
WITH (
    OIDS = FALSE
);

ALTER TABLE public."WANT_TAG_TB"
    OWNER to postgres;

-- -----------------------------------------------------
-- MAPPING TABLE
CREATE TABLE public."WANT_COMP_N_TAG_TB"
(
    "COMP_N_TAG_ID" serial NOT NULL,
    "COMP_TAG_ID" integer,
    "COMP_NAME_ID" integer,
    PRIMARY KEY ("COMP_N_TAG_ID"),
    FOREIGN KEY ("COMP_NAME_ID") REFERENCES public."WANT_COMP_NAME_TB"("COMP_NAME_ID"),
    FOREIGN KEY ("COMP_TAG_ID") REFERENCES public."WANT_TAG_TB"("TAG_ID")
    
)
WITH (
    OIDS = FALSE
);

ALTER TABLE public."WANT_COMP_NAME_TB"
    OWNER to postgres;




