parent(john, jim).
parent(john, sara).
parent(jane, jim).
parent(jane, sara).
parent(jim, ann).
parent(anna, ann).
parent(sara, mike).
parent(sam, mike).

father(Father, Child) :-
    parent(Father, Child),
    male(Father).

mother(Mother, Child) :-
    parent(Mother, Child),
    female(Mother).

sibling(Sibling1, Sibling2) :-
    parent(Parent, Sibling1),
    parent(Parent, Sibling2),
    Sibling1 \= Sibling2.

male(john).
male(jim).
male(mike).
male(sam).

female(jane).
female(sara).
female(anna).
female(ann).