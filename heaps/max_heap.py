

class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self):
        # Place at end
        # percolate up
        pass

    def get_max(self):
        # If heap is empty
        if not self.heap:
            return None
        else:
            return self.heap[0]

    def remove_max(self):
        if self.heap:
            max = self.heap[0]
            # Replace with last element
            # heapify
        else:
            return None

    def __percolate_up(self):
        # Compare to parent
        # If larger, then swap
        # recursively call on parent
        pass

    def __max_heapify(self):
        # Compare to children
        # If smaller, then swap
        # recursively call on child
        pass

if __name__ == '__main__':

