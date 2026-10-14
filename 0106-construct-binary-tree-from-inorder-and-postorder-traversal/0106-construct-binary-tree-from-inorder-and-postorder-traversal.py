class Solution:
    def buildTree(self, inorder, postorder):
        inorder_index = {val: i for i, val in enumerate(inorder)}
        postorder_index = len(postorder) - 1

        def build(left, right):
            nonlocal postorder_index

            if left > right:
                return None

            root_val = postorder[postorder_index]
            postorder_index -= 1

            root = TreeNode(root_val)
            mid = inorder_index[root_val]

            root.right = build(mid + 1, right)
            root.left = build(left, mid - 1)

            return root

        return build(0, len(inorder) - 1)