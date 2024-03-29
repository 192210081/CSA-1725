diet_suggestion(heart_disease, 'Low-fat and low-sodium diet is recommended. Include fruits, vegetables, and whole grains. Limit red meat and processed foods.').
diet_suggestion(diabetes, 'Control carbohydrate intake. Choose whole grains, lean proteins, and healthy fats. Monitor portion sizes and distribute meals throughout the day.').
diet_suggestion(fatigue, 'green and healthy items and instant energy boosters').
diet_suggestion(fewer, 'fluid items').

suggest_diet(Disease) :-
    diet_suggestion(Disease, Sugge),
    write('For '), write(Disease), write(':'), nl,
    write(Sugge), nl.
