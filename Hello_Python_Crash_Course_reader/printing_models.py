unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

# while unprinted_designs:
#     current_design = unprinted_designs.pop()
#     completed_models.append(current_design)
# print("completed modes: ")
# print(completed_models)
# print(unprinted_designs)


def print_models(var):
    while var:
        current_design = var.pop()
        completed_models.append(current_design)
    print("completed modes: ")
    print(completed_models)

    print("unprinted_designs: ")
    print(unprinted_designs)

print_models(unprinted_designs)