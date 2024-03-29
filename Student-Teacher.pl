student(john, cs101).
student(susan, math201).
student(mike, phy301).
student(alice, cs101).

teacher(prof_smith, cs101).
teacher(prof_jones, math201).
teacher(prof_doe, phy301).

subject(cs101, 'Introduction to Computer Science').
subject(math201, 'Advanced Mathematics').
subject(phy301, 'Physics for Engineers').

teaches_subject(Teacher, Subject) :-
    teacher(Teacher, SubjectCode),
    subject(SubjectCode, Subject).

enrolled_in_subject(Student, Subject) :-
    student(Student, SubjectCode),
    subject(SubjectCode, Subject).
