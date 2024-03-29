planet(mercury).
planet(venus).
planet(earth).
planet(mars).
planet(jupiter).
planet(saturn).
planet(uranus).
planet(neptune).

get_planet(planet) :-
    planet(Planet),
    write(Planet),
    write(' ').
