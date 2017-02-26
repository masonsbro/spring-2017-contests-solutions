import java.util.*;
import java.io.*;

public class ethan {

    private static class Tree {
        private static class Node implements Comparable<Node> {
            private int val;
            private int column;
            private int level;

            private Node left;
            private Node right;

            private Node(int val, int column, int level) {
                this.val = val;
                this.column = column;
                this.level = level;
            }

            @Override
            public int compareTo(Node other) {
                if (column != other.column)
                    return column - other.column;
                return level - other.level;
            }
        }

        private Node root;

        private Tree() {
            this.root = null;
        }

        private void insert(int val) {
            root = insert(root, 0, 0, val);
        }

        private Node insert(Node node, int column, int level, int val) {
            if (node == null) return new Node(val, column, level);
            if (val < node.val) {
                node.left = insert(node.left, column - 1, level + 1, val);
            } else if (val > node.val) {
                node.right = insert(node.right, column + 1, level + 1, val);
            } else {
                throw new AssertionError("Duplicate values in tree");
            }
            return node;
        }

        private List<Node> traverse() {
            List<Node> ret = new ArrayList<Node>();
            traverse(root, ret);
            return ret;
        }

        private void traverse(Node node, List<Node> list) {
            if (node == null) return;
            traverse(node.left, list);
            list.add(node);
            traverse(node.right, list);
        }
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int t = scan.nextInt();
        assert 1 <= t && t <= 100;
        for (int q = 0; q < t; q++) {
            int n = scan.nextInt();
            assert 1 <= n && n <= 1000;
            Tree tree = new Tree();
            for (int i = 0; i < n; i++) {
                int x = scan.nextInt();
                assert 0 <= x && x <= 65535;
                tree.insert(x);
            }
            List<Tree.Node> traversal = tree.traverse();
            Collections.sort(traversal);
            for (Tree.Node node : traversal) {
                System.out.printf("%d ", node.val);
            }
            System.out.println();
        }
    }

}
