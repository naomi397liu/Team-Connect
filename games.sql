--
-- PostgreSQL database dump
--

-- Dumped from database version 10.14 (Ubuntu 10.14-0ubuntu0.18.04.1)
-- Dumped by pg_dump version 10.14 (Ubuntu 10.14-0ubuntu0.18.04.1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

ALTER TABLE ONLY public.users DROP CONSTRAINT users_sport_id_fkey;
ALTER TABLE ONLY public.users DROP CONSTRAINT users_city_id_fkey;
ALTER TABLE ONLY public.teams DROP CONSTRAINT teams_user_id_fkey;
ALTER TABLE ONLY public.teams DROP CONSTRAINT teams_sport_id_fkey;
ALTER TABLE ONLY public.teams DROP CONSTRAINT teams_city_id_fkey;
ALTER TABLE ONLY public.players DROP CONSTRAINT players_user_id_fkey;
ALTER TABLE ONLY public.players DROP CONSTRAINT players_team_id_fkey;
ALTER TABLE ONLY public.parks DROP CONSTRAINT parks_city_id_fkey;
ALTER TABLE ONLY public.users DROP CONSTRAINT users_username_key;
ALTER TABLE ONLY public.users DROP CONSTRAINT users_pkey;
ALTER TABLE ONLY public.teams DROP CONSTRAINT teams_team_name_key;
ALTER TABLE ONLY public.teams DROP CONSTRAINT teams_pkey;
ALTER TABLE ONLY public.sports DROP CONSTRAINT sports_pkey;
ALTER TABLE ONLY public.players DROP CONSTRAINT players_pkey;
ALTER TABLE ONLY public.parks DROP CONSTRAINT parks_pkey;
ALTER TABLE ONLY public.cities DROP CONSTRAINT cities_pkey;
ALTER TABLE public.users ALTER COLUMN user_id DROP DEFAULT;
ALTER TABLE public.teams ALTER COLUMN team_id DROP DEFAULT;
ALTER TABLE public.sports ALTER COLUMN sport_id DROP DEFAULT;
ALTER TABLE public.players ALTER COLUMN player_id DROP DEFAULT;
ALTER TABLE public.parks ALTER COLUMN park_id DROP DEFAULT;
ALTER TABLE public.cities ALTER COLUMN city_id DROP DEFAULT;
DROP SEQUENCE public.users_user_id_seq;
DROP TABLE public.users;
DROP SEQUENCE public.teams_team_id_seq;
DROP TABLE public.teams;
DROP SEQUENCE public.sports_sport_id_seq;
DROP TABLE public.sports;
DROP SEQUENCE public.players_player_id_seq;
DROP TABLE public.players;
DROP SEQUENCE public.parks_park_id_seq;
DROP TABLE public.parks;
DROP SEQUENCE public.cities_city_id_seq;
DROP TABLE public.cities;
DROP EXTENSION plpgsql;
DROP SCHEMA public;
--
-- Name: public; Type: SCHEMA; Schema: -; Owner: -
--

CREATE SCHEMA public;


--
-- Name: SCHEMA public; Type: COMMENT; Schema: -; Owner: -
--

COMMENT ON SCHEMA public IS 'standard public schema';


--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: -
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: -
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: cities; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.cities (
    city_id integer NOT NULL,
    city_name character varying
);


--
-- Name: cities_city_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.cities_city_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: cities_city_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.cities_city_id_seq OWNED BY public.cities.city_id;


--
-- Name: parks; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.parks (
    park_id integer NOT NULL,
    park_name character varying,
    city_id integer
);


--
-- Name: parks_park_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.parks_park_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: parks_park_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.parks_park_id_seq OWNED BY public.parks.park_id;


--
-- Name: players; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.players (
    player_id integer NOT NULL,
    phone character varying,
    user_id integer,
    team_id integer
);


--
-- Name: players_player_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.players_player_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: players_player_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.players_player_id_seq OWNED BY public.players.player_id;


--
-- Name: sports; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.sports (
    sport_id integer NOT NULL,
    sport_name character varying
);


--
-- Name: sports_sport_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.sports_sport_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: sports_sport_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.sports_sport_id_seq OWNED BY public.sports.sport_id;


--
-- Name: teams; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.teams (
    team_id integer NOT NULL,
    team_name character varying,
    description character varying,
    user_id integer,
    sport_id integer,
    city_id integer
);


--
-- Name: teams_team_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.teams_team_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: teams_team_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.teams_team_id_seq OWNED BY public.teams.team_id;


--
-- Name: users; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.users (
    user_id integer NOT NULL,
    username character varying,
    password character varying,
    bio character varying,
    sport_id integer,
    city_id integer
);


--
-- Name: users_user_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.users_user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: users_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.users_user_id_seq OWNED BY public.users.user_id;


--
-- Name: cities city_id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.cities ALTER COLUMN city_id SET DEFAULT nextval('public.cities_city_id_seq'::regclass);


--
-- Name: parks park_id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.parks ALTER COLUMN park_id SET DEFAULT nextval('public.parks_park_id_seq'::regclass);


--
-- Name: players player_id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.players ALTER COLUMN player_id SET DEFAULT nextval('public.players_player_id_seq'::regclass);


--
-- Name: sports sport_id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.sports ALTER COLUMN sport_id SET DEFAULT nextval('public.sports_sport_id_seq'::regclass);


--
-- Name: teams team_id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.teams ALTER COLUMN team_id SET DEFAULT nextval('public.teams_team_id_seq'::regclass);


--
-- Name: users user_id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.users ALTER COLUMN user_id SET DEFAULT nextval('public.users_user_id_seq'::regclass);


--
-- Data for Name: cities; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.cities (city_id, city_name) FROM stdin;
1	San Francisco
2	Sacramento
3	Los Angeles
\.


--
-- Data for Name: parks; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.parks (park_id, park_name, city_id) FROM stdin;
\.


--
-- Data for Name: players; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.players (player_id, phone, user_id, team_id) FROM stdin;
1	+1-414-645-3118	1	1
2	137-926-2072x12281	2	1
3	(535)790-1418x55262	3	1
4	785.142.7377	4	2
5	430.185.0428	5	2
6	(827)966-3925	6	2
7	368.232.4480	7	2
8	001-804-567-7556x23991	8	2
9	(660)736-9347	9	2
10	4671713928	10	3
11	(675)765-9121	11	3
12	(562)242-7992x97637	12	3
13	411.187.3056x24043	13	3
14	049.249.6705x983	14	3
15	8474894553	15	3
16	913.249.5684	16	3
17	794.290.2592x0266	17	3
18	+1-738-074-9091x9876	18	3
19	+1-930-909-7530x287	19	4
20	001-171-534-3379x8929	20	4
21	(191)649-9390	21	4
22	001-695-134-6936	22	4
23	001-240-323-6187x3930	23	4
24	001-787-284-7999	24	4
25	(356)507-4905	25	5
26	746.973.0465x8931	26	5
27	9692451990	27	5
28	149.282.9924	28	5
29	+1-694-160-0728	29	6
30	956-850-8470x0606	30	6
31	001-190-829-8447x3298	31	6
32	611.340.6702x08198	32	6
33	2994096249	33	6
34	028-441-2045	34	6
35	001-425-597-4198x957	35	6
36	+1-352-211-5605x349	35	7
37	721.315.4752	36	8
38	+1-661-273-7396	37	9
39	001-660-312-3602x7911	38	10
40	721.252.2389	39	11
41	006-756-9757x2591	40	11
43	6504404464	43	3
45	666-666-4444	44	12
46	666-666-4444	44	1
47	666-666-4444	44	2
48	666-666-4444	44	3
49	666-666-4444	44	4
50	666-666-4444	44	5
51	666-666-4444	44	6
52	666-666-4444	44	7
53	666-666-4444	44	8
54	666-666-4444	44	9
55	666-666-4444	44	10
56	666-666-4444	44	11
59	6128393363	42	6
60	6128393363	42	13
\.


--
-- Data for Name: sports; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.sports (sport_id, sport_name) FROM stdin;
1	Soccer
2	Basketball
3	Volleyball
\.


--
-- Data for Name: teams; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.teams (team_id, team_name, description, user_id, sport_id, city_id) FROM stdin;
1	Killers	Play to win	1	1	1
2	Wombats	Best D, greatest offense	4	2	2
3	Cougars	Come play on Saturdays!	10	1	2
4	Wolves	Play ball with me on Tuesday nights!	19	2	1
5	Sharks	Speedsters! Playing every weekend!	25	3	3
6	Banana Slugs	Play to win	29	1	1
7	Peach Eaters	Best D, greatest offense	35	2	2
8	Cat Lovers	Farm for Fun	36	3	3
9	Shark Eaters	Come play on Saturdays!	37	1	2
10	Speedsters	Play ball with me on Tuesday nights!	38	2	1
11	Croissant Eaters	Speedsters! Playing every weekend!	39	3	3
12	Big OL Dino	I am the best. Bow before my superiority. My prowess knows no equal. I never lose, and I have no rivals. Everything is mine. I am the only true constant in the universe. We also have pizza parties on Fridays.	44	3	1
13	Cats	Saturdays 10am!	42	1	1
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.users (user_id, username, password, bio, sport_id, city_id) FROM stdin;
1	test_user1	test_pass1	Test user created for testing	2	3
2	James	733-64-3244	Space maybe detail why national.	1	3
3	Taylor	269-78-4247	Represent city resource individual look explain new similar.	1	1
4	Kevin	730-45-5599	System small old smile great detail husband seat.	3	1
5	Brian	802-54-6496	Science experience threat.	1	2
6	Elizabeth	055-81-9406	Magazine require lay.	1	1
7	Tricia	462-65-1460	Doctor write much president win worry compare.	3	2
8	Crystal	013-31-1121	Today put up thought address recent.	1	2
9	John	130-39-8643	Indicate feeling region.	1	2
10	Todd	014-94-9135	Painting anything local everybody professional develop sure.	3	1
11	Manuel	587-87-9252	Wall quality it investment at tax.	2	1
12	Terri	834-68-7336	Minute language computer.	2	3
13	Christopher	867-68-8460	Expect for table everything quickly woman.	3	3
14	Eric	373-27-0532	Protect you public simple executive city give.	2	2
15	Kyle	180-77-3037	Property bad machine important response.	2	2
16	Jason	677-60-6166	Future green lay program international statement these through.	1	1
17	Laura	780-90-9576	Scene military personal hair general dog.	2	3
18	Rebecca	779-72-7991	Population whatever such theory rate security.	2	2
19	Sandra	302-36-4420	Nice country dinner year.	3	3
20	Allison	848-85-1597	Risk only speak war.	3	1
21	Kendra	392-75-7423	Security different begin politics attention set especially.	1	1
22	Ashley	533-92-4284	Specific appear themselves crime draw act range out.	1	3
23	Thomas	100-46-3414	Space effort huge wife.	1	1
24	Olivia	281-31-4041	Others from large line wrong education range world.	1	3
25	Douglas	696-65-7976	Usually customer number could model might.	2	2
26	Amber	231-61-1358	Star wall watch.	2	2
27	Katherine	423-33-5900	Health determine eight which.	1	1
28	Gabriel	024-73-0661	Writer simply clear program instead.	3	2
29	Tanya	406-71-7533	Own heavy board not.	2	1
30	Anthony	743-57-7909	Sit energy usually.	1	2
31	Jasmine	665-17-9727	Less bad exactly.	2	3
32	Jose	727-97-3164	Appear large anyone fear environmental present.	1	2
33	Kathleen	178-43-8867	Glass little something pretty music speech these.	2	3
34	Amanda	262-91-6816	Company story PM cover.	2	3
35	Nicole	753-16-6694	Or magazine manager because despite claim give win.	2	3
36	Robert	551-51-9558	Across able class Democrat TV continue.	3	1
37	Emily	605-75-9875	Address sense as much sport short.	1	2
38	Steven	011-45-4702	Good plant nature which civil.	2	1
39	Ebony	149-22-5074	Material anything three leg.	3	2
40	David	499-99-7639	Successful control size direction then billion.	3	2
41	Angela	109-87-9902	Range same leave major public today.	2	2
42	nhliu	123		1	1
43	LongLegs	123	Setter but great server too!!	3	3
44	TheREX	1	I am the best at everything. I can do it all, just	3	1
\.


--
-- Name: cities_city_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.cities_city_id_seq', 3, true);


--
-- Name: parks_park_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.parks_park_id_seq', 1, false);


--
-- Name: players_player_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.players_player_id_seq', 60, true);


--
-- Name: sports_sport_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.sports_sport_id_seq', 3, true);


--
-- Name: teams_team_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.teams_team_id_seq', 13, true);


--
-- Name: users_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.users_user_id_seq', 44, true);


--
-- Name: cities cities_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.cities
    ADD CONSTRAINT cities_pkey PRIMARY KEY (city_id);


--
-- Name: parks parks_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.parks
    ADD CONSTRAINT parks_pkey PRIMARY KEY (park_id);


--
-- Name: players players_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.players
    ADD CONSTRAINT players_pkey PRIMARY KEY (player_id);


--
-- Name: sports sports_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.sports
    ADD CONSTRAINT sports_pkey PRIMARY KEY (sport_id);


--
-- Name: teams teams_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.teams
    ADD CONSTRAINT teams_pkey PRIMARY KEY (team_id);


--
-- Name: teams teams_team_name_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.teams
    ADD CONSTRAINT teams_team_name_key UNIQUE (team_name);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (user_id);


--
-- Name: users users_username_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_username_key UNIQUE (username);


--
-- Name: parks parks_city_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.parks
    ADD CONSTRAINT parks_city_id_fkey FOREIGN KEY (city_id) REFERENCES public.cities(city_id);


--
-- Name: players players_team_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.players
    ADD CONSTRAINT players_team_id_fkey FOREIGN KEY (team_id) REFERENCES public.teams(team_id);


--
-- Name: players players_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.players
    ADD CONSTRAINT players_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(user_id);


--
-- Name: teams teams_city_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.teams
    ADD CONSTRAINT teams_city_id_fkey FOREIGN KEY (city_id) REFERENCES public.cities(city_id);


--
-- Name: teams teams_sport_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.teams
    ADD CONSTRAINT teams_sport_id_fkey FOREIGN KEY (sport_id) REFERENCES public.sports(sport_id);


--
-- Name: teams teams_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.teams
    ADD CONSTRAINT teams_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(user_id);


--
-- Name: users users_city_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_city_id_fkey FOREIGN KEY (city_id) REFERENCES public.cities(city_id);


--
-- Name: users users_sport_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_sport_id_fkey FOREIGN KEY (sport_id) REFERENCES public.sports(sport_id);


--
-- Name: SCHEMA public; Type: ACL; Schema: -; Owner: -
--

GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--

