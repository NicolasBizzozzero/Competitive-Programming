import java.util.Scanner;

public class SimonSays {

	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		int nb = s.nextInt();
		s.nextLine();
		for (int i=0; i<nb; i++) {
			String in = s.nextLine();
			if (in.startsWith("simon says ")) {
				System.out.println(in.substring("simon says ".length()));
			}
			else
				System.out.println();
		}
		
		
	}

}
