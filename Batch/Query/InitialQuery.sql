-- ----------------------------------------------------
-- 회사이름
CREATE TABLE public."WANT_COMP_NAME_TB"
(
    "COMP_NAME_ID" serial NOT NULL,
    "COMP_NAME_NM" character varying(80) NOT NULL,
    PRIMARY KEY ("COMP_NAME_ID")
)
WITH (
    OIDS = FALSE
);

-- ----------------------------------------------------
-- 회사 CAT

CREATE TABLE public."WANT_COMP_CAT_TB"
(
    "COMP_CAT_ID" serial NOT NULL,
    "COMP_NAME_NM" character varying(80) NOT NULL,    
    PRIMARY KEY ("COMP_CAT_ID")
)
WITH (
    OIDS = FALSE
);

-- ----------------------------------------------------
-- 회사이름 N CAT 
CREATE TABLE public."WANT_COMP_NAME_CAT_TB"
(
    "COMP_NAME_CAT_ID" serial NOT NULL,
    "COMP_NAME_ID" integer NOT NULL,
    "COMP_CAT_ID" integer NOT NULL,

    PRIMARY KEY ("COMP_NAME_CAT_ID"),
    FOREIGN KEY ("COMP_NAME_ID") REFERENCES public."WANT_COMP_NAME_TB"("COMP_NAME_ID"),
    FOREIGN KEY ("COMP_CAT_ID") REFERENCES public."WANT_COMP_CAT_TB"("COMP_CAT_ID")
)
WITH (
    OIDS = FALSE
);

-- ----------------------------------------------------
-- TAG
CREATE TABLE public."WANT_TAG_NAME_TB"
(
    "TAG_NAME_ID" serial NOT NULL,
    "TAG_NAME_NM" character varying(80) NOT NULL,
    PRIMARY KEY ("TAG_NAME_ID")
)
WITH (
    OIDS = FALSE
);
-- ----------------------------------------------------
-- TAG CAT
CREATE TABLE public."WANT_TAG_CAT_TB"
(
    "TAG_CAT_ID" serial NOT NULL,
    "TAG_CAT_NM" character varying(80) NOT NULL,
    PRIMARY KEY ("TAG_CAT_ID")
)
WITH (
    OIDS = FALSE
);
-- -----------------------------------------------------
--  TAG MAPPED
CREATE TABLE public."WANT_TAG_NAME_CAT_TB"
(
    "TAG_NAME_CAT_ID" serial NOT NULL,
    "TAG_NAME_ID" integer NOT NULL,    
    "TAG_CAT_ID" integer NOT NULL,

    PRIMARY KEY ("TAG_NAME_CAT_ID"),
    FOREIGN KEY ("TAG_NAME_ID") REFERENCES public."WANT_TAG_NAME_TB"("TAG_NAME_ID"),
    FOREIGN KEY ("TAG_CAT_ID") REFERENCES public."WANT_TAG_CAT_TB"("TAG_CAT_ID")
)
WITH (
    OIDS = FALSE
);

-- -----------------------------------------------------
-- MAPPING TABLE
CREATE TABLE public."WANT_MAPPED_TB"
(
    "MAPPED_TB_ID" serial NOT NULL,
    "COMP_CAT_ID" integer,
    "TAG_CAT_ID" integer,
    PRIMARY KEY ("MAPPED_TB_ID"),
    FOREIGN KEY ("COMP_CAT_ID") REFERENCES public."WANT_COMP_CAT_TB"("COMP_CAT_ID"),
    FOREIGN KEY ("TAG_CAT_ID") REFERENCES public."WANT_TAG_CAT_TB"("TAG_CAT_ID")
    
)
WITH (
    OIDS = FALSE
);

ALTER TABLE public."WANT_COMP_NAME_TB" OWNER to postgres;
ALTER TABLE public."WANT_COMP_CAT_TB" OWNER to postgres;
ALTER TABLE public."WANT_COMP_NAME_CAT_TB" OWNER to postgres;
ALTER TABLE public."WANT_TAG_NAME_TB" OWNER to postgres;
ALTER TABLE public."WANT_TAG_CAT_TB" OWNER to postgres;
ALTER TABLE public."WANT_TAG_NAME_CAT_TB" OWNER to postgres;
ALTER TABLE public."WANT_MAPPED_TB" OWNER to postgres;

