transition(State, NextState, Cost) :-
    NextState is State + 1,
    Cost is 1.

heuristic(State, HeuristicValue) :-
    GoalState = 10,
    HeuristicValue is GoalState - State.

best_first_search(Start, Path) :-
    best_first_search_helper([node(Start, [], 0, 0)], Path).

best_first_search_helper(OpenSet, Path) :-
    min_heuristic_node(OpenSet, MinNode),
    MinNode = node(State, CurrentPath, _, _),
    
    (goal(State) ->
        reverse(CurrentPath, Path)
    ;
        findall(
            node(NextState, [NextState | CurrentPath], Cost, Heuristic),
            (
                transition(State, NextState, Cost),
                heuristic(NextState, Heuristic)
            ),
            Successors
        ),
        append(OpenSet, Successors, NewOpenSet),
        best_first_search_helper(NewOpenSet, Path)
    ).

min_heuristic_node([Node], Node).
min_heuristic_node([Node | Rest], MinNode) :-
    min_heuristic_node(Rest, RestMinNode),
    compare_nodes(Node, RestMinNode, MinNode).

compare_nodes(Node1, Node2, Node1) :-
    Node1 = node(_, _, _, Heuristic1),
    Node2 = node(_, _, _, Heuristic2),
    Heuristic1 =< Heuristic2.

compare_nodes(Node1, Node2, Node2) :-
    Node1 = node(_, _, _, Heuristic1),
    Node2 = node(_, _, _, Heuristic2),
    Heuristic1 > Heuristic2.

goal(State) :-
    State = 10.
