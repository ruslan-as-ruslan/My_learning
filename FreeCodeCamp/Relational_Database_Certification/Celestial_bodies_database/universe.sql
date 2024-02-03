-
-- PostgreSQL database dump
--

-- Dumped from database version 12.9 (Ubuntu 12.9-2.pgdg20.04+1)
-- Dumped by pg_dump version 12.9 (Ubuntu 12.9-2.pgdg20.04+1)

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

DROP DATABASE universe;
--
-- Name: universe; Type: DATABASE; Schema: -; Owner: freecodecamp
--

CREATE DATABASE universe WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'C.UTF-8' LC_CTYPE = 'C.UTF-8';


ALTER DATABASE universe OWNER TO freecodecamp;

\connect universe

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

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: galactic; Type: TABLE; Schema: public; Owner: freecodecamp
--

CREATE TABLE public.galactic (
    name character varying(40),
    volume integer NOT NULL,
    galactic_id integer NOT NULL
);


ALTER TABLE public.galactic OWNER TO freecodecamp;

--
-- Name: galaxy; Type: TABLE; Schema: public; Owner: freecodecamp
--

CREATE TABLE public.galaxy (
    galaxy_id integer NOT NULL,
    name character varying,
    distance_from_earth integer NOT NULL,
    age_in_millions_of_years numeric,
    description text,
    is_spherical boolean
);


ALTER TABLE public.galaxy OWNER TO freecodecamp;

--
-- Name: moon; Type: TABLE; Schema: public; Owner: freecodecamp
--

CREATE TABLE public.moon (
    moon_id integer NOT NULL,
    name character varying,
    distance_from_earth integer NOT NULL,
    age_in_millions_of_years numeric,
    description text,
    is_spherical boolean,
    planet_id integer NOT NULL
);


ALTER TABLE public.moon OWNER TO freecodecamp;

--
-- Name: planet; Type: TABLE; Schema: public; Owner: freecodecamp
--

CREATE TABLE public.planet (
    planet_id integer NOT NULL,
    name character varying,
    distance_from_earth integer NOT NULL,
    age_in_millions_of_years numeric,
    description text,
    is_spherical boolean,
    star_id integer NOT NULL
);


ALTER TABLE public.planet OWNER TO freecodecamp;

--
-- Name: star; Type: TABLE; Schema: public; Owner: freecodecamp
--

CREATE TABLE public.star (
    star_id integer NOT NULL,
    name character varying,
    distance_from_earth integer NOT NULL,
    age_in_millions_of_years numeric,
    description text,
    is_spherical boolean,
    galaxy_id integer NOT NULL
);


ALTER TABLE public.star OWNER TO freecodecamp;

--
-- Data for Name: galactic; Type: TABLE DATA; Schema: public; Owner: freecodecamp
--

INSERT INTO public.galactic VALUES ('sunny', 540000, 1);
INSERT INTO public.galactic VALUES ('snowy', 2700000, 2);
INSERT INTO public.galactic VALUES ('autumn', 1080000, 3);


--
-- Data for Name: galaxy; Type: TABLE DATA; Schema: public; Owner: freecodecamp
--

INSERT INTO public.galaxy VALUES (1, 'spiral galaxy', 9000000, NULL, NULL, NULL);
INSERT INTO public.galaxy VALUES (2, 'eliptical_galaxy', 789456, NULL, NULL, NULL);
INSERT INTO public.galaxy VALUES (3, 'barred_galaxy', 753951, NULL, NULL, NULL);
INSERT INTO public.galaxy VALUES (4, 'coliding_galaxy', 466, NULL, NULL, NULL);
INSERT INTO public.galaxy VALUES (5, 'irregural_galaxu', 466599, NULL, NULL, NULL);
INSERT INTO public.galaxy VALUES (6, 'lenticular_galaxy', 663279, NULL, NULL, NULL);


--
-- Data for Name: moon; Type: TABLE DATA; Schema: public; Owner: freecodecamp
--

INSERT INTO public.moon VALUES (1, 'Earths moon', 10000000, NULL, NULL, NULL, 1);
INSERT INTO public.moon VALUES (2, NULL, 666, NULL, NULL, NULL, 11);
INSERT INTO public.moon VALUES (3, NULL, 777, NULL, NULL, NULL, 10);
INSERT INTO public.moon VALUES (4, NULL, 333, NULL, NULL, NULL, 2);
INSERT INTO public.moon VALUES (5, NULL, 666, NULL, NULL, NULL, 3);
INSERT INTO public.moon VALUES (6, NULL, 999, NULL, NULL, NULL, 2);
INSERT INTO public.moon VALUES (7, NULL, 333, NULL, NULL, NULL, 10);
INSERT INTO public.moon VALUES (8, NULL, 5555, NULL, NULL, NULL, 4);
INSERT INTO public.moon VALUES (9, NULL, 6666, NULL, NULL, NULL, 2);
INSERT INTO public.moon VALUES (10, NULL, 7777, NULL, NULL, NULL, 3);
INSERT INTO public.moon VALUES (11, NULL, 2222, NULL, NULL, NULL, 4);
INSERT INTO public.moon VALUES (12, NULL, 3333, NULL, NULL, NULL, 5);
INSERT INTO public.moon VALUES (13, NULL, 1000, NULL, NULL, NULL, 2);
INSERT INTO public.moon VALUES (14, NULL, 400, NULL, NULL, NULL, 3);
INSERT INTO public.moon VALUES (15, NULL, 333, NULL, NULL, NULL, 2);
INSERT INTO public.moon VALUES (16, NULL, 3333, NULL, NULL, NULL, 4);
INSERT INTO public.moon VALUES (17, NULL, 7777, NULL, NULL, NULL, 8);
INSERT INTO public.moon VALUES (18, NULL, 10000, NULL, NULL, NULL, 10);
INSERT INTO public.moon VALUES (19, NULL, 7777, NULL, NULL, NULL, 4);
INSERT INTO public.moon VALUES (20, NULL, 99999, NULL, NULL, NULL, 5);
INSERT INTO public.moon VALUES (21, NULL, 2222, NULL, NULL, NULL, 2);
INSERT INTO public.moon VALUES (22, NULL, 22222, NULL, NULL, NULL, 9);


