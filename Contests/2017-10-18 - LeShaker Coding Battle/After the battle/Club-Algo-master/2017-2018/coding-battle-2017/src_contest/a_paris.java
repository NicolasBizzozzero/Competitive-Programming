import java.util.Arrays;
import java.util.Scanner;

public class a_paris {
	
	public static void main(String[] args) {
		try (Scanner in = new Scanner(System.in)) {
			int P = in.nextInt();
			
			int N = in.nextInt();
			
			int[] positions = new int[N];
			
			for (int i = 0; i < N; i++)
				positions[i] = Integer.parseInt(in.next());
			
			
			
			Arrays.sort(positions);
			float mediane = positions[positions.length / 2];
			if (positions.length % 2 == 0) {
				mediane += positions[positions.length / 2 - 1];
				mediane /= 2;
			}
			
			
			if (P > mediane + .0001) {
				System.out.println("Parie !");
			}
			else {
				System.out.println("Jockey suivant !");
			}
			
		}
	}
	
}
