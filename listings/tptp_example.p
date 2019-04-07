% File     : LCL001-1 : TPTP v7.2.0. Released v1.0.0.
cnf(condensed_detachment,axiom,
    ( ~ is_a_theorem(or(not(X),Y))
    | ~ is_a_theorem(X)
    | is_a_theorem(Y) )).

cnf(an_1,axiom,
    ( is_a_theorem(or(not(or(not(Y),Z)),or(not(or(X,Y)),or(X,Z)))) )).

cnf(an_2,axiom,
    ( is_a_theorem(or(not(or(X,Y)),or(Y,X))) )).

cnf(an_3,axiom,
    ( is_a_theorem(or(not(X),or(Y,X))) )).

cnf(an_4,axiom,
    ( is_a_theorem(or(not(or(X,X)),X)) )).

cnf(prove_an_CAMerideth,negated_conjecture,
    ( ~ is_a_theorem(or(not(or(not(or(not(a),b)),or(c,or(e,falsehood)))),or(not(or(not(e),a)),or(c,or(falsehood,a))))) )).


