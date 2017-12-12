import java.util.Scanner;

public class a_dis_papa {
	
	public static void main(String[] args) {
		try (Scanner in = new Scanner(System.in)) {
			
			String line = in.nextLine();
			
			if (line.startsWith("dis "))
				System.out.println(line.substring(4));
			else
				System.out.println();
			
		}
	}
}
