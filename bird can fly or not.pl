bird(sparrow, true).
bird(ostrich, false).
bird(penguin, false).
bird(crow, true).
bird(kiwi, false).
bird(pegion, true).

can_fly(Bird) :-
    bird(Bird, CanFly),
    CanFly = true,
    write(Bird), write(' can fly.').

can_fly(Bird) :-
    bird(Bird, CanFly),
    CanFly = false,
    write(Bird), write(' cannot fly.').
