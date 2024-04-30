# class node:
#     def __init__(self):
#         node.left=None
#         node.right=None
# class Huff:
#     def __init__(self):
#
# def tree(fre):
#     for key,value in fre.items():
#         if
# al=['A','B','C','D','E','A','B','C']
# fre={}
# for ele in al:
#     if ele in fre:
#         fre[ele]+=1
#     else:
#         fre[ele]=1
# print(fre)
# fre=sorted(fre.items(),key=lambda x:x[1])
# tree(fre)
import heapq


class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


def build_huffman_tree(frequencies):
    heap = [HuffmanNode(char, freq) for char, freq in frequencies]
    heapq.heapify(heap)
    while len(heap) > 1:
        left_child = heapq.heappop(heap)
        right_child = heapq.heappop(heap)
        merged_node = HuffmanNode(None, left_child.freq + right_child.freq)
        merged_node.left = left_child
        merged_node.right = right_child
        heapq.heappush(heap, merged_node)

    return heap[0]


def assign_codes(root, code='', codes={}):
    if root is None:
        return

    if root.char is not None:
        codes[root.char] = code

    assign_codes(root.left, code + '0', codes)
    assign_codes(root.right, code + '1', codes)


frequencies = [('A', 2), ('B', 2), ('C', 2), ('D', 1), ('E', 1)]


huffman_tree_root = build_huffman_tree(frequencies)

codes = {}
assign_codes(huffman_tree_root, '', codes)

print("Huffman Codes:")
for char, code in codes.items():
    print(char, ":", code)
