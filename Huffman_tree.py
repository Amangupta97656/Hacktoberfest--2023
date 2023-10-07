class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Predefined Huffman tree (for simplicity)
def build_huffman_tree():
    root = TreeNode('*')  # Root node
    root.left = TreeNode('A')
    root.right = TreeNode('*')
    root.right.left = TreeNode('B')
    root.right.right = TreeNode('C')
    return root

# Encode a message using Huffman tree
def huffman_encode(root, message):
    huffman_codes = {}

    def encode_helper(node, current_code):
        if node is not None:
            if node.data != '*':
                huffman_codes[node.data] = current_code
            encode_helper(node.left, current_code + '0')
            encode_helper(node.right, current_code + '1')

    encode_helper(root, '')
    
    encoded_message = ''.join([huffman_codes[char] for char in message])
    return encoded_message

# Decode a message using Huffman tree
def huffman_decode(root, encoded_message):
    decoded_message = ""
    current_node = root

    for bit in encoded_message:
        if bit == '0':
            current_node = current_node.left
        else:
            current_node = current_node.right

        if current_node.data != '*':
            decoded_message += current_node.data
            current_node = root

    return decoded_message

def main():
    root = build_huffman_tree()
    message = "ABC"
    
    encoded_message = huffman_encode(root, message)
    decoded_message = huffman_decode(root, encoded_message)
    
    print("Original Message:", message)
    print("Encoded Message:", encoded_message)
    print("Decoded Message:", decoded_message)

if __name__ == "__main__":
    main()
