import unittest
import DoublyLinkedList as DLL

class TestDoublyLinkedList(unittest.TestCase):

    words = DLL.DoublyLinkedList()
    
    def testclear(self):
        """
        tests removeLast method
        """
        self.words.clear()
        self.assertEqual(self.words.size(), 0)
        print("\nclear() : Passed")
    
    def testaddFirst(self):
        """
        tests addFirst method
        """
        self.words.clear()
        self.words.addFirst("Ace")
        self.assertEqual(self.words.size(), 1)
        self.assertEqual(self.words.toList()[0], "Ace")
        self.words.addFirst("One")
        self.assertEqual(self.words.size(), 2)
        self.assertEqual(self.words.toList()[0], "One")
        print("\naddFirst() : Passed")

    def testaddLast(self):
        """
        tests addLast method
        """
        self.words.clear()
        self.words.addLast("Ace")
        self.assertEqual(self.words.size(), 1)
        self.assertEqual(self.words.toList()[-1], "Ace")
        self.words.addLast("Queen")
        self.assertEqual(self.words.size(), 2)
        self.assertEqual(self.words.toList()[-1], "Queen")
        print("\naddLast() : Passed")

    def testadd(self):
        """
        tests add method
        """
        self.words.clear()
        self.words.addFirst("Ace")
        self.words.addLast("King")
        self.assertEqual(self.words.size(), 2)
        self.words.add(1, "One")
        self.words.add(1, "Two")
        self.words.add(2, "Queen")
        self.assertEqual(self.words.size(), 5)
        word_list = self.words.toList()
        # print(word_list)
        self.assertEqual(word_list[0], "Ace")
        self.assertEqual(word_list[1], "Two")
        self.assertEqual(word_list[2], "Queen")
        self.assertEqual(word_list[3], "One")
        self.assertEqual(word_list[4], "King")
        print("\nadd : Passed")
    
    def testremoveFirst(self):
        """
        tests removeFirst method
        """
        self.words.clear()
        self.words.addFirst("Ace")
        self.words.addLast("King")
        self.words.add(1, "One")
        self.words.add(1, "Two")
        self.words.add(2, "Queen")
        word = self.words.removeFirst()
        self.assertEqual(word, "Ace")
        word = self.words.removeFirst()
        self.assertEqual(word, "Two")
        word_list = self.words.toList()
        self.assertEqual(word_list[0], "Queen")
        self.assertEqual(word_list[1], "One")
        self.assertEqual(word_list[2], "King")
        print("\nremoveFirst() : Passed")
        
    def testremoveLast(self):
        """
        tests removeLast method
        """
        self.words.clear()
        self.words.addFirst("Ace")
        self.words.addLast("King")
        self.words.add(1, "One")
        self.words.add(1, "Two")
        self.words.add(2, "Queen")
        word = self.words.removeLast()
        self.assertEqual(word, "King")
        word = self.words.removeLast()
        self.assertEqual(word, "One")
        word_list = self.words.toList()
        self.assertEqual(word_list[0], "Ace")
        self.assertEqual(word_list[1], "Two")
        self.assertEqual(word_list[2], "Queen")
        print("\nremoveLast() : Passed")


    def testclone(self):
        """
        tests clone method
        """
        self.words.clear()
        self.words.addFirst("Ace")
        self.words.addLast("King")
        self.words.add(1, "One")
        self.words.add(1, "Two")
        self.words.add(2, "Queen")
        newWords = DLL.DoublyLinkedList()
        newWords = self.words.clone()
        word_list = self.words.toList()
        newWord_list = newWords.toList()
        size = self.words.size()
        newSize = newWords.size()
        for i in range(size):
            self.assertEqual(newWord_list[i], word_list[i])
        print("\nclone() : Passed")


    def testcontains(self):
        """
        tests contains method
        """
        self.words.clear()
        self.words.addFirst("Ace")
        self.words.addLast("King")
        self.words.add(1, "One")
        self.assertTrue(self.words.contains("Ace"))
        self.assertTrue(self.words.contains("One"))
        self.assertTrue(self.words.contains("King"))
        self.assertFalse(self.words.contains("Nine"))
        self.assertFalse(self.words.contains("Queen"))
        print("\ncontains : Passed")

    
    def testelement(self):
        """
        tests element method
        """
        self.words.clear()
        self.words.addFirst("Ace")
        self.words.addLast("King")
        self.words.add(1, "One")
        word = self.words.element()
        self.assertEqual(word, "Ace")
        self.assertEqual(self.words.size(), 3)
        print("\nelement() : Passed")

    def testget(self):
        """
        tests get method
        """
        self.words.clear()
        self.words.addFirst("Ace")
        self.words.addLast("King")
        self.words.add(1, "One")
        word1 = self.words.get(0)
        word2 = self.words.get(1)
        word3 = self.words.get(2)
        self.assertEqual(word1, "Ace")
        self.assertEqual(word2, "One")
        self.assertEqual(word3, "King")
        print("\nget() : Passed")


    def testgetFirst(self):
        """
        tests getFirst method
        """
        self.words.clear()
        self.words.addFirst("Ace")
        self.words.addLast("King")
        self.words.add(1, "One")
        word = self.words.getFirst()
        self.assertEqual(word, "Ace")
        self.words.removeFirst()
        word = self.words.getFirst()
        self.assertEqual(word, "One")
        print("\ngetFirst() : Passed")


    def testgetLast(self):
        """
        tests getLast method
        """
        self.words.clear()
        self.words.addFirst("Ace")
        self.words.addLast("King")
        self.words.add(1, "One")
        word = self.words.getLast()
        self.assertEqual(word, "King")
        self.words.removeLast()
        word = self.words.getLast()
        self.assertEqual(word, "One")
        print("\ngetLast() : Passed")

    def testindexOf(self):
        """
        tests indexOf method
        """
        self.words.clear()
        self.words.addFirst("Ace")
        self.words.addLast("King")
        self.words.add(1, "One")
        self.assertEqual(self.words.indexOf("Ace"), 0)
        self.assertEqual(self.words.indexOf("One"), 1)
        self.assertEqual(self.words.indexOf("King"), 2)
        print("\nindexOf() : Passed")

    def testsize(self):
        """
        tests size method
        """
        self.words.clear()
        self.assertEqual(self.words.size(), 0)
        self.words.addFirst("Ace")
        self.assertEqual(self.words.size(), 1)
        self.words.addLast("King")
        self.assertEqual(self.words.size(), 2)
        print("\nsize() : Passed")
    
    def testisEmpty(self):
        """
        tests isEmpty method
        """
        self.words.clear()
        self.assertTrue(self.words.isEmpty())
        self.words.addFirst("Ace")
        self.assertFalse(self.words.isEmpty())
        print("\nisEmpty() : Passed")

    def testiterate(self):
        """
        tests iterate method
        """
        self.words.clear()
        self.words.addFirst("Ace")
        self.words.addLast("King")
        self.words.add(1, "One")
        word_list = ["Ace", "One", "King"]
        self.assertEqual(self.words.size(), 3)
        idx = 0
        for word in self.words.iterate():
            self.assertEqual(word, word_list[idx])
            idx += 1
        print("\niterate() : Passed")

    def testtoList(self):
        """
        test toList method
        """
        self.words.clear()
        self.words.addFirst("Ace")
        self.words.addLast("King")
        self.words.add(1, "One")
        word_list = ["Ace", "One", "King"]
        idx = 0
        for word in self.words.toList():
            self.assertEqual(word, word_list[idx])
            idx += 1
        print("\ntoList: Passed")
    

if __name__ == '__main__':
    unittest.main()
