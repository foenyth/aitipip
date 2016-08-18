def favourite(instructor):
    """Returns the favourite thing of the given instructor."""

    if instructor == "Joe":
        return "games"
    elif instructor == "Scott":
        return "ties"
    elif instructor == "John":
        return "outdoor"
    else:
        print "favourite saw invalid instructor: ", instructor

print favourite("John")
print favourite("Jeannie")
