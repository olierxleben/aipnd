def create_groups(items, n):
    """Splits items into n groups of equal size, although the last one may be shorter."""
    # determine the size each group should be
    try:
        # this line could cause a ZeroDivisionError exception
        size = len(items) // n
    except ZeroDivisionError:
        print('WARNING: Returning empty list. Please use a nonzero number.')
        return []
    else:
        # create each group and append to a new list
        groups = []
        for i in range(0, len(items), size):
            groups.append(items[i:i + size])
        return groups
    finally:
        # print the number of groups and return groups
        print("{} groups returned.".format(n))


print("Creating 6 groups...")
for group in create_groups(range(32), 6):
    print(list(group))

print("\nCreating 0 groups...")
for group in create_groups(range(32), 0):
    print(list(group))
