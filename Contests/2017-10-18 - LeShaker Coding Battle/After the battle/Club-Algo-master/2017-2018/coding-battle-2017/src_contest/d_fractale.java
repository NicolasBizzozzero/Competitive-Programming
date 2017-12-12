import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

public class d_fractale {
	
	public static void main(String[] args) {
		try (Scanner in = new Scanner(System.in)) {
			int n = in.nextInt();
			
			
			String[] ret = x(n);
			
			System.out.println(String.join("\n", ret));
			
			
		}
	}
	
	
	
	
	
	public static String[] x(int n) {
		if (n == 0) {
			return new String[] { "X" };
		}
		int taille = (int)Math.pow(3, n);
		char[][] c = new char[taille][taille];
		for (int i = 0; i < taille; i++) {
			Arrays.fill(c[i], ' ');
		}
		int delta = taille / 3;
		
		String[] rec = x(n-1);
		
		List<int[]> coords = new ArrayList<>();
		coords.add(new int[] {0, 0});
		coords.add(new int[] {2, 0});
		coords.add(new int[] {1, 1});
		coords.add(new int[] {0, 2});
		coords.add(new int[] {2, 2});
		
		for (int[] coord : coords)
			for (int y = 0; y < delta; y++) {
				rec[y].getChars(0, delta, c[coord[1]*delta + y], coord[0]*delta);
			}
		
		String[] ret = new String[taille];
		for (int i = 0; i < taille; i++) {
			ret[i] = new String(c[i]);
		}
		return ret;
	}
	
	
	
}
