import unittest

from hw5 import *
import random


def _list_len(head):
    """
    Helper function to determine the length of the linked list.
    Note: don't pass in a linked list with a cycle (hehe).

    Input:
        head - the head of the linked list.
    
    Output:
        (int) the length of the linked list.
    """
    if head is None:
        return 0
    return 1 + _list_len(head.next_node)


def convertListToNode(lst):
    if lst is None:
        return None

    if len(lst) == 1:
        return Node(lst[0])
    return Node(lst[0], convertListToNode(lst[1:]))


def convertNodeToString(head):
    finalStr = ""

    while head is not None:
        currentStr = str(head.data)
        finalStr += currentStr
        head = head.next_node

    return finalStr


class tester(unittest.TestCase):
    def test_add_head(self):
        """
        Test for adding an element to the head of the linked list.

        Test Coverage:
            - nullity
            - head elements equal
            - length of the new list
        """
        head = None
        for element in range(1, 10):
            head = add_head(head, element)
            self.assertIsNotNone(head)
            self.assertEqual(head.data, element)
            self.assertEqual(_list_len(head), element)
    
    # Write your own tests!

    def test_add_position(self):
        arrayOfLists = [[1, 2, 1, 3, 2, 1], None, [5], [2, 2, 2, 2, 2, 2], [1546, 38101, 1746291]]

        for lst in arrayOfLists:
            dataRandom = random.randint(0, 9)
            positionRandom = random.randint(0, 10)

            linkedLst = convertListToNode(lst)
            addPosition = add_position(linkedLst, dataRandom, positionRandom)
            if positionRandom > _list_len(linkedLst):
                if linkedLst is None:
                    self.assertEqual(convertNodeToString(addPosition), str(dataRandom))
                else:
                    self.assertEqual(convertNodeToString(addPosition), ''.join(str(i) for i in lst) + str(dataRandom))
            else:
                if linkedLst is None:
                    self.assertEqual(convertNodeToString(addPosition), str(dataRandom))
                else:
                    lst.insert(positionRandom, dataRandom)
                    self.assertEqual(convertNodeToString(addPosition), ''.join(str(i) for i in lst))



    def test_remove_head(self):
        arrayOfLists = [[1, 2, 1, 3, 2, 1], None, [5], [2, 2, 2, 2, 2, 2], [1546, 38101, 1746291]]

        for lst in arrayOfLists:
            linkedLst = convertListToNode(lst)
            removeHead = remove_head(linkedLst)
            if linkedLst is None:
                self.assertEqual(removeHead, None)
            else:
                self.assertEqual(_list_len(removeHead), len(lst) - 1)
                self.assertEqual(convertNodeToString(removeHead), ''.join(str(i) for i in lst[1:]))


    def test_remove_position(self):
        arrayOfLists = [[1, 2, 1, 3, 2, 1], None, [2, 2, 2, 2, 2, 2], [1546, 38101, 1746291]]

        for lst in arrayOfLists:
            linkedLst = convertListToNode(lst)
            if linkedLst is None:
                self.assertEqual(remove_position(linkedLst, 3), None)
            else:
                linkedLst = convertListToNode(lst)
                self.assertEqual(convertNodeToString(remove_position(linkedLst, 9)), ''.join(str(i) for i in lst))
                self.assertEqual(convertNodeToString(remove_position(linkedLst, 0)), convertNodeToString(remove_head(linkedLst)))
                self.assertEqual(convertNodeToString(remove_position(linkedLst, 2)), ''.join(str(i) for i in lst[0:2]) + ''.join(str(j) for j in lst[3:]))


        lst1 = [1, 2, 1, 3, 2, 1]
        linkedLst1 = convertListToNode(lst1)
        self.assertEqual(convertNodeToString(remove_position(linkedLst1, 9)), ''.join(str(i) for i in lst1))


    
    def test_list_sum(self):
        arrayOfLists = [[1, 2, 1, 3, 2, 1], [5], [2, 2, 2, 2, 2, 2], [1546, 38101, 1746291]]

        self.assertEqual(list_sum(None), 0)
        for lst in arrayOfLists:
            linkedLst = convertListToNode(lst)
            answerSum = sum(lst)
            self.assertEqual(list_sum(linkedLst), answerSum)
    
    def test_is_merged(self):
        testNode = Node(1)
        testNode.next_node = Node(2)
        testNode.next_node.next_node = Node(1)
        testNode.next_node.next_node.next_node = Node(10)
        testNode.next_node.next_node.next_node.next_node = Node(2)
        testNode.next_node.next_node.next_node.next_node.next_node = Node(1)

        testNode2 = Node(4)
        testNode2.next_node = Node(5)
        testNode2.next_node.next_node = Node(6)
        testNode2.next_node.next_node.next_node = Node(7)
        testNode2.next_node.next_node.next_node.next_node = testNode.next_node.next_node.next_node

        self.assertEqual(is_merged(testNode, testNode2), True)

        testNode3 = Node(1546)
        testNode3.next_node = Node(38101)

        testNode4 = Node(1746291)

        self.assertEqual(is_merged(testNode3, testNode4), False)

    def test_find_merge_point(self):
        testNode = Node(1)
        testNode.next_node = Node(2)
        testNode.next_node.next_node = Node(1)
        testNode.next_node.next_node.next_node = Node(10)
        testNode.next_node.next_node.next_node.next_node = Node(2)
        testNode.next_node.next_node.next_node.next_node.next_node = Node(1)

        testNode2 = Node(4)
        testNode2.next_node = Node(5)
        testNode2.next_node.next_node = Node(6)
        testNode2.next_node.next_node.next_node = Node(7)
        testNode2.next_node.next_node.next_node.next_node = testNode.next_node.next_node.next_node

        self.assertEqual(find_merge_point(testNode, testNode2), 10)

        testNode3 = Node(1546)
        testNode3.next_node = Node(38101)

        testNode4 = testNode3.next_node

        self.assertEqual(find_merge_point(testNode3, testNode4), 38101)


    def test_find_cycle(self):
        node_a = Node(1)
        node_b = Node(2)
        node_c = Node(3)
        
        node_a.next_node = node_b
        node_b.next_node = node_c
        
        # create cycle between node_b and node_b
        node_c.next_node = node_b

        self.assertTrue(find_cycle(node_a))
    
if __name__ == '__main__':
    unittest.main(module=__name__, buffer=True, exit=False)
