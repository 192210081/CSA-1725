person(john, date(2004, 6, 28)).
person(susan, date(1985, 8, 23)).
person(mike, date(1995, 2, 10)).
person(alice, date(1980, 11, 3)).

get_name_dob(Name, DOB) :-
    person(Name, DOB).

get_age(Name, Age) :-
    person(Name, date(Year, _, _)),
    get_current_year(CurrentYear),
    Age is CurrentYear - Year.

get_current_year(2024).
