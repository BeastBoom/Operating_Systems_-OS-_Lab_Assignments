# =========================================================
# PAGE REPLACEMENT ALGORITHMS (OS LAB ASSIGNMENT 3)
# Algorithms: FIFO, LRU, Optimal, MRU, Second Chance
# =========================================================

# -------------------------
# TASK 1: INPUT
# -------------------------
frames = int(input("Enter number of frames: "))
pages = list(map(int, input("Enter page reference string: ").split()))

print("\nPage Reference String:")
print(pages)


# -------------------------
# FIFO
# -------------------------
def fifo(pages, frames):
    memory = []
    queue = []
    faults = 0

    print("\n--- FIFO ---")
    for page in pages:
        if page not in memory:
            faults += 1

            if len(memory) < frames:
                memory.append(page)
                queue.append(page)
            else:
                oldest = queue.pop(0)
                memory.remove(oldest)
                memory.append(page)
                queue.append(page)

        print(f"Page {page} -> {memory}")

    return faults


# -------------------------
# LRU
# -------------------------
def lru(pages, frames):
    memory = []
    faults = 0

    print("\n--- LRU ---")
    for i in range(len(pages)):
        page = pages[i]

        if page not in memory:
            faults += 1

            if len(memory) < frames:
                memory.append(page)
            else:
                lru_page = None
                farthest = -1

                for m in memory:
                    if m not in pages[:i]:
                        lru_page = m
                        break
                    else:
                        idx = pages[:i][::-1].index(m)
                        if idx > farthest:
                            farthest = idx
                            lru_page = m

                memory.remove(lru_page)
                memory.append(page)

        print(f"Page {page} -> {memory}")

    return faults


# -------------------------
# OPTIMAL
# -------------------------
def optimal(pages, frames):
    memory = []
    faults = 0

    print("\n--- OPTIMAL ---")
    for i in range(len(pages)):
        page = pages[i]

        if page not in memory:
            faults += 1

            if len(memory) < frames:
                memory.append(page)
            else:
                future = pages[i+1:]
                replace = None
                farthest = -1

                for m in memory:
                    if m not in future:
                        replace = m
                        break
                    else:
                        idx = future.index(m)
                        if idx > farthest:
                            farthest = idx
                            replace = m

                memory.remove(replace)
                memory.append(page)

        print(f"Page {page} -> {memory}")

    return faults


# -------------------------
# MRU
# -------------------------
def mru(pages, frames):
    memory = []
    faults = 0
    recent = []

    print("\n--- MRU ---")
    for page in pages:
        if page not in memory:
            faults += 1

            if len(memory) < frames:
                memory.append(page)
            else:
                mru_page = recent[-1]
                memory.remove(mru_page)
                memory.append(page)

        if page in recent:
            recent.remove(page)
        recent.append(page)

        print(f"Page {page} -> {memory}")

    return faults


# -------------------------
# SECOND CHANCE (CLOCK)
# -------------------------
def second_chance(pages, frames):
    memory = [-1] * frames
    reference = [0] * frames
    pointer = 0
    faults = 0

    print("\n--- SECOND CHANCE ---")
    for page in pages:
        if page in memory:
            index = memory.index(page)
            reference[index] = 1
        else:
            while reference[pointer] == 1:
                reference[pointer] = 0
                pointer = (pointer + 1) % frames

            memory[pointer] = page
            reference[pointer] = 1
            pointer = (pointer + 1) % frames
            faults += 1

        print(f"Page {page} -> {memory}")

    return faults


# -------------------------
# RUN ALL ALGORITHMS
# -------------------------
fifo_faults = fifo(pages, frames)
lru_faults = lru(pages, frames)
optimal_faults = optimal(pages, frames)
mru_faults = mru(pages, frames)
sc_faults = second_chance(pages, frames)


# -------------------------
# PERFORMANCE COMPARISON
# -------------------------
print("\n=================================")
print("PAGE FAULTS COMPARISON")
print("=================================")

print(f"FIFO: {fifo_faults}")
print(f"LRU: {lru_faults}")
print(f"Optimal: {optimal_faults}")
print(f"MRU: {mru_faults}")
print(f"Second Chance: {sc_faults}")


# -------------------------
# RESULT ANALYSIS
# -------------------------
results = {
    "FIFO": fifo_faults,
    "LRU": lru_faults,
    "Optimal": optimal_faults,
    "MRU": mru_faults,
    "Second Chance": sc_faults
}

best = min(results, key=results.get)
worst = max(results, key=results.get)

print("\n=================================")
print("ANALYSIS")
print("=================================")

print(f"Best Algorithm: {best} (Least Page Faults)")
print(f"Worst Algorithm: {worst} (Most Page Faults)")