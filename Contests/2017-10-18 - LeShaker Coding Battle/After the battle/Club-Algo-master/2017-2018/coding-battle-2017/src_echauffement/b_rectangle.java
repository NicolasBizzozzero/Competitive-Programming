import java.util.Arrays;
import java.util.Scanner;

public class b_rectangle {
	
	public static void main(String[] args) {
		try (Scanner in = new Scanner(System.in)) {

			int n = in.nextInt();
			int m = in.nextInt();
			char c = in.next().toCharArray()[0];
			
			char[] arr = new char[n*m + n];
			Arrays.fill(arr, c);
			
			
			for (int i = 0; i < n; i++) {
				arr[(i+1)*(m+1) - 1] = '\n';
			}
			
			System.out.print(arr);
		}
	}
}
