"""Create a TikZ LaTeX file representing a finite automata."""

def load_automata(stream):
    """Load an automata from a stream containing its description."""
    start = stream.readline().strip()
    sigma = tuple(word for word in stream.readline().strip().split(" "))
    accept = tuple(
        state
        for state in stream.readline().strip().split(" ")
        if state and state != '*'
    )
    rules = [rule.strip().split(" ") for rule in stream.readlines()]
    rules = [tuple(item for item in rule if item) for rule in rules]
    states = [rule[0] for rule in rules] + [rule[-1] for rule in rules]
    return (list(set(states)), sigma, start, rules, accept)


def gen_nodes(automata):
    """Generate TikZ nodes for automata states."""
    return []


def gen_path(automata):
    """Generate TikZ path for automata rules."""
    return []


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        infilename = sys.argv[1]
    else:
        raise RuntimeError("You must provida an automata description.")
    with open(infilename, "rt") as infile:
        automata = load_automata(infile)
    
    nodes = gen_nodes(automata)
    path = gen_path(automata)

    with open("automata.tex", "rt") as texfile:
        for line in texfile.readlines():
            if "@NODES@" in line:
                line = line.replace("@NODES@", "\n".join(nodes))
            if "@PATH@" in line:
                line = line.replace("@PATH@", "\n".join(path))
            print(line, end="")
        
