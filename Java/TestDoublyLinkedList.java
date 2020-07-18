import org.junit.Test;

import jdk.jfr.Timestamp;

import static org.junit.Assert.*;

public class TestDoublyLinkedList {

    private DoublyLinkedList<String> words;

    public TestDoublyLinkedList() {

        this.words = new DoublyLinkedList<String>();
        
    }

    @Test
    public void testisEmpty() {

        assertTrue(words.isEmpty());
        words.addFirst("Ace");
        assertFalse(words.isEmpty());
        words.clear();
        System.out.println("\n isEmpty() : passed");

    }

    @Test
    public void testsize() {

        int result1 = words.size();
        words.addFirst("One");
        int result2 = words.size();
        words.addFirst("Two");
        int result3 = words.size();
        words.removeFirst();
        int result4 = words.size();
        assertEquals(result1, 0);
        assertEquals(result2, 1);
        assertEquals(result3, 2);
        assertEquals(result4, 1);
        System.out.println("\n size() : passed");
        words.clear();

    }

    @Test
    public void testclear() {

        words.addFirst("one");
        words.clear();
        int size = words.size();
        assertEquals(size, 0);
        System.out.println("\n clear() : passed");
        words.clear();

    }

    @Test
    public void testaddFirst() {

        words.addFirst("King");
        String word = words.getFirst();
        assertEquals(word, "King");
        words.addFirst("Ace");
        word = words.getFirst();
        assertEquals(word, "Ace");
        System.out.println("\n addFirst() : passed");
        words.clear();

    }

    @Test
    public void testaddLast() {

        words.addLast("Ace");
        String last = words.getLast();
        assertEquals(last, "Ace");
        words.addLast("Rook");
        last = words.getLast();
        assertEquals(last, "Rook");
        System.out.println("\n addLast() : passed");
        words.clear();

    }

    @Test
    public void testadd() {

        words.addFirst("King");
        words.addLast("Queen");
        words.add(1, "Rook");
        int idx = 0;
        String word = "";
        for (String s: words) {
            if (idx == 1) {
                word = s;
                break;
            }
            idx++;
        }
        assertEquals(word, "Rook");
        System.out.println("\n add() : passed");
        words.clear();

    }

    @Test
    public void testremoveFirst() {

        words.addFirst("Ace");
        words.addLast("Jack");
        words.add(1, "King");
        String word = words.removeFirst();
        assertEquals(word, "Ace");
        assertEquals(words.getFirst(), "King");
        System.out.println("\n removeFirst() : passed");
        words.clear();

    }

    @Test
    public void testremoveLast() {

        words.addFirst("King");
        words.addLast("Queen");
        words.addLast("Jack");
        words.addLast("One");
        String word = words.removeLast();
        assertEquals(word, "One");
        assertEquals(words.getLast(), "Jack");
        System.out.println("\n removeLast() : passed");
        words.clear();

    }

    @Test
    public void testclone() {

        words.addFirst("One");
        words.addLast("Two");
        words.addLast("Three");
        DoublyLinkedList<String> cloned = words.clone();
        int size = cloned.size();
        assertEquals(size, words.size());
        assertEquals(cloned.getFirst(), "One");
        assertEquals(cloned.getLast(), "Three");
        String word = cloned.removeFirst();
        assertEquals(cloned.getFirst(), "Two");
        System.out.println("\n clone() : passed");
        words.clear();

    }

    @Test
    public void testcontains() {

        words.addFirst("Pawn");
        words.addFirst("Bishop");
        words.addFirst("Rook");
        words.addFirst("Knight");
        assertTrue(words.contains("Pawn"));
        assertTrue(words.contains("Bishop"));
        assertTrue(words.contains("Rook"));
        assertTrue(words.contains("Knight"));
        assertFalse(words.contains("Queen"));
        assertFalse(words.contains("Ace"));
        System.out.println("\n contains() : passed");
        words.clear();

    }

    @Test
    public void testelement() {

        words.addFirst("King");
        words.addLast("One");
        String word = words.element();
        assertEquals(word, "King");
        System.out.println("\n element() : passed");
        words.clear();

    }

    @Test
    public void testgetmethods() {

        words.addFirst("King");
        words.addLast("Queen");
        words.addLast("Rook");
        words.addLast("Knight");
        words.addLast("Bishop");
        String word = words.get(1);
        assertEquals(word, "Queen");
        word = words.get(2);
        assertEquals(word, "Rook");
        word = words.get(3);
        assertEquals(word, "Knight");
        word = words.getFirst();
        assertEquals(word, "King");
        word = words.getLast();
        assertEquals(word, "Bishop");
        System.out.println("\n get() : passed");
        System.out.println("\n getFirst() : passed");
        System.out.println("\n getLast() : passed");
        words.clear();

    }

    @Test
    public void testindexOf() {

        words.addFirst("One");
        words.addLast("One");
        words.addLast("One");
        words.addLast("Rook");
        int idx = words.indexOf("One");
        assertEquals(idx, 0);
        idx = words.indexOf("Rook");
        assertEquals(idx, 3);
        idx = words.indexOf("Queen");
        assertEquals(idx, -1);
        System.out.println("\n indexOf() : passed");
        words.clear();

    }

    public static void main(String[] args) {

        TestDoublyLinkedList TDL = new TestDoublyLinkedList();
        TDL.testisEmpty();
        TDL.testsize();
        TDL.testclear();
        TDL.testaddFirst();
        TDL.testaddLast();
        TDL.testadd();
        TDL.testremoveFirst();
        TDL.testremoveLast();
        TDL.testclone();
        TDL.testcontains();
        TDL.testelement();
        TDL.testgetmethods();
        TDL.testindexOf();

    }

}

