class Solution:
    def sortedListToBST(self, head):
        def findMiddle(left):
            slow = fast = left
            prev = None

            while fast and fast.next:
                prev = slow
                slow = slow.next
                fast = fast.next.next

            if prev:
                prev.next = None

            return slow

        def build(head):
            if not head:
                return None

            mid = findMiddle(head)
            root = TreeNode(mid.val)

            if head != mid:
                root.left = build(head)

            root.right = build(mid.next)

            return root

        return build(head)