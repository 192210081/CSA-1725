hanoi(N, A, B, C) :-
    move(N, A, B, C).

move(0, _, _, _) :- !.

move(N, A, B, C) :-
    N > 0,
    M is N - 1,
    move(M, A, C, B),
    write('Move a disc from '), write(A), write(' to '), write(C), nl,
    move(M, B, A, C).