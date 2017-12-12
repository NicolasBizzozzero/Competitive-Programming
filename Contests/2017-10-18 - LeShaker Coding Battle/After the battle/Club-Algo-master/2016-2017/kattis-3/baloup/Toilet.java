import java.util.Scanner;

public class Toilet {
	public static void main(String[] args) {

		Scanner s = new Scanner(System.in);
		String in = s.nextLine();
		
		boolean initState = in.charAt(0) == 'U';
		
		int p1 = 0, p2 = 0, p3 = 0;
		boolean state1 = initState,
				state2 = initState,
				state3 = initState;
		
		for (int i = 1; i < in.length(); i++) {
			boolean wantedState = in.charAt(i) == 'U';

			// on change l'état de la lunette si besoin
			if (state1 != wantedState)
				p1++;
			if (state2 != wantedState)
				p2++;
			if (state3 != wantedState)
				p3++;
			
			// on fait ses besoins
			state1 = state2 = state3 = wantedState;

			// on remet en respectant les règles
			if (!state1) {
				p1++;
				state1 = true;
			}
			if (state2) {
				p2++;
				state2 = false;
			}
			
		}

		System.out.println(p1);
		System.out.println(p2);
		System.out.println(p3);
		
	}
}
