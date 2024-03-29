fruit_color(apple, red).
fruit_color(banana, yellow).
fruit_color(grape, purple).
fruit_color(orange, orange).
fruit_color(pear, green).
fruit_color(cherry, red).
fruit_color(berry, blue).

fruit_and_color(Fruit, Color) :-
    fruit_color(Fruit, Color).