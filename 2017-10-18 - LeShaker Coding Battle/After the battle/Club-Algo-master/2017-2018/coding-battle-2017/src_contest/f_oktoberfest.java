import java.util.Scanner;

public class f_oktoberfest {
	
	public static void main(String[] args) {
		try (Scanner in = new Scanner(System.in)) {

			int V = in.nextInt();
			int Va = in.nextInt();
			int Vb = in.nextInt();
			
			
			int res = recursive(0, V, Va, Vb);
			
			System.out.println(res);
		}
	}
	
	
	
	
	
	
	
	static int recursive(int profondeur, int vol, int va, int vb) {
		
		int max = 0;
		max = va + vb;
		
		if (profondeur > 17)
			return max;
		
		int[] op = op1(va, vb);
		if (op[0] + op[1] <= vol) {
			int ret = recursive(profondeur + 1, vol, op[0], op[1]);
			if (ret > max)
				max = ret;
		}
		op = op2(va, vb);
		if (op[0] + op[1] <= vol) {
			int ret = recursive(profondeur + 1, vol, op[0], op[1]);
			if (ret > max)
				max = ret;
		}
		op = op3(va, vb);
		if (op[0] + op[1] <= vol) {
			int ret = recursive(profondeur + 1, vol, op[0], op[1]);
			if (ret > max)
				max = ret;
		}
		
		
		return max;
	}
	
	
	
	
	
	static int[] op1(int va, int vb) {
		return new int[] {va*va*va, vb*vb};
	}

	static int[] op2(int va, int vb) {
		return new int[] {va*va, vb*vb*vb};
	}

	static int[] op3(int va, int vb) {
		return new int[] {(int)Math.sqrt(va), (int)Math.sqrt(vb)};
	}
	
	
	
	
	
}
