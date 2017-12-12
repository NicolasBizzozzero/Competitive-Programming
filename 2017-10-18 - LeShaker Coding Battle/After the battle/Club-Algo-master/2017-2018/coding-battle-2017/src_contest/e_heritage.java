import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class e_heritage {
	
	public static void main(String[] args) {
		try (Scanner in = new Scanner(System.in)) {

			List<Node> existants = new ArrayList<>();
			
			Node startAt = new Node(in.next());
			existants.add(startAt);
			
			int n = in.nextInt();
			
			for (int i = 0; i < n - 1; i++) {
				String parent = in.next();
				String enfant = in.next();

				Node parentNode = search(existants, parent);
				Node enfantNode = search(existants, enfant);
				if (parentNode == null) {
					parentNode = new Node(parent);
					existants.add(parentNode);
				}
				if (enfantNode == null) {
					enfantNode = new Node(enfant);
					existants.add(enfantNode);
				}
				
				parentNode.childrens.add(enfantNode);
				enfantNode.parent = parentNode;
				
			}
			
			n = in.nextInt();
			
			for (int i = 0; i < n; i++) {
				String dead = in.next();
				search(existants, dead).dead = true;
			}
			
			
			Node current = startAt;
			Node heritier = null;
			
			while (heritier == null && current != null) {
				heritier = heritier(current);
				current = current.parent;
			}
			
			System.out.println("God save "+heritier.name);
			
			
			
			
		}
	}
	
	
	
	
	
	static Node search(List<Node> list, String name) {
		for (Node n : list) {
			if (n.name.equals(name))
				return n;
		}
		return null;
	}
	
	
	
	
	static Node heritier(Node root) {
		if (!root.dead)
			return root;
		for (Node n : root.childrens) {
			Node f = heritier(n);
			if (f != null)
				return f;
		}
		return null;
	}
	
	
	
	
	
	
	
	static class Node {
		
		final String name;
		
		Node parent;
		
		boolean dead = false;
		
		final List<Node> childrens = new ArrayList<>();
		
		public Node(String n) {
			name = n;
		}
		
	}
	
	
	
	
	
}
