grammar = """

?assignment: "$" CNAME ":=" value

?addition: NUMBER "+" NUMBER
?subtraction: NUMBER "-" NUMBER

value: ESCAPED_STRING -> string
    | NUMBER          -> number
    | "true"          -> true
    | "false"         -> false
    | nil

nil: "NIL"

%import common.CNAME
%import common.NUMBER
%import common.WS
%import common.ESCAPED_STRING
%ignore  WS
"""