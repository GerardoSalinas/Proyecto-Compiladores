grammar = """

?assignment: "$" CNAME ":=" value
?addition: NUMBER "+" NUMBER
?subtraction: NUMBER "-" NUMBER
repetition: INT"*"WORD

value: ESCAPED_STRING -> string
    | NUMBER          -> number
    | "true"          -> true
    | "false"         -> false
    | nil

nil: "NIL"

%import common.CNAME
%import common.NUMBER
%import common.WS
%import common.INT
%import common.WORD
%import common.ESCAPED_STRING
%ignore  WS
"""