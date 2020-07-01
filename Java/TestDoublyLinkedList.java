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
        // ...

    }

    public static void main(String[] args) {

        TestDoublyLinkedList TDL = new TestDoublyLinkedList();
        TDL.testisEmpty();
        TDL.testsize();
        TDL.testclear();
    
    }

}

