// import com.thealgorithms.datastructures.trees.SplayTree;

public class Main {
    public static void main(String[] args) {
        // Create a SplayTree instance
        SplayTree tree = new SplayTree();

        // Insert keys into the SplayTree
        tree.insert(10);
        tree.insert(20);
        tree.insert(30);
        tree.insert(40);

        // Search for a key in the SplayTree
        boolean found = tree.search(20);
        System.out.println("Search for 20: " + (found ? "Found" : "Not Found"));

        // Traverse the SplayTree in In-Order
        System.out.println("In-Order Traversal:");
        System.out.println(tree.traverse(SplayTree.IN_ORDER));

        // Delete a key from the SplayTree
        tree.delete(20);
        System.out.println("In-Order Traversal after deleting 20:");
        System.out.println(tree.traverse(SplayTree.IN_ORDER));
    }
}
