import sys
import collections

class Node(object):
    def __init__(self,char=None,freq = None):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    def fusion_nodes(self,node_1,node_2):
        fused_node = Node()

        if node_1.freq <= node_2.freq:
            fused_node.left = node_1
            fused_node.right = node_2
        else:
            fused_node.left = node_2
            fused_node.right = node_1

        fused_node.freq = node_1.freq + node_2.freq 

        return fused_node
    def __repr__(self):
        return f"Node({self.char},{self.freq})"

class Queue:
    def __init__(self,string):
        _ = collections.Counter(string)
        self.arr = [Node(char = letter,freq = _[letter]) for letter in _]
        self.sort()
    def sort(self):
        self.arr = sorted(self.arr, key = lambda x:x.freq, reverse = True)

    def fuse_step(self):
        low_node_1 = self.arr.pop()
        low_node_2 = self.arr.pop()
        node = Node()
        self.arr.append(node.fusion_nodes(low_node_1,low_node_2))
        self.sort()

class Tree(object):
    def __init__(self,queue : Queue):
        while len(queue.arr) > 1:
            queue.fuse_step()
        self.root = queue.arr[0]
    def binary_encode_tree(self):
        if self.root is None:
            return None
        self.root = self.binary_encode_tree_rec(self.root)
        self.root.freq = 1

    def binary_encode_tree_rec(self,root):
        if root is None:
            return 
        if root.left is not None:
            root.left= self.binary_encode_tree_rec(root.left)
            root.left.freq = 0
        if root.right is not None:
            root.right = self.binary_encode_tree_rec(root.right)
            root.right.freq = 1
        return root



class Huffman_code(object):
    def __init__(self,string,tree):
        self.table = self.create_encoding_table('',tree.root)
        self.encoder_dict = None
        self.decoder_dict = None

    def create_encoder(self):
        encoder_dict = dict()
        for element in self.table:
            encoder_dict[element[0]] = element[1]
        self.encoder_dict = encoder_dict

    def create_decoder(self):
        decoded_dict = dict()
        for element in self.table:
            decoded_dict[element[1]] = element[0]
        self.decoder_dict = decoded_dict

    def encode(self,string):
        coded_text = ""
        for char in string:
            coded_text += self.encoder_dict[char]
        return coded_text

    def decode(self,encoded_text : str):
        decoded_text = ""
        while len(encoded_text) > 0:
            i_decoder = 1
            while True:
                if encoded_text[:i_decoder] in self.decoder_dict.keys():
                    decoded_text += self.decoder_dict[encoded_text[:i_decoder]]
                    encoded_text = encoded_text[i_decoder:]
                    break
                i_decoder += 1
        return decoded_text

    def create_encoding_table(self,base_code,node):
        if (node.left is None) and (node.right is None):
            return [(node.char, base_code + str(node.freq))]
        if node.freq == -1:
            current_code = ""
        else:
            current_code = base_code + str(node.freq)
        coding_dict = []
        if node.char is not None:
            coding_dict.append((node.char,current_code + str(node.freq)))
        if node.left is not None:
            coding_dict.extend(self.create_encoding_table(current_code,node.left))
        if node.right is not None:
            coding_dict.extend(self.create_encoding_table(current_code,node.right))
        return coding_dict

def huffman_encoding(data: str):
    if len(data) == 0:
        print("Please enter a valid text")
        return
    queue = Queue(data)
    tree = Tree(queue)
    tree.binary_encode_tree()  
    huffman_encoder = Huffman_code(data,tree)
    huffman_encoder.create_encoder()

    return huffman_encoder.encode(data),huffman_encoder
def huffman_decoding(data : str,  encoder : Huffman_code):
    if len(data) == 0:
        print("input valid id")
        return
    encoder.create_decoder()
    return encoder.decode(data)
# a = Huffman_encoding(data)
#%% Testing official
if __name__ == "__main__":

    # Normal Cases:
    # Case 1
    print('Case 1:')

    a_great_sentence = "The bird is the word"

    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    # The size of the data is: 69
    print("The content of the data is: {}\n".format(a_great_sentence))
    # The content of the data is: The bird is the word

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    # The size of the encoded data is: 36
    print("The content of the encoded data is: {}\n".format(encoded_data))
    # The content of the encoded data is: 0001011011101000111001010010011000000001000011101110100110001111010010

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    # The size of the decoded data is: 69
    print("The content of the encoded data is: {}\n".format(decoded_data))
    # The content of the encoded data is: The bird is the word

    # Case 2
    print('Case 2:')

    a_great_sentence = "I just want to have fun coding"

    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    # The size of the data is: 79
    print("The content of the data is: {}\n".format(a_great_sentence))
    # The size of the data is: 79

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    # The size of the encoded data is: 40
    print("The content of the encoded data is: {}\n".format(encoded_data))
    # The content of the encoded data is: 00110110011100010010010111001011000000010111101100111010101000010110100
    # 0110100100010000110111010010111101100000001101

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    # The size of the decoded data is: 79
    print("The content of the encoded data is: {}\n".format(decoded_data))
    # The content of the encoded data is: I just want to have fun coding

    # Case 3
    print('Case 3:')

    a_great_sentence = "The sun shines and I go to the beach"

    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    # The size of the data is: 85
    print("The content of the data is: {}\n".format(a_great_sentence))
    # The content of the data is: The sun shines and I go to the beach

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    # The size of the encoded data is: 44
    print("The content of the encoded data is: {}\n".format(encoded_data))
    # The content of the encoded data is: 1001011011101000110011001001000111010000001011100010100110010100010110110
    # 01101110000001000010000001000011101110110100111001110101110

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    # The size of the decoded data is: 85
    print("The content of the encoded data is: {}\n".format(decoded_data))
    # The content of the encoded data is: The sun shines and I go to the beach

    # Edge Cases
    # Case 4
    print('Edge Cases:')
    print('Case 4:')

    a_not_so_great_sentence = "aaa"

    print("The size of the data is: {}\n".format(sys.getsizeof(a_not_so_great_sentence)))
    # The size of the data is: 52
    print("The content of the data is: {}\n".format(a_not_so_great_sentence))
    # The content of the data is: aaa

    encoded_data, tree = huffman_encoding(a_not_so_great_sentence)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    # The size of the encoded data is: 24
    print("The content of the encoded data is: {}\n".format(encoded_data))
    # The content of the encoded data is: 000

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    # The size of the decoded data is: 52
    print("The content of the encoded data is: {}\n".format(decoded_data))
    # The content of the encoded data is: aaa

    # Case 5
    print('Case 5:')
    a_not_so_great_sentence = ""

    print("The size of the data is: {}\n".format(sys.getsizeof(a_not_so_great_sentence)))
    # The size of the data is: 49
    print("The content of the data is: {}\n".format(a_not_so_great_sentence))
    # The content of the data is:

    huffman_encoding(a_not_so_great_sentence)
    # Please introduce a non null string