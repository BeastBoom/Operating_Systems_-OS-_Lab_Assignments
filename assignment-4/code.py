# =========================================================
# DISK SCHEDULING ALGORITHMS (OS LAB ASSIGNMENT 4)
# Algorithms: FCFS, SSTF, SCAN, C-SCAN
# =========================================================

# -------------------------
# TASK 1: INPUT
# -------------------------
n = int(input("Enter number of disk requests: "))
requests = list(map(int, input("Enter request sequence: ").split()))
head = int(input("Enter initial head position: "))
disk_size = int(input("Enter disk size: "))

print("\nRequest Queue:", requests)
print("Initial Head Position:", head)


# -------------------------
# FCFS
# -------------------------
def fcfs(requests, head):
    seek_time = 0
    sequence = []

    print("\n--- FCFS ---")
    for req in requests:
        seek = abs(head - req)
        seek_time += seek
        sequence.append(req)
        print(f"Move from {head} to {req} (Seek = {seek})")
        head = req

    print("Sequence:", sequence)
    print("Total Seek Time:", seek_time)
    return seek_time


# -------------------------
# SSTF
# -------------------------
def sstf(requests, head):
    seek_time = 0
    sequence = []
    reqs = requests.copy()

    print("\n--- SSTF ---")
    while reqs:
        nearest = min(reqs, key=lambda x: abs(x - head))
        seek = abs(head - nearest)

        seek_time += seek
        print(f"Move from {head} to {nearest} (Seek = {seek})")

        head = nearest
        sequence.append(nearest)
        reqs.remove(nearest)

    print("Sequence:", sequence)
    print("Total Seek Time:", seek_time)
    return seek_time


# -------------------------
# SCAN (Elevator)
# -------------------------
def scan(requests, head, disk_size):
    seek_time = 0
    sequence = []

    left = [r for r in requests if r < head]
    right = [r for r in requests if r >= head]

    left.sort(reverse=True)
    right.sort()

    print("\n--- SCAN ---")

    # Move right
    for r in right:
        seek = abs(head - r)
        seek_time += seek
        print(f"Move from {head} to {r} (Seek = {seek})")
        head = r
        sequence.append(r)

    # Move to end
    if head != disk_size - 1:
        seek = abs(head - (disk_size - 1))
        seek_time += seek
        print(f"Move from {head} to {disk_size - 1} (Seek = {seek})")
        head = disk_size - 1

    # Reverse direction
    for r in left:
        seek = abs(head - r)
        seek_time += seek
        print(f"Move from {head} to {r} (Seek = {seek})")
        head = r
        sequence.append(r)

    print("Sequence:", sequence)
    print("Total Seek Time:", seek_time)
    return seek_time


# -------------------------
# C-SCAN
# -------------------------
def cscan(requests, head, disk_size):
    seek_time = 0
    sequence = []

    left = [r for r in requests if r < head]
    right = [r for r in requests if r >= head]

    left.sort()
    right.sort()

    print("\n--- C-SCAN ---")

    # Move right
    for r in right:
        seek = abs(head - r)
        seek_time += seek
        print(f"Move from {head} to {r} (Seek = {seek})")
        head = r
        sequence.append(r)

    # Move to end
    if head != disk_size - 1:
        seek = abs(head - (disk_size - 1))
        seek_time += seek
        print(f"Move from {head} to {disk_size - 1} (Seek = {seek})")

    # Jump to start
    print(f"Jump from {disk_size - 1} to 0")
    seek_time += (disk_size - 1)
    head = 0

    # Continue servicing
    for r in left:
        seek = abs(head - r)
        seek_time += seek
        print(f"Move from {head} to {r} (Seek = {seek})")
        head = r
        sequence.append(r)

    print("Sequence:", sequence)
    print("Total Seek Time:", seek_time)
    return seek_time


# -------------------------
# RUN ALL ALGORITHMS
# -------------------------
fcfs_time = fcfs(requests, head)
sstf_time = sstf(requests, head)
scan_time = scan(requests, head, disk_size)
cscan_time = cscan(requests, head, disk_size)


# -------------------------
# PERFORMANCE COMPARISON
# -------------------------
print("\n=================================")
print("PERFORMANCE COMPARISON")
print("=================================")

print(f"FCFS Seek Time: {fcfs_time}")
print(f"SSTF Seek Time: {sstf_time}")
print(f"SCAN Seek Time: {scan_time}")
print(f"C-SCAN Seek Time: {cscan_time}")


# -------------------------
# RESULT ANALYSIS
# -------------------------
results = {
    "FCFS": fcfs_time,
    "SSTF": sstf_time,
    "SCAN": scan_time,
    "C-SCAN": cscan_time
}

best = min(results, key=results.get)
worst = max(results, key=results.get)

print("\n=================================")
print("ANALYSIS")
print("=================================")

print(f"Best Algorithm: {best} (Minimum Seek Time)")
print(f"Worst Algorithm: {worst} (Maximum Seek Time)")