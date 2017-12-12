import java.util.Scanner;

public class BuggyEditors {

	public static void main(String[] args) {
		

		try (Scanner s = new Scanner(System.in)) {
			char[] line = s.nextLine().toCharArray();
			int outPos = 0;
			for (int i=0; i<line.length; i++) {
				if (line[i] == '<') {
					outPos--;
				}
				else {
					line[outPos++] = line[i];
				}
			}
			System.out.println(String.valueOf(line, 0, outPos));
		}

	}

}