--
-- Data for Name: planet; Type: TABLE DATA; Schema: public; Owner: freecodecamp
--

INSERT INTO public.planet VALUES (1, 'Moonlight', 6548999, NULL, NULL, NULL, 1);
INSERT INTO public.planet VALUES (2, NULL, 6, NULL, NULL, NULL, 1);
INSERT INTO public.planet VALUES (3, NULL, 15, NULL, NULL, NULL, 2);
INSERT INTO public.planet VALUES (4, NULL, 99, NULL, NULL, NULL, 3);
INSERT INTO public.planet VALUES (5, NULL, 44, NULL, NULL, NULL, 4);
INSERT INTO public.planet VALUES (6, NULL, 111, NULL, NULL, NULL, 2);
INSERT INTO public.planet VALUES (7, NULL, 66, NULL, NULL, NULL, 3);
INSERT INTO public.planet VALUES (8, NULL, 999, NULL, NULL, NULL, 3);
INSERT INTO public.planet VALUES (9, NULL, 1111, NULL, NULL, NULL, 5);
INSERT INTO public.planet VALUES (10, NULL, 6666, NULL, NULL, NULL, 2);
INSERT INTO public.planet VALUES (11, NULL, 1222, NULL, NULL, NULL, 4);
INSERT INTO public.planet VALUES (12, NULL, 1333, NULL, NULL, NULL, 4);


--
-- Data for Name: star; Type: TABLE DATA; Schema: public; Owner: freecodecamp
--

INSERT INTO public.star VALUES (1, 'earth', 999999999, NULL, NULL, NULL, 1);
INSERT INTO public.star VALUES (2, NULL, 666, NULL, NULL, NULL, 4);
INSERT INTO public.star VALUES (3, NULL, 9999, NULL, NULL, NULL, 5);
INSERT INTO public.star VALUES (4, NULL, 687321, NULL, NULL, NULL, 1);
INSERT INTO public.star VALUES (5, NULL, 6666666, NULL, NULL, NULL, 3);
INSERT INTO public.star VALUES (6, NULL, 58746, NULL, NULL, NULL, 2);
INSERT INTO public.star VALUES (7, NULL, 1, NULL, NULL, NULL, 5);


--
-- Name: galaxy constraintname; Type: CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.galaxy
    ADD CONSTRAINT constraintname UNIQUE (galaxy_id);


--
-- Name: galactic galactic_galactic_id_key; Type: CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.galactic
    ADD CONSTRAINT galactic_galactic_id_key UNIQUE (galactic_id);


--
-- Name: galactic galactic_pkey; Type: CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.galactic
    ADD CONSTRAINT galactic_pkey PRIMARY KEY (galactic_id);


--
-- Name: galactic galactic_volume_key; Type: CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.galactic
    ADD CONSTRAINT galactic_volume_key UNIQUE (volume);


--
-- Name: galaxy galaxy_galaxy_id_key; Type: CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.galaxy
    ADD CONSTRAINT galaxy_galaxy_id_key UNIQUE (galaxy_id);


--
-- Name: galaxy galaxy_pkey; Type: CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.galaxy
    ADD CONSTRAINT galaxy_pkey PRIMARY KEY (galaxy_id);


--
-- Name: moon moon_moon_id_key; Type: CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.moon
    ADD CONSTRAINT moon_moon_id_key UNIQUE (moon_id);


--
-- Name: moon moon_pkey; Type: CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.moon
    ADD CONSTRAINT moon_pkey PRIMARY KEY (moon_id);


--
-- Name: planet planet_pkey; Type: CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.planet
    ADD CONSTRAINT planet_pkey PRIMARY KEY (planet_id);


--
-- Name: planet planet_planet_id_key; Type: CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.planet
    ADD CONSTRAINT planet_planet_id_key UNIQUE (planet_id);


--
-- Name: star star_pkey; Type: CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.star
    ADD CONSTRAINT star_pkey PRIMARY KEY (star_id);


--
-- Name: star star_star_id_key; Type: CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.star
    ADD CONSTRAINT star_star_id_key UNIQUE (star_id);


--
-- Name: moon moon_planet_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.moon
    ADD CONSTRAINT moon_planet_id_fkey FOREIGN KEY (planet_id) REFERENCES public.planet(planet_id);


--
-- Name: planet planet_star_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.planet
    ADD CONSTRAINT planet_star_id_fkey FOREIGN KEY (star_id) REFERENCES public.star(star_id);


--
-- Name: star star_galaxy_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.star
    ADD CONSTRAINT star_galaxy_id_fkey FOREIGN KEY (galaxy_id) REFERENCES public.galaxy(galaxy_id);


--
-- PostgreSQL database dump complete
--

